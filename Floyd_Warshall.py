from Matrice import villes, M

def floyd_warshall():
    n = len(villes)
    # Initialisation de la matrice des distances
    # Si i==j distance 0, si arête existe distance M[i][j], sinon infini
    dist = [[float('inf')] * n for _ in range(n)]
    
    for i in range(n):
        dist[i][i] = 0
        for j in range(n):
            if M[i][j] > 0:
                dist[i][j] = M[i][j]

    # Algorithme principal (3 boucles imbriquées)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

# --- TEST ---
print("\n--- Floyd-Warshall ---")
matrice_distances = floyd_warshall()
# Exemple d'affichage: Distance Rennes -> Lyon
d = villes.index("Rennes")
a = villes.index("Lyon")
print(f"Distance calculée Rennes -> Lyon : {matrice_distances[d][a]}")