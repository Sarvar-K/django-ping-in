from django.http import HttpResponse
from django.views import View


class BasicPingView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse("OK")
