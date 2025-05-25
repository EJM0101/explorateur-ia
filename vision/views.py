import os
import requests
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def index(request):
    return render(request, 'vision/index.html')

@csrf_exempt
def detect(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        if not image:
            return JsonResponse({'objets': ["[Erreur] Aucune image reçue."]})
        
        try:
            response = requests.post(
                "https://api-inference.huggingface.co/models/facebook/detr-resnet-50",
                headers={
                    "Authorization": f"Bearer {os.getenv('HF_API_KEY')}",
                },
                files={"file": image}
            )
            raw = response.text
            data = response.json()
            objets = [r['label'] for r in data if 'label' in r]
            return JsonResponse({'objets': objets, 'debug': raw})
        except Exception as e:
            return JsonResponse({'objets': [f"[Erreur API Hugging Face : {str(e)}]"]})
    
    return JsonResponse({'objets': ["Méthode invalide."]})