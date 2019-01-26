from django.urls import path

from api_rest import views

urlpatterns = [
    path('v1/temp-h/', views.get_temp_h, name="api_get_temp_h"),
    path('v1/read-t-h/', views.TempHumidity, name="read_t_h"),
]
