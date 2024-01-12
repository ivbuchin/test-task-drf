from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User

from .permissions import AdminPermission, FinanceManagerPermission, ManagerPermission
from .models import Employee, Permission
from .serializers import AdminEmployeeSerializer, EmployeeSerializer, PermissionSerializer


class AdminEmployeeCreateAPIView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = AdminEmployeeSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            password = request.data.get('password')
            user = Employee(**serializer.validated_data)
            user.set_password(password)
            admin_permission, created = Permission.objects.get_or_create(name='Admin')
            user.permission = admin_permission
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeCreateAPIView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if AdminPermission.has_permission(self, request, None):
                return Response("У тебя есть доступ", status=status.HTTP_200_OK)

        return Response("У тебя нет доступа", status=status.HTTP_403_FORBIDDEN)


class PermissionCreateAPIView(CreateAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
          if AdminPermission.has_permission(self, request, None):
              return Response("У тебя есть доступ", status=status.HTTP_200_OK)

        return Response("У тебя нет доступа", status=status.HTTP_403_FORBIDDEN)


class PnLView(APIView):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
          if FinanceManagerPermission.has_permission(self, request, None):
              return Response("Ты видишь инфо", status=status.HTTP_200_OK)

        return Response("У тебя нет доступа", status=status.HTTP_403_FORBIDDEN)


class DDSView(APIView):

    def get(self, request, *args, **kwargs):
      if request.user.is_authenticated:
        if FinanceManagerPermission.has_permission(self, request, None):
            return Response("Ты видишь инфо", status=status.HTTP_200_OK)
      
      return Response("У тебя нет доступа", status=status.HTTP_403_FORBIDDEN)


class BalanceView(APIView):

    def get(self, request, *args, **kwargs):
      if request.user.is_authenticated:
        if FinanceManagerPermission.has_permission(self, request, None):
            return Response("Ты видишь инфо", status=status.HTTP_200_OK)

      return Response("У тебя нет доступа", status=status.HTTP_403_FORBIDDEN)


class CashboxView(APIView):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if ManagerPermission.has_permission(self, request, None):
                return Response("Ты видишь инфо", status=status.HTTP_200_OK)

        return Response("У тебя нет доступа", status=status.HTTP_403_FORBIDDEN)
