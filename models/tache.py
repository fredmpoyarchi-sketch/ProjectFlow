class Tache:
    """Représente une tâche appartenant à un projet."""

    def __init__(self, titre: str, description: str) -> None:
        """Initialise une nouvelle tâche."""
        self.titre = titre
        self.description = description
        self.terminee = False

    def terminer(self) -> None:
        """Marque la tâche comme terminée."""
        self.terminee = True

    def afficher(self) -> None:
        """Affiche les informations de la tâche."""
        print(f"Tâche : {self.titre}")
        print(f"Description : {self.description}")
        print(f"Terminée : {self.terminee}")


if __name__ == "__main__":
    tache1 = Tache(
        "Étudier le site",
        "Effectuer l'analyse préliminaire du terrain"
    )

    tache1.afficher()

    tache1.terminer()

    tache1.afficher()