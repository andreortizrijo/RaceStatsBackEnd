from django.conf.global_settings import SECRET_KEY
from django.http.response import HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .models import User, WhiteList, BlackList
from .serializers import UserSerializer, WhiteListSerializer, BlackListSerializer
import jwt, datetime, cryptocode

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    def post(self, request):
        response = Response()
        username = request.data['username']
        password = request.data['password']

        user = User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id':user.id,
            'created_at':datetime.datetime.utcnow().isoformat(),
        }

        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        whiteList = WhiteList.objects.filter(token=token).first()
        blackList = BlackList.objects.filter(token=token).first()

        if blackList is None:
            if whiteList is None:
                serializer = WhiteListSerializer(data={'token':token})
                serializer.is_valid(raise_exception=True)
                serializer.save()
        
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
        token = request.headers['token']
        whiteList = WhiteList.objects.filter(token=token).first()
        blackList = BlackList.objects.filter(token=token).first()
        
        if whiteList:
            whiteList.delete()

        if blackList is None:
            serializer = BlackListSerializer(data={'token':token})
            serializer.is_valid(raise_exception=True)
            serializer.save()

        response = Response()
        response.data = {
            'message':'You have logout!'
        }

        return response

def download_file(request):
    token = request.headers['token']
    
    token = cryptocode.encrypt(token, SECRET_KEY)

    data = """[AUTH]
token = %s""" % token

    response = HttpResponse(data, headers={
        'Content-Type': 'application/json',
        'Content-Disposition': 'attachment; filename="config.ini"'
    })

    return response