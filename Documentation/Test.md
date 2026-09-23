# Tests manuels

## 1. Tests sur les champions

### GET /champions
- Vérifier que la liste retourne bien les champions disponibles.
- Contrôler que les champs principaux sont présents : nom, titre, rôles, lanes, stats.

### GET /champion?id=1
- Vérifier une réponse HTTP 200 pour un identifiant existant.

### GET /champion?name=Ashe
- Vérifier la recherche par nom case-insensitive.

### GET /champion
- Vérifier qu’une erreur 422 est renvoyée si aucun paramètre n’est fourni.

## 2. Tests sur les items

### GET /items
- Vérifier la liste complète des objets.

### GET /item?id=2
- Vérifier qu’un item existant est bien renvoyé.

### GET /filterItems
- Tester le paramètre `categorie`.
- Tester les paramètres `limit` et `offset`.
- Tester le tri via `sort_by=name` ou `sort_by=prix`.

### GET /stats
- Vérifier le total d’items.
- Vérifier la moyenne des prix.
- Vérifier la catégorie la plus fréquente.

## 3. Tests sur les équipes

### POST /team
- Envoyer une équipe valide avec 1 à 6 champions.
- Vérifier le code HTTP attendu (`200` ou `201`).

### POST /team
- Envoyer une équipe sans champion.
- Vérifier qu’une erreur 422 est retournée.

### POST /team
- Réutiliser un nom déjà existant.
- Vérifier qu’une erreur 409 est retournée.

### GET /teams
- Vérifier la liste des équipes créées.

### GET /team?name=EquipeA
- Vérifier la récupération d’une équipe existante.

### DELETE /team?id=1
- Vérifier la suppression d’une équipe existante.

### DELETE /team?name=EquipeA
- Vérifier la suppression par nom.

## 4. Tests sur l’ajout d’objets

### PATCH /add
- Ajouter un objet valide à un champion d’une équipe.
- Vérifier le code 200 de réponse.

### PATCH /add
- Ajouter un objet déjà présent.
- Vérifier qu’une erreur 409 est renvoyée.

### PATCH /add
- Ajouter un 7e objet à un champion.
- Vérifier qu’une erreur 422 est renvoyée.

## 5. Cas d’erreur attendus

- 404 si la ressource n’existe pas
- 422 si un paramètre de recherche est absent ou incorrect
- 409 si un conflit métier est détecté
- 400/422 si les données sont incohérentes

## 6. Résultat attendu

L’API doit rester stable, avec des réponses cohérentes et des messages explicites lors d’erreurs métier.
