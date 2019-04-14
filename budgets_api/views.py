from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from budgets.models import Budget, Transaction
from .serializers import UserSerializer,User
# Create your views here.
class RegisterApiView(generics.CreateAPIView):
    permission_classes = ''
    authentication_classes = (TokenAuthentication,)
    serializer_class = UserSerializer

class UserAPIView(generics.RetrieveAPIView):
    permission_classes = ''
    serializer_class = UserSerializer
    def get_queryset(self):
        return User.objects.filter(id=self.kwargs['pk'])


