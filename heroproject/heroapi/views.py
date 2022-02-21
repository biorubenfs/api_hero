from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from heroapi.models import Hero
from heroapi.serializers import HeroSerializer

@csrf_exempt
def heroes_list(request):
    """ List all code heroes, or create a new hero. """
    if request.method == 'GET':
        heroes = Hero.objects.all()
        serializer = HeroSerializer(heroes, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = HeroSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def hero_detail(request, pk):
    """ Retrieve, update or delete a hero."""
    try:
        hero = Hero.objects.get(pk=pk)
    except Hero.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = HeroSerializer(hero)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = HeroSerializer(hero, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        hero.delete()
        return HttpResponse(status=204)