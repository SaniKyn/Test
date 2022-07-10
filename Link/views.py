from django.shortcuts import render, redirect
from . import service
from django.urls import reverse



def shorten(request, url):
    shortened_url_hash = service.shorten(url)
    shortened_url = request.build_absolute_uri(reverse('redirect', args=[shortened_url_hash]))
    return render(request, 'link.html', {'shortened_url': shortened_url})


def index(request):
    return render(request, 'index.html')


def shorten_post(request):
    return shorten(request, request.POST['url'])


def redirect_hash(request, url_hash):
    original_url = service.load_url(url_hash).original_url
    return redirect(original_url)

