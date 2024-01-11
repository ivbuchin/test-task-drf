from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken import views as auth_views

from staff.views import AdminEmployeeCreateAPIView, EmployeeCreateAPIView, \
                        PermissionCreateAPIView, PnLView, DDSView, BalanceView, CashboxView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', AdminEmployeeCreateAPIView.as_view(), name='user-create'),
    path('api-auth/', include('rest_framework.urls')), # api-auth/login
    path('token-login/', ObtainAuthToken.as_view(), name='token-auth'),
    
    path('add_employee/', EmployeeCreateAPIView.as_view(), name='add-employee'),
    path('create-permission/', PermissionCreateAPIView.as_view(), name='create-permission'),

    path('pnl/', PnLView.as_view(), name='pnl-view'),
    path('dds/', DDSView.as_view(), name='dds-view'),
    path('balance/', BalanceView.as_view(), name='balance-view'),
    path('cashbox/', CashboxView.as_view(), name='cashbox-view'),
]
