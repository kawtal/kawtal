from django.shortcuts import render

from django.http import HttpResponse

posts = [
    {
        'author': "Samba",
        'content': "Hello I am looking for a barber",
        'location': "Medina",
        'date': "September 29, 2018"
    },
    {
        'author': "Sira",
        'content': "Hello, where is Bus 23",
        'location': "Dakar Plateau",
        'date': "September 29, 2018"
    },
    {
        'author': "Samba",
        'content': "I have just lost my pocket",
        'location': "Dakar Plateau",
        'date': "September 29, 2018"
    },
    {
        'author': "Sira",
        'content': "Taxi please",
        'location': "Dakar Plateau",
        'date': "September 29, 2018"
    },

]


def home(request):
    context = {
        'posts': posts,
    }
    return render(request, 'street/home.html', context)
