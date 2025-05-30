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
        hf_token = os.getenv('HF_API_KEY')

        headers = {
            "Authorization": f"Bearer {hf_token}",
            "Content-Type": "image/jpeg"
        }

        # === 1. Détection d'objets ===
        try:
            obj_response = requests.post(
                "https://api-inference.huggingface.co/models/facebook/detr-resnet-50",
                headers=headers,
                data=binary_data
            )
            objets = [
                {
                    "label": o["label"],
                    "score": o.get("score", 0),
                    "xmin": o["box"]["xmin"],
                    "ymin": o["box"]["ymin"],
                    "xmax": o["box"]["xmax"],
                    "ymax": o["box"]["ymax"]
                }
                for o in obj_response.json()
                if "label" in o and "box" in o
            ]
        except Exception:
            objets = []

        # === 2. Détection de visages ===
        try:
            face_response = requests.post(
                "https://api-inference.huggingface.co/models/nashory/ultraface-onnx",
                headers=headers,
                data=binary_data
            )
            faces = [
                {
                    "label": "visage",
                    "score": f.get("score", 0),
                    "xmin": f["box"]["xmin"],
                    "ymin": f["box"]["ymin"],
                    "xmax": f["box"]["xmax"],
                    "ymax": f["box"]["ymax"]
                }
                for f in face_response.json()
                if "box" in f
            ]
        except Exception:
            faces = []

        # Fusion des objets et visages
        return JsonResponse({
            "objets": objets + faces
        })

    return JsonResponse({'error': 'Aucune image reçue'})