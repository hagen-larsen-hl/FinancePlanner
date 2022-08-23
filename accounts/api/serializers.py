from rest_framework.serializers import ModelSerializer
from accounts.models import *


class AccountCheckpointSerializer(ModelSerializer):
    class Meta:
        model = AccountCheckpoint
        fields = '__all__'


class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

    