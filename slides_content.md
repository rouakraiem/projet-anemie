# Plan de Présentation Soutenance Anémie (7-8 Slides)

## Slide 1 : Titre du Projet
- **Titre** : Prédiction de l'Anémie par Machine Learning
- **Sous-titre** : Utilisation de données hématologiques pour un diagnostic assisté
- **Présenté par** : Roua Kraiem & Rania Mani
- **Encadré par** : M. Abdallah Khemais
- **Date** : Juin 2026

## Slide 2 : Contexte et Problématique
- **Contexte** : L'anémie touche 1,8 milliard de personnes.
- **Enjeu** : Diagnostic rapide et accessible.
- **Problématique** : Peut-on automatiser la détection de l'anémie à partir d'une simple numération sanguine (NFS) ?

## Slide 3 : Présentation du Dataset
- **Source** : Kaggle (Anemia Dataset).
- **Volume** : 1421 patients.
- **Variables clés** : Hémoglobine (Hb), MCH, MCHC, MCV, Genre.
- **Répartition** : 43.6% anémiques / 56.4% sains.

## Slide 4 : Analyse Exploratoire (EDA)
- **Visualisation** : Corrélation forte entre l'Hémoglobine et le diagnostic.
- **Observation** : Les patients anémiques présentent des taux d'Hb significativement plus bas.
- **Nettoyage** : Traitement des outliers par capping pour stabiliser les modèles.

## Slide 5 : Méthodologie et Prétraitement
- **Pipeline** : 
    1. Scaling (StandardScaler) des variables numériques.
    2. Split Train/Test (80/20) stratifié.
- **Algorithmes testés** : Logistic Regression, Random Forest, XGBoost, SVM.

## Slide 6 : Résultats et Comparaison
- **Comparaison** : Random Forest et XGBoost affichent les meilleures performances.
- **Métriques** : F1-Score et Recall de 100% (sur ce jeu de données).
- **Choix final** : Random Forest pour sa robustesse et son interprétabilité.

## Slide 7 : Démonstration Application (Bonus)
- **Outil** : Streamlit.
- **Fonctionnalité** : Interface web permettant de saisir ses résultats NFS et d'obtenir une prédiction instantanée avec probabilité.

## Slide 8 : Conclusion et Perspectives
- **Conclusion** : Objectifs atteints avec un modèle très performant.
- **Perspectives** : 
    - Tester sur des datasets plus complexes (différents types d'anémie).
    - Intégrer plus de variables cliniques.
    - Déploiement réel en milieu médical.
