from django.shortcuts import render

def syllogisme(p1, p2):
    # Cas simple : Tous les X sont Y ; Z est un X → Z est un Y
    try:
        tous, x1, sont, y1 = p1.lower().split()
        z, est, un, x2 = p2.lower().split()

        if x1 == x2 and tous == "tous" and sont == "sont" and est == "est":
            return f"{z.capitalize()} est {y1}"
        else:
            return "Conclusion non déductible automatiquement."
    except:
        return "Syllogisme mal formulé."

def index(request):
    p1 = request.GET.get('p1', "Tous les hommes sont mortels")
    p2 = request.GET.get('p2', "Socrate est un homme")
    conclusion = syllogisme(p1, p2)

    return render(request, 'raisonnement/index.html', {
        'p1': p1,
        'p2': p2,
        'conclusion': conclusion
    })