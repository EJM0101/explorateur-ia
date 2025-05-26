from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def appliquer_regles(faits, regles):
    faits = set(faits)
    trace = []
    liens = []
    invalides = []

    changed = True
    while changed:
        changed = False
        for r in regles:
            parts = [s.strip() for s in r.lower().split("alors")]
            if len(parts) != 2:
                if r not in invalides:
                    invalides.append(r)
                continue
            condition, conclusion = parts
            if condition in faits and conclusion not in faits:
                faits.add(conclusion)
                trace.append(f"{condition} → {conclusion}")
                liens.append({"from": condition, "to": conclusion})
                changed = True

    return faits, trace, liens, invalides

@csrf_exempt
def index(request):
    if request.method == 'POST':
        faits_brut = request.POST.get('faits', '')
        regles_brut = request.POST.get('regles', '')

        faits_initiaux = [f.strip().lower() for f in faits_brut.strip().splitlines() if f.strip()]
        regles = [r.strip() for r in regles_brut.strip().splitlines() if r.strip()]

        faits_final, trace, liens, invalides = appliquer_regles(faits_initiaux, regles)

        return render(request, 'connaissance/index.html', {
            'faits_initiaux': faits_initiaux,
            'faits_final': sorted(faits_final),
            'regles': regles,
            'trace': trace,
            'liens': liens,
            'invalides': invalides,
        })

    # Exemples
    exemples_faits = "oiseau\nmange"
    exemples_regles = "oiseau alors animal\nanimal alors vivant\nmange alors actif"

    return render(request, 'connaissance/index.html', {
        'faits_initiaux': exemples_faits.splitlines(),
        'faits_final': [],
        'regles': exemples_regles.splitlines(),
        'trace': [],
        'liens': [],
        'invalides': [],
    })