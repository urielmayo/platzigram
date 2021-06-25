#Django
from django.http import HttpResponse
from django.http import JsonResponse
#Datetime
from datetime import datetime

#creamos nuestra primera pagina
def hello_world(request):
    now = datetime.now()
    return HttpResponse(f"Hello World! Current server time is: {now}")

def hi(request):
    return HttpResponse('HI!')

def numeros(request):
    #making a list of the entered numbers
    numbers_list = map(lambda x: int(x), request.GET['numbers'].split(','))

    #returning numbers_list as json
    return JsonResponse(
        {
            'numbers': sorted(numbers_list)
        }
    )