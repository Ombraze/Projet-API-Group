# LoLTeamBuilder

Projet FastAPI de gestion d’une équipe de League of Legends, avec construction de composition, consultation de champions et d’objets, ainsi que validation et gestion d’erreurs.

## 1. Sujet du projet

- Nom du projet : LoLTeamBuilder
- Thème choisi : League of Legends Team Builder
- Description : Cette API permet de consulter les champions et objets du jeu, de construire une équipe d’un maximum de 6 champions, d’ajouter des objets à ces champions, et de vérifier les contraintes métier de validation sur les équipes.

## 2. Membres du groupe

- Langella Mathis
- Dahmane Yanis
- Dzneladze Luka

## 3. Objectif du projet

L’objectif du projet est de créer une API REST robuste en FastAPI qui couvre les paliers demandés :

- Palier 1 : fondations et CRUD
- Palier 2 : validation avancée via Pydantic
- Palier 3 : filtrage, tri, recherche et statistiques
- Palier 4 : robustesse, gestion des erreurs et documentation de test
- Palier 5 : défi bonus (facultatif)

## 4. Ressources de l’API

L’API expose 3 ressources principales :

- Champions : personnages jouables avec leurs rôles, lanes, statistiques et objets équipés.
- Items : objets du jeu classés par catégorie, prix, rôle et composants.
- Teams : équipes de champions créées par l’utilisateur, avec un nom et une composition limitée à 6 champions.

### Structure métier

- Un champion peut porter plusieurs items.
- Un item peut contenir des composants imbriqués via `sub_item_ids`.
- Une équipe contient plusieurs champions.
- Un champion appartient à des lanes et des rôles.

## 5. Relations entre les ressources

Le projet contient plusieurs relations logiques :

- Team -> Champion via `champion_ids` et `champion_name`
- Champion -> Item via `Items`
- Item -> Item via `sub_item_ids` (composants d’un objet)
- Champion -> Role/Lane via les listes de rôles et de lanes

## 6. Modèles Pydantic

Le projet utilise plusieurs modèles validés :

- `Champion`
- `Item`
- `Team`
- `TeamCreate`
- `ShowChampion`
- `Show_Item`
- `ShowTeam`

### Contraintes et validations principales

- `name` : non vide, trimé et vérifié par `field_validator`
- `TeamCreate.name` : longueur min/max imposée
- `TeamCreate.champion_ids` et `champion_name` : maximum 6 choix combinés
- `Champion.Items` : maximum 6 objets par champion
- `Item.sub_item_ids` : un item ne peut pas être un composant de lui-même
- `role`, `lane` et `categorie` : valeurs contraintes par les enums et les données JSON du projet

### Enum utilisés

- `Role`
- `Lane`
- `Activable`

### Validators personnalisés

- `validateNonBlank` : empêche les chaînes vides ou composées uniquement d’espaces
- `validateName` : nettoie le nom avant validation
- `validateTeamChampionSelection` : vérifie qu’au moins un champion est sélectionné et que le total ne dépasse pas 6
- `validateItemComponents` : interdit les composants récursifs invalides

## 7. API endpoints

### Ressources principales

- `GET /` : page d’accueil
- `GET /champions` : liste tous les champions
- `GET /champion?id=...` : recherche d’un champion par ID
- `GET /champion?name=...` : recherche d’un champion par nom
- `GET /items` : liste tous les objets
- `GET /item?id=...` : recherche d’un item par ID
- `GET /item?name=...` : recherche d’un item par nom
- `GET /filterItems` : filtre, tri et pagination sur les items
- `GET /stats` : statistiques globales sur les objets
- `GET /teams` : liste toutes les équipes
- `GET /team?name=...` : récupère une équipe précise par nom
- `POST /team` : création d’une équipe
- `DELETE /team` : suppression d’une équipe par ID ou nom
- `PATCH /add?team_name=...&champion_name=...&item_name=...` : ajoute un objet à un champion de l’équipe

### Routes avancées

- `GET /filterItems?categorie=...` : filtrage par catégorie
- `GET /filterItems?sort_by=...` : tri par `name`, `prix`, `categorie` ou `role`
- `GET /filterItems?limit=X&offset=Y` : pagination
- `GET /stats` : calcul de moyenne de prix et catégorie la plus fréquente

## 8. Validation avancée

Les validations sont centralisées dans `Class/validators.py` et s’appliquent sur les modèles Pydantic.

Exemples :

- `min_length` et `max_length` sur les noms et équipes
- `field_validator` pour assurer qu’un nom n’est pas vide
- `model_validator` pour contrôler le nombre de champions et les composants d’item
- `Field(max_items=6)` pour limiter le nombre d’objets par champion

## 9. Gestion des erreurs

L’API renvoie des `HTTPException` explicites pour chaque cas critique :

- `404` : ressource introuvable (`team`, `champion`, `item` absent)
- `422` : paramètre manquant ou invalide
- `409` : conflit métier (nom d’équipe déjà existant, item déjà dans l’inventaire)
- `400` / `422` : données incohérentes ou invalides

Exemples concrets :

- recherche sans `id` ni `name` → `422`
- équipe inexistante → `404`
- équipe avec 0 champion → `422`
- dédoublonnage d’un item déjà porté → `409`

## 10. Documentation automatique

L’application FastAPI expose automatiquement la documentation interactive :

- Swagger UI : http://localhost:8000/docs
- Redoc : http://localhost:8000/redoc

## 11. Installation

### Prérequis

- Python 3.11+
- pip
- Git

### Installation manuelle

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

PowerShell :

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## 12. Lancer le projet

Le plus simple est de lancer le script Windows :

```bat
start.bat
```

Ou manuellement :

```bash
uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

Puis ouvrez :

- http://localhost:8000/docs

## 13. Structure du dépôt

```text
Projet-API-Group/
├── main.py
├── data.py
├── README.md
├── start.bat
├── requirements.txt
├── Class/
│   ├── Champion.py
│   ├── Lane.py
│   ├── Role.py
│   ├── Team.py
│   ├── validators.py
│   └── Object/
│       ├── __init__.py
│       ├── consumable.py
│       └── item.py
├── Data/
│   ├── champions.json
│   └── items.json
├── Documentation/
│   ├── Journal.md
│   ├── requirements.txt
│   ├── Review.md
│   └── Test.md
└── .git/
```

## 14. Journal de bord

Le journal de bord est disponible dans [Documentation/Journal.md](Documentation/Journal.md). Il détaille :

- choix des ressources métier,
- validation Pydantic importante,
- difficultés rencontrées,
- solutions mises en place.

## 15. Tests manuels

Les cas de test sont détaillés dans [Documentation/Test.md](Documentation/Test.md).

Les vérifications principales couvrent :

- lecture des champions / items
- recherche par ID et par nom
- filtrage et tri des objets
- statistiques globales
- création d’équipe valide
- création d’équipe invalide
- suppression d’équipe
- ajout d’item sur un champion

## 16. Review de code

La revue croisée est documentée dans [Documentation/Review.md](Documentation/Review.md). Elle contient :

- points de vigilance sur la robustesse,
- bugs ou comportements suspects détectés,
- suggestions d’amélioration.

## 17. Défi bonus

Le projet peut être étendu avec :

- export CSV des équipes,
- recherche globale multi-ressources,
- duplication d’une équipe avec ses objets,
- validation croisée entre champions et items.

## 18. Checklist finale

- [x] Nom du projet défini
- [x] Ressources principales créées
- [x] CRUD complet sur les équipes
- [x] Validation Pydantic robuste
- [x] Enum et validators ajoutés
- [x] Filtres et statistiques implémentés
- [x] Gestion des erreurs complétée
- [x] Documentation Swagger fonctionnelle
- [x] Journal de bord écrit
- [x] Tests manuels listés
- [x] Review intégrée

## 19. Résumé rapide

Cette API permet de gérer une équipe de League of Legends en recoupant des données de champions, d’objets et d’équipes. Elle met en œuvre une architecture simple, des validations métier fortes et une documentation fonctionnelle adaptée au palier 4 du projet.

---
