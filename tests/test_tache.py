from models.tache import Tache
from exceptions.exceptions import TacheInvalideError


def test_creation_tache() -> None:
    """Teste la création d'une tâche valide."""

    tache = Tache(
        "Étudier le site",
        "Effectuer l'étude du terrain"
    )

    assert tache.titre == "Étudier le site"
    assert tache.description == "Effectuer l'étude du terrain"
    assert tache.terminee is False


def test_terminer_tache() -> None:
    """Teste qu'une tâche peut être terminée."""

    tache = Tache(
        "Préparer les plans",
        "Réaliser les plans architecturaux"
    )

    tache.terminer()

    assert tache.terminee is True


def test_modification_titre() -> None:
    """Teste la modification valide du titre."""

    tache = Tache(
        "Ancien titre",
        "Description de la tâche"
    )

    tache.titre = "Nouveau titre"

    assert tache.titre == "Nouveau titre"


def test_titre_invalide() -> None:
    """Teste qu'un titre vide est refusé."""

    try:
        Tache(
            "",
            "Description valide"
        )

        assert False, (
            "TacheInvalideError aurait dû être déclenchée."
        )

    except TacheInvalideError:
        pass


def test_description_invalide() -> None:
    """Teste qu'une description vide est refusée."""

    try:
        Tache(
            "Titre valide",
            ""
        )

        assert False, (
            "TacheInvalideError aurait dû être déclenchée."
        )

    except TacheInvalideError:
        pass


if __name__ == "__main__":

    test_creation_tache()
    test_terminer_tache()
    test_modification_titre()
    test_titre_invalide()
    test_description_invalide()

    print("Tous les tests de Tache sont passés avec succès.")