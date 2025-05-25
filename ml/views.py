from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

import numpy as np
from sklearn.linear_model import LogisticRegression

# Création d’un modèle simple à la volée
X = np.array([
    [1, 1], [2, 1], [1, 2],     # classe 0
    [5, 5], [6, 5], [5, 6],     # classe 1
])
y = np.array([0, 0, 0, 1, 1, 1])
model = LogisticRegression().fit(X, y)

@csrf_exempt
def index(request):
    return render(request, 'ml/index.html')

@csrf_exempt
def predict(request):
    try:
        x = float(request.POST.get('x'))
        y_ = float(request.POST.get('y'))
        result = model.predict([[x, y_]])[0]
        return JsonResponse({'classe': f'Classe prédite : {result}'})
    except Exception as e:
        return JsonResponse({'classe': f'[Erreur ML : {str(e)}]'})