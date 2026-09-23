# Review de code

## Points positifs

- La structure du projet est claire et facile à suivre.
- Les modèles Pydantic sont bien utilisés pour valider les données.
- Les relations entre champions, items et équipes sont cohérentes.
- Les erreurs HTTP sont bien exploitées pour améliorer la robustesse.

## Bugs ou comportements suspects

1. La route `GET /team` n’accepte qu’un `name` obligatoire, ce qui limite l’usage par `id` alors que d’autres routes permettent les deux identifiants.
2. Les routes de recherche `GET /champion` et `GET /item` renvoient `None` si aucune donnée n’est trouvée, ce qui pourrait être remplacé par un `HTTPException(404)` plus explicite.
3. La gestion des suppressions sur `DELETE /team` renvoie un message générique quand l’action est impossible au lieu d’un statut HTTP plus propre.

## Suggestions d’amélioration

- Ajouter des `HTTPException(404)` explicites dans les recherches par « no match ».
- Uniformiser la gestion des IDs et noms sur toutes les routes.
- Ajouter des tests automatisés avec `pytest` pour couvrir les cas limites.
- Définir davantage de réponses de type `response_model` pour standardiser les API responses.

## Conclusion

Le projet est bien avancé et couvre les attentes du palier 4 : validation, robustesse et documentation sont présents. Le point le plus important à améliorer est la cohérence globale entre les routes et les messages de retour.
