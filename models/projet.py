from models.responsable import Responsable
from models.tache import Tache


class Projet:
    """Représente un projet contenant plusieurs tâches."""

    def __init__(
        self,
        nom: str,
        responsable: Responsable
    ) -> None:
        """Initialise un nouveau projet."""
        self.nom = nom
        self.responsable = responsable
        self.taches: list[Tache] = []

    def ajouter_tache(self, tache: Tache) -> None:
        """Ajoute une tâche au projet."""
        self.taches.append(tache)

    def nombre_taches(self) -> int:
        """Retourne le nombre total de tâches du projet."""
        return len(self.taches)

    def afficher_taches(self) -> None:
        """Affiche toutes les tâches du projet."""
        for tache in self.taches:
            tache.afficher()

    def calculer_progression(self) -> float:
        """Calcule le pourcentage de tâches terminées."""

        if not self.taches:
            return 0.0

        nombre_terminees = 0

        for tache in self.taches:
            if tache.terminee:
                nombre_terminees += 1

        progression = (
            nombre_terminees / len(self.taches) * 100
        )

        return progression

    def afficher_resume(self) -> None:
        """Affiche un résumé du projet."""
        print("=" * 40)
        print(f"Projet : {self.nom}")
        print(f"Responsable : {self.responsable.nom}")
        print(f"Nombre de tâches : {self.nombre_taches()}")
        print(
            f"Progression : "
            f"{self.calculer_progression():.2f} %"
        )
        print("=" * 40)

    def afficher_projet_complet(self) -> None:
        """Affiche toutes les informations du projet."""
        print("=" * 40)
        print("PROJECTFLOW")
        print("=" * 40)

        print(f"\nProjet : {self.nom}")
        print(f"Responsable : {self.responsable.nom}")
        print(f"Fonction : {self.responsable.fonction}")

        print("\nTâches :")

        if not self.taches:
            print("Aucune tâche enregistrée.")
        else:
            for tache in self.taches:
                print()
                tache.afficher()

        print(
            f"\nProgression : "
            f"{self.calculer_progression():.2f} %"
        )

        print("=" * 40)


if __name__ == "__main__":

    # Création du responsable
    responsable = Responsable(
        "Freddy",
        "freddy@example.com",
        "Chef de projet"
    )

    # Création du projet
    projet = Projet(
        "Construction Cité A",
        responsable
    )

    # Création des tâches
    tache1 = Tache(
        "Étudier le site",
        "Effectuer l'étude préliminaire du terrain"
    )

    tache2 = Tache(
        "Préparer les plans",
        "Réaliser les plans architecturaux"
    )

    tache3 = Tache(
        "Établir le budget",
        "Préparer le budget prévisionnel du projet"
    )

    # Ajout des tâches au projet
    projet.ajouter_tache(tache1)
    projet.ajouter_tache(tache2)
    projet.ajouter_tache(tache3)

    # Simulation de l'avancement
    tache1.terminer()
    tache2.terminer()

    # Affichage du projet
    projet.afficher_projet_complet()