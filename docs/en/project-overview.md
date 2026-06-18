### 1. Project context
As part of the decentralised federal administration, EPFL must meet ambitious greenhouse gas emission reduction targets. As an academic institution, the largest share of its environmental footprint stems from its research activities. Laboratories consume around ten times more energy than conventional offices due, for example, to their specific ventilation requirements, the use of energy-intensive equipment, and data management in high-performance computing centers [1]. Beyond energy consumption, purchases and travel, to name but a few, account for a significant proportion of CO₂ emissions and present a major challenge in terms of reduction.

[1] Freese, T., Elzinga, N., Heinemann, M., Lerch, M. M., & Feringa, B. L. (2024). The relevance of sustainable laboratory practices. RSC Sustainability, 2(5), 1300-1336.

### 2. From a prototype to large-scale deployment

In order to better understand — by providing orders of magnitude — and better quantify the carbon footprint of laboratories, a prototype of the CO₂ calculator was developed in 2019 within the School of Life Sciences (SV) at EPFL.

Its design is based on a collaborative approach involving laboratories and platforms within the faculty, the SV Sustainability office, central services of the faculty and EPFL, the student association Zero Emission Group, and external partners, particularly the consulting firm Quantis. This prototype was then tested in around thirty EPFL laboratories, paving the way for the development of a tool deployed across all faculties.

More information: **[SV CO₂ Calculator](https://www.epfl.ch/schools/sv/school-of-life-sciences/about-us/sv-sustainability-office/co2-calculator/)**

The project evolution is part of an ongoing dialogue with external initiatives, particularly **[Labos1point5]([https://labos1point5.org/](https://labos1point5.org/))**, as well as several international networks and conferences. These exchanges have made it possible to align the tool with scientific and international standards. In addition, it integrates recommendations from various research consortia, including certain initiatives of the SCENE program, as well as evolving sustainability requirements in funding applications.

In 2025, EPFL Sustainability, together with the IT department of the School of Architecture, Civil and Environmental Engineering **[(ENAC‑IT)](https://www.epfl.ch/schools/enac/about/enac-it-en/)** and the Domain of Information Systems **[(DSI)](https://www.epfl.ch/about/vice-presidencies/vice-presidency-for-operations-vpo/dsi/)**, launched the development of an open-source version of the CO₂ calculator tool. 

Specific work has been carried out with the Swiss Data Science Center **[(SDSC)](https://www.epfl.ch/research/domains/sdsc/)** to adapt EPFL’s purchasing typology to the Labo 1point5 classification, which shares its emissions factor database (UNSPSC to NACRES), thereby facilitating the analysis of emissions related to purchases.
Finally, the EPFL tool is designed to be adjustable to other academic institutions specific characteristics, particularly those in Switzerland.

Un travail spécifique a également été mené avec le Swiss Data Science Center **[(SDSC)](https://www.epfl.ch/research/domains/sdsc/)**, afin d’adapter la typologie des achats EPFL à la classification utilisée par le Labo 1point5 qui nous partage sa base de facteurs d’émissions ([UNSPSC](https://www.undp.org/unspsc) vers [NACRES](https://apps.labos1point5.org/static/carbon/FacteursEmission_BiensEtServices_janvier2022_FR.pdf)), facilitant ainsi l’analyse des émissions liées aux achats. 

Finally, the EPFL tool is designed to be adjustable to other academic institutions specific characteristics, particularly those in Switzerland.

### 3. The tool and its functionalities

The CO₂ calculator tool has two workspaces: 

#### *CO₂ Calculator space* 
This space allows the evaluation of the unit carbon footprint each year, based on the previous calendar year (from January 1 to December 31). This includes the following modules:

- **Process emissions**
- **Buildings**
- **Equipment**
- **External clouds and AI**
- **Professional travel**
- **Purchases**
- **EPFL research facilities**
- **Additional categories** – *Commuting, Food, Waste, Construction and renovation*

This space also allows tracking the evolution of the unit’s emissions over time.

#### *CO₂ Simulator space*
The CO₂ Simulator space has two functionalities.

The *Explore* functionality, allows estimating the footprint of one or more specific modules. Simulation is possible for the following modules:
- **Process emissions**
- **Equipment**
- **Purchases**
- **Professional travel**
- **External clouds & AI**

The *Plan*, functionality, allows estimating the footprint of an ongoing or upcoming research project. It is particularly relevant, for example, when applying for a grant or funding request.

In most modules within this space, data is automatically retrieved from the CO₂ calculator and only requires validation; only in certain cases is manual data entry required.

### 4. Objectifs de l’outil
The open-source CO₂ calculator tool  is designed to: 

- Propose a consistent approach to identify and visualize the main emission sources related to laboratory activities and their impacts
- Identify carbon emission profiles specific to each type of laboratory
- Estimate the carbon footprint of a module (new purchase, future business travel, electricity consumption of equipment, etc.) or of an ongoing or future research project
- Provide a decision-support tool to take targeted measures aimed at reducing the carbon footprint
- Meet future European and national requirements regarding the assessment of the environmental impact of research projects
- Anticipate regulatory developments by equipping EPFL with tools to understand, target, and reduce its carbon emissions

### 5. EPFL Climate & Sustainability Strategy 2030 and the GreenLabs initiative

The CO₂ calculator is fully part of the School’s environmental strategy:

- **[EPFL Climate & Sustainability Strategy 2030](https://www.epfl.ch/about/sustainability/strategy/)** ;
- **[EPFL GreenLabs](https://www.epfl.ch/about/sustainability/fr/recherche-et-innovation/green-labs/)** initiative ;
- Future international and national requirements regarding the evaluation of the environmental impact of research projects

The **[EPFL Climate & Sustainability Strategy 2030](https://www.epfl.ch/about/sustainability/strategy/)** sets ambitious targets by integrating sustainability into the School’s core missions: education, research, and innovation. It also includes measures to reduce environmental impacts related to the institution’s operations. These goals include in particular:

- A 40% overall reduction in greenhouse gas emissions by 2030 compared to 2019
- A 50% reduction in energy-related emissions compared to 2006
- A 30% reduction in emissions related to air travel compared to 2019 (targets defined at the federal level)

Since the entry into force, on January 1, 2025, of the Climate and Innovation Act and the Climate Protection Ordinance, EPFL also aims to reach net zero for scopes 1 and 2 (energy), and, as far as possible, for scope 3 (indirect emissions) by 2040.

In this context, the CO₂ calculator makes it possible to estimate the carbon footprint at the level of research units. The data can then be aggregated at different levels (institutes, faculties).

The **[EPFL GreenLabs](https://www.epfl.ch/about/sustainability/fr/recherche-et-innovation/green-labs/)** initiative, part of this strategy, aims to promote responsible research practices in environmental and social terms, without compromising scientific quality and while respecting planetary boundaries. It seeks to quantify, analyze, and optimize the operational processes of research activities.
 
Figure 1: EPFL GreenLabs approach
The CO₂ calculator makes it possible to anticipate future obligations regarding monitoring and reporting carbon emissions related to research activities.
In addition, the CO₂ Simulation space allows estimating the carbon footprint of one or more modules (e.g. equipment purchase, business travel, electricity consumption of additional equipment) or of a research project, thereby guiding decision-making at the level of a research project or specific module.


Depuis l’entrée en vigueur, le 1er janvier 2025, de la loi sur le climat et l’innovation et de l’ordonnance sur la protection du climat, l’EPFL vise également l’atteinte du net zéro pour les scopes 1 et 2 (énergie), et, dans la mesure du possible, pour le scope 3 (émissions indirectes) à l’horizon 2040.

Dans ce contexte, le calculateur CO₂ permet d’estimer l’empreinte carbone au niveau des unités de recherche. Les données peuvent ensuite être agrégées à différents niveaux (instituts, facultés,). 

L’initiative **[GreenLabs](https://www.epfl.ch/about/sustainability/fr/recherche-et-innovation/green-labs/)**, inscrite dans cette stratégie a pour objectif de promouvoir des pratiques de recherche responsables sur les plans environnemental et social, sans compromettre la qualité scientifique et en respectant les limites planétaires. Elle vise à quantifier, analyser et optimiser les processus opérationnels des activités de recherche 

<img width="902" height="402" alt="image" src="https://github.com/user-attachments/assets/90050d79-1111-489b-a0e8-ca92bfa9cc85" />

      Figure 1: EPFL GreenLabs approach 

The CO₂ calculator makes it possible to anticipate future obligations regarding monitoring and reporting carbon emissions related to research activities.

In addition, the CO₂ Simulation space allows estimating the carbon footprint of one or more modules (e.g. equipment purchase, business travel, electricity consumption of additional equipment) or of a research project, thereby guiding decision-making at the level of a research project or specific module.
