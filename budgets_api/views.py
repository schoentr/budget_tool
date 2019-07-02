from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializers import UserSerializer, User, BudgetSerializer, TransactionSerializer,Budget,Transaction


class RegisterApiView(generics.CreateAPIView):
    permission_classes = ''
    authentication_classes = (TokenAuthentication,)
    serializer_class = UserSerializer


class UserAPIView(generics.RetrieveAPIView):
    permission_classes = ''
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.kwargs['pk'])


class BudgetListAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = BudgetSerializer

    def get_queryset(self):
        return Budget.objects.filter(user__username=self.request.user.username)

    def perform_create(self, serializer):
        return serializer.save(user_id=self.request.user.id)


class BudgetDetailAPIView(generics.RetrieveAPIView):

    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = BudgetSerializer

    def get_queryset(self):
        return Budget.objects.filter(user__username=self.request.user.username)


class TransactionListAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = TransactionSerializer

    def get_queryset(self):

        return Transaction.objects.filter(budget__user__username=self.request.user.username)

    def perform_create(self, serializer):
        return serializer.save()


class TransactionDetailAPIView(generics.RetrieveAPIView):

    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = TransactionSerializer

    def get_queryset(self):

        return Transaction.objects.filter(budget__user__username=self.request.user.username)
