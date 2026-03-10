import pandas as pd
import folium
import math

# Fonction pour obtenir les coordonnées GPS de la ville depuis le fichier CSV
def obtenir_coordonnees_de_csv(nom_ville, fichier_csv):
    data = pd.read_csv(fichier_csv, sep=';')  # Assurez-vous que le séparateur correspond à votre fichier
    ville_data = data[data['ville'] == nom_ville]

    if not ville_data.empty:
        latitude = ville_data['latitude'].values[0]
        longitude = ville_data['longitude'].values[0]
        return latitude, longitude
    else:
        print(f"Coordonnées non trouvées pour {nom_ville}.")
        return None, None

# Fonction pour calculer la distance à vol d'oiseau entre deux coordonnées GPS
def calculer_distance(coord1, coord2):
    lat1, lon1 = math.radians(coord1[0]), math.radians(coord1[1])
    lat2, lon2 = math.radians(coord2[0]), math.radians(coord2[1])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    earth_radius_km = 6371.0  # Rayon moyen de la Terre en kilomètres

    distance_km = earth_radius_km * c
    return distance_km

# Fonction principale
def main():
    fichier_csv = "./villes_coo.csv"  # Remplacez par le chemin relatif ou absolu correct vers votre fichier CSV
    ville1 = input("Entrez le nom de la première ville : ")
    ville2 = input("Entrez le nom de la deuxième ville : ")

    # Obtenir les coordonnées GPS des deux villes depuis le fichier CSV
    latitude1, longitude1 = obtenir_coordonnees_de_csv(ville1, fichier_csv)
    latitude2, longitude2 = obtenir_coordonnees_de_csv(ville2, fichier_csv)

    if latitude1 is not None and longitude1 is not None and latitude2 is not None and longitude2 is not None:
        # Placer les deux villes sur la carte avec leur nom comme étiquette
        carte = folium.Map(location=[latitude1, longitude1], zoom_start=6)
        folium.Marker([latitude1, longitude1], popup=ville1).add_to(carte)
        folium.Marker([latitude2, longitude2], popup=ville2).add_to(carte)

        # Tracer une ligne entre les deux villes
        folium.PolyLine([(latitude1, longitude1), (latitude2, longitude2)], color="blue").add_to(carte)

        # Calculer et afficher la distance à vol d'oiseau
        coord1 = (latitude1, longitude1)
        coord2 = (latitude2, longitude2)
        distance_vol_oiseau = calculer_distance(coord1, coord2)
        print(f"La distance à vol d'oiseau entre {ville1} et {ville2} est d'environ {distance_vol_oiseau:.2f} kilomètres.")

        # Enregistrer la carte au format HTML
        carte.save("carte_villes_vol_oiseau.html")
        print(f"La carte a été enregistrée sous le nom 'carte_villes.html'.")
    else:
        print("Coordonnées non trouvées. Vérifiez le nom des villes ou le fichier CSV.")

if __name__ == "__main__":
    main()
