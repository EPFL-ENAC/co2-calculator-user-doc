### 1.	Contexte
Les catégories additionnelles dans ce module sont : 

- Pendularité
- Alimentation
- Déchets
- Construction et rénovation

Ces catégories sont appelées additionnelles parce que leurs émissions sont calculées à partir des données campus de l’EPFL et utilisent uniquement le nombre de personnes et la superficie des salles utilisées par l’unité comme donnée spécifique à l’unité. Elles ne donnent donc pas des informations spécifiques au comportement de l’unité, mais sont tout de même utiles pour avoir une idée plus complète de l’ordre de grandeur du bilan carbone de l’unité. 


### 2.	Données collectées
Les données collectées et utilisées pour le calcul des émissions des catégories additionnelles sont relatives au nombre de personnel et population étudiante de l’EPFL (via le ***module Personnel***) et de la superficie des salles utilisées (via le ***module Bâtiments***), plus d’autres données spécifiques décrites ici :

- ***Pendularité*** : nombre total de kilomètres par personne (personnel ou étudiants) et par mode de transport (vélo, voiture, transport public, etc). Ces chiffres sont calculés en utilisant les réponses de l’Enquête de mobilité envoyé tous les deux ans à la communauté EPFL, et combinés avec les informations d’utilisation des places de parking pour les km en voiture parcourus.
- ***Alimentation*** : quantité totale (en kg/personne) de nourriture achetée par type de personne (personnel ou étudiants), et par type (végétarien et non végétarien). Ces chiffres sont basés sur les données de vente aux différents restaurants et foodtrucks présents, croisées avec les quantités de marchandises commandées.
- ***Déchets*** : total en kg/personne de tous les déchets non dangereux, par type (papier, plastique, etc.) et par mode de traitement final (incinération, recyclage, etc.) Ces chiffres sont récoltés par la VPO chaque année.
- ***Construction et rénovation*** : Seules les données du module bâtiment, et les facteurs décrits plus bas sont utilisés pour le calcul. 


### 3.	Facteurs d’émissions

- ***Pendularité*** : les facteurs d’émissions utilisés sont ceux du **[calculateur environnemental transport](https://www.suisseenergie.ch/programmes/calculateur-environnemental-transport/?pk_vid=d874ca860cec98e71773910695abdffd)**, outil développé par Suisseénergie. Pour les voitures, un facteur spécifique à l’EPFL a été calculé basé sur le type de voitures de la communauté EPFL. Les facteurs sont en kg CO₂-eq/km par mode de transport (à pied, vélo, voiture, transport public, moto).
- ***Alimentation*** : les facteurs d’émissions utilisés sont construits sur la base de commandes de marchandises effectuées à l’EPFL, et sont fournis par le prestataire externe **[Beelong](https://beelong.ch/en/)** qui analyse les commandes et les quantités. Les facteurs sont en kg CO₂-eq/kg de nourriture selon le type (végétarien ou non végétarien).
- ***Déchets*** : les facteurs d’émissions sont en kg CO₂-eqkg de déchets (facteurs spécifiques par type : papier, plastique, etc. et par mode de traitement : recyclage, incineration, etc). Les facteurs viennent d’**[Ecoinvent v3.12 (2026)](https://ecoquery.ecoinvent.org/3.12/cutoff)**.
- ***Construction et rénovation*** : les facteurs d’émissions sont en kg CO₂-eq/m2, par type de construction : nouvelles constructions - enveloppe thermique, nouvelles constructions - installations techniques, rénovations - enveloppe thermique, rénovations – installations techniques, démolitions. Les facteurs ont été construit sur la base d’une analyse interne à l’EPFL. 

### 4.	Méthodologie

***Pendularité***

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


### 5. Limites

De manière générale, la précision de ces catégories additionnelles est limitée par l'absence de données individuelles et spécifiques à chaque unité :

- Pour des raisons de confidentialité, il n'est pas possible de savoir quels membres d'une unité consomment de la viande ou des produits végétariens, ni quels modes de transport ils utilisent individuellement. Les émissions sont donc estimées sur la base de moyennes campus, sans refléter le comportement réel de l'unité. À titre indicatif, la viande est significativement plus émettrice que les alternatives végétariennes, et la voiture constitue le mode de transport le plus impactant.
- Pour les déchets, les déchets dangereux ont été exclus de cette analyse, faute de données permettant d'attribuer leur consommation à des unités spécifiques. Si l'unité en produit, son bilan réel est plus élevé que celui estimé ici.
- La construction et la rénovation représentent un défi supplémentaire : au-delà du manque de données spécifiques aux bâtiments, les facteurs d'émission disponibles — notamment les facteurs KBOB suisses — requièrent des informations très précises sur les quantités et types de matériaux utilisés (en kg ou m³), qui ne sont pas systématiquement disponibles. Des facteurs par défaut ont donc été construits en interne, ce qui introduit une incertitude supplémentaire.

### 6. Références
- [Calculateur environnemental transport (Mobitool v3.1)](https://www.suisseenergie.ch/programmes/calculateur-environnemental-transport/?pk_vid=d874ca860cec98e71773910695abdffd)
- [Beelong](https://beelong.ch/en/) – Prestataire externe pour l'analyse des commandes alimentaires et le calcul des facteurs d'émission associés.
- [Ecoinvent v3.12 (2026)](https://ecoquery.ecoinvent.org/3.12/cutoff) – Base de données de cycle de vie utilisée pour les facteurs d'émission liés aux déchets.
- Analyse interne EPFL – Facteurs d'émission pour la construction et rénovation des bâtiments (nouvelles constructions, rénovations, démolitions), développés sur la base de projets de construction du campus.

