from django.urls import path

from custom_users.views import ListCreateCustomUser, CustomUserDetails

urlpatterns = [
    path('users', ListCreateCustomUser.as_view()),
    path('users/<int:pk>', CustomUserDetails.as_view())

]