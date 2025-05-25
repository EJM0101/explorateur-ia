import re
from django.shortcuts import render

def syllogisme(p1, p2):
    """
    Analyse deux phrases simples pour faire une inférence logique :
    - P1 : Tous les X sont Y
    - P2 : Z est un X
    Retourne : Z est Y
    """
    try:
        # Exemple : "Tous les chats sont mignons"
        m1 = re.match(r"tous les (\w+) sont (\w+)", p1.lower())
        m2 = re.match(r"(\w+) est un (\w+)", p2.lower())

        if m1 and m2:
            x1, y = m1.groups()
            z, x2 = m2.groups()

            if x1 == x2:
                return f"{z.capitalize()} est {y}"
            else:
                return f"Les termes ne correspondent pas : '{x1}' ≠ '{x2}'. Pas d'inférence possible."
        else:
            return (
                "Structure non reconnue. Veuillez utiliser des phrases comme :\n"
                "« Tous les chats sont mignons » et « Garfield est un chat »"
            )
    except Exception as e:
        return f"Syllogisme mal formulé. Erreur : {str(e)}"

def index(request):
    p1 = request.GET.get('p1', "Tous les chats sont mignons")
    p2 = request.GET.get('p2', "Garfield est un chat")
    conclusion = syllogisme(p1, p2)

    return render(request, 'raisonnement/index.html', {
        'p1': p1,
        'p2': p2,
        'conclusion': conclusion
    })