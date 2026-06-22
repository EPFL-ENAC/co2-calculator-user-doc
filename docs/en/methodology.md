The development of such a tool to assess emissions related to research activities requires a particularly rigorous and pragmatic methodology. Depending on data availability, certain assumptions had to be made regarding the calculation of the footprint; these are detailed below to ensure full transparency. For each sub-module and module, the methodology and references used are detailed in the “Module Specifications” section.

### 1. Emissions calculation framework


The CO₂ calculator follows the **[Greenhouse Gas Protocol (GHG Protocol)](https://ghgprotocol.org/blog/you-too-can-master-value-chain-emissions)**, the international reference standard for calculating and accounting for greenhouse gas (GHG) emissions.

Developed in 1998 by the World Resources Institute (WRI) and the World Business Council for Sustainable Development (WBCSD), the GHG Protocol is the most widely recognized and used standard worldwide for accounting and reporting greenhouse gas emissions. It provides organisations with a clear framework to calculate emissions related to their activities and value chain in order to identify reduction levers.

This tool strives to follow the GHG Protocol as rigorously as possible, notably through the integration of the three emission scopes described below.

#### The three emission scopes

The GHG Protocol distinguishes three main categories of emissions, called scopes. 

<img width="383" height="256" alt="image" src="https://github.com/user-attachments/assets/cac70157-c3c7-4f32-85d1-f931fa65a082" />
      
        Figure 2 :  The Greenhouse Gas Protocol Corporate Standard (2019, p. 26).

##### Scope 1 — Direct emissions
These are GHG emissions from sources directly controlled by the organisation, for example:

- Combustion of fossil fuels in buildings or facilities
- Emissions from industrial processes, such as CO₂, CH₄, and N₂O

##### Scope 2 — Indirect emissions from energy 
This scope covers emissions associated with the production of electricity, heat, or steam purchased and consumed by the organisation. 

##### Scope 3 – Autres émissions indirectes
Scope 3 includes all other indirect emissions resulting from the organisation’s activities, such as:

- Purchases of goods and services
- Professional travel
- Commuting
- Waste management

Other categories included in the GHG Protocol, such as investments, are not considered in this version of the tool.

### 2. Scope of application

#### CO₂ Calculator space 

The scope of this calculator applies to emissions related to the operational activities of a research unit such as: 

- **Process emissions (Scope 1)**
- **Buildings** – *Combustion energy **(Scope 1)**
- **Buildings** – *Rooms* **(Scope 1 and/ or 2)**
- **Equipment (Scope 2)**
- **External Cloud and AI (Scope 3)**
- **Professional Travel (Scope 3)**
- **Purchases (Scope 3)**
- **EPFL Research facilities (Scope 3)**
- **Additional categories** - *Commuting, Food, Waste, Construction and renovations* **(Scope 3)**

Some emissions related to rooms in the **Buildings** module may also fall under Scope 1, depending on the building’s heating source.

This organisational scope corresponds to the facilities and activities over which research units have direct or indirect control, and for which they have concrete levers for reducing emissions. Indirect emissions related to capital investments are not included in the carbon footprint calculation.

For each sub-module and module, the estimation of the carbon footprint (CF) of a given category $$CF_{\text{category}}$$ follows the calculation below:

$$
CF_{\text{category}} = Q_{\text{category}} \cdot EF_{\text{category}}
$$

- $Q_{\text{category}}$: corresponds to the quantity of a given activity within the category

- $EF_{\text{category}}$: represents the emission factor of the category


For example, for the **Equipment** module, an incubator that is used for a total of 440 kWh over one year emits:
440 × 0.097 = 42.7 kg CO₂-eq, since the emission factor of one kWh of the Swiss consumption mix is 0.097 kg CO₂-eq (BAFU, 2025).

Depending on data availability, it is sometimes necessary to perform calculations to obtain the quantity of the emitting activity. For example, in the case of the incubator above, the kWh quantity was estimated based on the average active and standby power, as well as the weekly usage hours for a given year. More details on assumptions and calculation methods are available in the “Module Specifications” section.

#### CO₂ Simulator space 

The CO₂ Simulator space includes two functionalities.

The *Explore* functionality allows estimating the footprint of one or more modules corresponding to those in the CO₂ Calculator space:

- **Process emissions**: same interface as in the CO₂ Calculator with manual input.
- **Equipment**: same interface as in the CO₂ Calculator, but no data is pre-filled automatically. Equipment is selected via a drop-down menu, with the option to upload a CSV file.
- **External clouds & AI**: same interface as in the CO₂ Calculator with manual entry.
- **Professional travel**: manual entry of professional travel by plane and train.
- **Purchases**: entry of the purchasing budget and distribution across main categories.

The *Plan* functionality allows estimating the footprint of an ongoing or future research project. The carbon footprint of a **research project** is calculated based on the data entered for one reference year from the CO₂ calculator, as well as for the relevant unit. Information is then completed for each module below, either manually or based on the reference year’s data:

- **Headcount**: manual input of full-time equivalents (FTE), selection of job categories
- **Process emissions:** data retrieved from the selected reference year, with input of the percentage related to the research project for each line, and possibility to add a process via a dropdown menu
- **Buildings**: data retrieved from the selected reference year, with input of the percentage attributed to the project
- **Equipment**: display of the equipment list (values set to 0 except standby), input of usage percentage for the project, with possibility to add equipment via a dropdown menu
- **External clouds & AI**: retrieval of cloud and AI services from the selected reference year, same methodology as the existing module, selection of services used and associated usage percentage
- **Professional travel**: manual input of air and train travel
- **Purchases**: input of purchase budget, distribution across main categories, application of corresponding emission factors (input in CHF)
- **EPFL research facilities**: retrieval of platforms used in the selected reference year, selection of platforms for the project, input of available budget, and possibility to add infrastructure via a dropdown menu

Access to these two functionalities in the *CO₂ Simulator* space is individual, and entries are not reported back to the unit manager. Simulations can, however, be saved and shared via CSV or PDF export if the sharing option is selected.

### 3. Unit of measurement: kg CO₂-eq and t CO₂-eq 
Several gases contribute to the greenhouse effect, such as methane (CH₄), nitrous oxide (N₂O), and carbon dioxide (CO₂), among others. These gases have different global warming potentials. Carbon dioxide, being the most widely known gas, is used as the reference gas. Therefore, in greenhouse gas accounting, emissions are expressed either in kilograms (kg CO₂-eq) or metric tonnes (t CO₂-eq) of CO₂ equivalent.

### 4. Results 
After validating all modules, the user can see the results of the unit carbon footprint calculation. This “Results” page presents various visualizations and information related to the unit’s carbon footprint. 

At the top of the page, a summary section displays three key indicators:

- Total emissions expressed in CO₂ equivalents;
- Emissions per ful-time equivalent (FTE);
- Year-on-year comparison where data is available.

Several summary graphs:

- A bar chart showing category’s totals. The results are displayed both by category and by scope; Insert image of results graph 
- A stacked bar chart showing emissions per FTE; Insert image of emissions per FTE graph
- An interactive graph allowing users to view, on the one hand, the institution’s ideal emissions reduction trajectory to meet its climate targets and, on the other hand, the trajectory corresponding to the unit. Sliders allow users to interact with the graph to simulate the implementation of actions likely to reduce emissions. Insert image of emissions reduction trajectory graph 

The page then provides a breakdown by category, following the structure of the CO₂ Calculator modules. For each category, additional visualizations allow a detailed examination of the nature of the contributions to emissions.

A specific IT-focus is also provided. As this category appears across several modules, a summary is presented here to enable users to visualize the unit’s overall impact.

Finally, the page may include graphs for additional categories, based on generic data rather than unit-specific data. An emission breakdown is presented here to raise awareness of the nature of these emissions at the institutional level and to provide additional orders of magnitude. These additional categories can be displayed or hidden using the tick box provided for this purpose.

### 5. Updates of results and emission factors

Emissions factors are reviewed annually. When an update is made, it applies only from the following year onwards, without altering data from previous years. 

Exception: in the case of significant errors in emission factors and/or if **EPFL research facilities** have updated their carbon footprint during the year, a correction may be made by EPFL Sustainability. A message will appear on the homepage for affected units to ensure full transparency.

<a id="limitations"></a>
### 6. Limitations 
Like any carbon footprint tool, this tool provides estimates that include a degree of uncertainty. The reliability of results also depends on the reliability of the primary data used in the calculations. Data cleaning may be necessary to refine results (e.g. inventory data). Results should therefore be interpreted as orders of magnitude and handled with caution. This is also the first iteration that will be updated and improved as new data becomes available.

#### Inventory data
For each module, the most relevant data available at the time of calculation has been used. However, it may be the case that this data only partially allows for the calculation of the carbon footprint in the desired category. Where such data is unavailable, approximations have been made using related data or supplementary information.

This is why some modules require manual data entry to improve estimation accuracy. Furthermore, manual entry is available in most modules to complete missing information. Further details specific to each module are available in their dedicated tabs.

#### Emission factors
Depending on the modules and sub-modules within the CO₂ Calculator, the most reliable and available emission factors are used. However, their level of accuracy varies depending on the maturity of the methods and the complexity of the activities: some are close to physical data (such as the national electricity mix), whilst others provide a more approximate estimate (for example, for certain digital services). 

Furthermore, emission factors can be calculated using two complementary approaches:

- The so-called ‘physical’ approach involves converting measurable data (e.g. kWh consumed or kilometers travelled) into CO₂ equivalent emissions.
- Conversely, the ‘monetary’ approach is based on converting expenditure (in euros or another currency) into CO₂ equivalent emissions.

In the latter case, emission factors are adjusted to account for inflation, in order to reflect current economic conditions. In this tool, factors expressed in a reference year are updated using inflation rates provided by the European Central Bank between 2019 and the year considered. This ensures consistency between historical factors and current financial data.

The monetary approach introduces a higher level of uncertainty compared to the physical approach. However, it is often used due to limitations in data availability for physical calculations.

Finally, it should be noted that emission factors always include a degree of uncertainty. Based on modeling, they rely on assumptions and may, in some cases, represent approximations of real-world situations.

#### Confidence level
For the reasons cited above, each module is associated with a degree of confidence. This considers, the quality of the inventory data, its accuracy and coverage, the accuracy of the used emission factors, and the method employed (e.g. physical approach or monetary approach).

#### Results valid only in Switzerland

Please note that the results shown are valid only for a facility located in Switzerland. If used in another country, the results may not be fully accurate, as certain emission factors are specific to the Swiss context. 

This applies, on the one hand, to emission factors related to electricity: in Switzerland, around 60% of electricity is generated from hydropower and around 30% from nuclear power, which are low-carbon sources [2]. Switzerland also imports electricity from Germany, France and Austria, mainly in winter to make up for a shortfall in production. This includes electricity consumption by industry and households, as well as all emissions related to electric transport (trains, trams, metros, electric cars, etc.). Furthermore, the emission factors for local heating networks are also specific to the means of production: each district heating network has a different energy mix and therefore its own emission factor. Organization based outside Switzerland can still use the tool by entering their own emission factors, allowing them to  generate results tailored to the geographical context.

[2] https://www.energie-environnement.ch/eclairage-electricite-du-menage/mix-electrique-et-mix-energetique
