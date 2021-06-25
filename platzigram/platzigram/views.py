#Django
from django.http import HttpResponse

#Datetime
from datetime import datetime
#creamos nuestra primera pagina
def hello_world(request):
    now = datetime.now()
    return HttpResponse(f"Hello World! Current server time is: {now}")