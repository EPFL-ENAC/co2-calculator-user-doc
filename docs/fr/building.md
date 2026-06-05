## 4.3 Bâtiments 

### 1.	Contexte 
L’empreinte carbone considérée dans le module **Bâtiments** comprend l’impact lié aux deux sous modules suivants : 

- Le sous-module *Locaux* couvre les émissions relatives au chauffage, climatisation, ventilation et éclairage des différentes surfaces de bâtiments liées aux données entrées dans la base de données interne relative aux surfaces des locaux.
- Le sous-module *Émissions de combustion d’énergie* est disponible pour compléter avec d'autres émissions de combustion d'énergie dans le cas où une unité utilise une source d'énergie non-centralisée. Les émissions liées à la combustion d'énergie dans les laboratoires proviennent principalement de la combustion sur place de combustibles destinés au chauffage, à la ventilation, à l'eau chaude et à des équipements spécialisés.

Le module **Bâtiments** vise à capturer ces émissions en lien avec l’énergie. Le sous-module *Locaux* concerne les émissions indirectes et donc le scope 2. Le sous-module *Émissions de combustion d’énergie* concerne les émissions directes et donc le scope 1.

### 2.	Données collectées

*Sous-module Locaux*

La base de données interne relative aux surfaces des locaux fournit la liste des locaux utilisés par une unité et leur surface.

Les données de consommation d’énergie (en kWh/m2) et des typologies de salle (normes DIN/SIA) sont fournies par la Vice-présidence pour les opérations à l’EPFL (VPO). Les données de consommation sont ensuite redistribuées en fonction de la typologie des salles utilisées par une unité. 

*Sous-module Émissions de combustion d’énergie*

Les données de consommation d’énergie thermique centralisée pour le sous-module Émissions de combustion d’énergie sont saisies manuellement.

### 3.	Facteurs d’émissions

*Sous-module Locaux*

Pour l’électricité, le facteur d’émission 0.097 kg CO₂-eq/kWh (BAFU, 2025) est utilisé dans ce module.

*Sous-module Émissions de combustion d’énergie*

Pour la consommation d’énergie thermique centralisée, les facteurs d’émission proviennent du Corporate Footprint Calculator, et en particulier de la base de données BAFU (2025). 

Pour les émissions de combustion d’énergie de systèmes non-centralisés, les facteurs d’émissions de Labos1point5 (2021, 2022) sont utilisés (voir section 7 Annexe).  


 
