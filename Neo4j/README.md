#  Base de Données Neo4j — *Gen V* (Amazon Prime)

##  Objectif

Ce projet a pour but de modéliser l’univers de la série **Gen V** à l’aide de **Neo4j**, une base de données orientée graphes.  
L’objectif est de représenter les **personnages**, leurs **pouvoirs**, leurs **relations**, et les **organisations** de l’univers de la série.

---

##  Outils utilisés

-  **Neo4j Desktop** (ou Neo4j Browser)
-  **Langage : Cypher**
-  **Captures d’écran** des résultats de requêtes

Aucun autre outil ou langage n’a été utilisé : tout le projet repose uniquement sur Neo4j.

---

##  Structure du graphe

### Types de nœuds (Labels)
| Label | Description |
|--------|--------------|
| `Person` | Personnages de la série |
| `Group` | Organisations et institutions (Vought, Godolkin University, etc.) |
| `Power` | Super-pouvoirs |
| `Place` | Lieux importants |
| `Crime` | Crimes, expériences ou manipulations |

### Types de relations
| Relation | Description |
|-----------|-------------|
| `:STUDIES_AT` | Un étudiant est inscrit dans une université |
| `:WORKS_FOR` | Travaille pour une organisation |
| `:HAS_POWER` | Possède un pouvoir |
| `:RESPONSIBLE_FOR` | Responsable ou auteur d’un crime |
| `:OPERATES` | Supervise un lieu |
| `:FRIEND_WITH` | Amitié ou alliance |
| `:ENEMY_OF` | Rivalité ou hostilité |

---

##  Exemples de requêtes utilisées

### 1️⃣ Afficher tous les nœuds
```cypher
MATCH (n)
RETURN n
LIMIT 100;
```
<img width="1209" height="568" alt="Capture d&#39;écran 2025-11-13 150031" src="https://github.com/user-attachments/assets/406b600b-4cfa-43bd-a447-0089a4d87ab1" />

### 2️⃣ Afficher toutes les relations
```cypher
MATCH (a)-[r]->(b)
RETURN a, r, b
LIMIT 50;
```
<img width="1212" height="573" alt="Capture d&#39;écran 2025-11-13 150017" src="https://github.com/user-attachments/assets/e78c642f-5845-4f7c-8a44-9649b090f7f8" />

### 3️⃣ Voir les étudiants de Godolkin University
```cypher
MATCH (p:Person)-[:STUDIES_AT]->(g:Group {name:"Godolkin University"})
RETURN p, g;
```
<img width="1212" height="577" alt="Capture d&#39;écran 2025-11-13 151747" src="https://github.com/user-attachments/assets/e040ab98-d73d-4a7a-8e0c-ca4d17572d51" />

### 4️⃣ Lister les pouvoirs de chaque personnage
```cypher
MATCH (p:Person)-[:HAS_POWER]->(pow:Power)
RETURN p.name AS Personnage, collect(pow.name) AS Pouvoirs;
```
<img width="1206" height="492" alt="Capture d&#39;écran 2025-11-13 151857" src="https://github.com/user-attachments/assets/367b56d3-ab0e-4e7c-bc0e-49462e3fa6f0" />
