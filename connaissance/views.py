from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Inférence logique simple : "si A alors B"
def appliquer_regles(faits, regles):
    faits = set(faits)
    nouvelles_inf = set()
    trace = []

    changed = True
    while changed:
        changed = False
        for r in regles:
            condition, conclusion = [s.strip() for s in r.lower().split("alors")]
            if condition in faits and conclusion not in faits:
                faits.add(conclusion)
                nouvelles_inf.add(conclusion)
                trace.append(f"{condition} → {conclusion}")
                changed = True
    return faits, trace

@csrf_exempt
def index(request):
    if request.method == 'POST':
        faits_brut = request.POST.get('faits', '')
        regles_brut = request.POST.get('regles', '')

        faits_initiaux = [f.strip().lower() for f in faits_brut.strip().splitlines() if f.strip()]
        regles = [r.strip().lower() for r in regles_brut.strip().splitlines() if "alors" in r.lower()]

        faits_final, trace = appliquer_regles(faits_initiaux, regles)

        # Préparer le graphe (liens pour vis.js)
        liens = []
        for ligne in trace:
            condition, conclusion = ligne.split("→")
            liens.append({
                "from": condition.strip(),
                "to": conclusion.strip()
            })

        return render(request, 'connaissance/index.html', {
            'faits_initiaux': faits_initiaux,
            'faits_final': sorted(faits_final),
            'regles': regles,
            'trace': trace,
            'liens': liens,
        })

    # Par défaut : exemple simple
    exemples_faits = "oiseau\nmange"
    exemples_regles = "oiseau alors animal\nanimal alors vivant\nmange alors actif"

    return render(request, 'connaissance/index.html', {
        'faits_initiaux': exemples_faits.splitlines(),
        'faits_final': [],
        'regles': exemples_regles.splitlines(),
        'trace': [],
        'liens': [],
    })