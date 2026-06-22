### 1.	Context
The additional categories in this module are: 

- Commuting
- Food
- Waste
- Construction and renovation

These categories are referred to as ‘additional’ because their emissions are calculated using EPFL campus data and rely solely on the number of unit FTE. They therefore do not provide specific information on the unit’s behaviour but are nonetheless useful for gaining a more comprehensive understanding of the order of magnitude of the unit’s carbon footprint. 


### 2.	Data collected 
The data collected and used to calculate emissions for the additional categories relate to the number of staff and students at EPFL (via the ***Headcount*** module) and the floor location of the rooms used (via the ***Buildings*** module), plus other specific data described here:

- ***Commuting***: total number of kilometers per person (staff or students) and by mode of transport (cycle, car, public transport, etc.). These figures are calculated using responses from the Mobility survey sent out every two years to the EPFL community and combined with information on car park usage to estimate kilometers travelled by car.
  
- ***Food***: total quantity (in kg/person) of food purchased by type of person (staff or students), and by type (vegetarian and non-vegetarian). These figures are based on sales data from the various restaurants and food trucks on site, cross-referenced with the quantities of goods ordered.
  
- ***Waste***: total in kg/person of all non-hazardous waste, by type (paper, plastic, etc.) and by final treatment method (incineration, recycling, etc.). These figures are collected by the VPO each year.
  
- ***Construction and renovation***: Only data from the building module and the factors described below are used for the calculation. 


### 3.	Emission factors 

- ***Commuting***: the emission factors used are those from the **[transportation environmental calculator](https://www.suisseenergie.ch/programmes/calculateur-environnemental-transport/?pk_vid=d874ca860cec98e71773910695abdffd)**, tool developped by Swissenergy. For cars, a factor specific to EPFL has been calculated based on the types of car used by the EPFL community. The factors are given in kg CO₂-eq/km by mode of transport (on foot, by bike, by car, by public transport, by motorbike).

- ***Food***: the emission factors used are based on goods orders placed at EPFL and are provided by the external service provider **[Beelong](https://beelong.ch/en/)**, which analyses the orders and quantities. The factors are in kg CO₂-eq/kg of food depending on the type (vegetarian or non-vegetarian). 

  
- ***Waste***: emission factors are given in kg CO₂-eq/kg of waste (specific factors by type: paper, plastic, etc. and by treatment method: recycling, incineration, etc.). The factors are taken from **[Ecoinvent v3.12 (2026)](https://ecoquery.ecoinvent.org/3.12/cutoff)**. 

  
- ***Construction and renovation***: emission factors are given in kg CO₂-eq/m², by type of construction: new builds – thermal envelope, new builds – technical installations, renovations – thermal envelope, renovations – technical installations, demolitions. The factors were developed based on an internal analysis at EPFL.


### 4.	Methodology 

***Commuting***

Les émissions totales de CO₂ liées à la pendularité sont estimées en agrégeant, pour chaque mode de transport, les émissions générées par la population étudiante et par le personnel. Pour chaque unité, l’empreinte carbone de pendularité $CF_{commuting}$ est calculée comme le produit du nombre de personnes dans l’unité, de la distance moyenne parcourue selon chaque mode de transport, et du facteur d’émission associé à ce mode tel que :

$$
CF_{commuting} = \sum_{trans~type}^{} N_{students} \cdot Dist_{students, trans~type} \cdot EF_{trans~type} + \sum_{trans~type}^{} N_{staff} \cdot Dist_{staff, trans~type} \cdot EF_{trans~type}
$$


Où :

- $trans~type$ : transport public, vélo, voiture, marche à pied, etc
- $N_{students}$  : nombre d’étudiants total par année de référence en EPT
- $N_{staff}$ : nombre de membres du personnel total par année de référence en EPT
- $Dist_{students,trans~type}$ : distance parcourue par étudiant par mode de transport, en km
- $Dist_{staff,trans~type}$ : distance parcourue par membre du personnel par mode de transport, en km
- $EF_{trans~type}$ : facteur d’émission du mode de transport trans_type(kg CO₂-eq/km)


***Alimentation***

Les émissions totales de CO₂ liées à l’alimentation sont estimées en agrégeant, pour chaque catégorie de repas (végétarien ou carné), les émissions associées à la consommation de la population étudiante et du personnel. Pour chaque unité, les émissions $CF_{food}$ sont calculées comme le produit du nombre de personnes dans l’unité, de la quantité moyenne de nourriture consommée par catégorie, et du facteur d’émission correspondant.

$$
CF_{food} =
\sum_{food~type}^{} N_{students} \cdot Q_{students, food~type} \cdot EF_{food~type} + \sum_{food~type}^{} N_{staff} \cdot Q_{staff, food~type} \cdot EF_{food~type}
$$

Où :

- $food_{type}$ : type de nourriture (végétarien, non végétarien)
- $N_{students}$  : nombre d’étudiantes ou étudiants total par année de référence en EPT
- $N_{staff}$  : nombre de membres du personnel total par année de référence en EPT
- $Q_{students,food~type}$  : quantité de nourriture achetée par étudiante ou étudiant pour le type de nourriture en kg/EPT
- $Q_{staff,food_type}$  : quantité de nourriture achetée par membre du personnel pour le type de nourriture en kg/personne
- $EF_{food_type}$  : facteur d’émission du type de nourriture en kg CO₂-eq/kg


***Déchets***

Le total de $CF_{waste}$ est obtenu en multipliant le nombre de personne dans l’unité pour les kg de déchet par personne pour les facteurs d’émissions.  

$$
CF_{waste} = \sum_{waste~type}^{}\sum_{eol}^{}(N \cdot Q_{waste~type, eol} \cdot EF_{waste~type,eol})
$$

Où :

- $waste~type$ : type de déchet (papier, plastique, etc.)
- $eol$ : mode de traitement final (incinération, recyclage, etc.)
- $N$ : nombre de membres du personnel total par année de référence en EPT
- $Q_{waste~type,eol}$  : quantité de déchets par EPT en kg/EPT pour le type et le traitement
- $EF_{waste~type,eol})$ : facteur d’émission associé au type de déchet et au mode de traitement en kg CO₂-eq/kg


***Construction et rénovation***

Le total des émissions de CO₂ liées à la construction et rénovation $CF_{construction}$ est obtenu en identifiant les bâtiments dans lesquels l’unité exerce des activités (laboratoires, bureaux, etc.) à partir des données du module bâtiments. Pour chaque bâtiment concerné, la superficie totale des locaux concernés est multipliée par les facteurs d’émission correspondants, exprimés en kg CO₂-eq/m², et spécifiques au type d’activité de construction (nouvelles constructions – enveloppe thermique, nouvelles constructions – installations techniques, rénovations – enveloppe thermique, rénovations – installations techniques, démolitions). Le total des émissions est obtenu en additionnant les émissions pour tous les locaux concernés et tous les types d’activité. Les facteurs sont calculés sur la base de la surface totale des bâtiments et au type d’activité de construction et appliqués uniquement pour les années où les travaux ont lieu, conformément aux recommandations du GHG Protocol.

$$
CF_{construction}
= \sum_{building}^{}\sum_{activity~type}^{}(Surface_{building} \cdot EF_{building,activity~type})
$$

Où :

- $building$ : bâtiment de l’EPFL (AAB, BCH, BS, etc)
- $activity~type$ : type de construction par bâtiment (new_env, new_tec, ren_env, ren_tec, dem)
- $surface_{building}$ : superficie totale du bâtiment building (m²)
- $EF_{building,activity~type}$ : facteur d’émission pour le bâtiment building et le type d’activité activity_type(kg CO₂-eq/m²)

Lorsque les données détaillées par bâtiment ne sont pas disponibles, des facteurs d’émission par défaut peuvent être utilisés. Dans ce cas, une entrée « default » est définie et appliquée à l’ensemble des bâtiments utilisés par l’institution. Ces facteurs par défaut permettent d’estimer les émissions à l’échelle du campus et de les répartir entre les unités sans nécessiter d’informations spécifiques sur chaque bâtiment. 


### 5. Limitations

De manière générale, la précision de ces catégories additionnelles est limitée par l'absence de données individuelles et spécifiques à chaque unité :

- Pour des raisons de confidentialité, il n'est pas possible de savoir quels membres d'une unité consomment de la viande ou des produits végétariens, ni quels modes de transport ils utilisent individuellement. Les émissions sont donc estimées sur la base de moyennes campus, sans refléter le comportement réel de l'unité. À titre indicatif, la viande est significativement plus émettrice que les alternatives végétariennes, et la voiture constitue le mode de transport le plus impactant.
- Pour les déchets, les déchets dangereux ont été exclus de cette analyse, faute de données permettant d'attribuer leur consommation à des unités spécifiques. Si l'unité en produit, son bilan réel est plus élevé que celui estimé ici.
- La construction et la rénovation représentent un défi supplémentaire : au-delà du manque de données spécifiques aux bâtiments, les facteurs d'émission disponibles — notamment les facteurs KBOB suisses — requièrent des informations très précises sur les quantités et types de matériaux utilisés (en kg ou m³), qui ne sont pas systématiquement disponibles. Des facteurs par défaut ont donc été construits en interne, ce qui introduit une incertitude supplémentaire.

### 6. References
- [Transportation environmental calculator (Mobitool v3.1)](https://www.suisseenergie.ch/programmes/calculateur-environnemental-transport/?pk_vid=d874ca860cec98e71773910695abdffd)
- [Beelong](https://beelong.ch/en/) – Prestataire externe pour l'analyse des commandes alimentaires et le calcul des facteurs d'émission associés.
- [Ecoinvent v3.12 (2026)](https://ecoquery.ecoinvent.org/3.12/cutoff) – Base de données de cycle de vie utilisée pour les facteurs d'émission liés aux déchets.
- Analyse interne EPFL – Facteurs d'émission pour la construction et rénovation des bâtiments (nouvelles constructions, rénovations, démolitions), développés sur la base de projets de construction du campus.
