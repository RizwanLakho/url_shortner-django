# views.py
from django.shortcuts import render
from django.contrib import messages
import requests
import json

def index(request):
    return render(request, 'index.html')

def index_form(request):
    if request.method == "POST":
        long_url = request.POST.get('long_url')
        try:
            new_url = shorten_url(long_url)
            return render(request, "new_url.html", {'url': new_url})
        except Exception as e:
            messages.error(request, f"Error shortening URL: {str(e)}")
    return render(request, 'index.html')

def shorten_url(url):
    if not url:
        raise ValueError("URL cannot be empty")
        
    headers = {
        'Authorization': '79b6e198faa3c9d859d1bd6ee0dbf28fef33e378',
        'Content-Type': 'application/json',
    }
    
    data = json.dumps({
        "long_url": url,
        "domain": "bit.ly"
    })
    
    response = requests.post(
        'https://api-ssl.bitly.com/v4/shorten',
        headers=headers,
        data=data
    )
    
    if response.status_code != 200:
        raise Exception(f"Bitly API error: {response.text}")
        
    return response.json()['link']