from rest_framework import viewsets, routers
from django.contrib.auth.models import User
from .models import Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

@api_view(['GET'])
def api_root(request, format=None):
    import os
    # Try to get codespace name from environment or headers
    codespace_name = os.environ.get('CODESPACE_NAME')
    # If running in Codespaces, the host header will be like: <codespace_name>-8000.app.github.dev
    host = request.get_host()
    # If host matches codespace pattern, extract codespace name
    import re
    match = re.match(r"([^.]+)-8000\\.app\\.github\\.dev", host)
    if match:
        codespace_name = match.group(1)
    if codespace_name:
        base_url = f"https://{codespace_name}-8000.app.github.dev"
    else:
        # fallback to localhost
        base_url = f"http://localhost:8000"
    return Response({
        'users': base_url + reverse('user-list'),
        'teams': base_url + reverse('team-list'),
        'activities': base_url + reverse('activity-list'),
        'leaderboard': base_url + reverse('leaderboard-list'),
        'workouts': base_url + reverse('workout-list'),
    })
