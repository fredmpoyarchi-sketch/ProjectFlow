from models.utilisateur import Utilisateur


class Responsable(Utilisateur):
    """Représente un responsable de projet."""

    def __init__(
        self,
        nom: str,
        email: str,
        fonction: str
    ) -> None:
        """Initialise un responsable."""
        super().__init__(nom, email)
        self.fonction = fonction

    def afficher_profil(self) -> None:
        """Affiche le profil complet du responsable."""
        super().afficher_profil()
        print(f"Fonction : {self.fonction}")


if __name__ == "__main__":
    responsable1 = Responsable(
        "Freddy",
        "freddy@example.com",
        "Chef de projet"
    )

    responsable1.afficher_profil()