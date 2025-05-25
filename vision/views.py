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
            response = requests.post(
                "https://api-inference.huggingface.co/models/facebook/detr-resnet-50",
                headers={
                    "Authorization": f"Bearer {os.getenv('HF_API_KEY')}",
                },
                files={"file": image_file}
            )
            data = response.json()
            objets = [r['label'] for r in data if 'label' in r]
        except Exception as e:
            objets = [f"[Erreur : {str(e)}]"]
        return JsonResponse({'objets': objets})
    return JsonResponse({'objets': []})