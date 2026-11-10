from pathlib import Path

from inbox_to_crm.mails import lire_eml


def test_lire_eml_decode_nom_accentue():
    mail = lire_eml(Path("data/mails/017.eml"))
    assert mail.nom_expediteur == "Gérard Blanc"
