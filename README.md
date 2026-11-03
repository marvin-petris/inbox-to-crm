# inbox-to-crm

Transforme les mails entrants en leads CRM, avec validation humaine

## Limites

Ce projet est une démonstration construite sur des données 100 % fictives. Voici ce qu'il ne prouve pas.

### Les mails de test sont générés par un LLM

Les 50 mails de test ont été générés par un modèle de langage, puis seront classés par un modèle de langage. Ce n'est pas indépendant : un mail écrit par un LLM est plus propre, plus explicite et plus typique qu'un vrai mail (pas de fautes, un seul sujet, des mots attendus). Le système les classe donc plus facilement qu'il ne classerait des mails réels, avec leurs chaînes de transferts, leurs ambiguïtés et leurs sujets mélangés. Le score affiché est une borne haute, pas une performance mesurée en conditions réelles.

Pour limiter ce biais, je prévois d'ajouter des mails écrits à la main, avec des fautes et des formulations ambiguës, et de les évaluer séparément des mails générés.

### 50 mails couvrent des scénarios, pas un taux

Le jeu de test couvre les cas importants : 9 catégories, contacts connus, spam, hors sujet, injections de prompt, 3 langues. Il sert à détecter les régressions et à vérifier chaque piège. Il est en revanche trop petit pour mesurer un taux de réussite fiable : sur 50 mails, une seule erreur fait déjà bouger le score de 2 points. Certaines catégories n'ont que 3 mails, donc une erreur y représente un tiers du résultat. Les chiffres par catégorie sont à lire comme des indications, pas comme des mesures.

### Les pièces jointes ne sont pas lues

Trois mails (013, 026, 049) mentionnent une pièce jointe, mais aucun fichier n'est réellement joint. Le système ne lit que le texte du mail. La lecture des pièces jointes (extraction de PDF, OCR, risques d'injection dans le contenu) est hors périmètre de la v1.0.

### Ce que le projet ne couvre pas non plus

- Aucun vrai client, aucune vraie donnée, aucune donnée d'un employeur : le projet ne dit rien de la qualité des réponses sur du courrier réel.
- Les tarifs et les règles de la base de connaissances sont inventés. Le système répond fidèlement à cette base, pas à la réalité d'un cabinet.
- La validation humaine est obligatoire avant toute action : le système propose, il ne décide pas.
