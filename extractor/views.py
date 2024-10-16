from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import requests
from bs4 import BeautifulSoup
# Create your views here.
def home(request):
    return HttpResponse("hello world ")

def og(request):
    url = request.GET.get('url')
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        og_tags = {}
        for meta in soup.find_all('meta'):
            if meta.get('property') and 'og:' in meta.get('property'):
                og_tags[meta['property']] = meta.get('content')

        return JsonResponse(og_tags)

    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return JsonResponse({})