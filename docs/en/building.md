### 1.	Context 
The carbon footprint considered in the **Buildings** module includes the impact associated with the following two sub-modules: 

- The *Rooms* sub-module covers emissions relating to heating, cooling, ventilation and lighting of the various building locations related to the data entered in the internal database relating to rooms location.
- The *Energy Combustion Emissions* sub-module is available to account for other energy combustion emissions in cases where a unit uses a non-centralised energy source. Emissions related to energy combustion in laboratories stem mainly from the on-site combustion of fuels used for heating, ventilation, hot water and specialized equipment.

The **Buildings** module aims to capture these energy-related emissions. The *Rooms* sub-module covers indirect emissions and therefore Scope 2. The *Energy Combustion Emissions* sub-module covers direct emissions and therefore Scope 1.

### 2.	Data collected 

***Rooms sub-module***

The internal database on floor location provides a list of the rooms used by a unit and their floor locations.

Data on energy consumption (in kWh/m²) and room types (DIN/SIA standards) are provided by the Vice-Presidency for Operations at EPFL (VPO). Consumption data is then redistributed according to the types of rooms used by a unit. 

***Energy Combustion Emissions sub-module***

Data on centralised thermal energy consumption for the ‘Energy Combustion Emissions’ sub-module is entered manually.

<a id="factors"></a>
### 3.	Emission factors

***Rooms sub-module***

For electricity, the emission factor 0.097 kg CO₂-eq/kWh (BAFU, 2025) is used in this module.

***Energy Combustion Emissions sub-module***

For centralised thermal energy consumption, the emission factors are taken from the Corporate Footprint Calculator, and in particular from the BAFU database (2025). 

For energy combustion emissions from non-centralised systems, the emission factors from Labos1point5 (2021, 2022) are used (see Section 7, Appendix).  

<a id="methodology"></a>
### 4.	Methodology

***Rooms sub-module***

The carbon footprint of each room $CF_{rooms}$ is calculated as the product of the room’s floor location in m² and the consumption of heating, cooling, ventilation and lighting in kWh per m² by room type and by building as well as the emission factor for Swiss electricity as follows: 

$$
CF_{rooms} = Surface \cdot \left(
Cons_{heating, building, room_{type}} +
Cons_{cooling, building, room_{type}} +
Cons_{ventilation, building, room_{type}} +
Cons_{lighting, building, room_{type}}
\right) \cdot EF_{electricity}
$$

Where:

- $buildings$: the building in which the unit’s rooms are located
- $room_{type}$: type from the categories *office, miscellaneous, laboratories, archives, libraries and auditoriums*  
- $Surface$: floor occupation in m²  
- $Cons_{heating, building, room_{type}}$
- $Cons_{cooling, building, room_{type}}$
- $Cons_{ventilation, building, room_{type}}$
- $Cons_{lighting, building, room_{type}}$: electricity consumption for heating, cooling, ventilation and lighting of the room in kWh/m² extrapolated from VPO data, depending on the buildings and room type
- $EF_{electricity}$: emission factor for electricity consumption (0.097 kg CO₂-eq/kWh (BAFU, 2025))
  
***Energy Combustion Emissions sub-module***

$CF_{combustion}$ carbon footprint is calculated as the product of the amount of fuel consumed in kg or kWh and the corresponding emission factor, as follows:

$$
CF_{combustion} = Q_{fuel_{type}} \cdot EF_{fuel_{type}}
$$

Where: 

- $fuel_{type}$: type of fuel used: natural gas, domestic fuel oil, biomethane, wood pellets, wood chips and logs
- $Q_{{fuel}_{type}}$: amount of fuel used for a non-centralised heating source in kg or kWh, entered manually.
- $EF_{{fuel}_{type}}$: emission factor for each fuel in kg CO₂-eq/kWh or kg CO₂-eq/kg.


### 5. Limitations
- The floor location in m² provided by the internal database on rooms may not reflect reality in cases where rooms are shared or loaned.
- Electricity consumption for heating, cooling, ventilation and lighting of the rooms is extrapolated from a single consumption value per building provided by the VPO to derive a specific value per use (heating, cooling, ventilation and lighting) and per type of room (office, miscellaneous, laboratories, archives, libraries or auditorium) based on the SIA standard.
- The emission factor of 0.097 kg CO₂-eq/kWh represents a Swiss annual average, not the electricity mix at the time the equipment is in use.
- Fuel consumption for estimating energy combustion emissions from a non-centralised heating system must be entered manually. The quality of the results therefore depends on the quality of this input data.

  
### 6. References
- Internal database on floor locations
- Labos1point5 : [Emission factors – June 2021 version](https://apps.labos1point5.org/static/carbon/FacteursEmission_GES1point5_Juin2021.pdf) et [Emission factors goods and services – January 2022 version](https://apps.labos1point5.org/static/carbon/FacteursEmission_BiensEtServices_janvier2022_FR.pdf). For goods and services, you may also consult a more detailed discussion in [De Paepe 2023](https://doi.org/10.1101/2023.04.04.535626).
- Corporate Footprint Calculator v 1.0, [https://www.itinero.admin.ch/fr/feuilles-de-route-zero-net#Corporate-Footprint-Calculator](https://www.itinero.admin.ch/fr/feuilles-de-route-zero-net#Corporate-Footprint-Calculator)
- BAFU 2025, [https://nexus.openlca.org/database/BAFU](https://nexus.openlca.org/database/BAFU)
- SIA Standards: [https://www.sia.ch/en/cms/services/standards-regulations](https://www.sia.ch/en/cms/services/standards-regulations)


### 7. Appendix
 | Energy combustion emission category | Unit   | Name | Year | Emission factor | Unit of the emission factor |
|-----------------------------------------------|----------------------|-----------------------------------------------------------|-------|---------------------|------------------------------|
| Natural gas                                    | kWh (net calorific value) | Natural gas, average mix                                | 2022  | 0.24                | kg CO₂-eq / kWh PCI          |
| Heating oil  | kWh PCI | Heating oil                                       | 2014  | 0.3243              | kg CO₂-eq / kWh PCI          |
| Biomethan    | kWh PCI | Biomethane – Injected into the networks – Average mix        | 2020  | 0.0444              | kg CO₂-eq / kWh PCI          |
| Wood pellets | kg      | Wood pellets – 8% of humidity        | 2014  | 0.1108              | kg CO₂-eq / kg               |
| Forest chips | kg      | Forest chips – 25% of humidity  | 2022  | 0.0503              | kg CO₂-eq / kg               |
| Wood logs  | kg      | Wood logs – 20% of humidity   | 2014  | 0.1138              | kg CO₂-eq / kg               |

    Table 2 : Energy combustion emissions from non-centralised systems (Labos 1point5, 2021, 2022)

