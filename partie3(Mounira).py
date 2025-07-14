def main():
    graphe = GrapheOriente()
    print("\n" + "═"*50)
    print("GESTION DE GRAPHE ORIENTÉ".center(50))
    print("═"*50)
    graphe.creer_graphe_personnalise()
    graphe.visualiser()

if __name__ == "__main__":
    main() 