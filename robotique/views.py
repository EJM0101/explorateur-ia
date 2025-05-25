from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def index(request):
    return render(request, 'robotique/index.html')

@csrf_exempt
def executer(request):
    actions = request.POST.getlist('actions[]')
    x, y, orientation = 0, 0, 'NORD'
    log = []

    for action in actions:
        if action == 'AVANCER':
            if orientation == 'NORD':
                y += 1
            elif orientation == 'SUD':
                y -= 1
            elif orientation == 'EST':
                x += 1
            elif orientation == 'OUEST':
                x -= 1
            log.append(f"Avancé à ({x}, {y})")
        elif action == 'TOURNER_GAUCHE':
            orientation = {'NORD': 'OUEST', 'OUEST': 'SUD', 'SUD': 'EST', 'EST': 'NORD'}[orientation]
            log.append(f"Tourné à gauche → {orientation}")
        elif action == 'TOURNER_DROITE':
            orientation = {'NORD': 'EST', 'EST': 'SUD', 'SUD': 'OUEST', 'OUEST': 'NORD'}[orientation]
            log.append(f"Tourné à droite → {orientation}")
        elif action == 'RAMASSER':
            log.append("Ramassé un objet (virtuel)")

    return JsonResponse({
        'position': f"({x}, {y})",
        'orientation': orientation,
        'log': log
    })