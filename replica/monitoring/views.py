from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

def health_check(request):
    return JsonResponse({'message': 'OK'}, status=200)

def health_check(request):
    return JsonResponse({'message': 'OK'}, status=200)