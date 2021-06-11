from django.conf.global_settings import SECRET_KEY
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import SessionSerializer, TrackSerializer, CarSerializer
import jwt, json, cryptocode

class IncomingData(APIView):
    def post(self, request):
        response = Response()
        metadata = {}

        data = request.data
        data = json.loads(data['data'])

        for lst in data:
            metadata = lst['METADATA']

            realmsg = cryptocode.decrypt(metadata['TOKEN'], SECRET_KEY)

            print(realmsg)

            #if lst['SESSION_INFO']:
            #    print(lst['SESSION_INFO'])

        try:
            payload = jwt.decode(metadata['TOKEN'], SECRET_KEY, algorithms='HS256')
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        #sessionserializer = SessionSerializer(data={})
        #sessionserializer.is_valid()
        #sessionserializer.save()

        response.data = {
            'Upload':request.data
        }

        return response