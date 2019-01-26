from django.urls import path

from api_rest import views

urlpatterns = [
    path(r'v1/temp-h/', views.get_temp_h, name="api_get_temp_h"),

]
