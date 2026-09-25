class Utilisateur:
    """Représente un utilisateur de ProjectFlow."""

    def __init__(self, nom: str, email: str) -> None:
        """Initialise un utilisateur."""
        self.nom = nom
        self.email = email

    def afficher_profil(self) -> None:
        """Affiche le profil de l'utilisateur."""
        print(f"Nom : {self.nom}")
        print(f"Email : {self.email}")


if __name__ == "__main__":
    utilisateur1 = Utilisateur(
        "Freddy",
        "freddy@example.com"
    )

    utilisateur1.afficher_profil()