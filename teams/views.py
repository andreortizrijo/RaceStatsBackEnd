from django.conf.global_settings import SECRET_KEY
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import *
from .models import *
from users.models import User
import jwt

class Teams(APIView):
	def post(self, request):
		token = request.headers['token']

		try:
			payload = jwt.decode(token, SECRET_KEY, algorithms='HS256')
		except jwt.ExpiredSignatureError:
			raise AuthenticationFailed('Unauthenticated!')

		user = User.objects.filter(id=payload['id']).first()

		if user.team:
			return Response('You already have a team!')

		team = Team(owner=user)
		
		serialed_data = TeamSerializer(team, data=request.data)
		serialed_data.is_valid(raise_exception=True)
		serialed_data.save()

		user.team = team
		user.save()

		team = Team.objects.filter(owner=user.id).last();
		res = team.id

		return Response(res, status=status.HTTP_200_OK)

	def get(self, request):
		content = []
		structure = {}

		if request.headers['teamid'] == '0':
			teams = Team.objects.filter().all()

			for team in teams.iterator():
				user = User.objects.filter(team_id=team.id)
				structure = {
				'id': team.id,
				'name': team.name,
				'members': len(user),
				}

				content.append(structure)
			return Response(content, status=status.HTTP_200_OK)
		
		team = Team.objects.filter(id=request.headers['teamid']).first()
		usersid = User.objects.filter(team_id=team.id).all().values_list('id', flat=True)
		usersname = User.objects.filter(team_id=team.id).all().values_list('username', flat=True)

		description = ''

		if team.description == None:
			description = 'Team has no description.'
		else:
			description = team.description

		structure = {
			'id': team.id,
			'name': team.name,
			'description': description,
			'members': {'id': usersid, 'name': usersname}
		}

		return Response(structure, status=status.HTTP_200_OK)