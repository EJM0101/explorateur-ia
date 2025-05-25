import os
import requests
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def index(request):
    return render(request, 'nlp/index.html')

@csrf_exempt
def chat_api(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')
        try:
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": "openai/gpt-3.5-turbo",
                    "messages": [{"role": "user", "content": message}]
                }
            )
            data = response.json()
            reply = data["choices"][0]["message"]["content"]
        except Exception as e:
            reply = f"[Erreur GPT : {str(e)}]"
        return JsonResponse({'reply': reply})