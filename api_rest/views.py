from django.http import JsonResponse

from rberry.models import TempHumidity


# Create your views here.
def get_temp_h(request):
    r_data = None
    data = dict()
    if request.method == 'POST':
        r_data = request.POST
    elif request.method == 'GET':
        r_data = request.GET

    temp = r_data.get("t")
    h = r_data.get("h")

    t = TempHumidity(temp=temp, humidity=h)
    t.save()
    data["SUCCESS"] = True

    return JsonResponse(data, status=200)


def read_temp_h(request):
    t = TempHumidity.objects.all()[180]
