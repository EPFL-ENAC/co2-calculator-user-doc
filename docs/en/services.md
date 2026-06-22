### 1.	Context 
To carry out their research activities, many laboratories—as well as external academic institutions, companies and start-ups—use the research facilities provided by EPFL. This includes, for example, cleanrooms, high-performance computing centres, IT services and animal facilities, to name but a few. This sharing of resources is an excellent way to reduce the carbon footprint.

The use of EPFL research facilities might be part of a unit’s operational activities and must therefore be included in its carbon footprint. This footprint is broken down into emissions related to **Process Emissions, Buildings, Equipment and Purchases** for these research facilities. These emissions correspond to the main areas where units can act, particularly through their choices regarding usage, equipment and research practices.


### 2.	Data collected 
The data collected relates to the categories of emissions arising from the activities of the research facilities mentioned above, calculated directly in the calculator with a few exceptions.  

- **Process emissions**:  
  The data collected is listed in the tab for the Process Emissions module (see Section 4.2.2). 

- **Buildings**:  
  The data collected is listed in the tab for the Buildings module (see Section 4.3.2).
  Exception: for animal facilities, the data collected comes from life cycle assessments (see further details here [https://www.epfl.ch/schools/sv/school-of-life-sciences/about-us/sv-sustainability-office/green-lab-project/](https://www.epfl.ch/schools/sv/school-of-life-sciences/about-us/sv-sustainability-office/green-lab-project/)

- **Equipment**:  
  The data collected is listed in the tab for the Equipment module (see Section 4.4.2).
  Exception: for animal facilities, the data collected comes from life cycle assessments (see further details here [https://www.epfl.ch/schools/sv/school-of-life-sciences/about-us/sv-sustainability-office/green-lab-project/](https://www.epfl.ch/schools/sv/school-of-life-sciences/about-us/sv-sustainability-office/green-lab-project/)
  
- **Purchases**:  
  The data collected is listed in the Purchasing module tab (see Section 4.7.2).


### Allocation key 
Part of the carbon footprint of research facilities is allocated to the user units. This approach considers the fact that EPFL’s research facilities are essential to the units’ research activities and must therefore be included in their carbon footprint. 

An allocation key is applied for the use of research facilities. This is based on:

- Total invoicing (internal and external clients)
- Usage hours of EPFL research facilities
- The number of animal housings used by the unit

As the rate is differentiated for external units, a calculation is carried out subsequently to allocate the footprint at a standardised price level between internal and external user units. 

The data required for these calculations is derived from billing data or provided directly by the research facilities.


### 3.	Emission factors 

This module is unique in that the emission factors depend on several factors: 
1. Emissions from the categories **Process Emissions, Buildings, Equipment and Purchases** of the research facility
2. The allocation key of the facility for the user unit. 

- ***[See Process emissions Emission factors](./processes.md#factors)***
- ***[See Buildings Emission factors](./building.md#factors)***
- ***[See Equipment Emission factors](./equipment.md#factors)***
- ***[See Purchases Emission factors](./purchases.md#factors)***


### 4.	Methodology

The carbon footprint associated with the use of a research facility is calculated based on the carbon footprint of the following modules: ***Process emissions, Buildings, Equipment and Purchases***. 

The usage rate of a user unit in relation to an EPFL research facility $UsageRate_{RF,unit}$ corresponds to the proportion of its total usage relative to all user units (internal and external) of the research facility in question. This annual usage rate is expressed based on available data (invoices, hours of use or number of hostings), according to the following formula:

$$
UsageRate_{RF,unit} = \frac{Usage_{RF,unit}}{\sum_{unit}^{}Usage_{RF,unit}}
$$

Where:

- $RF$: the research infrastructure in question
- $unit$: the user unit
- $Usage_{RF,unit}$: use of EPFL research facilities by unit and by reference year (invoicing, hours of use or number of hostings)

The proportion of the carbon footprint attributable to a user unit $CF_{RF~attribution,unit}$ is then determined by multiplying this footprint by the unit’s specific usage rate, according to the following formula:

$$
CF_{RF~attribution,unit} = CF_{RF~attribution,total} \cdot UsageRate_{RF,unit}
$$

Where:

- $CF_{RF~attribution,total}$: the carbon footprint of the research infrastructure to be allocated to the user units
- $UsageRate_{RF,unit}$: the user unit’s specific usage rate  

The calculation method for animal facilities follows the same logic. Emissions are allocated to each user unit based on its level of use, measured by the number of animal housings. This allows the total carbon footprint of the facility to be distributed proportionally among all user units.

To grasp the methodology for each category used in the calculation of the research infrastructure carbon footprint, please refer to the links below: 

- ***[Process emissions](./processes.md#methodology)*** 
- ***[Buildings](./building.md#methodology)***
- ***[Equipment](./equipment.md#methodology)*** 
- ***[Purchases](./purchases.md#methodology)*** 


### 5. Limitations

This module has a high level of uncertainty as it is based on the carbon footprints of the **Process Emissions, Buildings, Equipment and Purchasing** modules, which themselves have their own limitations.  
- ***[See Limitations from Process emissions module](./processes.md#5-limites)***
- ***[See Limitations from Buildings module](./building.md#5-limites)***
- ***[See Limitations from Equipment module](./equipment.md#5-limites)*** 
- ***[See Limitations from Purchases module](./purchases.md#5-limites)*** 

Furthermore, the CO₂ Calculator section relies on partially automated modules, which by default use the data reported by each module. Thus, if the research facilities considered modules have not been validated, errors may remain, which can affect the allocation of their carbon footprint to the user units.

Furthermore, certains limitations are associated with the allocation key, based primarily on financial data, except for certain platforms where the number of used hours or the number of housings are considered. 

- Billing data is a primary indicator of research infrastructure usage. However, there are numerous limitations, particularly due to the differentiated pricing between internal and external units and even between internal units belonging to different faculties or departments.
- Usage hours are more relevant indicators with less uncertainty and are prioritised if the research infrastructure holds this data for all user units. 


### 6. References
- The methodology for this module was developed partly by drawing on the methodology developed by Labos1point5 within GES1point5 [https://apps.labos1point5.org/documentation/carbon/ges-calculating-methods](https://apps.labos1point5.org/documentation/carbon/ges-calculating-methods) and refined for the EPFL context by the EPFL Research Facility Working Group. 
