from django.shortcuts import render

from django.http import HttpResponse

posts = [
    {
        'author': "Samba",
        'content': "Hello I am looking for a barber",
        'location': "Medina",
        'date': "13d"
    },
    {
        'author': "Sira",
        'content': "Hello, where is Bus 23",
        'location': "Dakar Plateau",
        'date': "2w"
    },
    {
        'author': "Samba",
        'content': "I have just lost my pocket",
        'location': "Dakar Plateau",
        'date': "3h"
    },
    {
        'author': "Sira",
        'content': "Taxi please",
        'location': "Dakar Plateau",
        'date': "10m"
    },

]

user = {
    "firstname": "Moctar",
    "lastname": "Diallo",
    'image': "street/img/mctr-fb.jpg",
    "location": "street/img/user-location.jpg"
}

sites = [
    {
        "name": "Guedjewaye",
        "content": "Brief Content"
    },
    {
        "name": "Grand Dakar",
        "content": "Brief Content"
    },
    {
        "name": "Medina, Rue 11x27",
        "content": "Brief Content"
    }
]


def home(request):
    context = {
        'posts': posts,
        'user': user,
        'sites': sites
    }
    return render(request, 'street/home.html', context)
