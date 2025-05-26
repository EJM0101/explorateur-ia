import os
import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    return render(request, 'vision/index.html')

@csrf_exempt
def detect(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image_file = request.FILES['image']
        binary_data = image_file.read()

        try:
            response = requests.post(
                "https://api-inference.huggingface.co/models/facebook/detr-resnet-50",
                headers={
                    "Authorization": f"Bearer {os.getenv('HF_API_KEY')}",
                    "Content-Type": "image/jpeg"
                },
                data=binary_data
            )
            data = response.json()
            objets = []
            for r in data:
                if 'label' in r and 'box' in r:
                    objets.append({
                        "label": r['label'],
                        "xmin": r['box']['xmin'],
                        "ymin": r['box']['ymin'],
                        "xmax": r['box']['xmax'],
                        "ymax": r['box']['ymax'],
                    })
            return JsonResponse({'objets': objets})
        except Exception as e:
            return JsonResponse({'objets': [], 'error': str(e)})

    return JsonResponse({'objets': [], 'error': 'Aucune image reçue'})