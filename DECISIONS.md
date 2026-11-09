# Journal des décisions

Je note ici chaque choix technique ou de méthode, avec l'alternative écartée et la raison afin de ne pas oublié l'avancement du projet au fur et à mesure de son avancé.

## 2026-11-03

### uv pour gérer le projet Python

- **Choix** : uv pour installer Python, créer l'environnement et gérer les dépendances.
- **Alternative écartée** : pip avec venv et un fichier requirements.txt.
- **Raison** : un seul outil, et un fichier de verrouillage (`uv.lock`) qui fige les versions exactes. Le projet s'installera à l'identique sur un mini PC que j'acheterais ultérieurement.
- **À revoir si** : une bibliothèque ne s'installe pas correctement avec uv.

### Docker Desktop avec WSL2 pour Postgres et n8n

- **Choix** : faire tourner Postgres et n8n dans des conteneurs, sur mon PC puis sur le mini PC à terme.
- **Alternative écartée** : installer Postgres directement sur Windows.
- **Raison** : le même fichier `docker-compose.yml` servira en local et en production. Je ne refais pas l'installation, je recopie le fichier.
- **Test fait** : `docker run hello-world`, image téléchargée et conteneur créé.

### PME fictive : Fiduciaire AdminRAGnoir

- **Choix** : une fiduciaire luxembourgeoise inventée, avec 7 offres à code fixe (CREATION, DOMICILIATION, COMPTA, PAIE, TVA, BILAN, CONSEIL).
- **Alternative écartée** : le nom « Valtis », abandonné parce qu'une société réelle porte ce nom.
- **Raison** : toutes les données du projet doivent être 100 % fictives, sans risque de confusion avec une vraie entreprise. La liste fermée d'offres donne des valeurs mesurables pour le champ « offre concernée ».
- **Fichier** : `docs/fiche_pme.md`.

### Dépôt public, notes personnelles hors du dépôt

- **Choix** : dépôt public sur le compte portfolio. La roadmap et mes notes de planification restent hors du dépôt.
- **Alternative écartée** : un dossier « ne pas commit » dans le dépôt, protégé par `.gitignore`.
- **Raison** : une règle dans un fichier de configuration peut être oubliée ou cassée par un `git add .`. Un fichier placé hors du dossier ne peut pas partir par erreur.

### Un dépôt Git parasite neutralisé

- **Constat** : mon dossier utilisateur était lui-même un dépôt Git vide, créé par erreur. Git l'aurait pris pour le dépôt du projet.
- **Choix** : renommer son dossier `.git` plutôt que le supprimer, puis créer le vrai dépôt dans `Inbox-to-CRM`.
- **Raison** : le renommage est réversible, et le dépôt vide ne contenait ni commit ni adresse distante.
- **Leçon** : lancer `git rev-parse --show-toplevel` avant de commiter dans un nouveau dossier.

## À trancher plus tard

- **Version de Python** : le projet utilise la version trouvée sur le PC (3.14). À vérifier au premier `uv add` en v0.1 : si une bibliothèque ne la supporte pas, passer à 3.13 avec `uv python pin 3.13`.
- pydantic 2.14.2 a bien été installé, reste à vérifier psycopg et pgvector le moment venu.

## 2026-11-09

### Convention de nommage

- **Choix** : Code en minuscule avec "_" en séparateur au lieu de "-" pour les mots composé (par exemple "hors_sujet" au lieu de "hors-sujet")
- **Alternative ecartée** : mettre les catégories dans le fichier CSV en majuscule pour une meilleure lisibilité.
- **Raison** : ça respecte les conventions de nommage des développeurs et ça me permet de ne pas faire d'erreur car je retranspose cette même règles aux fichiers du projet

### Gestion de la langue 

- **Choix** : Retenir uniquement EN, FR et DE, les autres sont prise en compte par le LLM mais les traitera dans "autres"
- **Raison** : Dans le cas d'un email d'une autre langue que les 3 autorisées, le LLM aurait choisis au hasard entre les 3 propositions, rajouter autre permet d'écartée ce scénario

### Choix des champs à utiliser dans le jeu de verité

- **Choix** : Les champs "piege" et "scenario" du CSV ont été écartés dans le traitement par le code Python
- **Raison** : Ces champs avaient été créés afin de générer des emails via LLM. Nous n'en avons pas l'utilité.

