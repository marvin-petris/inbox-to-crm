# Catégories, champs et format du jeu de vérité

Données 100 % fictives. Ce document fixe les règles du jeu de vérité (`data/verite.csv`) : une ligne par mail, avec la bonne réponse pour chaque champ. Les mails sont générés à partir de ces lignes, jamais l'inverse.

## Catégories (valeur exacte à écrire dans le CSV)

| Code | Définition |
| --- | --- |
| devis | Demande de prix ou de proposition pour une offre précise. |
| question | Demande d'information (offres, tarifs, horaires, procédure) sans demande de devis. |
| reclamation | Mécontentement sur un service rendu, une facture ou un délai. |
| rendez_vous | Demande de prendre, déplacer ou annuler un rendez-vous. |
| candidature | Candidature spontanée ou réponse à une offre d'emploi. |
| prospection | Démarchage commercial légitime d'un fournisseur ou d'un partenaire. |
| rgpd | Demande d'accès, de rectification ou de suppression de données personnelles. |
| spam | Message de masse, arnaque ou hameçonnage, sans lien réel avec le cabinet. |
| hors_sujet | Message sans malveillance, adressé au cabinet par erreur ou sans rapport avec son activité. |

**Règle de priorité quand un mail mélange plusieurs sujets** : rgpd, puis reclamation, puis devis, puis rendez_vous, puis question. Exemple : un mail qui réclame ET demande un devis est classé reclamation.

## Champs

| Champ | Valeurs autorisées |
| --- | --- |
| id | Numéro à trois chiffres : 001 à 050. |
| categorie | Un des 9 codes ci-dessus. |
| urgence | haute, normale ou basse. |
| langue | fr, en ou de. |
| nom | Nom de l'expéditeur, vide s'il n'est pas donné. |
| societe | Société de l'expéditeur, vide si absente. |
| email | Adresse de l'expéditeur. Toujours en `.example`. |
| telephone | Numéro fictif, vide si absent. |
| besoin_resume | Une phrase courte qui résume la demande. |
| offre_concernee | Un des 7 codes de la fiche PME (CREATION, DOMICILIATION, COMPTA, PAIE, TVA, BILAN, CONSEIL) ou `aucune`. |
| piege | aucun, contact_connu, spam, hors_sujet ou injection. |
| scenario | 1 ou 2 lignes qui décrivent le mail à générer : qui écrit, ton, détails voulus. Ne fait pas partie de ce que le modèle doit retrouver. |

**Critère d'urgence** :
- haute : un délai légal ou une date limite sous 5 jours ouvrés est citée, ou le client menace de résilier ou de saisir un avocat.
- normale : cas par défaut.
- basse : demande générale sans échéance, prospection, spam, hors sujet.

## Répartition visée pour les 50 mails

| Catégorie | Nombre |
| --- | --- |
| devis | 11 |
| question | 10 |
| reclamation | 6 |
| rendez_vous | 6 |
| candidature | 3 |
| prospection | 5 |
| rgpd | 3 |
| spam | 3 |
| hors_sujet | 3 |

**Langues** : environ 30 en français, 15 en anglais, 5 en allemand.

**Pièges** (ils sont comptés dans les catégories ci-dessus, pas en plus) :
- 3 contacts déjà connus, dont les adresses sont reprises dans `data/crm_test.csv`.
- 3 spams.
- 2 hors sujet.
- 2 tentatives d'injection de prompt. Chacune est classée selon ce que le mail prétend être (par exemple un faux devis) et marquée `injection` dans la colonne piege.

## Format du fichier `data/verite.csv`

Encodage UTF-8, séparateur virgule, une ligne d'en-tête, guillemets autour d'une valeur qui contient une virgule.

```
id,categorie,urgence,langue,nom,societe,email,telephone,besoin_resume,offre_concernee,piege,scenario
001,devis,normale,fr,Claire Dumont,Boulangerie Dumont,claire.dumont@dumont-demo.example,,Demande de prix pour la comptabilité mensuelle d'une boulangerie,COMPTA,aucun,"Une gérante demande le prix de la compta mensuelle, ton cordial"
002,question,basse,en,Tom Reeves,,tom.reeves@reeves-demo.example,,Asks about opening hours and how to book a first call,aucune,aucun,"A freelancer asks when the office is open, short and informal"
003,spam,basse,fr,,,promo@gains-rapides-demo.example,,Promesse de gains rapides avec un investissement,aucune,spam,"Message de masse promettant un rendement garanti, ton agressif"
```
