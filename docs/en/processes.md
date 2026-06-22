### 1.	Context
Certain laboratory activities directly emit gases, such as CO₂ used in some SV laboratories or SF₆ as a refrigerant. These are process emissions. This module aims to capture these direct emissions (Scope 1).

### 2.	Data collected  
The quantities of gas emitted from process emissions must be entered manually.

<a id="factors"></a>
### 3.	Emission factors
For CO₂, CH4, N2O, the IPCC AR5 values are used (GHG Protocol, 2024). For refrigerants, the emission factors provided by Labos 1point5 (2021, 2022) are used (see tables of emission factors in Section 7, Appendix). These factors are also based on IPCC AR5.

<a id="methodology"></a>
### 4.	Methodology
The carbon footprint of each process emission $CF_{{process~emission}}$ is calculated as the product of the process emission consumption in kg and the corresponding emission factor.

$$
CF_{process~emission} = Q_{{process_{type}}} \cdot EF_{{process_{type}}}
$$

Where: 

- ${process_{type}}$ : see Table 1 in Section 7, Appendix.
- $Q_{process_{type}}$ : quantity of process emissions in kg entered manually.
- $EF_{process_{type}}$ : emission factor in kg CO₂-eq/kg. 

The total emissions for each element are displayed in tons of CO₂-eq once the module has been validated. 

### 5.	Limitations 
The **Process Emissions** module must be completed manually. The quality of the results therefore depends directly on the quality of the data entered. These figures may be estimated or measured depending on the data available.

### 6.	References 
- Greenhouse Gas Protocol (2024) : [IPCC Global Warming Potential Values](https://ghgprotocol.org/sites/default/files/2024-08/Global-Warming-Potential-Values%20%28August%202024%29.pdf)
- Labos 1point5 :  [Emission factors – June 2021 version](http://apps.labos1point5.org/static/carbon/FacteursEmission_GES1point5_Juin2021.pdf) et  [Emission factors for goods and services – January 2022 version](https://apps.labos1point5.org/static/carbon/FacteursEmission_BiensEtServices_janvier2022_FR.pdf).
- For goods and services, you may also consult a more detailed discussion in [De Paepe 2023](https://doi.org/10.1101/2023.04.04.535626).

### 7. Appendix
| Gases emitted       | Sub-category | Unit              | CO₂-eq unit |
|------------------------|----------------|--------------------|-------------|
| CO₂                    |                | kg CO₂-eq / kg     | 1           |
| CH₄ fossil             |                | kg CO₂-eq / kg     | 30          |
| N₂O                    |                | kg CO₂-eq / kg     | 265         |
|                | NF3                | kg CO₂-eq / kg     | 16100       |
| Refrigerants| R116           | kg CO₂-eq / kg     | 11100       |
| Refrigerants   | R125           | kg CO₂-eq / kg     | 3170        |
| Refrigerants   | R134a          | kg CO₂-eq / kg     | 1300        |
| Refrigerants   | R14            | kg CO₂-eq / kg     | 6630        |
| Refrigerants   | R143a          | kg CO₂-eq / kg     | 4800        |
| Refrigerants   | R152a          | kg CO₂-eq / kg     | 138         |
| Refrigerants   | R218           | kg CO₂-eq / kg     | 8900        |
| Refrigerants   | R227ea         | kg CO₂-eq / kg     | 2640        |
| Refrigerants   | R23            | kg CO₂-eq / kg     | 12400       |
| Refrigerants   | R318           | kg CO₂-eq / kg     | 9540        |
| Refrigerants   | R32            | kg CO₂-eq / kg     | 677         |
| Refrigerants   | R404a          | kg CO₂-eq / kg     | 3943        |
| Refrigerants   | R407a          | kg CO₂-eq / kg     | 1923        |
| Refrigerants   | R407c          | kg CO₂-eq / kg     | 1624        |
| Refrigerants   | R407f          | kg CO₂-eq / kg     | 1674        |
| Refrigerants   | R410a          | kg CO₂-eq / kg     | 1924        |
| Refrigerants   | R417a          | kg CO₂-eq / kg     | 2127        |
| Refrigerants   | R422a          | kg CO₂-eq / kg     | 2844        |
| Refrigerants   | R422d          | kg CO₂-eq / kg     | 2473        |
| Refrigerants   | R427a          | kg CO₂-eq / kg     | 2024        |
| Refrigerants   | R4310mee       | kg CO₂-eq / kg     | 1650        |
| Refrigerants   | R507           | kg CO₂-eq / kg     | 3985        |
| Refrigerants   | R507a          | kg CO₂-eq / kg     | 2235        |
| Refrigerants   | R5114          | kg CO₂-eq / kg     | 7910        |
| Refrigerants   | SF6            | kg CO₂-eq / kg     | 23500       |
| Refrigerants   | R11            | kg CO₂-eq / kg     | 4660        |
| Refrigerants   | R113           | kg CO₂-eq / kg     | 5820        |
| Refrigerants   | R114           | kg CO₂-eq / kg     | 8590        |
| Refrigerants   | R115           | kg CO₂-eq / kg     | 7670        |
| Refrigerants   | R12            | kg CO₂-eq / kg     | 10200       |
| Refrigerants   | R122           | kg CO₂-eq / kg     | 59          |
| Refrigerants   | R122a          | kg CO₂-eq / kg     | 258         |
| Refrigerants   | R123           | kg CO₂-eq / kg     | 79          |
| Refrigerants   | R123a          | kg CO₂-eq / kg     | 370         |
| Refrigerants   | R124           | kg CO₂-eq / kg     | 527         |
| Refrigerants   | R13            | kg CO₂-eq / kg     | 13900       |
| Refrigerants   | R132c          | kg CO₂-eq / kg     | 338         |
| Refrigerants   | R141b          | kg CO₂-eq / kg     | 782         |
| Refrigerants   | R142b          | kg CO₂-eq / kg     | 1980        |
| Refrigerants   | R21            | kg CO₂-eq / kg     | 148         |
| Refrigerants   | R22            | kg CO₂-eq / kg     | 1760        |
| Refrigerants   | R225ca         | kg CO₂-eq / kg     | 127         |
| Refrigerants   | R225cb         | kg CO₂-eq / kg     | 525         |
| Refrigerants   | R290           | kg CO₂-eq / kg     | 3           |
| Refrigerants   | R401a          | kg CO₂-eq / kg     | 1130        |
| Refrigerants   | R408a          | kg CO₂-eq / kg     | 3257        |
| Refrigerants   | R502           | kg CO₂-eq / kg     | 4786        |

    Table 1: Emission factors for goods and services (Labos1point5, 2022).



