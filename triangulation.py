import folium
from math import *

def obtenir_coordonnees_de_csv(ville, fichier_csv):
    with open(fichier_csv, 'r', encoding='utf-8') as file:
        for line in file:
            values = line.strip().split(';')
            if values[0] == ville:
                try:
                    latitude = float(values[1])
                    longitude = float(values[2])
                    return latitude, longitude
                except (IndexError, ValueError):
                    print(f"Les coordonnées pour {ville} ne sont pas valides dans le fichier CSV.")
                    return None, None
    print(f"Les coordonnées pour {ville} n'ont pas été trouvées dans le fichier CSV.")
    return None, None

def calculer_distance(coord1, coord2):
    R = 6371  # Rayon de la Terre en kilomètres
    lat1, lon1 = radians(coord1[0]), radians(coord1[1])
    lat2, lon2 = radians(coord2[0]), radians(coord2[1])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance

def main():
    fichier_csv = "villes_coo.csv"  # Assurez-vous que le chemin du fichier est correct
    ville1 = input("Entrez le nom de la première ville : ")
    ville2 = input("Entrez le nom de la deuxième ville : ")
    ville3 = input("Entrez le nom de la troisième ville : ")

    # Demander le rayon pour chaque ville
    rayon_ville1 = float(input(f"Entrez le rayon en kilomètres pour {ville1} : "))
    rayon_ville2 = float(input(f"Entrez le rayon en kilomètres pour {ville2} : "))
    rayon_ville3 = float(input(f"Entrez le rayon en kilomètres pour {ville3} : "))

    coord1 = obtenir_coordonnees_de_csv(ville1, fichier_csv)
    coord2 = obtenir_coordonnees_de_csv(ville2, fichier_csv)
    coord3 = obtenir_coordonnees_de_csv(ville3, fichier_csv)

    if coord1 and coord2 and coord3:
        carte = folium.Map(location=[coord1[0], coord1[1]], zoom_start=10)

        # Ajout des cercles avec les rayons définis par l'utilisateur
        folium.Circle(location=[coord1[0], coord1[1]], radius=rayon_ville1 * 1000, color='blue', fill=True).add_to(carte)
        folium.Circle(location=[coord2[0], coord2[1]], radius=rayon_ville2 * 1000, color='red', fill=True).add_to(carte)
        folium.Circle(location=[coord3[0], coord3[1]], radius=rayon_ville3 * 1000, color='green', fill=True).add_to(carte)

        # Ajout des marqueurs pour chaque ville
        folium.Marker(location=[coord1[0], coord1[1]], popup=ville1).add_to(carte)
        folium.Marker(location=[coord2[0], coord2[1]], popup=ville2).add_to(carte)
        folium.Marker(location=[coord3[0], coord3[1]], popup=ville3).add_to(carte)

        # Enregistrement de la carte au format HTML
        carte.save("carte_tri.html")
        print(f"La carte a été enregistrée sous le nom 'carte_tri.html'.")
    else:
        print("Coordonnées non trouvées. Vérifiez le nom de la ville ou le fichier CSV.")

if __name__ == "__main__":
    main()

