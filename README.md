# Détecteur Automatisé d'Anomalies Astronomiques 🌌

**Projet de session - MGA 802 : Introduction à la programmation avec Python**

## Description du projet
Ce projet est une bibliothèque Python orientée objet conçue pour automatiser le traitement, l'analyse et la classification de courbes de lumière stellaire. Inspiré des méthodes de *Citizen Science*, notre algorithme vise à repérer des anomalies astronomiques (exoplanètes, microlentilles gravitationnelles liées à des trous noirs, et éruptions stellaires) au sein de données brutes issues des télescopes spatiaux tel que le téléscope TESS.
<img width="6016" height="4016" alt="TESS_alone_high_res (1)" src="https://github.com/user-attachments/assets/7a09a459-5070-4a32-b8d5-50f49f39b129" />
<img width="999" height="691" alt="image" src="https://github.com/user-attachments/assets/5ad33a7c-ec4a-4ebd-8039-eb3aad4ee2f7" />

## Fonctionnalités principales
- **Extraction automatisée :** Connexion et téléchargement de données réelles via l'API de la NASA (`lightkurve`).
- **Prétraitement :** Nettoyage des séries temporelles (lissage, gestion des données manquantes/trous d'observation).
- **Détection algorithmique :** Identification des variations anormales de luminosité par rapport à une ligne de base.
- **Classification :** Analyse de la forme de l'anomalie (Pic brutal, Creux en "U", Cloche symétrique) pour en déduire la nature de l'événement.
- **Visualisation :** Génération de graphiques clairs mettant en évidence les détections pour l'utilisateur.

## Équipe et Répartition des Tâches

Afin d'assurer une participation équitable et de couvrir tous les requis du cours (manipulation de données, algorithmique, architecture logicielle), les tâches ont été réparties de la manière suivante :

* **Maxence : Ingénierie des données et Prétraitement**
  * Implémentation du module de connexion aux API (récupération des fichiers `.fits` ou données Kaggle).
  * Développement des fonctions mathématiques de lissage et de normalisation du flux lumineux.
  * Création de la logique permettant d'ignorer les "trous" de données (interruptions d'observation du télescope).

* **Jules : Algorithmique et Modélisation (Machine Learning / Statistiques)**
  * Définition des seuils d'alerte pour la détection initiale des anomalies.
  * Implémentation du moteur de classification pour différencier les 3 événements (Éruption, Transit d'exoplanète, Trou noir).
  * Calcul de la probabilité ou de l'indice de confiance de la détection.

* **Alexandre : Architecture, Interface Utilisateur (CLI) et Visualisation**
  * Structuration globale du code en programmation orientée objet (création du module distribuable).
  * Développement de l'interaction utilisateur (gestion des paramètres d'entrée comme le numéro de l'astre, les dates, etc.).
  * Création du module de visualisation graphique (Matplotlib/Seaborn) pour afficher les courbes avant/après et surligner les anomalies détectées.

## Installation et Utilisation
*(À compléter lors de la phase de développement)*
1. Cloner le dépôt : `git clone https://fr.wikipedia.org/wiki/Repo_%28finance%29`
2. Installer les dépendances : `pip install -r requirements.txt`
3. Lancer une analyse d'exemple : `python main.py --target KIC_XXXXXXX`

## 📚 Références et Dépendances
- [[Lightkurve Documentation](https://docs.lightkurve.org/)](https://lightkurve.github.io/lightkurve/)
- Numpy, Pandas, Matplotlib, Scikit-Learn
