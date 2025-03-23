from django.http import HttpResponse
from django.shortcuts import render

data={
      'movies': [{  'id':5,
                   'title': "inception",
                    'year':2010

                }, 
                {  'id':7,
                   'title': "interstellar",
                   'year':2013

                }]
}
def movies(request):
  return HttpResponse("hello there")

def drinks(request):
  return HttpResponse("nice test")

def test(request):
  return render(request, 'tests/test.html', data) #data stocke les données mais quand on veut afficher ces derniers on utilise le nom de la variable directement ici "movies"