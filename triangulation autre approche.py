# ... (les mêmes imports et déclarations)

def main():
    fichier_csv = "villes_coo.csv"  # Chemin relatif du fichier CSV

    villes = []
    rayons = []

    for i in range(1, 4):
        ville_nom = input(f"Entrer le nom de la ville #{i}: ")
        while True:
            try:
                ville_rayon = float(input(f"Entrer le rayon de {ville_nom} (km): "))
                break
            except ValueError:
                print(f"Veuillez entrer un nombre entier positif pour le rayon de {ville_nom}. Réessayez.")

        villes.append(ville_nom)
        rayons.append(ville_rayon)

    coords = [obtenir_coordonnees_de_csv(ville, fichier_csv) for ville in villes]

    if None not in coords:
        map = create_map(*zip(*coords))
        add_circles_and_markers(map, villes, rayons)
        save_map(map, "cartes_test.html")
        print("Carte générée avec succès et enregistrée au format HTML !")
    else:
        print("Impossible de trouver les coordonnées de l'une des villes demandées.")

# ... (la même fonction calculer_distance)

# Fonction supplémentaire pour simplifier l'ajout de cercles et de marqueurs
def add_circles_and_markers(map, villes, rayons):
    for ville, rayon, coord in zip(villes, rayons, coords):
        map.add_child(folium.Circle(location=coord, radius=rayon*1000, color="blue", fill=True))
        map.add_child(folium.Marker(location=coord, popup=ville, icon=folium.Icon(color="black")))

# Fonction supplémentaire pour enregistrer simplement la carte
def save_map(map, filename):
    map.save(filename)

if __name__ == "__main__":
    main()