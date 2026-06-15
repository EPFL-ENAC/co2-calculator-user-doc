# 3. Méthodologie

Le développement d’un tel outil pour évaluer les émissions liées aux activités de recherche exige une méthodologie particulièrement rigoureuse et pragmatique. Selon la disponibilité des données, certains choix quant aux hypothèses du calcul de l’empreinte ont dû être faits et sont détaillés ci-dessous et ce afin d’assurer une transparence totale. Pour chaque sous-module et module, la méthodologie ainsi que les références utilisées sont détaillées dans la partie "Spécification des modules”. 

## 3.1 Référentiel de calcul des émissions 

Le calculateur CO₂ s’appuie sur le **[Greenhouse Gas Protocol (GHG Protocol)](https://ghgprotocol.org/blog/you-too-can-master-value-chain-emissions)**, la norme internationale de référence pour le calcul et la comptabilisation des émissions de gaz à effet de serre (GES).

Développé en 1998 par le World Resources Institute (WRI) et le World Business Council for Sustainable Development (WBCSD), le GHG Protocol est la norme de référence la plus largement reconnue et utilisée au niveau mondial pour la comptabilisation et le compte rendu des émissions de gaz à effet de serre. Il fournit aux organisations un cadre clair pour calculer les émissions liées à leurs activités et à leur chaîne de valeur, afin d’identifier des leviers de réduction. 

Cet ouil s’efforce de suivre le GHG Protocol avec la plus grande rigueur possible et détaillée ci-dessous, notamment via l’intégration des trois scopes d’émissions.

### Les trois scopes d’émissions

Le GHG Protocol distingue trois grandes catégories d’émissions, appelées scopes. 

<img width="383" height="256" alt="image" src="https://github.com/user-attachments/assets/cac70157-c3c7-4f32-85d1-f931fa65a082" />
        
        Figure 2 :  The Greenhouse Gas Protocol Corporate Standard (2019, p. 26).

#### Scope 1 – Émissions directes
Il s’agit des émissions de GES provenant de sources directement contrôlées par l’organisation, par exemple : 
- La combustion de combustibles fossiles dans les bâtiments ou installations ; 
- Les émissions issues de procédés industriels, tels que le CO₂, le CH₄ et le N₂O.

#### Scope 2 – Émissions indirectes liées à l’énergie
Ce scope couvre les émissions associées à la production d’électricité, de chaleur ou de vapeur achetées et consommées par l’organisation.

#### Scope 3 – Autres émissions indirectes
Le scope 3 regroupe l’ensemble des autres émissions indirectes résultant des activités de l’organisation, telles que :

- Les achats de biens et services ;
- Les voyages professionnels ;
- La mobilité pendulaire ;
- La gestion des déchets ;
  
D'autres catégories présentes dans le GHG Protocol, comme les investissements, ne sont pas considérées dans cette version de l’outil. 

## 3.2 Application du périmètre
### Espace Calculateur CO₂

Le périmètre de ce calculateur s’applique aux émissions liées aux activités opérationnelles d’une unité de recherche telles que :
- **Émissions de procédés (Scope 1)**
- **Bâtiments** – *Énergie de combustion* **(Scope 1)**
- **Bâtiments** – *Locaux* **(Scope 1 et/ ou 2)**
- **Équipements (Scope 2)**
- **Clouds externes et IA (Scope 3)**
- **Voyages professionnels (Scope 3)**
- **Achats (Scope 3)**
- **Infrastructures de recherche EPFL (Scope 3)**
- **Catégories additionnelles** - *Pendularité, Alimentation, Déchets, Constructions et rénovations* **(Scope 3)**

Certaines émissions liées aux Locaux dans le module **Bâtiments** peuvent aussi apparaitre dans le scope 1, selon la source de chauffage du bâtiment.

Ce périmètre organisationnel correspond aux installations et activités sur lesquelles les unités de recherche exercent un contrôle, direct ou indirect, et pour lesquelles elles disposent de leviers d’action concrets afin de réduire leurs émissions. Les émissions indirectes associées aux investissements de capital ne sont pas inclus dans le calcul de l’empreinte carbone. 

Pour chacun des sous-modules et modules, l’estimation de l’empreinte carbone (CF) d’une catégorie donnée $$CF_{\text{category}}$$ suit le calcul suivant :

$$
CF_{\text{category}} = Q_{\text{category}} \cdot EF_{\text{category}}
$$

- $Q_{\text{category}}$ : correspond à la quantité d’une activité donnée dans la catégorie
- $EF_{\text{category}}$ : représente le facteur d’émission de la catégorie

Par exemple, pour le module **Équipements**, un incubateur qui est utilisé sur une année pour un total de 440 kWh émet 440 x 0,097 = 42.7 kg CO₂-eq, car le facteur d’émission d’un kWh du mix de consommation suisse est de 0,097 kg CO₂-eq (BAFU, 2025). 

Selon les données disponibles, il est parfois nécessaire d’effectuer des calculs afin d’obtenir la quantité de l’activité émettrice. Par exemple, dans le cas de l’incubateur ci-dessus, la quantité de kWh a été estimée sur la base de la puissance moyenne en standby en activité, et selon le rapport des heures d’utilisation par semaine. Plus de détails et d’information sur les choix et les méthodes de calcul sont accessibles dans l’onglet « Spécification des modules ».


### Espace Simulateur CO₂

L’espace *Simulateur CO₂* possède deux fonctionnalités.  

La fonctionnalité *Explorer* permet d’estimer l’empreinte d’un ou plusieurs modules relatifs à ceux figurant dans l’espace Calculateur CO₂.

- **Émissions de procédés** : même espace que dans le Calculateur CO₂ avec saisie manuelle.
- **Équipements** : même espace que dans le Calculateur CO₂, mais aucune donnée n’est préremplie automatiquement. Les équipements sont sélectionnés via un menu déroulant, avec possibilité de télécharger un fichier CSV.
- **Clouds externes & IA** : même espace que dans le Calculateur CO₂ avec saisie manuelle.
- **Voyages professionnels** : saisie manuelle des voyages professionnels en avion et train.
- **Achats** : saisie du budget d’achats, répartition par grandes catégories d’achat.

La fonctionnalité *Planifier* permet d’estimer l’empreinte d’un projet de recherche en cours ou à venir. L’empreinte carbone d’un **projet de recherche** est calculée à partir des données saisies pour une année tirée du calculateur CO₂ ainsi que pour l’unité concernée. Les informations sont complétées ensuite pour chaque module ci-dessous, soit par saisie manuelle, soit à partir des données de l’année de référence dans l’outil.

- **Personnel** : saisie manuelle du nombre d’équivalents plein-temps (EPT), sélection des catégories de métiers concernées.
- Émissions de procédés : données reprises de l’année de référence choisie avec saisie du pourcentage lié au projet de recherche pour chaque ligne, avec possibilité d’ajouter un procédé via un menu déroulant (similaire à la fonctionnalité « ajouter une émission de procédés »).
- **Bâtiments** : données reprises de l’année de référence choisie avec saisie du pourcentage attribué au projet.
- **Équipements** : affichage de la liste des équipements (valeurs à 0 sauf la colonne standby), saisie du pourcentage d’utilisation pour le projet, avec possibilité d’ajouter un équipement via un menu déroulant (similaire à la fonctionnalité « ajouter Équipement »).
- **Cloud externes & IA** : récupération de la liste des services cloud et IA de l’année de référence choisie, méthodologie identique au module existant, sélection des services utilisés pour le projet et saisie du pourcentage d’utilisation associé.
- **Voyages professionnels** : saisie manuelle des voyages professionnels en avion et en train.
- **Achats** : saisie du budget d’achats, répartition par grandes catégories d’achats et application des facteurs d’émission correspondants à préciser : saisie en CHF.
- **Infrastructures de recherche EPFL** : récupération de la liste des plateformes utilisées de l’année de référence choisie, sélection des plateformes utilisées pour le projet, saisie du budget disponible, et possibilité d’ajouter une infrastructure via un menu déroulant. 

L’accès à ces deux fonctionnalités dans l’espace *Simulateur CO₂* est individuel et les saisies ne remontent pas vers la ou le responsable d’unité. Les simulations peuvent cependant être sauvegardées et partagées via l’extraction en CSV ou PDF dans le cas où la personne cocherait l’option de partage. 

## 3.3 Unité de mesure : kg CO₂-eq et t CO₂-eq
Plusieurs gaz contribuent à l'effet de serre, tels que le méthane (CH₄), l'oxyde nitreux (N₂O) et le dioxyde de carbone (CO₂), pour n'en citer que quelques-uns. Ces différents gaz ont un potentiel de réchauffement global plus ou moins élevé. Le dioxyde de carbone, étant le gaz le plus connu, il sert de gaz de référence. Par conséquent, dans la comptabilisation des GES, les émissions sont exprimées soit en kilogrammes (kg CO₂-eq) ou en tonnes métriques (t CO₂-eq) d'équivalent CO₂. 

## 3.4 Résultats 
Après avoir validé tous les modules, l’utilisatrice ou l’utilisateur accède à la page des résultats. Cette page présente différentes visualisations et informations relatives au bilan carbone de l’unité.

En particulier, un résumé en haut de la page, composé de trois encadrés qui affichent :
- Le total des émissions en équivalent CO₂ pour l’unité ;
- Le total par équivalent plein temps (EPT) ;
- Une comparaison avec les années précédentes, lorsque ces données sont disponibles.

Plusieurs graphes de synthèse :
- Un diagramme en barres présentant les totaux par catégorie. Les résultats y sont visualisés à la fois par catégorie et par scope ;
	Insérer image graphe résultats
- Un diagramme en barres empilées montrant les émissions par EPT ;
	Insérer image graphe émissions par EPT
- Un graphe interactif permettant de visualiser, d’une part, la trajectoire idéale de réduction des émissions de l’institution afin de respecter ses objectifs climatiques et, d’autre part, la trajectoire correspondant à l’unité. Des curseurs permettent d’interagir avec le graphe afin de simuler la mise en œuvre d’actions susceptibles de réduire les émissions.
	Insérer image graphe trajection réduction émissions 

La page présente ensuite un focus par catégorie, qui suit la structure des modules dans l’espace Calculateur CO₂. Pour chaque catégorie, des visualisations supplémentaires permettent d’examiner plus en détail la nature des contributions aux émissions.

Un focus spécifique sur le numérique est également proposé. Cette catégorie apparaissant de manière transversale dans plusieurs modules, un résumé est présenté ici afin de permettre de visualiser l’ensemble de son impact pour l’unité.

Enfin, la page peut inclure des graphes pour les catégories additionnelles, basées sur des données génériques et non pas sur des données spécifiques à l’unité. Une distribution des émissions y est présentée afin de sensibiliser l’utilisatrice ou l’utilisateur à la nature de ces émissions à l’échelle de l’institution et de fournir des ordres de grandeur supplémentaires. Il est possible de visualiser ou non ces catégories additionnelles en utilisant la coche prévue à cet effet.

## 3.5 Mises à jour des résultats et facteurs d’émissions 
Les facteurs d’émissions font l’objet d’une revue annuelle. Lorsqu’une mise à jour est effectuée, elle s’applique uniquement à partir de l’année suivante, sans modification des données des années précédentes. 

Exception : dans le cas où les facteurs d’émissions comportent des erreurs importantes et/ou si les **Infrastructures de recherche EPFL** ont mis à jour leur empreinte carbone en cours d’année, une rectification peut être effectuée par la Durabilité EPFL. Un message s’affichera alors dans la page d’accueil pour les unités utilisatrices concernées afin de garantir une transparence totale. 

## 3.6 Limites 
Cet outil, comme tout outil d’empreinte carbone, fournit des estimations, qui comportent une part d’incertitude. La fiabilité des résultats dépend également de la fiabilité des données primaires sur lesquelles se basent les calculs. Un besoin de nettoyage des données d’entrée peut s’avérer nécessaire pour affiner les résultats (ex : données d’inventaire).  Les résultats doivent donc être compris comme des ordres de grandeur, à interpréter avec précaution. Il s’agit par ailleurs d’une première itération, qui sera mise à jour et améliorée au fur et à mesure que de nouvelles données deviendront disponibles. 

### Données d’inventaire
Pour chaque module, les données les plus pertinentes à disposition au moment du calcul ont été utilisées. Toutefois, il peut arriver que ces données ne permettent que partiellement le calcul de l’empreinte carbone dans la catégorie désirée. Dans le cas où ces données ne sont pas disponibles, des approximations ont été réalisées à partir de données connexes, ou d’informations complémentaires.

C’est pourquoi certains modules requièrent une saisie de données manuelle afin de permettre une estimation plus précise de l’empreinte carbone. Par ailleurs, une saisie manuelle est disponible dans la plupart des modules, afin de compléter les informations si des éléments importants manquent. Plus de détails propres à chaque module sont disponibles dans leur documentation respective.

### Facteurs d’émission
Selon les modules et sous-modules de l’espace Calculateur CO₂, les facteurs d’émission les plus fiables et disponibles sont utilisés. Leur niveau de précision varie toutefois en fonction de la maturité des méthodes et de la complexité des activités : certains sont proches des données physiques (comme le mix électrique national), tandis que d’autres, donnent une estimation plus approximative (par exemple pour certains services numériques).

De plus, les facteurs d’émission peuvent être calculés selon deux approches complémentaires.

- L’approche dite « physique » consiste à convertir des données mesurables (par exemple kWh consommés ou kilomètres parcourus) en émissions de CO₂ équivalent.
- À l’inverse, l’approche « monétaire » repose sur la conversion de dépenses (en euros, ou autre devise) en émissions de CO₂ équivalent.

Dans ce second cas, les facteurs d’émission sont ajustés pour tenir compte de l’inflation, afin de refléter les conditions économiques actuelles. Concrètement, dans cet outil, les facteurs exprimés dans une année de référence sont actualisés à l’aide des taux d’inflation fournis par la Banque centrale européenne entre 2019 et l’année considérée. Cette méthode permet de garantir la cohérence entre des facteurs historiques et des données financières actuelles.

L’approche monétaire introduit un niveau d’incertitude supplémentaire par rapport à l’approche physique. Cette approche est néanmoins privilégiée compte tenu de la disponibilité des données pour recourir à l’approche physique.  

Enfin, il convient de noter que les facteurs d’émission comportent toujours une part d’incertitude. Issus de modélisations, ils reposent sur des hypothèses et peuvent, dans certains cas, constituer des approximations par rapport aux situations réelles auxquelles ils sont appliqués.

### Degré de confiance
Pour l’ensemble de ces raisons, chaque module est associé à un degré de confiance. Celui-ci prend en compte notamment la qualité des données d’inventaire, leur précision et leur niveau de couverture, la précision des facteurs d’émission utilisés, ainsi que la méthode employée (par exemple : approche physique ou approche monétaire).


### Résultats valables seulement en Suisse
Les résultats affichés sont valables pour une structure implantée en Suisse. Pour un autre pays, les résultats ne seront pas totalement pertinents car certains facteurs d'émission sont propres à la Suisse. Cela concerne d'une part les facteurs d'émission liés à l'électricité : en Suisse, l'électricité est produite en grande majorité à partir de l'énergie hydraulique (environ 60%) et nucléaire (environ 30%), peu carbonée [2]. La Suisse importe aussi de l'électricité d'Allemagne, de France et d'Autriche, principalement en hiver pour combler un déficit de production. Cela inclut les consommations d'électricité au sein des industries et ménages, mais aussi toutes les émissions relatives à la mobilité électrique (train, tramway, métro, voiture électrique, etc.). D'autre part, les facteurs d'émission des réseaux de chaleur locaux sont aussi spécifiques au moyen de production : chaque réseau urbain de chaleur a un mix énergétique différent et donc un facteur d'émission propre. Il est toutefois possible pour une autre organisation qui souhaiterait utiliser l’outil d'entrer ses propres facteurs d’émission et donc de créer des résultats adaptés à la géographie de son activité.


[2] https://www.energie-environnement.ch/eclairage-electricite-du-menage/mix-electrique-et-mix-energetique


