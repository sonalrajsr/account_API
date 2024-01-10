
from rest_framework.response import Response
from .models import student_data
from .serializers import StudentDataSerializer
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
# from rest_framework.authentication import SessionAuthentication
# from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import authentication_classes, api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['GET', 'POST'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def student_data_list(request):
    if request.method == 'GET':
        students = student_data.objects.all()
        serializer = StudentDataSerializer(students, many=True)
        serialized_data = serializer.data
        return Response(serialized_data)
    
    if request.method == 'POST':
        serializer = StudentDataSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "data" : serializer.data,
                'msg' : 'Saved Successfully'
            })
        else:
            return Response(serializer.ValidationError)
    
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def student_specific(request, pk):
    if request.method == 'GET':
        try:
            student = student_data.objects.get(pk=pk) #selected that entry to delete
        except student_data.DoesNotExist:
            return Response({'error': 'Student not found'})
        # student = student_data.objects.get(pk = pk)
        serializer = StudentDataSerializer(student)
        serialized_data = serializer.data
        return Response(serialized_data)
    
    if request.method == 'PUT':
        try:
            student = student_data.objects.get(pk=pk) #selected that entry to delete
        except student_data.DoesNotExist:
            return Response({'error': 'Student not found'})
        # else:
        #     print('Everything is fine')
        
        serializer = StudentDataSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            raise Response(serializer.errors)
        
    if request.method == 'DELETE':
        try:
            student = student_data.objects.get(pk=pk) #selected that entry to delete
        except student_data.DoesNotExist:
            return Response({'error': 'Student not found'})

        student.delete()
        return Response("Deleted successfully")