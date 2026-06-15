## 4.3 Bâtiments 

### 1.	Contexte 
L’empreinte carbone considérée dans le module **Bâtiments** comprend l’impact lié aux deux sous modules suivants : 

- Le sous-module *Locaux* couvre les émissions relatives au chauffage, climatisation, ventilation et éclairage des différentes surfaces de bâtiments liées aux données entrées dans la base de données interne relative aux surfaces des locaux.
- Le sous-module *Émissions de combustion d’énergie* est disponible pour compléter avec d'autres émissions de combustion d'énergie dans le cas où une unité utilise une source d'énergie non-centralisée. Les émissions liées à la combustion d'énergie dans les laboratoires proviennent principalement de la combustion sur place de combustibles destinés au chauffage, à la ventilation, à l'eau chaude et à des équipements spécialisés.

Le module **Bâtiments** vise à capturer ces émissions en lien avec l’énergie. Le sous-module *Locaux* concerne les émissions indirectes et donc le scope 2. Le sous-module *Émissions de combustion d’énergie* concerne les émissions directes et donc le scope 1.

### 2.	Données collectées

***Sous-module Locaux***

La base de données interne relative aux surfaces des locaux fournit la liste des locaux utilisés par une unité et leur surface.

Les données de consommation d’énergie (en kWh/m2) et des typologies de salle (normes DIN/SIA) sont fournies par la Vice-présidence pour les opérations à l’EPFL (VPO). Les données de consommation sont ensuite redistribuées en fonction de la typologie des salles utilisées par une unité. 

***Sous-module Émissions de combustion d’énergie***

Les données de consommation d’énergie thermique centralisée pour le sous-module Émissions de combustion d’énergie sont saisies manuellement.

### 3.	Facteurs d’émissions

***Sous-module Locaux***

Pour l’électricité, le facteur d’émission 0.097 kg CO₂-eq/kWh (BAFU, 2025) est utilisé dans ce module.

***Sous-module Émissions de combustion d’énergie***

Pour la consommation d’énergie thermique centralisée, les facteurs d’émission proviennent du Corporate Footprint Calculator, et en particulier de la base de données BAFU (2025). 

Pour les émissions de combustion d’énergie de systèmes non-centralisés, les facteurs d’émissions de Labos1point5 (2021, 2022) sont utilisés (voir section 7 Annexe).  

### 4.	Méthodologie

***Sous-module Locaux***

L’empreinte carbone de chaque local $CF_{rooms}$ est calculée comme le produit de la surface du local en m2 et la consommation de chauffage, refroidissement, ventilation et éclairage en kWh par m2 par type de salle et par bâtiment ainsi que le facteur d’émission de l’électricité suisse tel que :

$$
CF_{rooms} = Surface \cdot \left(
Cons_{heating, building, room_{type}} +
Cons_{cooling, building, room_{type}} +
Cons_{ventilation, building, room_{type}} +
Cons_{lighting, building, room_{type}}
\right) \cdot EF_{electricity}
$$

Où :

-  $buildings$ : bâtiment où les locaux de l’unité se situent  
- $room_{type}$ : type de local parmi les catégories *bureau, divers, laboratoires, archives, bibliothèques, auditoires*  
- $Surface$: surface occupée (m²)  
- $Cons_{heating, building, room_{type}}$
- $Cons_{cooling, building, room_{type}}$
- $Cons_{ventilation, building, room_{type}}$
- $Cons_{lighting, building, room_{type}}$ : consommation électrique pour le chauffage, refroidissement, ventilation et éclairage du local (kWh/m²), extrapolée à partir des données de la VPO, selon le bâtiment et le type de salle  
- $EF_{electricity}$ : facteur d’émission de l’électricité (0.097 kg CO₂-eq/kWh, BAFU, 2025)
  

***Sous-module Émissions de combustion d’énergie***

L’empreinte carbone $CF_{combustion}$ est calculée comme le produit de la quantité de consommation de combustible en kg ou kWh ou kWh et le facteur d’émission correspondant tel que :

$$
CF_{combustion} = Q_{fuel_{type}} \cdot EF_{fuel_{type}}
$$

Où : 

- $fuel_{type}$ : type de combustible utilisé : gaz naturel, fioul domestique, biométhane, granulés de bois, plaquettes forestières et bois bûche
- $Q_{{fuel}_{type}}$ : quantité de combustibles utilisée pour une source de chauffage non-centralisé en kg ou kWh saisie manuellement.
- $EF_{{fuel}_{type}}$ : facteur d’émission de chaque combustible en kg CO₂-eq/kWh ou kg CO₂-ep/kg.

### 5. Limites
- L’occupation en m2 donnée par la base de données interne relative aux surfaces des locaux peut ne pas être représentative de la réalité en cas de mutualisation ou prêt de locaux.
- La consommation électrique pour le chauffage, refroidissement, ventilation et éclairage des locaux est extrapolée à partir d’une valeur unique de consommation par bâtiment fournie par la VPO pour déduire une valeur spécifique par utilisation (chauffage, refroidissement, ventilation et éclairage) et par type de local (office, miscellenious, laboratories, archives, libraries ou auditorium) basée sur la norme SIA.
- Le facteur d’émission 0.097 kg CO₂-eq/kWh représente une moyenne annuelle suisse, et non du mix électrique au moment de l’utilisation de l’équipement.
- La consommation de combustibles pour estimer les émissions de combustion d’énergie d’un système de chauffage non-centralisé doit être saisie manuellement. La qualité des résultats dépend donc de la qualité de cette donnée d’entrée.
  
### 6. Références
- Base de données interne relative aux surfaces des locaux Labos1point5 : [Facteurs d'emission - version de juin 2021](https://apps.labos1point5.org/static/carbon/FacteursEmission_GES1point5_Juin2021.pdf) et [Facteurs d'emission biens et services - version de janvier 2022](https://apps.labos1point5.org/static/carbon/FacteursEmission_BiensEtServices_janvier2022_FR.pdf). Pour les biens et services vous pouvez également consulter une discussion plus détaillée dans [De Paepe 2023].
- Corporate Footprint Calculator v 1.0, [https://www.itinero.admin.ch/fr/feuilles-de-route-zero-net#Corporate-Footprint-Calculator](https://www.itinero.admin.ch/fr/feuilles-de-route-zero-net#Corporate-Footprint-Calculator)
- BAFU 2025, [https://nexus.openlca.org/database/BAFU](https://nexus.openlca.org/database/BAFU)
- Norme SIA: [https://www.bak.admin.ch/bak/fr/home/baukultur/qualitaet/normen/sia-normen.html](https://www.bak.admin.ch/bak/fr/home/baukultur/qualitaet/normen/sia-normen.html)


### 7. Annexe
 | Catégorie d’émission de combustion d’énergie | English        | Unité   | Nom                                                       | Année | Facteur d’émission | Unité du facteur d’émission |
|-----------------------------------------------|---------------|---------|-----------------------------------------------------------|-------|---------------------|------------------------------|
| Gaz naturel                                   | Natural gas   | kWh PCI | Gaz naturel, mix moyen                                   | 2022  | 0.24                | kg CO₂-eq / kWh PCI          |
| Fioul domestique                              | Heating oil   | kWh PCI | Fioul domestique                                         | 2014  | 0.3243              | kg CO₂-eq / kWh PCI          |
| Biométhane                                    | Biomethane    | kWh PCI | Biométhane – Injecté dans les réseaux – Mix moyen        | 2020  | 0.0444              | kg CO₂-eq / kWh PCI          |
| Granulés de bois                              | Pellets       | kg      | Granulés bois – 8% d'humidité                            | 2014  | 0.1108              | kg CO₂-eq / kg               |
| Plaquettes forestières                        | Forest chips  | kg      | Plaquettes forestières – 25% d'humidité                  | 2022  | 0.0503              | kg CO₂-eq / kg               |
| Bois bûche                                    | Wood logs     | kg      | Bois bûche – 20% d'humidité                             | 2014  | 0.1138              | kg CO₂-eq / kg               |

    Tableau 2 : Émissions de combustion d’énergie de systèmes non-centralisés (Labos 1point5, 2021,2022)
