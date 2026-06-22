### 1.	Context
The additional categories in this module are: 

- Commuting
- Food
- Waste
- Construction and renovation

These categories are referred to as ‘additional’ because their emissions are calculated using EPFL campus data and rely solely on the number of unit FTE. They therefore do not provide specific information on the unit’s behaviour but are nonetheless useful for gaining a more comprehensive understanding of the order of magnitude of the unit’s carbon footprint. 


### 2.	Data collected 
The data collected and used to calculate emissions for the additional categories relate to the number of staff and students at EPFL (via the ***Headcount*** module) and the floor location of the rooms used (via the ***Buildings*** module), plus other specific data described here:

- ***Commuting***: total number of kilometers per person (staff or students) and by mode of transport (cycle, car, public transport, etc.). These figures are calculated using responses from the Mobility survey sent out every two years to the EPFL community and combined with information on car park usage to estimate kilometers travelled by car.
  
- ***Food***: total quantity (in kg/person) of food purchased by type of person (staff or students), and by type (vegetarian and non-vegetarian). These figures are based on sales data from the various restaurants and food trucks on site, cross-referenced with the quantities of goods ordered.
  
- ***Waste***: total in kg/person of all non-hazardous waste, by type (paper, plastic, etc.) and by final treatment method (incineration, recycling, etc.). These figures are collected by the VPO each year.
  
- ***Construction and renovation***: Only data from the building module and the factors described below are used for the calculation. 


### 3.	Emission factors 

- ***Commuting***: the emission factors used are those from the **[transportation environmental calculator](https://www.suisseenergie.ch/programmes/calculateur-environnemental-transport/?pk_vid=d874ca860cec98e71773910695abdffd)**, tool developped by Swissenergy. For cars, a factor specific to EPFL has been calculated based on the types of car used by the EPFL community. The factors are given in kg CO₂-eq/km by mode of transport (on foot, by bike, by car, by public transport, by motorbike).

- ***Food***: the emission factors used are based on goods orders placed at EPFL and are provided by the external service provider **[Beelong](https://beelong.ch/en/)**, which analyses the orders and quantities. The factors are in kg CO₂-eq/kg of food depending on the type (vegetarian or non-vegetarian). 

  
- ***Waste***: emission factors are given in kg CO₂-eq/kg of waste (specific factors by type: paper, plastic, etc. and by treatment method: recycling, incineration, etc.). The factors are taken from **[Ecoinvent v3.12 (2026)](https://ecoquery.ecoinvent.org/3.12/cutoff)**. 

  
- ***Construction and renovation***: emission factors are given in kg CO₂-eq/m², by type of construction: new builds – thermal envelope, new builds – technical installations, renovations – thermal envelope, renovations – technical installations, demolitions. The factors were developed based on an internal analysis at EPFL.


### 4.	Methodology 

***Commuting***

For each unit, the commuting carbon footprint $CF_{commuting}$ is calculated as the product of the number of people in the unit, the average distance travelled by each mode of transport, and the emission factor associated with that transport mode, as follows:


$$
CF_{commuting} = \sum_{trans~type}^{} N_{students} \cdot Dist_{students, trans~type} \cdot EF_{trans~type} + \sum_{trans~type}^{} N_{staff} \cdot Dist_{staff, trans~type} \cdot EF_{trans~type}
$$


Where:

- $trans~type$: public transport, cycling, car, walking, etc.
- $N_{students}$: total number of students per reference year in FTE
- $N_{staff}$: total number of staff members per reference year in FTE
- $Dist_{students,trans~type}$: distance travelled per student per mode of transport, in km
- $Dist_{staff,trans~type}$: distance travelled per staff member by mode of transport, in km
- $EF_{trans~type}$: emission factor for the mode of transport (kg CO₂-eq/km)


***Alimentation***

The total CO₂ emissions related to food $CF_{food}$ are estimated by aggregating, for each meal category (vegetarian or meat-based), the emissions associated with consumption by the student population and staff. For each unit, emissions are calculated as the product of the number of people in the unit, the average amount of food consumed per category, and the corresponding emission factor. 

$$
CF_{food} =
\sum_{food~type}^{} N_{students} \cdot Q_{students, food~type} \cdot EF_{food~type} + \sum_{food~type}^{} N_{staff} \cdot Q_{staff, food~type} \cdot EF_{food~type}
$$

Where:

- $food_{type}$: type of food (vegetarian, non-vegetarian)
- $N_{students}$: total number of students per reference year (FTE)
- $N_{staff}$: total number of staff members per reference year in FTE
- $Q_{students,food~type}$: quantity of food purchased per student for the food type in kg/FTE
- $Q_{staff,food_type}$: quantity of food purchased per staff for the food type in kg/FTE
- $EF_{food_type}$: emission factor for the food type in kg CO₂-eq/kg


***Waste***

The total CO₂ emissions related to waste - $CF_{waste}$ is obtained by multiplying the number of people in the unit by the kg of waste per person and the emission factors.


$$
CF_{waste} = \sum_{waste~type}^{}\sum_{eol}^{}(N \cdot Q_{waste~type, eol} \cdot EF_{waste~type,eol})
$$

Where:

- $waste~type$: type of waste (paper, plastic, etc.)
- $eol$: final treatment method (incineration, recycling, etc.)
- $N$: total number of staff per reference year in FTE
- $Q_{waste~type,eol}$: amount of waste per FTE in kg/FTE for the type and treatment
- $EF_{waste~type,eol})$: emission factor associated with the waste type and treatment method in kg CO₂-eq/kg


***Construction and renovation***

The total CO₂ emissions related to construction and renovation $CF_{construction}$ are calculated by identifying the buildings in which the unit carries out its activities (laboratories, offices, etc.) using data from the **Buildings** module. For each building concerned, the total floor location of the rooms in question is multiplied by the corresponding emission factors, expressed in kg CO₂-eq/m², and specific to the type of construction activity (new builds – thermal envelope, new builds – technical installations, renovations – thermal envelope, renovations – technical installations, demolitions). Total emissions are obtained by adding together the emissions for all the rooms concerned and all types of activity. The factors are calculated based on the total floor location of the buildings and the type of construction activity and are applied only for the years in which the works take place, in accordance with the recommendations of the GHG Protocol. 


$$
CF_{construction}
= \sum_{building}^{}\sum_{activity~type}^{}(Surface_{building} \cdot EF_{building,activity~type})
$$

Where:

- $building$: EPFL building (AAB, BCH, BS, etc.)
- $activity~type$: type of construction per building (new_env, new_tec, ren_env, ren_tec, dem)
- $surface_{building}$: total surface of the building (m²)
- $EF_{building,activity~type}$: emission factor for the buildingbuilding  and the type of activity activity_type (kg CO₂-eq/m²)

Where detailed data per building is not available, default emission factors may be used. In this case, a ‘default’ entry is defined and applied to all buildings used by the institution. These default factors enable emissions to be estimated at campus level and allocated across units without requiring specific information on each building.

### 5. Limitations

The accuracy of these additional categories is limited by the lack of individual data specific to each unit:

- For confidentiality reasons, it is not possible to know which members of a unit consume meat or vegetarian products, nor which modes of transport they use individually. Emissions are therefore estimated based on campus averages, without reflecting the unit’s actual behaviour. As a guide, meat generates significantly higher emissions than vegetarian alternatives, and the car is the mode of transport with the greatest impact.

- As for waste, hazardous waste has been excluded from this analysis due to a lack of data enabling its consumption to be attributed to specific units. If the unit produces any, its actual emissions are higher than those estimated here.

- Construction and renovation present an additional challenge: beyond the lack of building-specific data, the available emission factors — notably the Swiss KBOB factors — require very precise information on the quantities and types of materials used (in kg or m³), which are not systematically available. Default factors have therefore been developed internally, introducing an additional degree of uncertainty.


### 6. References
- [Transportation environmental calculator (Mobitool v3.1)](https://www.suisseenergie.ch/programmes/calculateur-environnemental-transport/?pk_vid=d874ca860cec98e71773910695abdffd)
- [Beelong](https://beelong.ch/en/) – External service provider for the analysis of food orders and the calculation of associated emission factors.
- [Ecoinvent v3.12 (2026)](https://ecoquery.ecoinvent.org/3.12/cutoff) – Life cycle database used for waste-related emission factors.
- EPFL internal analysis – Emission factors for building construction and renovation (new builds, renovations, demolitions), developed based on campus construction projects.
