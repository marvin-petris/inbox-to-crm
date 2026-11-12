"""Modèles de données du projet Inbox-to-CRM."""

from typing import Literal

from pydantic import BaseModel


class Extraction(BaseModel):
    """Ce que le LLM extrait d'un mail : tout, sauf ce que le code connaît déjà."""

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


class Fiche(Extraction):
    """Fiche complète : l'extraction du LLM, plus l'adresse de l'expéditeur lue dans l'en-tête."""

    # Toujours présent : c'est l'adresse de l'expéditeur, dans l'en-tête.
    # cette valeur fait foi pour l'envoi de la réponse.
    email: str


class Mail(BaseModel):
    """Informations expediteur extrait d'un mail entrant ainsi que le contenu du mail (sujet et corps)."""

    nom_expediteur: str | None = None
    adresse_expediteur: str
    sujet: str | None = None
    contenu: str | None = None
