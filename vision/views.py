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
    if request.method == 'POST' and request.FILES.get('image'):
        image_file = request.FILES['image']

        try:
            # Lire le fichier en binaire brut
            binary_data = image_file.read()

            response = requests.post(
                "https://api-inference.huggingface.co/models/facebook/detr-resnet-50",
                headers={
                    "Authorization": f"Bearer {os.getenv('HF_API_KEY')}",
                    "Content-Type": "image/jpeg"  # ou image/png selon le cas
                },
                data=binary_data
            )
            raw = response.text
            data = response.json()

            objets = [r['label'] for r in data if 'label' in r]
            return JsonResponse({'objets': objets, 'debug': raw})

        except Exception as e:
            return JsonResponse({'objets': [f"[Erreur : {str(e)}]"]})

    return JsonResponse({'objets': ["Aucune image reçue."]})