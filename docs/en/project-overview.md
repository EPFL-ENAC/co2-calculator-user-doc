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

Finally, the EPFL tool is designed to be adjustable to other academic institutions specific characteristics, particularly those in Switzerland.

### 3. The tool and its functionalities

The CO₂ calculator tool has three workspaces: 

#### *CO₂ calculator space* 

The CO₂ Calculator tool includes three workspaces:

#### *3.1 CO₂ Calculator Workspace*

This workspace enables users to assess the carbon footprint of their unit each year, based on the previous calendar year (from January 1 to December 31), using the following modules:

- **Headcount**: this module estimates the carbon footprint associated with the additional categories displayed on the Results page (Food, Commuting, Waste).
- **Process Emissions**: this module estimates greenhouse gas emissions related to experimental procedures and equipment leaks.
- **Buildings**: this module estimates the carbon footprint associated with energy combustion emissions (if the unit uses a non-centralized energy source), as well as emissions related to the building itself (heating, cooling, ventilation, and lighting).
- **Equipment**: this module estimates the carbon footprint associated with the electricity consumption of equipment (scientific, IT, etc.) during both active use and standby mode.
- **External Clouds and AI**: this module estimates the carbon footprint associated with the use of external cloud services and artificial intelligence (AI).
- **Professional Travel**: this module estimates and visualizes the carbon footprint of profesionnal travel by air and rail.
- **Purchases**: this module estimates the carbon footprint associated with the unit’s purchases, item by item, using procurement data recorded in the invoicing system.
- **EPFL Research Facilities**: this module estimates the carbon footprint associated with your unit’s use of EPFL research facilities.

Principal users have access to and can view all the modules listed above, whereas standard users can only complete the External Clouds and AI and profesionnal Travel modules. However, they can view the aggregated results of the other modules on the Results page once these have been validated.

This workspace also makes it possible to track the evolution of the unit’s emissions over time.

#### *3.2 CO₂ project planner workspace*

The CO₂ Project Planner workspace makes it possible to estimate the carbon footprint of various projects, whether for funding applications or for past, ongoing, or future projects, based on data retrieved from the CO₂ Calculator.

***Grant proposal***

Estimating the carbon footprint of a project linked to a funding application can be performed by either standard or principle users.
 
In addition to entering the total budget and the budget allocated to each module, users must manually add funding application data for certain modules.

For principle users, data from some modules are automatically retrieved from the CO₂ Calculator (Process Emissions, Buildings, Equipment, External Clouds and AI), while data for others must be entered manually (Headcount, Profesionnal Travel, Purchases, EPFL Research facilities). To simplify data entry, the Equipment module allows users to apply an overall usage percentage rather than entering each piece of equipment individually. Similarly, the Purchases module offers two estimation methods: based either on an overall budget or on a budget by purchasing category.

For standard users, data must be added manually for each module. These different data retrieval options were implemented in particular to ensure the protection of personal data.

The estimate can also be made visible to all members of the unit, regardless of their role (principle or standard user).

The reference year determines the emission factors used by the CO₂ Project Planner to calculate the emissions attributable to the project.

***Detailed per year***

For principle users, estimating the carbon footprint of a project, whether past, ongoing, or future, is carried out through the automatic retrieval of data from the CO₂ Calculator.

To obtain an annual estimate of a project’s carbon footprint, principle users can indicate the share represented by the project relative to the unit’s total activities for the reference year. This can be done by using the slider available in each module table and entering the project’s relative weight in the “% of reference year” column.

For standard users, it is also possible to estimate the carbon footprint of a project, whether past, ongoing, or future. However, unlike principle users, this estimate does not benefit from automatic data retrieval from the CO₂ Calculator, in order to ensure the protection of personal data. Data must therefore be entered manually for each module.

For the same reason, the annual breakdown of a project is not accessible to all members of the unit, since it relies on data originating from the CO₂ Calculator. Access to this section is restricted to individuals accredited as principle users.

As an alternative, it is possible to download the project PDF report and share it with members of the unit.

#### *3.3 CO₂ Explorer Workspace*

The CO₂ Explorer makes it possible to estimate the carbon footprint of specific items or actions. It facilitates the assessment of different scenarios and offers the possibility of downloading the results in a PDF report.

Exploration is available for all modules included in the CO₂ Calculator and is accessible to all types of users (both principle and standard users).


### 4. Tool objectives
The open-source CO₂ calculator tool  is designed to: 

- Propose a consistent approach to identify and visualize the main emission sources related to laboratory activities and their impacts
- Identify carbon emission profiles specific to each type of laboratory
- Estimate the carbon footprint of a research project (grant proposal or detailed per year ) or of specific items or actions (new purchases, future professional travel, electricity consumption of a piece of equipment, etc.)
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

<img width="451" height="201" alt="image" src="https://github.com/user-attachments/assets/90050d79-1111-489b-a0e8-ca92bfa9cc85" />

Figure 1: EPFL GreenLabs approach

The CO₂ calculator makes it possible to anticipate future obligations regarding monitoring and reporting carbon emissions related to research activities.

In addition, the CO₂ Project Planner workspace makes it possible to estimate the carbon footprint of a project related to a funding application, whether it is past, ongoing, or future, while the CO₂ Explorer workspace makes it possible to estimate the carbon footprint of a specific action, such as a business trip, the use of scientific equipment, and so forth.
