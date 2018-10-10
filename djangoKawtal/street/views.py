from django.shortcuts import render

from django.http import HttpResponse

posts = [
    {
        'author': "Samba",
        'image': "street/img/mctr-fb.jpg",
        'content': "Hello I am looking for a barber",
        'location': "Medina",
        'date': "September 29, 2018"
    },
    {
        'author': "Sira",
        'image': "street/img/mctr-fb.jpg",
        'content': "Hello, where is Bus 23",
        'location': "Dakar Plateau",
        'date': "September 29, 2018"
    },
    {
        'author': "Samba",
        'image': "street/img/mctr-fb.jpg",
        'content': "I have just lost my pocket",
        'location': "Dakar Plateau",
        'date': "September 29, 2018"
    },
    {
        'author': "Sira",
        'image': "street/img/mctr-fb.jpg",
        'content': "Taxi please",
        'location': "Dakar Plateau",
        'date': "September 29, 2018"
    },

]

user = {
    "firstname": "Moctar",
    "lastname": "Diallo",
    'image': "street/img/mctr-fb.jpg",
    "location": "street/img/user-location.jpg"
}


def home(request):
    context = {
        'posts': posts,
        'user': user
    }
    return render(request, 'street/home.html', context)
