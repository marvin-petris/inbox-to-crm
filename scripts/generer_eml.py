# ce script génère des fichiers .eml à partir d'un fichier CSV contenant des informations sur les emails à créer. le fichier CSV doit
# contenir les colonnes suivantes : id, nom, email, besoin_resume.
# le script crée un dossier "data/mails_generes" s'il n'existe pas et y enregistre les fichiers .eml générés.
# Ces mails ne servent pas à l’évaluation (corps français quelle que soit la langue)
import csv
from email.message import EmailMessage
from pathlib import Path

dossier = Path("data/mails_generes")
dossier.mkdir(parents=True, exist_ok=True)

with open("data/verite.csv", encoding="utf-8", newline="") as f:
    lecteur = csv.DictReader(f)
    for ligne in lecteur:
        msg = EmailMessage()
        if not ligne["nom"]:
            msg["From"] = f"<{ligne['email']}>"
        else:
            msg["From"] = f"{ligne['nom']} <{ligne['email']}>"
        msg["To"] = "demo@adminragnoir-demo.example"
        msg["Subject"] = f"demande : {ligne['besoin_resume'][:40]}"
        msg.set_content(
            ligne["besoin_resume"],
            cte="quoted-printable",
        )
        chemin = dossier / f"{ligne['id']}.eml"
        chemin.write_bytes(msg.as_bytes())
