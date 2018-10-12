from django.shortcuts import render

from django.http import HttpResponse

posts = [
    {
        'author': "Samba",
        'content': "Il y'a beacoup d'innondation ici",
        'location': "Guedjewaye",
        'date': "13d"
    },
    {
        'author': "Sira",
        'content': "Les marches sont en greve",
        'location': "Dakar Plateau",
        'date': "2w"
    },
    {
        'author': "Modou",
        'content': "Notre association vous invite a notre evenement culturel",
        'location': "Medina",
        'date': "3h"
    },
    {
        'author': "Fatou",
        'content': "J'ai perdu un sac couleur noir, avec beaucoup de bijoux",
        'location': "Colobane",
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
