### 1.	Context
Certain activities directly emit greenhouse gases (GHGs). Common examples include SF₆ leaks during etching, fluorinated gas leaks from refrigeration systems, and fluorinated ether evaporation during sample handling. Because many of these gases trap significantly more heat and remain in the atmosphere much longer than CO₂, tracking them is crucial. This module is designed to capture these direct process and fugitive emissions (Scope 1).

### 2.	Data collected  
The available GHGs in this module are selected in accordance with the GHG Protocol (GHG Protocol, 2024), specifically targeting potential emission sources found in academic and research settings.

The quantities of gases associated with process and fugitive emissions are entered manually in the CO₂ Calculator, CO₂ Project planner (Grant proposal), and CO₂ Explorer workspaces.

When this module has been completed in the CO₂ Calculator workspace, the data are automatically imported to the CO₂ Project planner workspace (Grant proposal and detailed per year sections) for principal users. They can then define, for each year, a reference percentage in order to estimate the share of process emissions attributable to the project.

<a id="factors"></a>
### 3.	Emission factors
This module uses the 100-year time horizon Global Warming Potential (GWP) relative to CO₂ as its standard emission factor. These values are provided by the GHG Protocol (GHG Protocol, 2024), adapted from the IPCC Fifth Assessment Report, 2014 (AR5).

<a id="methodology"></a>
### 4.	Methodology
The carbon footprint of each process emission $CF_{{process~emission}}$ is calculated as the product of the process emission consumption in kg and the corresponding emission factor.

$$
CF_{process~emission} = Q_{{process_{gas}}} \cdot EF_{{process_{gas}}}
$$

Where: 

- $Q_{gas}$ : quantity of process and fugitive gas in kg entered manually.
- $EF_{gas}$ : emission factor in kg CO₂-eq/kg. 

The total emissions for each element are displayed in tons of CO₂-eq once the module has been validated. 

### 5.	Limitations 
The **Process Emissions** module must be completed manually. The quality of the results therefore depends directly on the quality of the data entered. These figures may be estimated or measured depending on the data available.

### 6.	References 
- Greenhouse Gas Protocol (2024) : [IPCC Global Warming Potential Values](https://ghgprotocol.org/sites/default/files/2024-08/Global-Warming-Potential-Values%20%28August%202024%29.pdf)



