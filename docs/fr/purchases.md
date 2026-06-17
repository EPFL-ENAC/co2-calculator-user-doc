### 1.	Contexte
Les achats représentent une part significative de l’empreinte carbone des activités de recherche, en particulier dans les environnements de laboratoire où les consommables, les produits chimiques et les équipements sont utilisés de manière intensive. Au-delà de leur usage direct, les biens achetés intègrent des émissions en amont liées à l’extraction des matières premières, à la fabrication, à l’emballage et au transport.

Le module Achats vise à capturer ces émissions indirectes (scope 3). Il couvre ***8 sous-modules*** :

- *Équipements scientifiques*
- *Équipements informatiques*
- *Consommables et accessoires*
- *Produits biologiques, chimiques et gazeux*
- *Services*
- *Véhicules*
- *Autres achats*
- *Achats centralisés* 

### 2.	Données collectées
Le module inclut l’ensemble des biens et services achetés auprès de fournisseurs externes durant l’année de référence.

Pour chaque achat, les informations suivantes sont automatiquement intégrées à partir des factures payées, liées au centre financier de chaque unité :

- Description de l’article
- Fournisseur
- Code UNSPSC
- Quantité
- Montant total payé

Le ***sous-module Achats centralisés*** est destiné à intégrer des éléments prédéfinis correspondant à des achats centralisés et/ou mutualisés entre plusieurs unités. Lorsque cela s’applique, la consommation annuelle pour ces éléments doit être renseignée.

<a id="facteurs"></a>
### 3.	Facteurs d’émissions

***Sous-modules Achats standards***
Ils comprennent les sous-modules suivants : *Équipements scientifiques, Équipements informatiques, Consommables et accessoires, Produits biologiques, chimiques et gazeux, Services, Véhicules, et Autres achats*.

Chaque article acheté se voit attribuer un facteur d’émission spécifique (kg CO₂-eq / EUR), issu de la base de données partagée par Labos 1point5 ([2021](https://apps.labos1point5.org/static/carbon/FacteursEmission_GES1point5_Juin2021.pdf), [2022](https://apps.labos1point5.org/static/carbon/FacteursEmission_BiensEtServices_janvier2022_FR.pdf), [De Paepe 2024](https://www.biorxiv.org/content/10.1101/2023.04.04.535626v3)). Ce facteur est affiné afin de correspondre au mieux au type de produit ou à sa catégorie, notamment à l’aide d’un outil d’IA développé par le SDSC. Cette approche à l’échelle de l’article permet une estimation plus précise que l’utilisation de facteurs génériques. Cependant, pour les achats ajoutés manuellement, une méthode de correspondance est utilisée. Chaque article catégorisé via un code [UNSPSC](https://www.undp.org/unspsc) est associé à un code NACRES (nomenclature d’achat utilisée en France), auquel correspond un facteur d’émission (Labos 1point5). Ce facteur est ensuite appliqué à l’article.

***Sous-module Achats centralisés***
Chaque élément est associé à un facteur d’émission spécifique issu de la base de données [Ecoinvent](https://ecoinvent.org/) (2026).


<a id="methodologie"></a>
### 4.	Méthodologie

***Sous-modules Achats standards***

L’empreinte carbone de chaque achat $CF_{purchase}$ est calculée comme le produit du montant total financier de l’article et le facteur d’émission associé tel que :

$$
CF_{purchase} =Amount_{item,euro,2019} \cdot EF_{item}
$$

Où : 

$$
Amount_{item,euro,2019} =Amount_{item,currency,year} \cdot Ex_{currency,year} \cdot Inflation_{year,2019}
$$

- $item$ : article acheté par l’unité
- $currency$ : devise appliquée pour l’achat de l’article
- $year$ : l’année de référence
- $Amount_{item,euro,2019}$ : coût total de l’achat d’un article en euros en 2019 en tenant compte de l’inflation entre 2019 et l’année correspondante
- $Amount_{item,currency,year}$ : montant total de l’achat d’un article en devise appliquée
- $Ex_{currency,year}$ : taux d’échange entre la devise appliquée et l’euro
- $Inflation_{year,2019}$ : taux d’inflation entre 2019 et l’année de référence
- $EF_{item}$ : facteur d’émission de l’article estimé avec montant converti en euros 2019 en kg CO₂-eq/EUR_2019

Le montant est converti en euros en utilisant le taux d’échange moyen de l’année de référence.

Les facteurs d’émission monétaires sont ajustés à l’aide d’un coefficient d’inflation, afin de refléter les conditions économiques actuelles. Les facteurs (exprimés dans une année de référence) sont multipliés par le taux d’inflation entre 2019 et l’année de référence tel que fourni par la Banque centrale européenne (BCE). Cela permet d’assurer une meilleure cohérence entre les facteurs historiques et les valeurs monétaires actuelles.


***Sous-module Achats centralisés***

Ces achats doivent être saisis manuellement pour une année donnée. 
L’empreinte carbone de chaque achat $CF_{centralised~purchases}$ est calculée comme le produit de la quantité de l’article acheté en unité appliqué, du coefficient permettant de convertir la quantité en kg, et du facteur d’émission associé tel que :

$$
CF_{centralised~purchases} = Q_{item} \cdot Coef_{kg ~ item} \cdot EF_{item}
$$

Où : 

- $item$ : article acheté en manière centralisée (ex : azote liquide)
- $Q_item$  : quantité de l’article acheté en unité appliqué saisie manuellement
- $Coef_{kg ~ item}$  : coefficient pour convertir la quantité en kg
- $EF_{item}$: facteur d’émission de l’article en kg CO₂-eq/kg

Les facteurs d’émission utilisés sont issus de la base ecoinvent (licence restreinte, non diffusables publiquement).

### 5. Limites

- Amortissement du matériel : conformément aux directives du GHG Protocol, l’outil calculateur CO2 adopte une approche par flux. Ainsi, bien que certains équipements soient utilisés sur plusieurs années, nous comptabilisons l’intégralité des émissions liées à leur fabrication l’année de leur achat. Cette approche écarte les incertitudes liées à une approche par stock, qui nécessiterait un inventaire détaillé et des durées de vie fiables. Aucune durée d’amortissement n’est donc appliquée, ce qui permet de réduire les hypothèses arbitraires. En contrepartie, cette méthode peut entraîner des variations importantes des émissions d’une année à l’autre, lesquelles doivent être analysées dans une perspective pluriannuelle.
- Les achats internes (par exemple via des magasins chimiques) ainsi que les achats réalisés par carte de crédit ne sont pas inclus automatiquement, sauf indication contraire. Ces données étant entrées manuellement via la fonction « ajout » disponible dans chaque sous-catégorie, la qualité des résultats est dépendante de la qualité de l’information saisie.
- La précision des résultats dépend de la qualité et de l’exhaustivité des données d’achat (description des articles, catégorisation) extraite de la base de données de l’École, ainsi que des facteurs d’émission utilisés. La méthodologie fournit un ordre de grandeur des émissions basé sur les données financières disponibles.
- L’utilisation de facteurs d’émission monétaires introduit une incertitude significative et ne permet pas de distinguer des choix d’achat ayant des impacts environnementaux différents au sein d’une même catégorie. 


### 6. Références
- Labos 1point5 :  [Facteurs d'emission - version de juin 2021](https://apps.labos1point5.org/static/carbon/FacteursEmission_GES1point5_Juin2021.pdf) et  [Facteurs d'emission biens et services - version de janvier 2022](https://apps.labos1point5.org/static/carbon/FacteursEmission_BiensEtServices_janvier2022_FR.pdf). Pour les biens et services vous pouvez également consulter une discussion plus détaillée dans [De Paepe 2023](https://www.biorxiv.org/content/10.1101/2023.04.04.535626v3).
- UNSPSC: United Nations Standard Products and Services Code (UNSPSC) [https://www.undp.org/unspsc](https://www.undp.org/unspsc)
- Ecoinvent: Ecoinvent Association (2026). ecoinvent data v3.12. [https://www.ecoinvent.org](https://www.ecoinvent.org)
