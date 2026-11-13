"""Extraction de tous les emails"""

from pathlib import Path

from dotenv import load_dotenv

from inbox_to_crm.extraction import extract
from inbox_to_crm.mails import lire_eml

load_dotenv()
dossier_sortie = Path("data/fiches")
dossier_sortie.mkdir(exist_ok=True)


for chemin in sorted(Path("data/mails").glob("*.eml"))[:2]:
    mail = lire_eml(chemin)
    extraction = extract(mail)
    sortie = dossier_sortie / f"{chemin.stem}.json"
    sortie.write_text(extraction.model_dump_json(indent=2), encoding="utf-8")
    print(chemin.stem, "ok")
