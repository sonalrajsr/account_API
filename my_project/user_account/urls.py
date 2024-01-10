from django.urls import path
from user_account import views
from rest_framework.authtoken.views import obtain_auth_token
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )


urlpatterns = [
    path('login/', obtain_auth_token),
    # path('users/', views.users_list),
    path('register/', views.registraion_view),
    path('logout/', views.logout_view),
    # path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

