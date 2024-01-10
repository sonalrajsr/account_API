from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from user_account.serializers import RegistrationSerializer
from django.contrib.auth.models import User
from user_account import models
from rest_framework.authtoken.models import Token
# from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

@api_view(['POST'])
def registraion_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        # defined data to overwrtie the actual data in django which will give only username and email
        # data = {}
        if serializer.is_valid():
            account = serializer.save()
            # data['response'] = "Registration Successful"
            # data['username'] = account.username
            # data['email'] = account.email
            
            # (<Token: 2f3c874bda525b2bd5ce4c379326cc67b2f6618f>, False)  
            # to get the value of token we need to do this [0].key
            token = Token.objects.get_or_create(user=account)[0].key
            # data['token'] = token
            
            # refresh = RefreshToken.for_user(account)
            # data['token'] = {
                            # 'refresh': str(refresh),
                            # 'access': str(refresh.access_token),
            
                            # }
            return Response(serializer.data)
            '''
            return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),})
            '''
        else:
            data = serializer.errors


@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response("Successfully Loged Out")

# from rest_framework.permissions import IsAuthenticated
# from rest_framework import status
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def logout_view(request):
#     if request.method == 'POST':
#         refresh_token = request.data.get('refresh_token')

#         if not refresh_token:
#             return Response({'error': 'Refresh token is required.'}, status=400)

#         try:
#             RefreshToken(refresh_token).blacklist()
#             return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response({'error': 'Invalid refresh token'}, status=status.HTTP_400_BAD_REQUEST)









# @api_view(['GET'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def users_list(request):
#     if request.method == 'GET':
#         users = User.objects.all()
#         serializer = RegistrationSerializer(users, many=True)
#         serialized_data = serializer.data
#         return Response(serialized_data)