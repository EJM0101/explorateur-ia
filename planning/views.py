from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from collections import deque

@csrf_exempt
def index(request):
    return render(request, 'planning/index.html')

@csrf_exempt
def calculer(request):
    try:
        data = json.loads(request.body)
        graphe = data.get('graphe', {})
        depart = data.get('depart')
        objectif = data.get('objectif')

        chemin = planifier(graphe, depart, objectif)
        return JsonResponse({'chemin': chemin})
    except Exception as e:
        return JsonResponse({'chemin': f"[Erreur] {str(e)}"})

def planifier(graphe, depart, objectif):
    visited = set()
    queue = deque([[depart]])

    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == objectif:
            return " → ".join(path)
        if node not in visited:
            visited.add(node)
            for voisin in graphe.get(node, []):
                new_path = list(path)
                new_path.append(voisin)
                queue.append(new_path)
    return "Aucun chemin trouvé"