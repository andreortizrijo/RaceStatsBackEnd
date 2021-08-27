from users.serializers import UserSerializer
from django.conf.global_settings import SECRET_KEY
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import *
from .models import *
from users.serializers import UserSerializer
from users.models import User
import jwt, json, cryptocode

class RegisterSession(APIView):
    def post(self, request):
        data = getData(request)
        token = getToken(data)
        user = getUser(token)

        session_info(data, user)

        return Response('Session Uploaded with Success', status=status.HTTP_200_OK)

class CarData(APIView):
        
    def post(self, request):
        data = getData(request)
        token = getToken(data[0])
        user = getUser(token)
        sessioninfo_id = getsessionId(SessionInfo, user)

        for lst in data:
            car_info(lst, sessioninfo_id)

        return Response('Data Uploaded with Success', status=status.HTTP_200_OK)

class TrackData(APIView):

    def post(self, request):
        data = getData(request)
        token = getToken(data[0])
        user = getUser(token)
        sessioninfo_id = getsessionId(SessionInfo, user)

        for lst in data:
            track_info(lst, sessioninfo_id)

        return Response('Data Uploaded with Success', status=status.HTTP_200_OK)

class TimeData(APIView):

    def post(self, request):
        data = getData(request)
        token = getToken(data[0])
        user = getUser(token)

        sessioninfo_id = getsessionId(SessionInfo, user)

        for lst in data:
            time_info(lst, sessioninfo_id)

        return Response('Data Uploaded with Success', status=status.HTTP_200_OK)

def getData(request):
    data = request.data
    data = json.loads(data['data'])
    return data

def getToken(data):
    token = data['METADATA']['TOKEN']
    return token

def getUser(token):
    user = cryptocode.decrypt(token, SECRET_KEY)

    try:
        payload = jwt.decode(user, SECRET_KEY, algorithms='HS256')
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated!')

    return User.objects.filter(id=payload['id']).first()

def getsessionId(model, user):
    session_id = model.record.through.objects.filter(user_id=user).last()
    return session_id

def save(serializer, data):   
    content_serialized = serializer(data=data)
    content_serialized.is_valid(raise_exception=True)
    return content_serialized.save()

def session_info(data, user):
    session_data = {}
    session_property = data['SESSION_INFO']

    if session_property['SESSION_TRACK_CONFIGURATION'] == '':
        session_property['SESSION_TRACK_CONFIGURATION'] = 'none'

    session_data = {
        'track':session_property['SESSION_TRACK'],
        'trackconfiguration':session_property['SESSION_TRACK_CONFIGURATION'],
    }

    current_session = save(SessionSerializer, session_data)
    current_session.record.add(user)

def track_info(data, session_id):
    track_data = {}
    track_property = data['TRACK_INFO']

    track_data = {
        'splinelength':track_property['TRACK_SPLINE_LENGTH'],
        'sectorcount':track_property['TRACK_SECTOR_COUNT'],
        'airdensity':track_property['TRACK_AIR_DENSITY'],
        'airtemperature':track_property['TRACK_AIR_TEMPERATURE'],
        'roadtemperature':track_property['TRACK_ROAD_TEMPERATURE'],
        'windspeed':track_property['TRACK_WIND_SPEED'],
        'winddirection':track_property['TRACK_WIND_DIRECTION'],
        'surfacegrip':track_property['TRACK_SURFACE_GRIP'],
        'sessionid': session_id.sessioninfo_id
    }

    save(TrackSerializer, track_data)

def car_info(data, session_id):
    car_data = {}
    car_property = data['CAR_INFO']

    car_data = {
        'model':car_property['CAR_MODEL'],
        'sponser':car_property['CAR_SPONSER'],
        'speedkmh':car_property['CAR_SPEEDKMH'],
        'rpm':car_property['CAR_RPM'],
        'gear':car_property['CAR_GEAR'],
        'gaspedal':car_property['CAR_GAS_PEDAL'],
        'brakepedal':car_property['CAR_BRAKE_PEDAL'],
        'clutchpedal':car_property['CAR_CLUTCH_PEDAL'],
        'steerangle':car_property['CAR_STEER_ANGLE'],
        'tyrecompound':car_property['CAR_TYRE_COMPOUND'],
        'sessionid': session_id.sessioninfo_id
    }

    save(CarSerializer, car_data)

def time_info(data, session_id):
    time_data = {}
    time_property = data['TIME_INFO']

    time_data = {
        'currenttime':time_property['TIME_CURRENT_TIME'],
        'besttime':time_property['TIME_BEST_TIME'],
        'sessionid': session_id.sessioninfo_id
    }

    save(TimeSerializer, time_data)

class GetRecordInfo(APIView):
    def get(self, request):
        token = request.headers['token']
        content = []
        structure = {}

        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms='HS256')
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        records = SessionInfo.record.through.objects.filter(user_id=user)
        
        for record in records.iterator():
            sessions = SessionInfo.objects.filter(id=record.sessioninfo_id)
            for session in sessions.iterator():
                car = CarInfo.objects.filter(sessionid=session.id).first()
                time = TimeInfo.objects.filter(sessionid=session.id).first()

                structure = {
                    'number': session.id,
                    'track': session.track,
                    'trackconfiguration': session.trackconfiguration,
                    'carmodel': car.model,
                    'besttime': time.besttime
                }

                content.append(structure)

        return Response(content, status=status.HTTP_200_OK)

class Live(APIView):
    def get(self, request):
        token = request.headers['token']
        content = []
        structure = {}

        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms='HS256')
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        record = SessionInfo.record.through.objects.filter(user_id=payload['id']).last()
        session = SessionInfo.objects.filter(id=record.sessioninfo_id).last()
        cars = CarInfo.objects.filter(sessionid=session.id)

        for car in cars.iterator():
            structure = {
                'rpm': car.rpm,
            }

            content.append(structure)

        return Response(content, status=status.HTTP_200_OK)