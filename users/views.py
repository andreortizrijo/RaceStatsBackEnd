from django.conf.global_settings import SECRET_KEY
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .models import User
from .serializers import UserSerializer
import jwt, datetime

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        expiration = datetime.datetime.utcnow() + datetime.timedelta(days=30)

        payload = {
            'id':user.id,
            'expiration':expiration.isoformat(),
            'created_at':datetime.datetime.utcnow().isoformat(),
        }

        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        response = Response()
        
        response.data = {
            'token':token
        }

        return response

class UserView(APIView):
    def get(self, request):
        token = request.headers['token']

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms='HS256')
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        
        response.delete_cookie('token')
        response.data = {
            'message':'You have logout!'
        }

        return response