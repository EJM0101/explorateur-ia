from django.shortcuts import render

def index(request):
    domaines = [
        ("Représentation des connaissances", "connaissance"),
        ("Raisonnement logique", "raisonnement"),
        ("Planification", "planning"),
        ("Vision par ordinateur", "vision"),
        ("Traitement du langage naturel (NLP)", "nlp"),
        ("Robotique", "robotique"),
        ("Apprentissage automatique", "ml"),
    ]
    return render(request, 'base/index.html', {'domaines': domaines})