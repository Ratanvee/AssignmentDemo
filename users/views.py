from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
import pandas as pd
import os
from .serializers import JobListingSerializer

@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                      status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(username=username, password=password)

    if user is None:
        return Response({'error': 'Invalid credentials'},
                      status=status.HTTP_401_UNAUTHORIZED)

    refresh = RefreshToken.for_user(user)

    return Response({
        'access_token': str(refresh.access_token),
        'refresh_token': str(refresh),
        'user_id': user.pk,
        'username': user.username
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def jobs_list(request):
    try:
        # Get the most recent jobs CSV file
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        csv_files = [f for f in os.listdir(base_dir) if f.startswith('ibps_jobs_') and f.endswith('.csv')]
        
        if not csv_files:
            return Response({'error': 'No job listings available'}, 
                          status=status.HTTP_404_NOT_FOUND)
        
        # Get the most recent file
        latest_file = sorted(csv_files)[-1]
        file_path = os.path.join(base_dir, latest_file)
        
        # Read the CSV file
        df = pd.read_csv(file_path)
        jobs = df.to_dict('records')
        
        # Serialize the data
        serializer = JobListingSerializer(jobs, many=True)
        
        return Response({
            'count': len(jobs),
            'jobs': serializer.data
        })
        
    except Exception as e:
        return Response({'error': str(e)}, 
                      status=status.HTTP_500_INTERNAL_SERVER_ERROR)
