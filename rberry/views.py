import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from django.views import View

from rberry.models import TempHumidity


class IndexView(View):
    requires_login = True
    requires_superuser = False
    login_url = '/login/?i=hm'

    permission_checker = None

    template_name = 'index.html'
    tabs = None

    def get(self, request):
        return render(
            request, self.template_name, context=locals(),
            content_type="text/html", status=200)


# LoginRequiredMixin
class HomeView(View):
    # requires_login = True
    # requires_superuser = False
    # login_url = '/login/?i=hm'

    # permission_checker = None

    template_name = 'dashboard.html'
    tabs = None

    def get(self, request):
        t1 = TempHumidity.objects.all()

        return render(
            request, self.template_name, context=locals(),
            content_type="text/html", status=200)

    def post(self, request):
        return self.get(request)
