from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def list_posts(request):
    """list existing posts"""
    #example
    fragrances = [
    {
        'Brand':'Versace',
        'Name': 'Eros',
        'Type': 'Eau de Toilette',
        'Picture': 'https://fimgs.net/mdimg/perfume/375x500.16657.jpg',
    },
    {
        'Brand':'Dior',
        'Name': 'Sauvage',
        'Type': 'Eau de Parfum',
        'Picture': 'https://perfumeriaspigmento.com.ar/media/catalog/product/cache/image/620x678/e9c3970ab036de70892d86c6d221abfe/3/3/3348901368247_100ml_1.jpg',
    },
    {
        'Brand':'Armani',
        'Name': 'Code Profumo',
        'Type': 'Eau de Parfum',
        'Picture': 'https://fimgs.net/mdimg/perfume/375x500.34761.jpg',
    },
]
    content = []
    
    for fragrance in fragrances:
        content.append(f"""
            <p><strong> {fragrance['Brand']} </strong></p>
            <p><small> {fragrance['Name']} - {fragrance['Type']}</small></p>
            <figure><img src="{fragrance['Picture']}"/></figure>
        """)
    
    return HttpResponse(content)