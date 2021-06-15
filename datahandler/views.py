from users.serializers import UserSerializer
from django.conf.global_settings import SECRET_KEY
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import SessionSerializer, TrackSerializer, CarSerializer
from .models import SessionInfo
from users.serializers import UserSerializer
from users.models import User
import jwt, json, cryptocode

class IncomingData(APIView):
    def post(self, request):
        response = Response()
        data = request.data
        token = ''

        data = json.loads(data['data'])

        for lst in data:
            token = cryptocode.decrypt(lst['METADATA']['TOKEN'], SECRET_KEY)

            try:
                payload = jwt.decode(token, SECRET_KEY, algorithms='HS256')
            except jwt.ExpiredSignatureError:
                raise AuthenticationFailed('Unauthenticated!')

            user = User.objects.filter(id=payload['id']).first()

            if 'SESSION_INFO' in lst:
                session_info = lst['SESSION_INFO']

                data = {
                    'track':session_info['SESSION_TRACK'],
                    'trackconfiguration':session_info['SESSION_TRACK_CONFIGURATION'],
                }

                sessionserializer = SessionSerializer(data=data)
                sessionserializer.is_valid(raise_exception=True)
                currentsession = sessionserializer.save()

                currentsession.record.add(user)
            
            if 'TRACK_INFO' in lst:
                track_info = lst['TRACK_INFO']
                session_id = SessionInfo.record.through.objects.last()

                data = {
                    'sectorcount':track_info['TRACK_SECTOR_COUNT'],
                    'airdensity':track_info['TRACK_AIR_DENSITY'],
                    'airtemperature':track_info['TRACK_AIR_TEMPERATURE'],
                    'roadtemperature':track_info['TRACK_ROAD_TEMPERATURE'],
                    'sessionid': session_id.sessioninfo_id
                }

                trackserializer = TrackSerializer(data=data)
                trackserializer.is_valid(raise_exception=True)
                trackserializer.save()

            if 'CAR_INFO' in lst:
                car_info = lst['CAR_INFO']
                session_id = SessionInfo.record.through.objects.last()

                data = {
                    'speedkmh':car_info['CAR_CURRENT_SPEEDKMH'],
                    'rpm':car_info['CAR_CURRENT_RPM'],
                    'gear':car_info['CAR_CURRENT_GEAR'],
                    'gaspedal':car_info['CAR_GAS_PEDAL'],
                    'brakepedal':car_info['CAR_BRAKE_PEDAL'],
                    'clutchpedal':car_info['CAR_CLUTCH_PEDAL'],
                    'sessionid': session_id.sessioninfo_id
                }

                carserializer = CarSerializer(data=data)
                carserializer.is_valid(raise_exception=True)
                carserializer.save()

        return Response('Data Uploaded with Success', status=status.HTTP_200_OK)