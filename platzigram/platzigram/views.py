#Django
from django.http import HttpResponse
from django.http import JsonResponse
#Datetime
from datetime import datetime
import json
#creamos nuestra primera pagina
def hello_world(request):
    now = datetime.now()
    return HttpResponse(f"Hello World! Current server time is: {now}")

def sorted_numbers(request):
    #making a list of the entered numbers
    numbers_list = map(lambda x: int(x), request.GET['numbers'].split(','))
    
    data = {
            'status': 'ok',
            'numbers': sorted(numbers_list),
            'message': 'numbers sorted succesfully'
        }
    
    #returning numbers_list as json with indentation
    return JsonResponse(
        data, 
        json_dumps_params={'indent': 4}
    )
    
    #returning numbers with http responce
    '''
    return HttpResponse(
        json.dumps(data,indent=4),
        content_type = 'application/json'
    )
    '''

def hi(request,age,name):
    if age < 18:
        message = f'We are sorry {name}, you are not allowed to enter to this web page'
    else:
        message = f'Hi {name}, welcome to our site'

    return HttpResponse(message)