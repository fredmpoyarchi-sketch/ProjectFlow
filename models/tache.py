from exceptions.exceptions import TacheInvalideError

class Tache:
    """Représente une tâche appartenant à un projet."""

    def __init__(self, titre: str, description: str) -> None:
        """
        Initialise une nouvelle tâche.

        Args:
            titre: Le titre de la tâche.
            description: La description de la tâche.

        Raises:
            ValueError: Si le titre ou la description est vide.
        """
        self.titre = titre
        self.description = description
        self.terminee = False

    # -------------------------------------------------
    # ENCAPSULATION DU TITRE
    # -------------------------------------------------

    @property
    def titre(self) -> str:
        """Retourne le titre de la tâche."""
        return self._titre

    @titre.setter
    def titre(self, nouveau_titre: str) -> None:
        """
        Modifie le titre après validation.

        Raises:
            ValueError: Si le titre est vide.
        """
        if not nouveau_titre.strip():
            raise TacheInvalideError(
                "Le titre de la tâche ne peut pas être vide."
            )

        self._titre = nouveau_titre.strip()

    # -------------------------------------------------
    # ENCAPSULATION DE LA DESCRIPTION
    # -------------------------------------------------

    @property
    def description(self) -> str:
        """Retourne la description de la tâche."""
        return self._description

    @description.setter
    def description(self, nouvelle_description: str) -> None:
        """
        Modifie la description après validation.

        Raises:
            ValueError: Si la description est vide.
        """
        if not nouvelle_description.strip():
            raise TacheInvalideError(
                "La description de la tâche ne peut pas être vide."
            )

        self._description = nouvelle_description.strip()

    # -------------------------------------------------
    # MÉTHODES
    # -------------------------------------------------

    def terminer(self) -> None:
        """Marque la tâche comme terminée."""
        self.terminee = True

    def afficher(self) -> None:
        """Affiche les informations de la tâche."""
        statut = "Terminée" if self.terminee else "À faire"

        print(f"Tâche : {self.titre}")
        print(f"Description : {self.description}")
        print(f"Statut : {statut}")


# -------------------------------------------------
# TESTS
# -------------------------------------------------

