from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Faits enrichis par défaut
FAITS_BASE = [
    "homme(socrate)",
    "homme(platon)",
    "femme(alice)",
    "chat(tom)",
    "animal(chat)",
    "animal(chien)",
    "animal(lion)",
    "humain(X) => mortel(X)",
    "homme(X) => humain(X)",
    "femme(X) => humain(X)",
]

@csrf_exempt
def index(request):
    faits_utilisateur = []
    regles_utilisateur = []

    # Récupération via POST
    if request.method == 'POST':
        new_faits = request.POST.get('faits', '')
        new_regles = request.POST.get('regles', '')
        faits_utilisateur = [l.strip() for l in new_faits.split('\n') if l.strip()]
        regles_utilisateur = [l.strip() for l in new_regles.split('\n') if l.strip()]

    # Fusion
    faits = list(FAITS_BASE) + faits_utilisateur
    regles = [r for r in faits if '=>' in r] + regles_utilisateur
    faits_atomiques = [f for f in faits if '=>' not in f]

    inférences = infere(faits_atomiques, regles)

    return render(request, 'connaissance/index.html', {
        'faits': faits_atomiques,
        'regles': regles,
        'inférences': sorted(set(inférences))
    })

# Moteur d'inférence basique (remplace X par valeurs existantes)
def infere(faits, regles):
    résultats = set(faits)
    for regle in regles:
        if "=>" not in regle:
            continue
        premise, conclusion = regle.split("=>")
        premise = premise.strip()
        conclusion = conclusion.strip()

        # Cas : prédicat(X) => autre(X)
        if "(X)" in premise and "(X)" in conclusion:
            pred = premise.replace("(X)", "")
            concl = conclusion.replace("(X)", "")
            for fait in faits:
                if fait.startswith(f"{pred}(") and fait.endswith(")"):
                    valeur = fait[len(pred)+1:-1]
                    résultats.add(f"{concl}({valeur})")

    return résultats