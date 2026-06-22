### 1.	Context 
To carry out their research activities, many laboratories—as well as external academic institutions, companies and start-ups—use the research facilities provided by EPFL. This includes, for example, cleanrooms, high-performance computing centres, IT services and animal facilities, to name but a few. This sharing of resources is an excellent way to reduce the carbon footprint.

The use of EPFL research facilities might be part of a unit’s operational activities and must therefore be included in its carbon footprint. This footprint is broken down into emissions related to **Process Emissions, Buildings, Equipment and Purchases** for these research facilities. These emissions correspond to the main areas where units can act, particularly through their choices regarding usage, equipment and research practices.


### 2.	Data collected 
The data collected relates to the categories of emissions arising from the activities of the research facilities mentioned above, calculated directly in the calculator with a few exceptions.  

- **Process emissions**:  
  The data collected is listed in the tab for the Process Emissions module (see Section 4.2.2). 

- **Buildings**:  
  The data collected is listed in the tab for the Buildings module (see Section 4.3.2).
  Exception: for animal facilities, the data collected comes from life cycle assessments (see further details here [https://www.epfl.ch/schools/sv/school-of-life-sciences/about-us/sv-sustainability-office/green-lab-project/](https://www.epfl.ch/schools/sv/school-of-life-sciences/about-us/sv-sustainability-office/green-lab-project/)

- **Equipment**:  
  The data collected is listed in the tab for the Equipment module (see Section 4.4.2).
  Exception: for animal facilities, the data collected comes from life cycle assessments (see further details here [https://www.epfl.ch/schools/sv/school-of-life-sciences/about-us/sv-sustainability-office/green-lab-project/](https://www.epfl.ch/schools/sv/school-of-life-sciences/about-us/sv-sustainability-office/green-lab-project/)
  
- **Purchases**:  
  The data collected is listed in the Purchasing module tab (see Section 4.7.2).


### Allocation key 
Part of the carbon footprint of research facilities is allocated to the user units. This approach considers the fact that EPFL’s research facilities are essential to the units’ research activities and must therefore be included in their carbon footprint. 

An allocation key is applied for the use of research facilities. This is based on:

- Total invoicing (internal and external clients)
- Hours of use of EPFL research facilities
- The number of animal housing used

As the rate is differentiated for external units, a calculation is carried out subsequently to allocate the footprint at a standardised price level between internal and external user units. 

The data required for these calculations is derived from billing data or provided directly by the research facilities.


### 3.	Emission factors 


Ce module est particulier dans le sens où les facteurs d’émissions dépendent de plusieurs facteurs :

1. Les émissions des catégories ***Process emissions***, ***Buildings***, ***Equipment*** et ***Purchases***  
2. L’utilisation par l’unité utilisatrice  


- ***[Voir Facteurs d’émissions Process emissions](./processes.md#facteurs)***
- ***[Voir Facteurs d’émissions Buildings](./building.md#facteurs)***
- ***[Voir Facteurs d’émissions Equipment](./equipment.md#facteurs)***
- ***[Voir Facteurs d’émissions Purchases](./purchases.md#facteurs)***




### 4.	Methodology

L’empreinte carbone associée à l’utilisation d’une infrastructure de recherche est calculée à partir de l’empreinte carbone des modules suivants de l’infrastructure : ***Process emissions***, ***Buildings***, ***Equipment*** et les ***Purchases***. 

Le taux d’utilisation d’une unité utilisatrice par rapport à une infrastructure de recherche EPFL $UsageRate_{RF,unit}$  correspond à la part de son utilisation totale par rapport à l’ensemble des unités utilisatrices (interne et externe) de l’infrastructure de recherche concernée. Ce taux d’utilisation annuel est exprimé en fonction des données disponibles (facturations, heures d’utilisation ou nombre d’hébergements), selon la formule suivante :

$$
UsageRate_{RF,unit} = \frac{Usage_{RF,unit}}{\sum_{unit}^{}Usage_{RF,unit}}
$$

Où :

- $RF$ : l’infrastructure de recherche concerné
- $unit$ : l’unité utilisatrice
- $Usage_{RF,unit}$ : utilisation de l’infrastructure de recherche EPFL par rapport à l’unité et selon l’année de référence (facturation, heures d’utilisation ou nombre d’hébergements)


La part d’empreinte carbone attribuable à une unité utilisatrice $CF_{RF~attribution,unit}$  est ensuite déterminée en multipliant cette empreinte par le taux d’utilisation spécifique de l’unité, selon la formule suivante :

$$
CF_{RF~attribution,unit} = CF_{RF~attribution,total} \cdot UsageRate_{RF,unit}
$$

Où :

- $CF_{RF~attribution,total}$ : l’empreinte carbone de l’infrastructure de recherche à attribuer aux unités utilisatrices
- $UsageRate_{RF,unit}$ : taux d’utilisation spécifique de l’unité utilisatrice 


Pour les animaleries, la méthode de calcul est similaire. Les émissions attribuées à une unité utilisatrice sont calculées en fonction de son niveau d’utilisation de l’animalerie concernée. Cette utilisation est basée sur le nombre d’hébergements et permet de répartir l’empreinte carbone de l’animalerie en question entre les différentes unités utilisatrices.

Pour consulter la méthodologie de chaque catégorie considérée pour le calcul de l’empreinte carbone de l’infrastructure de recherche attribuée à son utilisation, veuillez consulter les liens ci-dessous : 

- ***[Process emissions](./processes.md#methodologie)*** 
- ***[Buildings](./building.md#methodologie)***
- ***[Equipment](./equipment.md#methodologie)*** 
- ***[Purchases](./purchases.md#methodologie)*** 


### 5. Limitations

Ce module possède un niveau d’incertitude élevé. En effet, l’attribution de l’empreinte carbone liée à l’utilisation des infrastructures de recherche EPFL repose sur les empreintes carbones des modules ***Process emissions***, ***Buildings***, ***Equipment*** et ***Purchases***, qui eux-mêmes possèdent leurs propres les limites.  

- ***[Voir Limites du module Process emissions](./processes.md#5-limites)***
- ***[Voir Limites du module Buildings](./building.md#5-limites)***
- ***[Voir Limites du module Equipment](./equipment.md#5-limites)*** 
- ***[Voir Limites du module Purchases](./purchases.md#5-limites)*** 

Par ailleurs, l’espace Calculateur CO₂ repose sur des modules partiellement automatisés, qui utilisent par défaut les données remontées par chaque module. Ainsi, si les modules des infrastructures de recherche n’ont pas été validés, des erreurs peuvent subsister, ce qui peut influencer l’attribution de leur empreinte carbone aux unités utilisatrices.

De plus, il y a des limites liées à la clé de répartition qui repose principalement sur les données monétaires à l’exception de certaines plateformes où le nombre d’heures d’utilisation ou le nombre d’hébergements sont considérés. 

- Les données de facturation sont un premier indicateur pour l’utilisation des infrastructures de recherche. Cependant, il y a de nombreuses limites, notamment dues à la tarification différenciée entre les unités internes et externes et même entre unités internes faisant partie de différentes facultés ou services.
- Les heures d’utilisation sont des indicateurs plus pertinents avec moins d’incertitude et sont priorisés si les infrastructures de recherche possèdent ces données pour l’ensemble des unités utilisatrices. 


### 6. References
- La méthodologie de ce module a été développée en se référant pour une partie à la méthodologie développée par Labos1point5 dans le GES1point5 [https://apps.labos1point5.org/documentation/carbon/ges-calculating-methods](https://apps.labos1point5.org/documentation/carbon/ges-calculating-methods) et affinée au contexte EPFL par le GT infrastructures de recherche. 


