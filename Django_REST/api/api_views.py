from django.shortcuts import render

from rest_framework.decorators import api_view

#from rest_framework.response import response
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets


from . import models
from . import serializers
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response


from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# class FriendViewset(viewsets.ModelViewSet):
#     queryset = models.Friend.objects.all()
#     serializer_class = serializers.FriendSerializer

# class BelongingViewset(viewsets.ModelViewSet):
#     queryset = models.Belonging.objects.all()
#     serializer_class = serializers.BelongingSerializer

# class BorrowedViewset(viewsets.ModelViewSet):
#     queryset = models.Borrowed.objects.all()
#     serializer_class = serializers.BorrowedSerializer


@api_view(['GET','POST'])
def user_list(request):

    if request.method == 'GET':
        snippets = models.User.objects.all()
        serializer = serializers.RegistrationSerializer(snippets, many=True)
        return Response(serializer.data)
    
    
    elif request.method == 'POST':
        serializer = serializers.RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        serializer = serializers.RegistrationSerializer(data=request.data)

@api_view(['GET'])
def userid(request,pk):
    try:
        obj = models.User.objects.get(id=pk)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    serializer = serializers.RegistrationSerializer(obj)
    return Response(serializer.data)


@api_view(['DELETE'])
def userdelete(request,pk):
    try:
        obj= models.User.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    obj.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
#authentication_classes = [authentication.TokenAuthentication]
#permission_classes = [permissions.IsAdminUser]


def base(request):
  return render(request, 'base.html')