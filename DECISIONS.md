# Journal des décisions

Je note ici chaque choix technique ou de méthode, avec l'alternative écartée et la raison, afin de garder la trace de l'avancement du projet au fur et à mesure.

## 2026-11-03

### uv pour gérer le projet Python

- **Choix** : uv pour installer Python, créer l'environnement et gérer les dépendances.
- **Alternative écartée** : pip avec venv et un fichier requirements.txt.
- **Raison** : un seul outil, et un fichier de verrouillage (`uv.lock`) qui fige les versions exactes. Le projet s'installera à l'identique sur le mini PC que j'achèterai ultérieurement.
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
- **Mise à jour du 2026-11-09** : les codes d'offres sont passés en minuscules (voir « Convention de nommage »).

### Dépôt public, notes personnelles hors du dépôt

- **Choix** : dépôt public sur le compte portfolio. La roadmap et mes notes de planification restent hors du dépôt.
- **Alternative écartée** : un dossier « ne pas commit » dans le dépôt, protégé par `.gitignore`.
- **Raison** : une règle dans un fichier de configuration peut être oubliée ou cassée par un `git add .`. Un fichier placé hors du dossier ne peut pas partir par erreur.

### Un dépôt Git parasite neutralisé

- **Constat** : mon dossier utilisateur était lui-même un dépôt Git vide, créé par erreur. Git l'aurait pris pour le dépôt du projet.
- **Choix** : renommer son dossier `.git` plutôt que le supprimer, puis créer le vrai dépôt dans `Inbox-to-CRM`.
- **Raison** : le renommage est réversible, et le dépôt vide ne contenait ni commit ni adresse distante.
- **Leçon** : lancer `git rev-parse --show-toplevel` avant de commiter dans un nouveau dossier.

## 2026-11-09

### Convention de nommage

- **Choix** : codes en minuscules, avec `_` comme séparateur dans les mots composés (par exemple `hors_sujet` au lieu de `hors-sujet`). La règle s'applique aux catégories, aux urgences et aux codes d'offres (`creation`, `compta`…), identiques dans le code et dans le jeu de vérité.
- **Alternative écartée** : des valeurs en majuscules dans le fichier CSV, pour une meilleure lisibilité.
- **Raison** : c'est la convention des développeurs, et une règle unique appliquée partout évite les fausses erreurs à l'évaluation.

### Information absente = None

- **Choix** : une information absente du mail vaut `None` dans le code et une cellule vide dans le CSV.
- **Alternative écartée** : une chaîne vide `""` ou une valeur comme `"aucune"`.
- **Raison** : deux façons de dire « rien » feraient compter des erreurs qui n'en sont pas. Les bibliothèques ne connaissent pas cette règle (le module `email` renvoie `""` pour un nom absent) : le code convertit avec `valeur or None`.

### Gestion de la langue

- **Choix** : retenir `fr`, `en` et `de`, plus une valeur `autre` pour toutes les autres langues. Les mails en langue `autre` sont escaladés vers un humain.
- **Alternative écartée** : la seule liste `fr`, `en`, `de`.
- **Raison** : avec une liste fermée, le LLM serait obligé de choisir l'une des trois langues pour un mail en italien ou en japonais. Une valeur fausse mais valide ne se voit pas ; `autre` lui donne une sortie honnête.
- **Règle générale** : information absente du mail → `None` ; information présente mais hors de la liste → `autre`.

### Champs « piege » et « scenario » hors de la fiche

- **Choix** : ces colonnes restent dans le jeu de vérité, mais ne font pas partie de la fiche extraite.
- **Raison** : elles décrivent le test, pas le mail. En production, elles n'existent pas. Elles restent utiles pour analyser les erreurs (le modèle rate-t-il surtout les pièges ?).

## 2026-11-10

### Clé d'API dans un fichier .env

- **Choix** : la clé d'API est dans `.env`, exclu de Git, et chargée par `python-dotenv`. Le dépôt contient seulement `.env.example`, qui liste les variables attendues sans leur valeur.
- **Alternative écartée** : la clé écrite dans le code.
- **Raison** : le dépôt est public. Une clé qui fuite peut être utilisée par n'importe qui, à mes frais.

### Commandes lancées depuis la racine du projet

- **Choix** : toutes les commandes (`uv run`, pytest, Git) se lancent depuis la racine, et les chemins dans le code sont relatifs à la racine.
- **Alternative écartée** : des chemins absolus, du type `C:\Users\...`.
- **Raison** : un chemin relatif dépend du dossier depuis lequel on lance la commande, donc une convention unique le rend prévisible. Un chemin absolu ne fonctionnerait ni sur le mini PC ni dans GitHub Actions, et exposerait mon nom d'utilisateur.

## 2026-11-12

### Clé d'API dédiée au projet

- **Choix** : une clé `inbox-to-crm`, distincte de celle de mes autres projets.
- **Raison** : si elle fuite, je la révoque sans casser mes autres projets, et la Console affiche le coût réel de ce projet.

### L'adresse de l'expéditeur n'est pas extraite par le LLM

- **Choix** : deux modèles. `Extraction` contient ce que remplit le LLM ; `Fiche` en hérite et ajoute l'email, recopié depuis l'en-tête du mail.
- **Alternatives écartées** : demander l'email au LLM puis l'écraser ; ou un second modèle complet qui recopierait tous les champs.
- **Raison** : le LLM remplit ce qu'il est seul à pouvoir déduire, le code remplit ce qu'il sait déjà de façon exacte. Le LLM pourrait prendre une adresse de signature alors que la réponse doit partir vers l'expéditeur. Un test vérifie que `Extraction` ne contient pas le champ `email`.

### Ordre de priorité des catégories

- **Choix** : quand plusieurs catégories s'appliquent, la consigne impose l'ordre rgpd, puis reclamation, puis devis, puis rendez_vous, puis question.
- **Raison** : un mail mélange souvent plusieurs intentions. Sans règle, le LLM choisirait au hasard d'un mail à l'autre. Cet ordre est celui appliqué dans le jeu de vérité.

### Résumé du besoin en français

- **Choix** : le résumé est toujours rédigé en français, quelle que soit la langue du mail.
- **Raison** : la personne qui valide sur Telegram travaille en français.

### Client Anthropic créé dans la fonction

- **Choix** : `Anthropic()` est créé dans `extract`, pas au moment de l'import du module. `load_dotenv()` est appelé par le script qui lance le programme.
- **Raison** : créé à l'import, le client exigerait une clé d'API dès qu'un test importe le module. Les tests casseraient dans GitHub Actions, même ceux qui n'appellent pas Claude.

### Injection de prompt

- **Choix** : la consigne demande de traiter le mail comme une donnée, mais la protection repose sur l'architecture : sorties structurées, aucun outil pendant l'extraction, liste fermée d'actions et validation humaine en v0.3.
- **Raison** : une consigne réduit le risque sans jamais l'éliminer. L'objectif est qu'une injection réussie ne puisse rien faire de grave. Deux mails piégés du jeu de test mesurent si la consigne tient.

### Limite RGPD connue

- **Constat** : le corps du mail est transmis au LLM, données personnelles comprises. Retirer des champs du schéma ne changerait rien, puisque le LLM lit tout le mail.
- **Choix** : acceptable sur des données 100 % fictives.
- **En production, il faudrait** : un contrat de traitement avec le fournisseur du LLM, une durée de conservation des traces, et une pseudonymisation avant l'envoi.

## À trancher plus tard

- **Version de Python** : le projet utilise la version trouvée sur le PC (3.14). `pydantic` et `anthropic` s'installent sans problème. Reste à vérifier `psycopg` et `pgvector` en v0.2. En cas de blocage, passer à 3.13 avec `uv python pin 3.13`.
