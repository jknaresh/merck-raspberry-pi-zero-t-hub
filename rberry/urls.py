from django.contrib.auth import views as auth_views
from django.urls import path

from rberry import views
from rberry.forms import LoginForm

urlpatterns = [
    # session URL'S
    path('my-me/', views.HomeView.as_view(), name="home"),
    #
    # path('txt-me/logout/', auth_views.logout, {'next_page': '/login'},
    #      name="my-logout"),
    #
    # # non session URL's
    # path('login/', auth_views.login,
    #      {'template_name': 'registration/login.html',
    #       'authentication_form': LoginForm}, name="login"),
    # path('logout/', auth_views.logout, {'next_page': '/login'}),
    path('login/', auth_views.login, {'template_name': 'registration/login.html',
                                      'authentication_form': LoginForm}, name="login"),
    path('logout/', auth_views.logout, {'next_page': '/login'}),
    path('', views.IndexView.as_view(), name="index")
]
