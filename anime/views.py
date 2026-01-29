from django.shortcuts import render
from django.http import HttpResponse
from .models import Anime
import json

def show(request):
    return HttpResponse(Anime.objects.all().values())

def add(request):
	json_format = json.loads(request.body.decode('utf-8'))

	if len( Anime.objects.filter(name=json_format["Name"]).values()) == 0:
		current = Anime(name= json_format["Name"], synopsis= json_format["Synopsis"], rating= json_format["Rating"])
		current.save()

	return HttpResponse(request)

def find(request):
	json_format = json.loads(request.body.decode('utf-8'))

	return HttpResponse( Anime.objects.filter(name = json_format["Name"]).values() )
