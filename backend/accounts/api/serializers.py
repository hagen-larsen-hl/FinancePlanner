from rest_framework.serializers import ModelSerializer
from accounts.models import *

class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class AccountCheckpointSerializer(ModelSerializer):
    class Meta:
        model = AccountCheckpoint
        fields = '__all__'