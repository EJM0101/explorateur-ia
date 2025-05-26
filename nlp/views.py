import os
import requests
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    result = ""
    user_text = ""
    task = ""

    if request.method == "POST":
        user_text = request.POST.get("text", "").strip()
        task = request.POST.get("task", "resume")

        # Prompt personnalisé pour chaque tâche NLP
        prompts = {
            "resume": "Résume ce texte de manière concise en français :",
            "traduction": "Traduis ce texte en français :",
            "sentiment": "Donne le sentiment général (positif, négatif ou neutre) de ce texte :",
            "entites": "Liste les entités nommées présentes dans ce texte (personnes, lieux, organisations, etc.) :"
        }

        prompt_instruction = prompts.get(task, "Analyse ce texte :")

        api_payload = {
            "model": "openai/gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": "Tu es un assistant expert en traitement automatique du langage."},
                {"role": "user", "content": f"{prompt_instruction}\n\n{user_text}"}
            ]
        }

        try:
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY', '')}",
                    "Content-Type": "application/json"
                },
                json=api_payload,
                timeout=15
            )
            data = response.json()
            result = data["choices"][0]["message"]["content"].strip()
        except Exception as e:
            result = f"[Erreur API OpenRouter : {str(e)}]"

    return render(request, "nlp/index.html", {
        "text": user_text,
        "result": result,
        "task": task
    })