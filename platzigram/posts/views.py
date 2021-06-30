from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

fragrances = [
    {
        'brand':'Versace',
        'name': 'Eros',
        'type': 'Eau de Toilette',
        'picture': 'https://fimgs.net/mdimg/perfume/375x500.16657.jpg',
    },
    {
        'brand':'Dior',
        'name': 'Sauvage',
        'type': 'Eau de Parfum',
        'picture': 'https://perfumeriaspigmento.com.ar/media/catalog/product/cache/image/620x678/e9c3970ab036de70892d86c6d221abfe/3/3/3348901368247_100ml_1.jpg',
    },
    {
        'brand':'Armani',
        'name': 'Armani Code Profumo',
        'type': 'Eau de Parfum',
        'picture': 'https://fimgs.net/mdimg/perfume/375x500.34761.jpg',
    },
]

posts = [
    {
        'title': 'Mont Blanc',
        'user': {
            'name': 'Yésica Cortés',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600?image=1036',
    },
    {
        'title': 'Via Láctea',
        'user': {
            'name': 'Christian Van der Henst',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/800/?image=903',
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'Uriel (thespianartist)',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/500/700/?image=1076',
    }
]

# Create your views here.
def list_posts(request):
    """list existing posts"""
    #example

    content = []
    
    for fragrance in fragrances:
        content.append(f"""
            <p><strong> {fragrance['brand']} </strong></p>
            <p><small> {fragrance['name']} - {fragrance['type']}</small></p>
            <figure><img src="{fragrance['picture']}"/></figure>
        """)
    
    return HttpResponse(content)

#funcion de ejemplo que retorna un template
def run_template(request):

    contexto ={
        'posts': posts,
    }
    return render(request, 'feed.html',context=contexto)