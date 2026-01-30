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

def update(request):
	json_format = json.loads(request.body.decode('utf-8'))

	if len( Anime.objects.filter(name=json_format["Name"]).values()) > 0:
		for key in json_format.keys():
			if key == "Synopsis":
				Anime.objects.filter(name=json_format["Name"]).update(synopsis=json_format["Synopsis"])
			if key == "Rating":
				Anime.objects.filter(name=json_format["Name"]).update(rating=json_format["Rating"])

	return HttpResponse( Anime.objects.filter(name = json_format["Name"]).values() )

def delete(request):
	json_format = json.loads(request.body.decode('utf-8'))

	if len( Anime.objects.filter(name=json_format["Name"]).values()) > 0:
		Anime.objects.filter(name=json_format["Name"]).delete()

	return HttpResponse("Done")



