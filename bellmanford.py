from Matrice import villes, M

import copy

def bellman_ford(ville_depart):
    n = len(villes)
    try:
        src = villes.index(ville_depart)
    except ValueError:
        return "Ville inconnue"

    # Initialisation
    distances = [float('inf')] * n
    distances[src] = 0
    predecesseurs = [-1] * n

    # Création d'une liste d'arêtes (u, v, poids) à partir de la matrice permettant a l'algoritme de ne recuperer que les poids non nuls dans la matrice M
    aretes = []
    for i in range(n):
        for j in range(n):
            if M[i][j] != 0: # Si une route existe
                aretes.append((i, j, M[i][j]))

    # Cette etape sert à traiter les differents arêtes de notre liste arêtes au fur et a mesure tout en optimisant la distance entre le sommet de depart et les autres sommets
    for _ in range(n - 1):
        for u, v, poids in aretes:
            if distances[u] != float('inf') and distances[u] + poids < distances[v]:
                distances[v] = distances[u] + poids
                predecesseurs[v] = u

    # Détection ET identification du cycle
    sommet_dans_cycle = None
    for u, v, poids in aretes:
        if distances[u] != float('inf') and distances[u] + poids < distances[v]:
            sommet_dans_cycle = v  # v fait partie du cycle
            break

    # Pas de cycle
    if sommet_dans_cycle is None:
        return distances  
    
    # Remonter pour trouver le cycle complet
    # On remonte n fois pour être sûr d'être dans le cycle
    for _ in range(n):
        sommet_dans_cycle = predecesseurs[sommet_dans_cycle]
    
    # Reconstruire le cycle
    cycle = [sommet_dans_cycle]
    v = predecesseurs[sommet_dans_cycle]
    while v != sommet_dans_cycle:
        cycle.append(v)
        v = predecesseurs[v]
    cycle.reverse()
    
    # Afficher le cycle
    noms_cycle = [villes[i] for i in cycle]
    print(f"Cycle négatif trouvé : {' → '.join(noms_cycle)} → {villes[cycle[0]]}")
    
    return cycle

