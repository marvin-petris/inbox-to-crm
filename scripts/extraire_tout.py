"""Extraction de tous les emails"""

from pathlib import Path

import anthropic
from dotenv import load_dotenv

from inbox_to_crm.extraction import extract
from inbox_to_crm.mails import lire_eml

load_dotenv()

# Tarif en dollar par million de token de haiku 5.5 récupéré sur la page officielle de claude.com (https://platform.claude.com/docs/fr/about-claude/pricing)
TARIF_TOKENS_ENTREE = 0.10
TARIF_TOKENS_SORTIE = 0.50

dossier_sortie = Path("data/fiches")
dossier_sortie.mkdir(exist_ok=True)
echecs = []
total_tokens_entree = 0
total_tokens_sortie = 0
nb_mails_traites = 0


for chemin in sorted(Path("data/mails").glob("*.eml")):
    mail = lire_eml(chemin)
    try:
        fiche, tokens_entree, tokens_sortie = extract(mail)
    except anthropic.APIError as erreur:
        print(chemin.stem, "ECHEC", erreur)
        echecs.append(chemin.stem)
        continue
    sortie = dossier_sortie / f"{chemin.stem}.json"
    sortie.write_text(fiche.model_dump_json(indent=2), encoding="utf-8")
    print(
        chemin.stem,
        "ok | Tokens entrée :",
        tokens_entree,
        "| Token sortie :",
        tokens_sortie,
    )
    total_tokens_entree = total_tokens_entree + tokens_entree
    total_tokens_sortie = total_tokens_sortie + tokens_sortie
    nb_mails_traites += 1

print(
    f"Tokens d'entrée : {total_tokens_entree} | Tokens de sortie : {total_tokens_sortie}"
)
cout_total = (
    TARIF_TOKENS_ENTREE * total_tokens_entree / 1000000
    + TARIF_TOKENS_SORTIE * total_tokens_sortie / 1000000
)
if nb_mails_traites > 0:
    cout_moyen_mail = cout_total / nb_mails_traites
    print(f"Cout moyen du mail : {cout_moyen_mail:.6f}$")
    print(f"Cout total du script : {cout_total:.6f}$")

print(f"{len(echecs)} échec(s) : {echecs}")
