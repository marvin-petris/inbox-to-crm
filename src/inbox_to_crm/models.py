"""Modèles de données du projet Inbox-to-CRM."""

from typing import Literal

from pydantic import BaseModel


class Fiche(BaseModel):
    """Informations extraites d'un mail entrant, validées avant tout usage."""

    categorie: Literal[
        "devis",
        "question",
        "spam",
        "reclamation",
        "rgpd",
        "candidature",
        "prospection",
        "rendez_vous",
        "hors_sujet",
    ]
    urgence: Literal["basse", "normale", "haute"]

    # "autre" évite que le LLM soit forcé de choisir fr, en ou de
    # pour un mail en italien ou en japonais.
    langue: Literal["fr", "en", "de", "autre"]

    # Absent = None : l'info peut manquer dans le mail
    # (pas de signature, particulier sans société, pas de numéro).
    nom: str | None = None
    societe: str | None = None
    telephone: str | None = None

    # Toujours présent : c'est l'adresse de l'expéditeur, dans l'en-tête.
    email: str

    # Toujours rédigeable, même pour un spam : c'est ce que lit
    # la personne qui valide sur Telegram.
    besoin_resume: str

    # None quand le mail ne vise aucune offre
    # (spam, candidature, question générale).
    offre_concernee: (
        Literal[
            "creation",
            "domiciliation",
            "compta",
            "paie",
            "tva",
            "bilan",
            "conseil",
        ]
        | None
    ) = None


class Mail(BaseModel):
    """Informations expediteur extrait d'un mail entrant ainsi que le contenu du mail (sujet et corps)."""

    nom_expediteur: str | None = None
    adresse_expediteur: str
    sujet: str | None = None
    contenu: str | None = None
