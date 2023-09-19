from django.urls import path

from ping_in.views import BasicPingView

urlpatterns = [
    path('ping', BasicPingView.as_view(), name='basic-ping')
]