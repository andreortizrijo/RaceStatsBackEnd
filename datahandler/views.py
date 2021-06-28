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

class IncomingData(APIView):
        
    def post(self, request):
        data = request.data
        data = json.loads(data['data'])

        for lst in data:
            if 'SESSION_INFO' in lst:
                session_info(lst)
            else:
                track_info(lst)
                car_info(lst)
                time_info(lst)
                car_array_properties(lst)

        return Response('Data Uploaded with Success', status=status.HTTP_200_OK)

def getUser(data):
    token = cryptocode.decrypt(data, SECRET_KEY)

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms='HS256')
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated!')

    return User.objects.filter(id=payload['id']).first()

def getsessionId(model, token):
    user = getUser(token)
    session_id = model.record.through.objects.filter(user_id=user).last()
    return session_id

def save(serializer, data):   
    content_serialized = serializer(data=data)
    content_serialized.is_valid(raise_exception=True)
    return content_serialized.save()

def session_info(data):
    session_data = {}
    user = getUser(data['METADATA']['TOKEN'])
    session_property = data['SESSION_INFO']

    if session_property['SESSION_TRACK_CONFIGURATION'] == '':
        session_property['SESSION_TRACK_CONFIGURATION'] = 'none'

    session_data = {
        'track':session_property['SESSION_TRACK'],
        'trackconfiguration':session_property['SESSION_TRACK_CONFIGURATION'],
    }

    current_session = save(SessionSerializer, session_data)
    current_session.record.add(user)

def track_info(data):
    track_data = {}
    track_property = data['TRACK_INFO']
    session_id = getsessionId(SessionInfo, data['METADATA']['TOKEN'])

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

def car_info(data):
    car_data = {}
    car_property = data['CAR_INFO']
    session_id = getsessionId(SessionInfo, data['METADATA']['TOKEN'])

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
        'fuel':car_property['CAR_FUEL'],
        'maxfuel':car_property['CAR_MAX_FUEL'],
        'aidfuelrate':car_property['CAR_AID_FUEL_RATE'],
        'aidtyrerate':car_property['CAR_AID_TYRE_RATE'],
        'aidstability':car_property['CAR_AID_STABILITY'],
        'aidautoclutch':car_property['CAR_AID_AUTO_CLUTCH'],
        'aidautoblip':car_property['CAR_AID_AUTO_BLIP'],
        'hasdrs':car_property['CAR_HAS_DRS'],
        'hasers':car_property['CAR_HAS_ERS'],
        'haskers':car_property['CAR_HAS_KERS'],
        'turboboost':car_property['CAR_TURBO_BOOST'],
        'finalff':car_property['CAR_FINAL_FF'],
        'aicontroll':car_property['CAR_AI_CONTROLL'],
        'tyrecompound':car_property['CAR_TYRE_COMPOUND'],
        'sessionid': session_id.sessioninfo_id
    }

    save(CarSerializer, car_data)

def time_info(data):
    time_data = {}
    time_property = data['TIME_INFO']
    session_id = getsessionId(SessionInfo, data['METADATA']['TOKEN'])

    time_data = {
        'currenttime':time_property['TIME_CURRENT_TIME'],
        'besttime':time_property['TIME_BEST_TIME'],
        'sessionid': session_id.sessioninfo_id
    }

    save(TimeSerializer, time_data)

def car_array_properties(data):
    fromat_array(data, CarTyreWearSerializer, 'CAR_TYRE_WEAR', 4, True)
    fromat_array(data, CarCamberRADSerializer, 'CAR_CAMBER_RAD', 4, True)
    fromat_array(data, CarWheelSlipSerializer, 'CAR_WHEEL_SLIP', 4, True)
    fromat_array(data, CarTyreInnerTemperatureSerializer, 'CAR_TYRE_INNER_TEMPERATURE', 4, True)
    fromat_array(data, CarTyreMiddleTemperatureSerializer, 'CAR_TYRE_MIDDLE_TEMPERATURE', 4, True)
    fromat_array(data, CarTyreOuterTemperatureSerializer, 'CAR_TYRE_OUTER_TEMPERATURE', 4, True)
    fromat_array(data, CarTyreCoreTemperatureSerializer, 'CAR_TYRE_CORE_TEMPERATURE', 4, True)
    fromat_array(data, CarTyreDirtyLevelSerializer, 'CAR_TYRE_DIRTY_LEVEL', 4, True)
    fromat_array(data, CarWheelLoadSerializer, 'CAR_WHEEL_LOAD', 4, True)
    fromat_array(data, CarBrakeTemperatureSerializer, 'CAR_BRAKE_TEMPERATURE', 4, True)
    fromat_array(data, CarDamageSerializer, 'CAR_DAMAGE', 4, False)
    fromat_array(data, CarSuspensionTravelSerializer, 'CAR_SUSPENSION_TRAVEL', 4, True)
    fromat_array(data, CarAccGSerializer, 'CAR_ACCG', 3, False)
    fromat_array(data, CarWheelPressureSerializer, 'CAR_WHEEL_PRESSURE', 4, True)
    fromat_array(data, CarTyreRadiusSerializer, 'CAR_TYRE_RADIUS', 4, True)

def fromat_array(data, serializer, category, number, istyre):
    payload = {}
    property = data['CAR_INFO'][category].replace('[','')
    property = property.replace(']','')
    property = property.split(',')
    session_id = getsessionId(SessionInfo, data['METADATA']['TOKEN'])

    if istyre:
        propertieslist = ['tyrefl', 'tyrefr', 'tyrerl', 'tyrerr']
        for i in range(number):
            payload[propertieslist[i]] = property[i]
    if category == 'CAR_ACCG':
        propertieslist = ['x', 'y', 'z']
        for i in range(number):
            payload[propertieslist[i]] = property[i]
    if category == 'CAR_DAMAGE':
        propertieslist = ['section1', 'section2', 'section3', 'section4']
        for i in range(number):
            payload[propertieslist[i]] = property[i]

    payload['sessionid'] = session_id.sessioninfo_id
    save(serializer, payload)

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

class GetSessionData(APIView):
    def get(self, request):
        session_id = request.headers['session']
        content = []
        structure = {}

        session = SessionInfo.objects.filter(id=session_id).first()
        cars = CarInfo.objects.filter(sessionid=session.id)

        for car in cars.iterator():
            structure = {
                'rpm': car.rpm,
                'gear': car.gear
            }

            content.append(structure)

        return Response(content, status=status.HTTP_200_OK)