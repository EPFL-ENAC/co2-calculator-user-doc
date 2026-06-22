### 1.	Context
Thousands of scientific, IT and other equipment items are listed in the EPFL equipment inventory. The electricity consumption data associated with their use, allows to estimate the greenhouse gas emissions related to their electricity consumption (Scope 2). 


### 2.	Data collected 

The equipment inventory available on the internal staff management portal provides a list of scientific equipment (>CHF 10,000), IT equipment and other items by unit. 

The following columns are entered manually: 

- Active and standby power consumption: It is recommended to use a conservative estimate (which is not underestimated). If the average active or standby power consumption of your equipment differs from the default value, please contact the dedicated team at the following address: [co2calculator@epfl.ch](mailto:co2calculator@epfl.ch).
- Subclass: The subclass for equipment is entered manually where this information is required.
- Class: You can update the class if the one in your inventory is not appropriate. Please note that this will not update the inventory. 

<a id="factors"></a>
### 3.	Emission factors
Only the emission factor of 0.097 kg CO₂-eq/kWh (BAFU, 2025) is used in this module.

<a id="methodology"></a>
### 4.	Methodology
The carbon footprint related to the use of equipment $CF_{equipment}$ is calculated as the product of the average active and standby power of the equipment, the hours of use for each annual usage mode, and the emission factor for Swiss electricity, as follows:

$$
CF_{equipment} = \frac{P_{equipment,active} \cdot H_{active} + P_{equipment,standby} \cdot H_{standby}}{1000}
\cdot Weeksperyear
\cdot EF_{electricity}
$$

Where: 

- $equipment$: equipment used in the unit.
- $active,stanby$: equipment usage mode.
- $P_{equipment,active}$ and $P_{equipment,standby}$: average active and standby power ratings for the equipment, expressed in W and determined by the EPFL sustainability team through direct measurement or a literature review (see Section 7, Appendix).
- $H_{equipment,active}$ and $H_{equipment,standby}$: usage time in active and standby modes for the equipment in h/week, determined by the user.
- $EF_{electricity}$: emission factor 0.097 kg CO2-eq/kWh (BAFU, 2025). 


### 5. Limitations
- As the default usage time is based on generic estimates, these data must be updated to be more realistic and therefore more accurate.
- The power ratings of each piece of equipment have been determined by EPFL Sustainability through direct measurement or sourced from the literature. These data are not necessarily representative of the equipment in use; in such cases, it is recommended to contact the dedicated team at the following address: [co2calculator@epfl.ch](mailto:co2calculator@epfl.ch) to carry out the update.
- The emission factor of 0.097 kg CO₂-eq/kWh represents an annual average, not the electricity mix at the time the equipment is in use.


### 6. References
- Corporate Footprint Calculator v 1.0, [https://www.itinero.admin.ch/fr/feuilles-de-route-zero-net#Corporate-Footprint-Calculator](https://www.itinero.admin.ch/fr/feuilles-de-route-zero-net#Corporate-Footprint-Calculator)
- BAFU 2025, [https://nexus.openlca.org/database/BAFU](https://nexus.openlca.org/database/BAFU)
