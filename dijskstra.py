import heapq
from Matrice import villes, M

##

def dijkstra(ville_depart,ville_arrive) :
    n = len(villes)

    # on recherche l'index des villes  dans notre liste villes
    try:

        dep = villes.index(ville_depart)
        arr = villes.index(ville_arrive)
    except ValueError:
        return "une des villes n'existe pas dans la matrice"

    # Initialisation
    distances = [float('inf')] * n  # stocke les distances entre la ville de depart et les autres villes dans la liste villes
    distances[dep] = 0
    predecesseurs = [-1] * n
    # File de priorité : (distance, index_ville)
    file_prioritaire = [(0, dep)]



    while file_prioritaire:
        dist_actuelle, u = heapq.heappop(file_prioritaire)

        # Si on a déjà trouvé un chemin plus court, on ignore
        if dist_actuelle > distances[u]:
            continue
            
        # Si on a atteint la destination, on peut s'arrêter (optimisation)
        if u == arr:
            break

        # Exploration des voisins
        for v in range(n):
            poids = M[u][v]
            if poids > 0:  # Il existe une route
                distance = dist_actuelle + poids
                
                # Si un chemin plus court est trouvé
                if distance < distances[v]:
                    distances[v] = distance
                    predecesseurs[v] = u
                    heapq.heappush(file_prioritaire, (distance, v))

    # Reconstruction du chemin 
    if distances[arr] == float('inf'):
        return f"Aucun chemin entre {ville_depart} et {ville_arrive}"

    chemin = []
    etape = arr
    while etape != -1:
        chemin.insert(0, villes[etape])
        etape = predecesseurs[etape]

    return {
        "chemin": " -> ".join(chemin),
        "distance_totale": distances[arr]
    }

# Test suggéré par l'énoncé : Bordeaux -> Lille 
resultat = dijkstra("Bordeaux", "Lille")
print(f"Trajet : {resultat['chemin']}")
print(f"Distance : {resultat['distance_totale']} km")
