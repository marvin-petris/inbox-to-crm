"""Lecture des mails entrants au format .eml."""

from email import message_from_bytes, policy
from pathlib import Path

from inbox_to_crm.models import Mail


def lire_eml(chemin: Path) -> Mail:
    """Lit un fichier .eml et renvoie son expéditeur, son sujet et son corps."""

    message = message_from_bytes(chemin.read_bytes(), policy=policy.default)
    expediteur = message["From"].addresses[0]

    m = Mail(
        nom_expediteur=expediteur.display_name or None,
        adresse_expediteur=expediteur.addr_spec,
        sujet=message["Subject"] or None,
        contenu=message.get_content() or None,
    )
    return m
