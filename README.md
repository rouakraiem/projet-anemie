# 🩸 Prédiction de l'Anémie avec Machine Learning

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.8.0-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Kaggle](https://img.shields.io/badge/Dataset-Kaggle-blue.svg)](https://www.kaggle.com/datasets/biswaranjanrao/anemia-dataset)

---

## 📌 Description du Projet

Ce projet utilise le **Machine Learning** pour prédire la présence d'une anémie chez un patient à partir de paramètres sanguins simples (numération globulaire).

L'objectif est de développer un modèle **fiable**, **interprétable** et **performant** pour aider au dépistage précoce de l'anémie, un trouble qui touche près de **1,8 milliard de personnes dans le monde** selon l'OMS, en particulier les femmes et les enfants dans les pays en développement.

### 🎯 Problématique
> **"Comment prédire si un patient est anémique à partir de ses résultats de numération sanguine ?"**

### 🏆 Résultats Clés
- **Meilleur modèle** : Random Forest
- **Accuracy** : 100%
- **F1-Score** : 100%
- **Recall** : 100% *(détecte 100 malades sur 100 sur ce jeu de test)*
- **ROC-AUC** : 100%

> ⚠️ **Remarque d'analyse** : ces scores quasi parfaits s'expliquent par le fait que l'**Hémoglobine** est, par définition clinique, le marqueur central du diagnostic d'anémie. Elle est très fortement corrélée à la cible (corrélation de -0,80) et sépare presque parfaitement les deux classes à elle seule (voir `boxplots.png`). Ce projet reste donc pertinent pédagogiquement pour la méthodologie (EDA → preprocessing → modélisation), mais les performances ne doivent pas être interprétées comme représentatives d'un cas de diagnostic médical complexe.

---

## 📊 Dataset

### Source
- **Plateforme** : [Kaggle](https://www.kaggle.com/)
- **Dataset** : [Anemia Dataset](https://www.kaggle.com/datasets/biswaranjanrao/anemia-dataset) (par Biswa Ranjan Rao)
- **Miroir utilisé** : [GitHub - maladeep/anemia-detection-with-machine-learning](https://github.com/maladeep/anemia-detection-with-machine-learning)

### Caractéristiques

| Caractéristique | Valeur |
|-----------------|--------|
| **Patients** | 1421 |
| **Variables** | 5 |
| **Variables catégorielles** | 1 (Gender) |
| **Variables numériques** | 4 |
| **Variable cible** | Result (0 = Sain, 1 = Anémique) |
| **Distribution** | 43,6% anémiques / 56,4% sains |

### Variables

| Variable | Description | Type |
|----------|-------------|------|
| **Gender** | Sexe du patient (0 = Femme, 1 = Homme) | Binaire |
| **Hemoglobin** | Taux d'hémoglobine (g/dl) | Numérique |
| **MCH** | Mean Corpuscular Hemoglobin — teneur moyenne en hémoglobine par globule rouge | Numérique |
| **MCHC** | Mean Corpuscular Hemoglobin Concentration — concentration moyenne en hémoglobine | Numérique |
| **MCV** | Mean Corpuscular Volume — volume moyen des globules rouges | Numérique |
| **Result** | **CIBLE** : 0 = Sain, 1 = Anémique | Binaire |

---

## 🛠️ Méthodologie

### 1. Analyse Exploratoire (EDA)
- Analyse de la distribution des variables
- Identification des corrélations avec la cible
- Détection des valeurs manquantes et outliers
- Visualisations des relations clés (notamment Hémoglobine vs diagnostic)

### 2. Prétraitement des Données

| Étape | Méthode | Description |
|-------|---------|-------------|
| **Valeurs manquantes** | Aucune | Dataset déjà propre (0 valeur manquante) |
| **Outliers** | Winsorization (capping) | Bornes : Q1 − 1,5×IQR / Q3 + 1,5×IQR |
| **Encodage** | Aucun nécessaire | `Gender` déjà encodé en 0/1 dans le dataset source |
| **Standardisation** | StandardScaler | Moyenne = 0, Écart-type = 1 (sur les 4 variables numériques) |
| **Split** | Train/Test (80/20) | 1136 patients train / 285 patients test |

### 3. Modélisation

#### Modèles Testés

| Modèle | Type | Description |
|--------|------|--------------|
| **Logistic Regression** | Linéaire | Simple, rapide, interprétable |
| **Random Forest** | Ensemble (Bagging) | 100 arbres de décision |
| **Gradient Boosting** | Ensemble (Boosting) | Arbres séquentiels |
| **XGBoost** | Ensemble (Boosting) | Version optimisée |
| **SVM** | Marge | Séparateur à vaste marge |

#### Optimisation
- **Validation** : Train/Test split stratifié (80/20)
- **Métrique de sélection** : F1-Score

---

## 📈 Résultats

### Tableau Comparatif des Modèles

| Modèle | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|--------|----------|-----------|--------|----------|---------|
| **Random Forest** | **100%** | **100%** | **100%** | **100%** | **100%** |
| Gradient Boosting | 100% | 100% | 100% | 100% | 100% |
| XGBoost | 100% | 100% | 100% | 100% | 100% |
| Logistic Regression | 98,60% | 96,88% | 100% | 98,41% | 100% |
| SVM | 98,60% | 96,88% | 100% | 98,41% | 99,99% |

### 🏆 Meilleur Modèle : Random Forest

**Performances Finales :**

```python
Accuracy  : 100.00%
Precision : 100.00%
Recall    : 100.00%  ← Le plus important en médecine !
F1-Score  : 100.00%
ROC-AUC   : 100.00%
```

### 🔍 Variable la plus discriminante : Hémoglobine

La matrice de corrélation et les boxplots confirment que **l'Hémoglobine** porte presque seule le pouvoir prédictif du modèle, ce qui est cohérent avec sa définition clinique (l'anémie *est* un déficit en hémoglobine). Les autres variables (MCH, MCHC, MCV) apportent un complément plus marginal.

---

## 🚀 Application Web (Bonus)

Une application interactive a été développée avec **Streamlit** pour permettre aux utilisateurs de tester le modèle avec leurs propres données.

### Comment lancer l'application localement :
1. Installer les dépendances : `pip install streamlit pandas joblib scikit-learn`
2. Lancer l'application : `streamlit run app.py`

---

## 📁 Structure du Projet

```
projet-anemie/
├── notebook/
│   ├── 01_EDA.ipynb                  # Brouillon : Analyse exploratoire
│   ├── 02_preprocessing.ipynb        # Brouillon : Prétraitement
│   ├── 03_modeling.ipynb             # Brouillon : Modélisation
│   └── Notebook_Final.ipynb          # Notebook final soigné et complet
├── app.py                            # Application Streamlit (Bonus)
├── README.md                         # Documentation du projet
├── data/
│   ├── raw/anemia.csv                # Données brutes
│   └── processed/                    # Données traitées
├── models/
│   └── best_model.pkl                # Pipeline de prédiction sauvegardé
└── [images].png                      # Visualisations générées
```

---

## 👩‍💻 Réalisé en binôme par
**Roua Kraiem** & **Rania Mani**
