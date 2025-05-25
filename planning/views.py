from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': ['E'],
    'E': []
}

def planifier(depart, objectif):
    from collections import deque
    visited = set()
    queue = deque([[depart]])

    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == objectif:
            return path
        if node not in visited:
            visited.add(node)
            for voisin in graph.get(node, []):
                new_path = list(path)
                new_path.append(voisin)
                queue.append(new_path)
    return ["Pas de chemin trouvé"]

@csrf_exempt
def index(request):
    return render(request, 'planning/index.html', {'noeuds': list(graph.keys())})

@csrf_exempt
def calculer(request):
    depart = request.POST.get("depart")
    objectif = request.POST.get("objectif")
    chemin = planifier(depart, objectif)
    return JsonResponse({'chemin': " → ".join(chemin)})