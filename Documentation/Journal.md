# Journal de bord

## Choix de l’API

Nous avons choisi de construire une API de gestion d’équipe League of Legends. Le projet s’articule autour de trois ressources principales : les champions, les objets et les équipes.

- Les champions sont des personnages avec un nom, un titre, des rôles, des lanes, des statistiques et une liste d’objets.
- Les objets sont classés par catégorie, prix, rôle et composants.
- Les équipes regroupent plusieurs champions et sont créées par l’utilisateur avec un nom et une composition limitée.

## Validations les plus importantes

Les points les plus exigeants du projet étaient les validations métiers. Nous avons utilisé Pydantic pour garantir la cohérence des données :

- nom non vide après trim,
- équipe contenant au moins un champion,
- limite maximale de 6 champions par équipe,
- limite maximale de 6 objets par champion,
- interdiction que l’item soit un composant de lui-même,
- contrôle de doublons sur les objets ajoutés à un champion.

## Difficultés rencontrées

La difficulté principale venait des contraintes de robustesse. Il fallait gérer les cas où l’utilisateur fournit des paramètres incohérents ou incomplets, sans casser l’API.

Par exemple :

- aucune entrée de recherche,
- plusieurs filtres en même temps,
- nom d’équipe existant,
- champion ou item introuvable,
- action impossible sur une ressource absente.

## Solution mise en place

Nous avons centralisé les validations dans `Class/validators.py` et utilisé `HTTPException` pour renvoyer des erreurs explicites. Cela permet à l’API de rester lisible et de fournir une documentation claire via Swagger.

Le script `start.bat` automatise la création de l’environnement virtuel, l’installation des dépendances et le lancement du serveur pour faciliter le démarrage par un clone du dépôt.
