import pytest
from pydantic import ValidationError

from inbox_to_crm.models import Fiche
from inbox_to_crm.models import Extraction


def test_fiche_valide():
    f = Fiche(
        categorie="devis",
        urgence="normale",
        langue="fr",
        nom="Claire Dumont",
        societe="Boulangerie Dumont",
        email="claire.dumont@dumont-demo.example",
        besoin_resume="Demande de prix pour la comptabilité mensuelle d'une boulangerie",
        offre_concernee="compta",
    )
    assert f.telephone is None


def test_fiche_categorie_inconnue_refusee():
    with pytest.raises(ValidationError):
        Fiche(
            categorie="Devis",
            urgence="normale",
            langue="fr",
            nom="Claire Dumont",
            societe="Boulangerie Dumont",
            email="claire.dumont@dumont-demo.example",
            besoin_resume="Demande de prix pour la comptabilité mensuelle d'une boulangerie",
            offre_concernee="compta",
        )


def test_extraction_ne_demande_pas_email_au_llm():
    assert "email" not in Extraction.model_fields
