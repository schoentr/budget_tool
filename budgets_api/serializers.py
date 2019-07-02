from rest_framework import serializers
from budgets.models import Transaction,Budget
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'password',
            'first_name',
            'last_name')

    def create(self, validated_data):
        user = super().create({
            'username': validated_data['username'],
            'email': validated_data['email'],
        })

        user.set_password(validated_data['password'])
        user.save()
        return user
class BudgetSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.username')
    user = serializers.HyperlinkedRelatedField(view_name='user_detail', read_only=True)
    class Meta:
        model = Budget
        fields =  ('id',  'user', 'name', 'total_budget', 'remaining_budget')

class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    budget = serializers.HyperlinkedRelatedField(view_name='budget_detail_api', read_only=True)

    class Meta:
        model = Transaction
        fields = ('id', 'budget', 'status', 'amount', 'description')
