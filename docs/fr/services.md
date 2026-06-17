### 1.	Contexte 
Pour mener leurs activités de recherche, nombre de laboratoires mais aussi des institutions académiques externes, des entreprises et des startups utilisent les infrastructures de recherche mises à disposition par l’EPFL. Cela comprend par exemple des salles blanches, des centres de calculs de hautes performances, des services informatiques ou des animaleries, pour n'en nommer que quelques-unes. Cette mutualisation des ressources est un excellent moyen de réduire l'empreinte carbone.

L’utilisation des infrastructures de recherche EPFL fait partie des activités opérationnelles d’une unité et doit donc être incluse dans son empreinte carbone. Cette empreinte est répartie à partir des émissions liées aux ***Émissions de procédés***, aux ***Bâtiments***, aux ***Équipements*** et aux ***Achats*** de ces ***infrastructures de recherche***. Ces émissions correspondent aux principaux éléments sur lesquels les unités peuvent agir, notamment par leurs choix d’utilisation, d’équipements et de pratiques de recherche.


### 2.	Données collectées
Les données collectées se réfèrent aux catégories d’émissions provenant des activités des infrastructures de recherches mentionnées ci-dessus calculées directement dans le calculateur avec quelques exceptions.

- **Émissions de procédés** :  
  Les données collectées sont mentionnées dans l’onglet relatif au module Émissions de procédés (Voir Section 4.2.2).

- **Bâtiments** :  
  Les données collectées sont mentionnées dans l’onglet relatif au module Bâtiment (Voir Section 4.3.2).  
  Exception : pour les animaleries, les données collectées proviennent des analyses de cycle de vie (voir plus de détails ici : https://www.epfl.ch/schools/sv/school-of-life-sciences/about-us/sv-sustainability-office/green-lab-project/)

- **Équipements** :  
  Les données collectées sont mentionnées dans l’onglet relatif au module Équipements (Voir Section 4.4.2).  
  Exception : pour les animaleries, les données collectées proviennent des analyses de cycle de vie (voir plus de détails ici : https://www.epfl.ch/schools/sv/school-of-life-sciences/about-us/sv-sustainability-office/green-lab-project/)

- **Achats** :  
  Les données collectées sont mentionnées dans l’onglet relatif au module Achats (Voir Section 4.7.2).

### Clé de répartition 
Une partie de l’empreinte carbone des infrastructures de recherche est attribuée aux unités utilisatrices. Cette logique prend en considération le fait que les infrastructures de recherches EPFL sont essentielles aux activités de recherche des unités et doivent ainsi être prise en considération dans leur empreinte carbone. 

Afin d’attribuer l’utilisation des infrastructures de recherche, une clé de répartition est appliquée prenant en considération les unités utilisatrices internes et externes. Celle‑ci repose sur :

- les facturations totales 
- les heures d’utilisation
- le nombre d’hébergements (animaleries)

Comme le tarif est différencié pour les unités externes, un calcul est effectué ultérieurement afin de répartir l’empreinte à un niveau de prix normalisé entre les unités utilisatrices internes et externes. 

Les données nécessaires à ces calculs sont issues des données de facturation ou directement fournies par les infrastructures de recherche concernées.


### 3.	Facteurs d’émissions


Ce module est particulier dans le sens où les facteurs d’émissions dépendent de plusieurs facteurs :

1. Les émissions des catégories ***Émissions de procédés***, ***Bâtiments***, ***Équipements*** et ***Achats***  
2. L’utilisation par l’unité utilisatrice  


- ***[Voir Facteurs d’émissions Émissions de procédés](./processes.md#3-facteurs-démission)***
- ***[Voir Facteurs d’émissions Bâtiments](./building.md#3-facteurs-démission)***
- ***[Voir Facteurs d’émissions Équipements](./equipment.md#3-facteurs-démission)***
- ***[Voir Facteurs d’émissions Achats](./purchases.md#3-facteurs-démission)***




### 4.	Méthodologie

L’empreinte carbone associée à l’utilisation d’une infrastructure de recherche est calculée à partir de l’empreinte carbone des modules suivants de l’infrastructure : ***Émissions de procédés***, ***Bâtiments***, ***Équipements*** et les ***Achats***. 

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

- ***[Émissions de procédés](./processes.md#4-méthodologie)*** 
- ***[Bâtiments](./building.md#4-méthodologie)***
- ***[Équipements](./equipment.md#4-méthodologie)*** 
- ***[Achats](./purchases.md#4-méthodologie)*** 


### 5. Limites

Ce module possède un niveau d’incertitude élevé. En effet, l’attribution de l’empreinte carbone liée à l’utilisation des infrastructures de recherche EPFL repose sur les empreintes carbones des modules ***Émissions de procédés***, ***Bâtiments***, ***Équipements*** et ***Achats***, qui eux-mêmes possèdent leurs propres les limites.  

- ***[Limites du module Émissions de procédés](./processes.md#5-limites)***
- ***[Limites du module Bâtiments](./building.md#5-limites)***
- ***[Limites du module Équipements](./equipment.md#5-limites)*** 
- ***[Limites du module Achats](./purchases.md#5-limites)*** 

Par ailleurs, l’espace Calculateur CO₂ repose sur des modules partiellement automatisés, qui utilisent par défaut les données remontées par chaque module. Ainsi, si les modules des infrastructures de recherche n’ont pas été validés, des erreurs peuvent subsister, ce qui peut influencer l’attribution de leur empreinte carbone aux unités utilisatrices.

De plus, il y a des limites liées à la clé de répartition qui repose principalement sur les données monétaires à l’exception de certaines plateformes où le nombre d’heures d’utilisation ou le nombre d’hébergements sont considérés. 

- Les données de facturation sont un premier indicateur pour l’utilisation des infrastructures de recherche. Cependant, il y a de nombreuses limites, notamment dues à la tarification différenciée entre les unités internes et externes et même entre unités internes faisant partie de différentes facultés ou services.
- Les heures d’utilisation sont des indicateurs plus pertinents avec moins d’incertitude et sont priorisés si les infrastructures de recherche possèdent ces données pour l’ensemble des unités utilisatrices. 


### 6. Références
- La méthodologie de ce module a été développée en se référant pour une partie à la méthodologie développée par Labos1point5 dans le GES1point5 [https://apps.labos1point5.org/documentation/carbon/ges-calculating-methods](https://apps.labos1point5.org/documentation/carbon/ges-calculating-methods) et affinée au contexte EPFL par le GT infrastructures de recherche. 


