from django.shortcuts import render, redirect, get_object_or_404
from .serializers import AccountSerializer, AccountCheckpointSerializer
from accounts.models import Account, AccountCheckpoint
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def getAccounts(request):
    accounts = Account.objects.filter(user_id=request.user)
    serializer = AccountSerializer(accounts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getCheckpoints(request):
    accounts = Account.objects.filter(user_id=request.user)
    checkpoints = AccountCheckpoint.objects.filter(account_id__in=accounts)
    serializer = AccountCheckpointSerializer(checkpoints, many=True)
    return Response(serializer.data)