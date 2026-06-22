### 1.	Context
Purchases account for a significant proportion of the research activities carbon footprint, particularly in laboratory environments where consumables, chemicals and equipment are used intensively. Beyond their direct use, purchased goods incorporate upstream emissions related to the extraction of raw materials, manufacturing, packaging and transport.

The **Purchases** module is designed to capture these indirect emissions (Scope 3). It comprises *8 sub-modules*:

- *Scientific Equipment*
- *IT Equipment*
- *Consumables and Accessories*
- *Biological, Chemical and Gaseous Products*
- *Services*
- *Vehicles*
- *Other purchases*
- *Centralised purchases*

### 2.	Data collected
The module includes all goods and services purchased from external suppliers during the reference year.

For each purchase, the following information is automatically populated from paid invoices related to each unit’s financial center:

- Item description
- Supplier
- UNSPSC code
- Quantity
- Total amount paid

The *Centralised Purchases sub-module* is designed to incorporate predefined items corresponding to centralised and/or shared purchases between several units. Where applicable, the annual consumption for these items must be entered.


<a id="facteurs"></a>
### 3.	Emission factors

***Standard Purchases sub-modules***

They include the following sub-modules: *Scientific Equipments, IT Equipments, Consumables and Accessories, Biological, Chemical and Gaseous Products, Services, Vehicles, and Other Purchases*. 

Each purchased item is assigned with a specific emission factor (kg CO₂-eq / EUR), derived from the database shared by Labos 1point5 (2021, 2022, De Paepe 2024). This factor is refined to best match the product type or category, notably using an AI tool developed by the SDSC. This item-level approach allows for a more accurate estimate than the use of generic factors. However, for purchases added manually, a matching method is used. Each item categorised via a UNSPSC code is associated with a NACRES code (the purchases nomenclature used in France), to which an emission factor (Labos 1point5) corresponds. This factor is then applied to the item.

***Centralised Purchases sub-module***

Each item is associated with a specific emission factor from the [Ecoinvent](https://ecoinvent.org/) (2026) database.


<a id="methodology"></a>
### 4.	Methodology

***Standard Purchases sub-modules***

The carbon footprint of each purchase $CF_{purchase}$ is calculated as the product of the total financial value of the item and the associated emission factor, as follows:

$$
CF_{purchase} =Amount_{item,euro,2019} \cdot EF_{item}
$$

Where: 

$$
Amount_{item,euro,2019} =Amount_{item,currency,year} \cdot Ex_{currency,year} \cdot Inflation_{year,2019}
$$

- $item$: item purchased per unit
- $currency$: currency used for the purchase of the item 
- $year$: the reference year
- $Amount_{item,euro,2019}$: total cost of purchasing an item in euros in 2019, considering inflation between 2019 and the corresponding year 
- $Amount_{item,currency,year}$: total cost of purchasing an item in the applicable currency
- $Ex_{currency,year}$: exchange rate between the currency used and the euro 
- $Inflation_{year,2019}$: inflation rate between 2019 and the reference year
- $EF_{item}$: estimated emission factor for the item, with the amount converted to 2019 euros in kg CO₂-eq/EUR_2019

The amount is converted into euros using the average exchange rate for the reference year.

Monetary emission factors are adjusted using an inflation coefficient to reflect current economic conditions. The factors (expressed in a the base year) are multiplied by the inflation rate between 2019 and the base year as provided by the European Central Bank (ECB). This ensures greater consistency between historical factors and current monetary values.

***Centralised Purchases sub-module***

For a given year, all purchases must be entered manually for a given year. 

The carbon footprint of each purchase $CF_{centralised~purchases}$ is calculated as the product of the quantity of the item purchased in the applicable unit, the conversion factor used to convert the quantity into kg, and the associated emission factor, as follows:

$$
CF_{centralised~purchases} = Q_{item} \cdot Coef_{kg ~ item} \cdot EF_{item}
$$

Where: 

- $item$: item purchased centrally (e.g. liquid nitrogen)
- $Q_item$ : quantity of the item purchased in the unit of measurement, entered manually 
- $Coef_{kg ~ item}$: conversion factor to convert the quantity into kg
- $EF_{item}$: emission factor for the item in kg CO₂-eq/kg

The emission factors used are taken from the ecoinvent database (restricted licence, not for public distribution).

### 5. Limitations
- Depreciation of equipment: In accordance with the GHG Protocol guidelines, the CO₂ calculator adopts a flow-based approach. Thus, although some equipment is used over several years, we account for all emissions associated with its manufacture in the year of purchase. This approach avoids the uncertainties associated with a stock-based approach, which would require a detailed inventory and reliable lifetimes. No depreciation period is therefore applied, which helps to reduce arbitrary assumptions. Conversely, this method can lead to significant variations in emissions from one year to the next, which must be analysed from a multi-year perspective.
- Internal purchases (e.g. via chemical stores) and purchases made by credit card are not automatically included, unless otherwise specified. As these data are entered manually via the ‘add’ function available in each sub-category, the quality of the results depends on the quality of the information entered.
- The accuracy of the results depends on the quality and completeness of the purchasing data (item descriptions, categorisation) extracted from the School’s database, as well as on the emission factors used. The methodology provides an order of magnitude for emissions based on the available financial data.
- The use of monetary emission factors introduces significant uncertainty and does not allow for the distinction between purchasing choices with different environmental impacts within the same category. 


### 6. References
- Labos 1point5 :  [Facteurs d'emission - version de juin 2021](https://apps.labos1point5.org/static/carbon/FacteursEmission_GES1point5_Juin2021.pdf) et  [Facteurs d'emission biens et services - version de janvier 2022](https://apps.labos1point5.org/static/carbon/FacteursEmission_BiensEtServices_janvier2022_FR.pdf). Pour les biens et services vous pouvez également consulter une discussion plus détaillée dans [De Paepe 2023](https://www.biorxiv.org/content/10.1101/2023.04.04.535626v3).
- UNSPSC: United Nations Standard Products and Services Code (UNSPSC) [https://www.undp.org/unspsc](https://www.undp.org/unspsc)
- Ecoinvent: Ecoinvent Association (2026). ecoinvent data v3.12. [https://www.ecoinvent.org](https://www.ecoinvent.org)
