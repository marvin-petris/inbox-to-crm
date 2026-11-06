# Lexique du projet Inbox-to-CRM

Mis à jour au fil du projet. État au 6/11/2026, fin de Phase 0.

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
| Volume | Espace de stockage séparé du conteneur. Un volume **anonyme** (nom en hexadécimal) est créé automatiquement par l'image, survit à `docker compose down` et devient orphelin : un nouveau est créé à chaque `up`. Un volume **nommé**, déclaré dans le fichier, est réutilisé : c'est ce qu'on utilisera en v0.2 pour les données Postgres. |
| Docker Compose | Fichier `docker-compose.yml` qui décrit un ou plusieurs services et leur réseau. `up` les lance, `down` les supprime. Même moteur que `docker run`, mais reproductible et versionnable dans Git. |
| Tag d'image | La version après les deux-points (`postgres:16`). Sans tag, Docker prend `latest`, qui change avec le temps. |
| Réseau Compose | Réseau créé automatiquement par projet (`docker-tests_default`), qui permet aux services de se joindre par leur nom. |
| Service (Compose) | Un bloc du fichier (ex. `db`) qui décrit un conteneur : image, variables, ports. |

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

## Notions Python

| Terme | Définition |
| --- | --- |
| Module | Fichier de code réutilisable. `import csv` le charge entièrement, `from pathlib import Path` n'en prend qu'un élément. |
| Bibliothèque standard | Modules fournis avec Python (`csv`, `pathlib`, `email`). Ce qui s'installe avec `uv add` vient de l'extérieur. |
| `with open(...) as f:` | Ouvre un fichier et le ferme automatiquement à la fin du bloc. Toujours préciser `encoding="utf-8"`. |
| `csv.DictReader` | Lit un CSV et rend chaque ligne sous forme de dictionnaire, avec les noms de colonnes de l'en-tête. |
| Dictionnaire | Paires clé et valeur : `ligne["nom"]`. |
| f-string | Texte précédé de `f` où `{variable}` est remplacé par sa valeur. Sans le `f`, les accolades restent du texte, ou créent un ensemble. |
| Tranche | `texte[:40]` : les 40 premiers caractères. |
| `Path` (pathlib) | Objet qui représente un chemin. `dossier / "fichier.eml"` assemble des morceaux. `mkdir(parents=True, exist_ok=True)` crée le dossier sans erreur s'il existe. |
| Classe et objet | Une classe est un modèle, un objet en est un exemplaire. Analogie : l'image Docker et le conteneur. |
| Valeur « fausse » | Une chaîne vide est fausse dans un `if`. `if not nom:` teste « vide ». `nom == False` est toujours faux pour une chaîne, sans erreur. |
| Chemin relatif | Calculé depuis le dossier où l'on lance la commande, pas depuis l'endroit du script. |

## Notions e-mail

| Terme | Définition |
| --- | --- |
| `MIME-Version`, `Content-Type`, `Content-Transfer-Encoding` | En-têtes qui décrivent comment lire le mail : version de la norme, type et jeu de caractères, encodage du corps. |
| `7bit` / `8bit` | Texte brut. `7bit` : ASCII seulement. `8bit` : octets UTF-8 tels quels. |
| `quoted-printable` | N'encode que les caractères spéciaux (`é` devient `=C3=A9`), le reste reste lisible. Coupe les lignes de plus de 76 caractères avec un `=` final. |
| `base64` | Encode tout le corps en blocs illisibles. |
| `print(msg)` contre `as_bytes()` | `print` convertit en texte et peut afficher du base64 alors que l'objet est en `8bit`. Le fichier écrit dépend de la méthode d'écriture. On impose donc `cte="quoted-printable"`. |

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
| `docker run --name N -e VAR=val -p 5432:5432 -d --rm image` | PowerShell | Lance un conteneur : nom, variable d'environnement, port (PC:conteneur), arrière-plan, suppression à l'arrêt. L'image se met en dernier. |
| `docker stop N` | PowerShell | Arrête un conteneur. |
| `docker logs N` | PowerShell | Affiche les messages du conteneur. |
| `docker compose up -d` | Dossier du fichier | Lance les services du `docker-compose.yml` en arrière-plan. |
| `docker compose ps` | Dossier du fichier | Liste les conteneurs du projet. |
| `docker compose down` | Dossier du fichier | Supprime conteneurs et réseau. Les volumes restent. |
| `docker compose down -v` | Dossier du fichier | Supprime aussi les volumes rattachés aux conteneurs du moment. Les volumes orphelins restent. |
| `docker volume ls` | PowerShell | Liste les volumes. |
| `docker volume rm NOM` | PowerShell | Supprime un volume précis, définitivement. Docker refuse si un conteneur l'utilise. |
| `docker volume prune` | PowerShell | Supprime tous les volumes inutilisés, sans distinction. À éviter quand on a des données. |
| `uv run python scripts/generer_eml.py` | Racine du dépôt | Lance le script avec l'environnement du projet. |

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
- Terminal de VS Code : l'extension Python tape elle-même la commande d'activation du `.venv`. Si tu tapes ta commande trop tôt, elle se colle à la sienne (`Jeton inattendu`). Attendre la fin de l'activation, puis relancer.
- `docker` ne répond pas (`failed to connect to the docker API`) après un redémarrage : lancer Docker Desktop et attendre « Running ».
- Volumes anonymes orphelins après `down` : à nettoyer avec `docker volume rm`. Volume nommé en v0.2.
- `docker run` sans image : `requires at least 1 argument`. L'image est en dernier.
- `if nom == False` ne plante pas et ne fonctionne pas. Utiliser `if not nom:`.
- Retirer un `f` devant une f-string oblige à retirer aussi les accolades : `{valeur}` seul est un ensemble, pas du texte.
- Ruff : le linter signale des erreurs, le formateur (Maj + Alt + F) corrige l'espacement. Les deux sont distincts.
- Lire un `.eml` brut avec un `=` en fin de ligne : c'est la coupure du quoted-printable. Toujours lire les mails avec le module `email`.
- Pas de vrais noms dans un dépôt public : noms inventés uniquement.
