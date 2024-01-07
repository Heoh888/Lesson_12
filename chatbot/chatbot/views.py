from django. shortcuts import render
import requests
import collections
# Create your views here.

def start (request):
    return render(request, 'start.html')

def chat_bot (request):
    return render(request, 'chatbot.html')

def statistics (request):
    response = requests.get("http://127.0.0.1:5000/api/get_number_requests")
    return render(request, 'statistics.html', {'data': response.json()})
