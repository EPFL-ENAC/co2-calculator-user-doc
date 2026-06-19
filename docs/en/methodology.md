The development of such a tool to assess emissions related to research activities requires a particularly rigorous and pragmatic methodology. Depending on data availability, certain assumptions had to be made regarding the calculation of the footprint; these are detailed below to ensure full transparency. For each sub-module and module, the methodology and references used are detailed in the “Module Specifications” section.

### 1. Emissions calculation framework


The CO₂ calculator follows the **[Greenhouse Gas Protocol (GHG Protocol)](https://ghgprotocol.org/blog/you-too-can-master-value-chain-emissions)**, the international reference standard for calculating and accounting for greenhouse gas (GHG) emissions.

Developed in 1998 by the World Resources Institute (WRI) and the World Business Council for Sustainable Development (WBCSD), the GHG Protocol is the most widely recognized and used standard worldwide for accounting and reporting greenhouse gas emissions. It provides organisations with a clear framework to calculate emissions related to their activities and value chain in order to identify reduction levers.

This tool strives to follow the GHG Protocol as rigorously as possible, notably through the integration of the three emission scopes described below.

#### The three emission scopes

The GHG Protocol distinguishes three main categories of emissions, called scopes. 

<img width="383" height="256" alt="image" src="https://github.com/user-attachments/assets/cac70157-c3c7-4f32-85d1-f931fa65a082" />
      
        Figure 2 :  The Greenhouse Gas Protocol Corporate Standard (2019, p. 26).

##### Scope 1 — Direct emissions
These are GHG emissions from sources directly controlled by the organisation, for example:

- Combustion of fossil fuels in buildings or facilities
- Emissions from industrial processes, such as CO₂, CH₄, and N₂O

##### Scope 2 — Indirect emissions from energy 
This scope covers emissions associated with the production of electricity, heat, or steam purchased and consumed by the organisation. 

##### Scope 3 – Autres émissions indirectes
Scope 3 includes all other indirect emissions resulting from the organisation’s activities, such as:

- Purchases of goods and services
- Professional travel
- Commuting
- Waste management

Other categories included in the GHG Protocol, such as investments, are not considered in this version of the tool.

### 2. Scope of application

#### CO₂ Calculator space 

The scope of this calculator applies to emissions related to the operational activities of a research unit such as: 

- **Process emissions (Scope 1)**
- **Buildings** – *Combustion energy **(Scope 1)**
- **Buildings** – *Rooms* **(Scope 1 and/ or 2)**
- **Equipment (Scope 2)**
- **External Cloud and AI (Scope 3)**
- **Professional Travel (Scope 3)**
- **Purchases (Scope 3)**
- **EPFL Research facilities (Scope 3)**
- **Additional categories** - *Commuting, Food, Waste, Construction and renovations* **(Scope 3)**

Some emissions related to rooms in the **Buildings** module may also fall under Scope 1, depending on the building’s heating source.

This organisational scope corresponds to the facilities and activities over which research units have direct or indirect control, and for which they have concrete levers for reducing emissions. Indirect emissions related to capital investments are not included in the carbon footprint calculation.

For each sub-module and module, the estimation of the carbon footprint (CF) of a given category $$CF_{\text{category}}$$ follows the calculation below:

$$
CF_{\text{category}} = Q_{\text{category}} \cdot EF_{\text{category}}
$$

- $Q_{\text{category}}$: corresponds to the quantity of a given activity within the category

- $EF_{\text{category}}$: represents the emission factor of the category


For example, for the **Equipment** module, an incubator that is used for a total of 440 kWh over one year emits:
440 × 0.097 = 42.7 kg CO₂-eq, since the emission factor of one kWh of the Swiss consumption mix is 0.097 kg CO₂-eq (BAFU, 2025).

Depending on data availability, it is sometimes necessary to perform calculations to obtain the quantity of the emitting activity. For example, in the case of the incubator above, the kWh quantity was estimated based on the average active and standby power, as well as the weekly usage hours for a given year. More details on assumptions and calculation methods are available in the “Module Specifications” section.

#### CO₂ Simulator space 

The CO₂ Simulator space includes two functionalities.

The *Explore* functionality allows estimating the footprint of one or more modules corresponding to those in the CO₂ Calculator space:

- **Process emissions**: same interface as in the CO₂ Calculator with manual input.
- **Equipment**: same interface as in the CO₂ Calculator, but no data is pre-filled automatically. Equipment is selected via a drop-down menu, with the option to upload a CSV file.
- **External clouds & AI**: same interface as in the CO₂ Calculator with manual entry.
- **Professional travel**: manual entry of professional travel by plane and train.
- **Purchases**: entry of the purchasing budget and distribution across main categories.

The *Plan* functionality allows estimating the footprint of an ongoing or future research project. The carbon footprint of a **research project** is calculated based on the data entered for one reference year from the CO₂ calculator, as well as for the relevant unit. Information is then completed for each module below, either manually or based on the reference year’s data:

- **Headcount**: manual input of full-time equivalents (FTE), selection of job categories
- **Process emissions:** data retrieved from the selected reference year, with input of the percentage related to the research project for each line, and possibility to add a process via a dropdown menu
- **Buildings**: data retrieved from the selected reference year, with input of the percentage attributed to the project
- **Equipment**: display of the equipment list (values set to 0 except standby), input of usage percentage for the project, with possibility to add equipment via a dropdown menu
- **External clouds & AI**: retrieval of cloud and AI services from the selected reference year, same methodology as the existing module, selection of services used and associated usage percentage
- **Professional travel**: manual input of air and train travel
- **Purchases**: input of purchase budget, distribution across main categories, application of corresponding emission factors (input in CHF)
- **EPFL research facilities**: retrieval of platforms used in the selected reference year, selection of platforms for the project, input of available budget, and possibility to add infrastructure via a dropdown menu

Access to these two functionalities in the *CO₂ Simulator* space is individual, and entries are not reported back to the unit manager. Simulations can, however, be saved and shared via CSV or PDF export if the sharing option is selected.

--- 
### 3. Unité de mesure : kg CO₂-eq et t CO₂-eq
Plusieurs gaz contribuent à l'effet de serre, tels que le méthane (CH₄), l'oxyde nitreux (N₂O) et le dioxyde de carbone (CO₂), pour n'en citer que quelques-uns. Ces différents gaz ont un potentiel de réchauffement global plus ou moins élevé. Le dioxyde de carbone, étant le gaz le plus connu, il sert de gaz de référence. Par conséquent, dans la comptabilisation des GES, les émissions sont exprimées soit en kilogrammes (kg CO₂-eq) ou en tonnes métriques (t CO₂-eq) d'équivalent CO₂. 

### 4. Résultats 
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

### 5. Mises à jour des résultats et facteurs d’émissions 
Les facteurs d’émissions font l’objet d’une revue annuelle. Lorsqu’une mise à jour est effectuée, elle s’applique uniquement à partir de l’année suivante, sans modification des données des années précédentes. 

Exception : dans le cas où les facteurs d’émissions comportent des erreurs importantes et/ou si les **Infrastructures de recherche EPFL** ont mis à jour leur empreinte carbone en cours d’année, une rectification peut être effectuée par la Durabilité EPFL. Un message s’affichera alors dans la page d’accueil pour les unités utilisatrices concernées afin de garantir une transparence totale. 

<a id="limites"></a>
### 6. Limites 
Cet outil, comme tout outil d’empreinte carbone, fournit des estimations, qui comportent une part d’incertitude. La fiabilité des résultats dépend également de la fiabilité des données primaires sur lesquelles se basent les calculs. Un besoin de nettoyage des données d’entrée peut s’avérer nécessaire pour affiner les résultats (ex : données d’inventaire).  Les résultats doivent donc être compris comme des ordres de grandeur, à interpréter avec précaution. Il s’agit par ailleurs d’une première itération, qui sera mise à jour et améliorée au fur et à mesure que de nouvelles données deviendront disponibles. 

#### Données d’inventaire
Pour chaque module, les données les plus pertinentes à disposition au moment du calcul ont été utilisées. Toutefois, il peut arriver que ces données ne permettent que partiellement le calcul de l’empreinte carbone dans la catégorie désirée. Dans le cas où ces données ne sont pas disponibles, des approximations ont été réalisées à partir de données connexes, ou d’informations complémentaires.

C’est pourquoi certains modules requièrent une saisie de données manuelle afin de permettre une estimation plus précise de l’empreinte carbone. Par ailleurs, une saisie manuelle est disponible dans la plupart des modules, afin de compléter les informations si des éléments importants manquent. Plus de détails propres à chaque module sont disponibles dans leur documentation respective.

#### Facteurs d’émission
Selon les modules et sous-modules de l’espace Calculateur CO₂, les facteurs d’émission les plus fiables et disponibles sont utilisés. Leur niveau de précision varie toutefois en fonction de la maturité des méthodes et de la complexité des activités : certains sont proches des données physiques (comme le mix électrique national), tandis que d’autres, donnent une estimation plus approximative (par exemple pour certains services numériques).

De plus, les facteurs d’émission peuvent être calculés selon deux approches complémentaires.

- L’approche dite « physique » consiste à convertir des données mesurables (par exemple kWh consommés ou kilomètres parcourus) en émissions de CO₂ équivalent.
- À l’inverse, l’approche « monétaire » repose sur la conversion de dépenses (en euros, ou autre devise) en émissions de CO₂ équivalent.

Dans ce second cas, les facteurs d’émission sont ajustés pour tenir compte de l’inflation, afin de refléter les conditions économiques actuelles. Concrètement, dans cet outil, les facteurs exprimés dans une année de référence sont actualisés à l’aide des taux d’inflation fournis par la Banque centrale européenne entre 2019 et l’année considérée. Cette méthode permet de garantir la cohérence entre des facteurs historiques et des données financières actuelles.

L’approche monétaire introduit un niveau d’incertitude supplémentaire par rapport à l’approche physique. Cette approche est néanmoins privilégiée compte tenu de la disponibilité des données pour recourir à l’approche physique.  

Enfin, il convient de noter que les facteurs d’émission comportent toujours une part d’incertitude. Issus de modélisations, ils reposent sur des hypothèses et peuvent, dans certains cas, constituer des approximations par rapport aux situations réelles auxquelles ils sont appliqués.

#### Degré de confiance
Pour l’ensemble de ces raisons, chaque module est associé à un degré de confiance. Celui-ci prend en compte notamment la qualité des données d’inventaire, leur précision et leur niveau de couverture, la précision des facteurs d’émission utilisés, ainsi que la méthode employée (par exemple : approche physique ou approche monétaire).


#### Résultats valables seulement en Suisse
Les résultats affichés sont valables pour une structure implantée en Suisse. Pour un autre pays, les résultats ne seront pas totalement pertinents car certains facteurs d'émission sont propres à la Suisse. Cela concerne d'une part les facteurs d'émission liés à l'électricité : en Suisse, l'électricité est produite en grande majorité à partir de l'énergie hydraulique (environ 60%) et nucléaire (environ 30%), peu carbonée [2]. La Suisse importe aussi de l'électricité d'Allemagne, de France et d'Autriche, principalement en hiver pour combler un déficit de production. Cela inclut les consommations d'électricité au sein des industries et ménages, mais aussi toutes les émissions relatives à la mobilité électrique (train, tramway, métro, voiture électrique, etc.). D'autre part, les facteurs d'émission des réseaux de chaleur locaux sont aussi spécifiques au moyen de production : chaque réseau urbain de chaleur a un mix énergétique différent et donc un facteur d'émission propre. Il est toutefois possible pour une autre organisation qui souhaiterait utiliser l’outil d'entrer ses propres facteurs d’émission et donc de créer des résultats adaptés à la géographie de son activité.


[2] https://www.energie-environnement.ch/eclairage-electricite-du-menage/mix-electrique-et-mix-energetique
