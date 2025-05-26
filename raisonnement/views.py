from django.shortcuts import render

def analyser_syllogisme(p1, p2):
    p1 = p1.strip().lower()
    p2 = p2.strip().lower()

    try:
        # Cas 1 : "Tous les X sont Y" + "Z est un X"
        if p1.startswith("tous les") and "sont" in p1 and "est un" in p2:
            x = p1.split("tous les")[1].split("sont")[0].strip()
            y = p1.split("sont")[1].strip()
            z = p2.split("est un")[0].strip()
            x2 = p2.split("est un")[1].strip()
            if x == x2:
                conclusion = f"{z.capitalize()} est {y}."
                explication = [
                    f"P1 : Tous les {x} sont {y}",
                    f"P2 : {z.capitalize()} est un {x}",
                    f"Conclusion : {z.capitalize()} est {y}"
                ]
                return conclusion, explication

        # Cas 2 : "A est B" + "B est C"
        if " est " in p1 and " est " in p2:
            a, b = p1.split(" est ")
            b2, c = p2.split(" est ")
            if b == b2:
                conclusion = f"{a.capitalize()} est {c}."
                explication = [
                    f"P1 : {a} est {b}",
                    f"P2 : {b} est {c}",
                    f"Conclusion : {a.capitalize()} est {c}"
                ]
                return conclusion, explication

        # Cas 3 : "A implique B" + "B implique C"
        if " implique " in p1 and " implique " in p2:
            a, b = p1.split(" implique ")
            b2, c = p2.split(" implique ")
            if b == b2:
                conclusion = f"{a.capitalize()} implique {c}."
                explication = [
                    f"P1 : {a} implique {b}",
                    f"P2 : {b} implique {c}",
                    f"Conclusion : {a.capitalize()} implique {c}"
                ]
                return conclusion, explication

        return "Conclusion non déductible automatiquement.", []
    
    except Exception:
        return "Syllogisme mal formulé.", []

def index(request):
    p1 = request.GET.get('p1', "Tous les hommes sont mortels")
    p2 = request.GET.get('p2', "Socrate est un homme")
    conclusion, explication = analyser_syllogisme(p1, p2)

    return render(request, 'raisonnement/index.html', {
        'p1': p1,
        'p2': p2,
        'conclusion': conclusion,
        'explication': explication
    })