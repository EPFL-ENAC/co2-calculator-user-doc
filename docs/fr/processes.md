### 1.	Contexte 
Certaines activités émettent directement des gaz à effet de serre (GES). Parmi les exemples fréquents dans les milieux universitaires figurent les fuites de SF₆ lors de la gravure, les fuites de gaz fluorés provenant des systèmes de réfrigération, ainsi que l'évaporation d'éthers fluorés lors de la manipulation d'échantillons. Étant donné que bon nombre de ces gaz retiennent nettement plus de chaleur et persistent beaucoup plus longtemps dans l'atmosphère que le CO₂, il est crucial de les suivre. Ce module est conçu pour enregistrer ces émissions directes de procédés et fugitives (Scope 1).

### 2.	Données collectées 
Les GES disponibles dans ce module sont sélectionnés conformément au GHG Protocol (GHG Protocol, 2024), en ciblant spécifiquement les sources d'émissions potentielles que l'on trouve dans les milieux universitaires et de recherche.

Les quantités de gaz associées aux émissions de procédés sont saisies manuellement dans les espaces Calculateur CO₂, Planificateur de projet CO₂ (demande de financement) et Explorateur CO₂. 

Lorsque ce module a été renseigné dans l’espace Calculateur CO₂, les données sont automatiquement remontées dans l’espace Planificateur de projet CO₂ (sections demande de financement et détail par année) pour les utilisatrices et utilisateurs principaux. Elles et ils peuvent alors définir, pour chaque année, un pourcentage de référence afin d’estimer la part des émissions de procédés attribuable au projet.

Les quantités de gaz émises par les émissions de procédés sont saisies manuellement.

<a id="facteurs"></a>
### 3.	Facteurs d’émission
Ce module utilise le Potentiel de Réchauffement Global (PRG) sur un horizon de 100 ans par rapport au CO₂ comme facteur d'émission standard. Ces valeurs sont fournies par le GHG Protocol (GHG Protocol, 2024) et sont adaptées du Cinquième Rapport d'évaluation du GIEC de 2014 (AR5).

<a id="methodologie"></a>
### 4.	Méthodologie
L’empreinte carbone de chaque émission de procédés $CF_{{process~emission}}$ est calculée comme le produit de la quantité de gaz procédé ou fugitif en kg et le facteur d’émission correspondant.

$$
CF_{process~emission} = Q_{gas} \cdot EF_{gas}
$$

Où : 

- $Q_{gas}$ : quantité de gas procédé ou fugitif (kg), saisie manuellement 
- $EF_{gas}$ : facteur d’émission selon le type de gaz (kg CO₂-eq / kg)

Le total des émissions de l'ensemble de chaque élément s'affiche en t CO₂-eq une fois le module validé.

### 5.	Limites 
Le module Émissions de procédés doit être rempli manuellement. La qualité des résultats dépend donc directement de la qualité des données entrées. Ces chiffres peuvent être estimés ou mesurés selon les données à disposition.

### 6.	Références
- Greenhouse Gas Protocol (2024) : [IPCC Global Warming Potential Values](https://ghgprotocol.org/sites/default/files/2024-08/Global-Warming-Potential-Values%20%28August%202024%29.pdf) 

