from django.urls import path

from account.views import ProfileView, FollowView

app_name = "account"
urlpatterns = [
    path('<str:username>/', ProfileView.as_view(), name="profile"),
    path('follow/<str:username>/', FollowView.as_view(), name="follow")
]
