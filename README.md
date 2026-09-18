# Projet API Group

Ce projet est un projet de groupe réalisé dans le cadre de la séance 4 du module Python API. \
Il consiste à concevoir et développer une API REST originale en FastAPI, en s’appuyant sur les concepts vus précédemment : \
modèles Pydantic, validation, CRUD, documentation automatique, gestion d’erreurs, filtres, pagination et tests manuels.

> Ce README est un template de projet à compléter selon le thème choisi par votre groupe.

## 1. Sujet du projet

Nom du projet : [LoLTeamBuilder]

Thème choisi : [League of Legend Team builder]

Description :


## 2. Membres du groupe

- Langella Mathis
- Dahmane Yanis
- Dzneladze Luka

## 3. Objectif du projet

L’objectif de ce projet est de créer une API REST complète et cohérente, avec plusieurs ressources liées entre elles, une validation solide, des routes avancées et une bonne organisation de travail en équipe avec GitHub.

Le projet doit couvrir les différents paliers demandés :
- Palier 1 : Fondations et CRUD
- Palier 2 : Validation avancée
- Palier 3 : Recherche, pagination, tri et statistiques
- Palier 4 : Robustesse, gestion des erreurs et documentation de test
- Palier 5 : Défi bonus (facultatif)
- Palier x : Documentation fait durent tout le projet 

## 4. Ressources de l’API

L’API est composée de plusieurs ressources principales, par exemple :

- [Resource 1] : [description]
- [Resource 2] : [description]
- [Resource 3] : [description]
- [Resource 4] : [description]
- [Resource 5] : [description]

### Exemple de structure métier

- Un [Resource A] appartient à un [Resource B]
- Un [Resource C] est lié à plusieurs [Resource D]
- Un [Resource E] contient une liste de sous-objets imbriqués

## 5. Relations entre les ressources

Le projet doit contenir au moins 2 relations logiques distinctes entre les ressources.

Exemples à compléter :
- [Resource 1] -> [Resource 2] via [champ_id]
- [Resource 3] -> [Resource 4] via [id_utilisateur]
- [Resource 5] contient plusieurs [sous-objets] embarqués

## 6. Modèles Pydantic

Chaque ressource est représentée par un modèle Pydantic avec des champs validés.

### Exemple de modèle

```python
class ExampleModel(BaseModel):
    id: int
    name: str = Field(min_length=2, max_length=100)
    status: StatusEnum
```

### À compléter

- Nombre de modèles utilisés : [X]
- Champs avec contraintes : [décrire les contraintes principales]
- Enum utilisés : [nommer les enums]
- Validators personnalisés : [nombre et rôle]
- Modèles avec sous-objets imbriqués : [oui/non]
- Champs optionnels avec valeur par défaut : [liste]

## 7. API endpoints

L’API propose un CRUD complet sur plusieurs ressources.

### Exemple de routes attendues

- `POST /resource` : créer une ressource
- `GET /resource` : lister les ressources
- `GET /resource/{id}` : afficher une ressource
- `PATCH /resource/{id}` : modifier une ressource
- `DELETE /resource/{id}` : supprimer une ressource

### Routes avancées à ajouter

- `GET /resource?filter=...` : recherche / filtrage
- `GET /resource?limit=X&offset=Y` : pagination
- `GET /resource?sort_by=...` : tri
- `GET /stats` : statistiques agrégées

### À compléter selon votre API

- Nombre de ressources exposées : [X]
- Routes disponibles : [liste complète]
- Exemple de route : [URL + description]

## 8. Validation avancée

Le projet doit inclure une validation approfondie via Pydantic.

### À compléter

- Contraintes `Field` utilisées : [exemples]
- Enum distincts : [listes]
- `field_validator` : [nombre et rôle]
- `model_validator` : [nombre et rôle]
- Contrôles métier implémentés : [exemples]

## 9. Gestion des erreurs

L’API doit renvoyer des `HTTPException` claires dans plusieurs cas.

### Cas d’erreurs à gérer

- `404` : ressource introuvable
- `404` : identifiant lié introuvable
- `400` : donnée incohérente
- `403` ou `400` : action interdite
- `422` : validation Pydantic

### À compléter

- Liste des erreurs spécifiques à votre API : [décrire les cas métiers]

## 10. Documentation automatique

L’application utilise FastAPI et expose une documentation interactive Swagger et Redoc.

Accès local :
- Swagger UI : `http://localhost:8000/docs`
- Redoc : `http://localhost:8000/redoc`

## 11. Installation

Prérequis :
- Python 3.11+
- pip
- virtualenv ou venv

### Commandes

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Pour Windows PowerShell :

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## 12. Lancer le projet

```bash
uvicorn main:app --reload
```

Puis ouvrir :
- `http://localhost:8000/docs`

## 13. Structure du dépôt

```text
projet4-nomdugroupe/
├── main.py
├── requirements.txt
├── README.md
├── JOURNAL.md
├── TESTS.md
├── REVIEW.md
└── Documentation/
```

## 14. Journal de bord

Le fichier `JOURNAL.md` doit expliquer :
- les ressources choisies et leur logique,
- les validations les plus intéressantes,
- les difficultés rencontrées,
- la solution mise en place.

## 15. Tests manuels

Le fichier `TESTS.md` contient les cas de test de chaque route.

### Modèle de test

- `POST /resource` avec donnée valide -> 200/201
- `POST /resource` avec donnée invalide -> 422
- `GET /resource/{id}` avec id absent -> 404
- `PATCH /resource/{id}` avec valeur incohérente -> 400

## 16. Review de code / revue croisée

À la fin du projet, chaque groupe échange son dépôt et réalise une revue de l’API d’un autre groupe. Le fichier `REVIEW.md` contient :
- 3 bugs ou comportements suspects détectés,
- des observations sur la robustesse,
- des suggestions d’amélioration.

## 17. Défi bonus (facultatif)

Parmi les options possibles :
- duplication d’une ressource avec ses sous-objets,
- validation croisée entre deux ressources,
- export CSV,
- recherche globale sur plusieurs ressources.

## 18. Checklist de finalisation

- [ ] Nom du projet défini
- [ ] 5 ressources distinctes créées
- [ ] CRUD complet sur toutes les ressources
- [ ] Validation Pydantic robuste
- [ ] Enum et validators ajoutés
- [ ] Routes avancées implémentées
- [ ] Gestion des erreurs complète
- [ ] Documentation Swagger fonctionnelle
- [ ] Journal de bord écrit
- [ ] Tests manuels listés
- [ ] Review reçue intégrée
- [ ] GitHub public et historique de commits propre

## 19. Résumé rapide

Cette API a pour objectif de gérer [décrire votre domaine métier]. Elle met en œuvre une architecture simple, lisible et cohérente, inspirée des projets FastAPI déjà réalisés en cours, tout en ajoutant les éléments demandés pour atteindre les paliers du projet.

---

<!-- ### À compléter avant soumission

Remplacez les éléments entre crochets par les informations exactes de votre projet :
- nom du thème,
- ressources,
- relations,
- endpoints,
- validations,
- statistiques,
- résultats des tests,
- membres du groupe.
 -->
