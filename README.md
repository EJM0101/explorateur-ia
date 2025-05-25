# Explorateur IA — Démonstrateur Interactif des Sous-domaines de l’Intelligence Artificielle

**Explorateur IA** est une application Django conçue pour **explorer les grands domaines de l'intelligence artificielle** à travers des démonstrations interactives, pédagogiques et accessibles.

Elle est destinée aux :
- Étudiants
- Enseignants
- Curieux de l’IA

---

## 🚀 Fonctionnalités principales

- Interface web professionnelle
- Modules séparés pour chaque sous-domaine majeur de l’IA
- Simulations, visualisations et interactions avec des intelligences
- Compatible mobile et déployable sur Render ou Vercel

---

## 🧠 Objectif éducatif

L’IA regroupe **plusieurs disciplines**. Ce projet les **illustre par l’expérience**. Chaque module simule le fonctionnement d’un composant de l’IA :

---

## 📚 Modules inclus

### 1. Représentation des connaissances
- **But** : illustrer comment l’IA encode les faits et les règles
- **Exemple** :
  - Fait : `homme(socrate)`
  - Règle : `homme(X) => mortel(X)`
  - Inférence : `mortel(socrate)`
- **Concepts abordés** : logique de premier ordre, base de faits, moteurs d'inférence

### 2. Raisonnement logique
- **But** : déduire des conclusions logiques à partir de propositions (syllogismes)
- **Exemple** :
  - Tous les hommes sont mortels
  - Socrate est un homme
  - → Conclusion : Socrate est mortel
- **Concepts abordés** : syllogisme, implication, logique déductive

### 3. Traitement du langage naturel (NLP)
- **But** : discuter avec un chatbot intelligent basé sur GPT
- **Utilise** : [OpenRouter.ai](https://openrouter.ai)
- **Concepts abordés** : compréhension du langage, génération de texte, modèles de langage

### 4. Vision par ordinateur
- **But** : détecter des objets dans une image
- **Utilise** : API de Hugging Face (`facebook/detr-resnet-50`)
- **Exemple** : image → ["person", "dog", "car"]
- **Concepts abordés** : reconnaissance visuelle, réseaux convolutifs

### 5. Apprentissage automatique
- **But** : prédire la classe d’un point (x, y) avec un modèle entraîné
- **Modèle** : classification binaire via `scikit-learn`
- **Concepts abordés** : entraînement supervisé, classification, features, modèles linéaires

### 6. Planification
- **But** : calculer un plan d’actions d’un point A à B dans un graphe
- **Exemple** : A → C → D → E
- **Concepts abordés** : algorithmes de recherche (BFS), graphe, agents intelligents

### 7. Robotique
- **But** : simuler les actions d’un robot dans un espace
- **Commandes** : avancer, tourner, ramasser
- **Concepts abordés** : perception-action, séquence d’actions, contrôle IA

---

## 🛠️ Technologies

- **Django** (backend et templates)
- **HTML/CSS Vanilla** (UI responsive)
- **OpenRouter** (API GPT)
- **Hugging Face** (détection objets)
- **Scikit-learn** (classification ML)
- **AJAX** (`fetch`) pour les échanges dynamiques

---

## ▶️ Lancer le projet en local

1. **Cloner le projet**

```bash
git clone https://github.com/EJM0101/explorateur-ia.git
cd explorateur-ia