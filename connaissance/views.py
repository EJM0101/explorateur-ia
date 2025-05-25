from django.shortcuts import render

# Faits + règles codés en dur pour la démo
faits = ["homme(socrate)"]
regles = ["homme(X) => mortel(X)"]

def infere(faits, regles):
    resultats = set(faits)
    for regle in regles:
        if "=>" in regle:
            premise, conclusion = regle.split("=>")
            premise = premise.strip().replace("(X)", "")
            conclusion = conclusion.strip().replace("(X)", "")
            for fait in faits:
                if fait.startswith(f"{premise}("):
                    var = fait[len(premise)+1:-1]
                    resultats.add(f"{conclusion}({var})")
    return sorted(resultats)

def index(request):
    inférences = infere(faits, regles)
    return render(request, 'connaissance/index.html', {
        'faits': faits,
        'regles': regles,
        'inférences': inférences
    })