## 🗺️ géolocalisation et triangulation (Python)

> TD Géolocalisation Python — Calcul de distances à vol d'oiseau et triangulation géographique entre villes françaises. Scripts Python avec `folium` (cartes interactives) et `pandas`. Lecture de fichier CSV de coordonnées GPS.

---

## 📁 Structure du projet

```
geo-triangulation-python/
│
├── villes_coo.csv                    # Base de données des villes françaises (latitude, longitude)
├── villes_vol_oiseau01.py            # Distance à vol d'oiseau + carte (sans affichage distance)
├── villes_vol_oiseau02.py            # Distance à vol d'oiseau + carte (avec marqueur distance)
├── triangulation.py                  # Triangulation à 3 villes avec saisie utilisateur
├── triangulation_autre_approche.py   # Refactorisation orientée fonctions
│
├── carte_villes_vol_oiseau.html      # Exemple de carte générée (vol d'oiseau)
├── carte_villes_distance.html        # Exemple de carte générée (avec distance)
└── carte_tri.html                    # Exemple de carte générée (triangulation)
```

---

## 🎯 Objectifs pédagogiques

- Lire et exploiter un fichier **CSV** avec Python (`csv` et `pandas`)
- Générer des **cartes interactives** avec la bibliothèque `folium`
- Appliquer le principe de **triangulation géographique**
- Analyser et améliorer du code Python existant

---

## 🚀 Installation

```bash
git clone https://github.com//geo-triangulation-python.git
cd geo-triangulation-python
pip install folium pandas
```

---

## ▶️ Utilisation

### Distance à vol d'oiseau

```bash
python villes_vol_oiseau02.py
```
Entrez le nom de deux villes françaises (telles qu'elles apparaissent dans `villes_coo.csv`). Une carte HTML est générée avec le segment et la distance.

**Exemple :**
```
Entrez le nom de la première ville : Angers
Entrez le nom de la deuxième ville : Le Mans
→ Distance : 80.26 km  →  carte_villes_distance.html
```

### Triangulation

```bash
python triangulation.py
```
Entrez le nom de 3 villes de référence et un rayon en km pour chacune. La carte affiche les trois cercles dont l'intersection localise le point recherché.

**Exemple :**
```
Ville #1 : Bayonne   — rayon : 200 km
Ville #2 : Tarbes    — rayon : 250 km
Ville #3 : Dax       — rayon : 300 km
→  carte_tri.html
```

---

## 🧮 Formule de Haversine (donnée dans l'énoncé - L'étudiant n'a pas à la connaître)

Permet de calculer la distance entre deux points GPS sur la sphère terrestre (R ≈ 6371 km) :

```
a = sin(Δlat/2)² + cos(lat1) × cos(lat2) × sin(Δlon/2)²
c = 2 × atan2(√a, √(1−a))
distance = R × c
```

Les coordonnées doivent être converties en **radians** avant le calcul.

---

## 📦 Dépendances

| Bibliothèque | Usage |
|---|---|
| `folium` | Génération de cartes interactives (Leaflet.js) |
| `pandas` | Lecture du fichier CSV |
| `math` | Fonctions trigonométriques (Haversine) |

---

## 📄 Format du fichier CSV

```
ville;latitude;longitude
Angers;47.476657084;-0.556221025
Le Mans;47.988675810;0.200118821
...
```

Séparateur `;` — encodage `UTF-8 BOM`.

---

## 📝 Licence

Licence libre. Servez-vous 😃
#
👤 Auteur : SERRES Régis - Lycée E de Constant, La Flèche (72) - https://serres-regis-prof-estournelles.github.io/

