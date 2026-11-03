# Lexique du projet Inbox-to-CRM

Mis à jour au fil du projet. État au 3/11/2026, fin de Phase 0.

## Outils

| Outil | C'est quoi | À quoi il sert dans le projet |
| --- | --- | --- |
| PowerShell | Terminal de Windows | Lancer les commandes d'installation et de test. En mode administrateur, il peut installer des composants système (WSL). |
| winget | Gestionnaire de paquets de Windows | Installer un logiciel en une commande (ici Docker Desktop). |
| Git | Outil de gestion de versions | Garder l'historique du code, poser des tags de version (v0.1, v0.2...). Déjà installé. |
| VS Code | Éditeur de code | Écrire le code. Les extensions Python et Ruff ajoutent l'aide à la saisie et le formatage. Déjà installé. |
| uv | Gestionnaire de projet Python | Installe Python, crée l'environnement virtuel du projet, gère les dépendances (remplace pip, venv et requirements.txt). Verrouille les versions dans `uv.lock` pour que le projet s'installe à l'identique partout. |
| WSL2 | Windows Subsystem for Linux, version 2 | Fait tourner un vrai noyau Linux dans Windows. Docker Desktop en a besoin, car les conteneurs sont des programmes Linux. |
| Ubuntu (dans WSL) | Distribution Linux installée avec WSL | Fournit un Linux sur ton PC. Le mini PC tournera sous Ubuntu Server : même univers. |
| Docker Desktop | Application qui installe et pilote Docker sur Windows | Fait tourner Postgres et n8n sur ton PC avant le mini PC. |
| GitHub | Site qui héberge des dépôts Git | Copie distante du projet (dépôt public `inbox-to-crm`), vitrine du portfolio. |
| Ruff | Outil qui vérifie et formate le code Python | Repère les erreurs de style et de syntaxe avant l'exécution, extension VS Code installée. |

## Notions Docker

| Terme | Définition |
| --- | --- |
| Client Docker | La commande `docker` que tu tapes. Elle envoie des ordres au démon. |
| Démon Docker (moteur) | Le programme qui crée et fait tourner les conteneurs. Doit être « Running » pour que les commandes marchent. |
| Image | Modèle figé en lecture seule : un programme et tout ce dont il a besoin. Ne tourne pas. Analogie : une recette, ou une classe en Python. |
| Conteneur | Instance créée à partir d'une image, en cours d'exécution ou arrêtée. Analogie : le plat cuisiné, ou un objet en Python. Une image peut donner plusieurs conteneurs. |
| Docker Hub | Dépôt public d'où le démon télécharge les images (ex. `hello-world`). |
| Volume (à voir en v0.2) | Espace de stockage qui survit au conteneur. Les données Postgres y vivront, car on supprime et recrée les conteneurs sans cesse. |
| Docker Compose (à voir en v0.2) | Fichier `docker-compose.yml` qui décrit plusieurs conteneurs lancés ensemble. |

## Autres notions

| Terme | Définition |
| --- | --- |
| PATH | Liste des dossiers où Windows cherche les commandes. Un terminal ouvert avant une installation ne connaît pas le nouveau PATH : il faut le fermer et le rouvrir. |
| Environnement virtuel | Dossier isolé qui contient les bibliothèques d'un seul projet, pour éviter les conflits entre projets. Géré par uv. |
| Virtualisation | Fonction du processeur dont WSL2 a besoin. Vérifiée dans le Gestionnaire des tâches, onglet Performance, CPU : doit être « Activé ». |
| Mot de passe Ubuntu / sudo | Mot de passe du compte créé à l'intérieur d'Ubuntu. Sert à lancer des commandes d'administration (`sudo`). Distinct de celui de Windows. |

## Notions Git

| Terme | Définition |
| --- | --- |
| Dépôt (repo) | Dossier suivi par Git, avec son historique (dossier caché `.git`). Un dossier ne doit contenir qu'un seul dépôt : pas de dépôt dans un dépôt. |
| Commit | Photo de l'état du projet à un instant, avec un message. Se crée avec `git commit`. |
| Index (staging) | Zone d'attente où `git add` place les fichiers à inclure dans le prochain commit. |
| `origin` | Nom donné par convention au dépôt distant (GitHub). |
| Branche `main` | Branche principale du projet. |
| Push / pull | `push` envoie tes commits vers GitHub. `pull` récupère ceux de GitHub (fetch puis merge) sans écraser ton travail non commité. |
| `.gitignore` | Liste des fichiers que Git ignore (`.venv`, `.env`...). |
| `.env` / `.env.example` | `.env` contient les vraies clés secrètes et n'est jamais commité. `.env.example` montre les noms attendus, sans valeurs, et est commité. |

## Notions uv et Python

| Terme | Définition |
| --- | --- |
| `pyproject.toml` | Fiche d'identité du projet : nom, version, version de Python requise, dépendances. |
| `uv.lock` | Versions exactes de toutes les dépendances, pour une installation identique partout. Se commite. |
| `.python-version` | Version de Python utilisée par le projet (3.14). |
| `.venv` | Environnement virtuel du projet. Ne se commite pas, uv le recrée. |
| Dépendance | Bibliothèque externe dont le projet a besoin. S'ajoute avec `uv add`. |

## Notions données et évaluation

| Terme | Définition |
| --- | --- |
| Fichier `.eml` | Format standard d'un e-mail enregistré : en-têtes puis corps. Les accents y sont encodés (RFC 2047 pour les en-têtes, quoted-printable pour le corps). Illisible à l'œil, correctement lu par le module `email` de Python. |
| Vérité terrain | Fichier `verite.csv` contenant la bonne réponse attendue pour chaque mail. Sert à mesurer le système. |
| Piège | Mail construit pour tester une faiblesse : contact connu, spam, hors sujet, injection de prompt. |
| Injection de prompt | Mail qui contient une instruction destinée au système (« ignore tes règles »). Le contenu d'un mail est une donnée, jamais un ordre. |
| Circularité | Biais quand le même type de modèle génère les données et les évalue : le score paraît meilleur qu'en réalité. À documenter dans le README. |
| RAG | Le système cherche d'abord les passages utiles dans la base de connaissances, puis rédige la réponse à partir d'eux. Prévu en v0.2. |
| Chunking | Découpage des documents en morceaux indexables. Ici, un morceau par section `##`. |

## Commandes

| Commande | Où | Ce qu'elle fait |
| --- | --- | --- |
| `uv --version` | PowerShell | Vérifie que uv est installé et affiche sa version. |
| `docker --version` | PowerShell | Vérifie que le client Docker est installé. Ne dit rien sur le moteur. |
| `git --version` | PowerShell | Vérifie que Git est installé. |
| `code --version` | PowerShell | Vérifie que VS Code est installé. |
| `code --list-extensions` | PowerShell | Liste les extensions VS Code installées (pour voir si Python et Ruff y sont). |
| `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 \| iex"` | PowerShell | Télécharge et lance l'installeur de uv. |
| `wsl --install` | PowerShell (administrateur) | Installe WSL2 et la distribution Ubuntu. |
| `wsl --update` | PowerShell | Met à jour WSL si déjà installé. |
| `wsl --status` | PowerShell | Affiche l'état de WSL, dont la version par défaut (doit être 2). |
| `winget install -e --id Docker.DockerDesktop` | PowerShell | Installe Docker Desktop (`-e` pour un nom exact, `--id` pour l'identifiant du paquet). |
| `exit` | Terminal Ubuntu | Ferme la session Ubuntu et revient à PowerShell. |
| `docker run hello-world` | PowerShell | Télécharge l'image `hello-world` si elle est absente, crée un conteneur, l'exécute, affiche le message. Un nouveau conteneur à chaque lancement. |
| `docker run --rm hello-world` | PowerShell | Même chose, mais supprime le conteneur dès qu'il s'arrête. |
| `docker images` | PowerShell | Liste les images stockées sur ton PC. |
| `docker ps -a` | PowerShell | Liste tous les conteneurs, y compris arrêtés (`-a` pour all). Sans `-a`, seuls ceux qui tournent. |
| `docker container prune` | PowerShell | Supprime tous les conteneurs arrêtés. |
| `uv init --package` | PowerShell | Crée la structure d'un projet Python dans le dossier. |
| `uv add <paquet>` | PowerShell | Ajoute une dépendance, met à jour `pyproject.toml` et `uv.lock`. |
| `uv run python script.py` | PowerShell | Lance un script avec l'environnement du projet. À utiliser à la place de `python`. |
| `git init -b main` | PowerShell | Crée un dépôt dans le dossier courant avec la branche `main`. |
| `git remote add origin <url>` | PowerShell | Relie le dépôt local à GitHub. |
| `git status` | PowerShell | Montre ce qui est modifié, prêt à être commité ou non suivi. À lancer avant tout `add` et tout `commit`. |
| `git add .` | PowerShell | Place tous les changements dans l'index. |
| `git commit -m "message"` | PowerShell | Crée un commit avec les changements de l'index. |
| `git push` | PowerShell | Envoie les commits vers GitHub. |
| `git pull` | PowerShell | Récupère et fusionne les commits de GitHub. Ne détruit pas le travail local non commité. |
| `git rev-parse --show-toplevel` | PowerShell | Affiche le dossier racine du dépôt actif. Contrôle de sécurité avant de commiter. |

## Pièges déjà rencontrés

- `docker` ou `uv` « n'est pas reconnu » juste après l'installation : fermer et rouvrir le terminal (PATH).
- `failed to connect to the docker API` : Docker Desktop n'est pas lancé, le démon est arrêté.
- Le nom d'image est `hello-world`, avec un tiret et sans espace ni `!`.
- Le dossier personnel était un dépôt Git parasite : tout `git status` y affichait des centaines de fichiers. Corrigé en renommant son `.git`. Vérifier avec `git rev-parse --show-toplevel`.
- `LF will be replaced by CRLF` : avertissement Git sans gravité, lié aux fins de ligne Windows.
- Accents illisibles (`Ã©`) dans un CSV ouvert avec Excel : importer le fichier en UTF-8 (origine 65001) et ne pas enregistrer depuis l'affichage corrompu.
- En-têtes `=?utf-8?...` et corps avec `=C3=A9` dans un `.eml` : c'est le format normal, pas une erreur.
- En Python, ouvrir les fichiers texte avec `encoding="utf-8"`.
- Commandes à risque, à ne jamais lancer sans comprendre : `git reset --hard`, `git restore`, `git push --force`.
