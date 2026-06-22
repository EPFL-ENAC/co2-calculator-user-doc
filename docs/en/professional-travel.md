### 1.	Context
Professional travel at EPFL is mainly undertaken by plane and train. Professional plane trips are booked through EPFL travel agency (LEX 5.6.2), and the data containing the information required to calculate the carbon footprint is therefore collected automatically and used in this module. If planes have been booked outside the central travel agency, they must be entered manually. Train journeys must be entered manually.

### 2.	Data collected 
Data relating to air travel is provided by EPFL central travel agency and contains specific details such as the date, duration, departure and destination, class, distance, plane number, etc. This set of data is supplemented using the Atmosfair API to calculate the carbon footprint per flight in kg CO₂-eq.  
-> More information about the [Atmosfair calculation methodology](https://www.atmosfair.de/en/standards/emissions_calculation/)

For plane or train travel booked outside the central agency, the data must be entered manually: departure and arrival cities, travel dates, as well as the number of passengers and class. 

### 3.	Emission factors 

For flights booked through the central travel agency, the emission factors for plane carbon footprint come from Atmosfair database. These factors consider the specific characteristics of the plane, such as distance, class, as well as aircraft type, number of passengers, altitude, cargo load, etc. All these aspects are considered when determining the quantity of emissions associated with the journey. The radiative forcing index (RFI)[3] used in the carbon footprint is 2.7.

[3] One metric, known as the Radiative Forcing Index (RFI), is based on the radiative forcing of pollutants—that is, the direct change in the atmosphere’s energy balance caused by the introduced pollutant. The RFI expresses, for a specific point in time (e.g., 2015), the ratio of these changes in the energy balance caused by the pollutants present in the atmosphere at that time as a result of global aviation. The ratio is currently about 3 to 1 (factor of 3). This means that the direct warming effect of all aviation pollutants (non-CO₂ and CO₂) is three times greater than that of CO₂ alone (IPCC, 1999) (Atmosfair, 2023)

For plane and train travels entered manually, the emission factors come from the [Transportation Environmental Calculator](https://www.suisseenergie.ch/programmes/calculateur-environnemental-transport/?pk_vid=a0aa611ca3b1a5821782143404a2d0f1), a tool developed by Swissenergy. 

- The flight emission factors in kg CO₂-eq/km depend on the destination (Europe or intercontinental) and the class (economy, professional, etc.)
- For train travels, these factors depend on the country railways (Switzerland, Germany, Austria, Italy, France or the rest of the world. An average of regional and long-distance traffic is considered.

### 4.	Methodology

Plane travel booked via the EPFL central travel agency is automatically entered into the tool, along with an estimate of the associated emissions. 

Travel data must be entered manually for flights booked outside the central travel agency and for all train journeys.

***Plane sub-module (manual entry)***

The carbon footprint of each journey $CF_{plane}$ is calculated as the product of the distance between the departure and arrival cities, the associated emission factor, and the radiative forcing multiplier, as follows:

$$
CF_{plane} = Distance \cdot EF_{classe} \cdot RFI
$$

Where: 

- $Distance$: distance between the point of departure and arrival in km. 
- $classe$: ticket class. 
- $EF_{classe}$: aircraft emission factor according to class in kg CO₂-eq/km. 
- $RFI$: the ‘radiative forcing index’ (RFI), which represents the radiative forcing multiplier. 

Here, an RFI of 2.7 is used. 

***Train sub-module (manual entry)***

The carbon footprint of each journey $CF_{train}$  is calculated as the product of the distance between the departure and arrival cities and the associated emission factor, as follows: 

$$
CF_{train} = Distance \cdot EF_{train}
$$

Where: 

- $Distance$: distance between the departure and arrival points in km
- $EF_{train}$: emission factor for the train journey in kg CO₂-eq/km

The calculator then adds up the total impact of all professional travels: flights booked via the central travel agency and flights and train journeys entered manually. 


### 5. Limitations
- This module has a high degree of reliability, as data on air travel is collected by the travel agency, providing robust, accurate and almost complete source data (it is estimated that 90% of staff air travel is covered). Furthermore, the emission factors used for these journeys are sourced from the Atmosfair database, which adjusts them according to very specific flight parameters, such as distance, class, as well as the aircraft’s load factor, cargo load, aircraft model, etc.
- For remaining journeys entered manually, the quality of the final results therefore depends on the quality of the data entered. 


### 6. References
- Atmosfair methodology 2023 [https://www.atmosfair.de/wp-content/uploads/flight-emissionscalculator-documentation-calculationmethodology.pdf](https://www.atmosfair.de/wp-content/uploads/flight-emissionscalculator-documentation-calculationmethodology.pdf) et [https://www.atmosfair.de/wp-content/uploads/vdr-reporting-standard-en-19022024-1.pdf](https://www.atmosfair.de/wp-content/uploads/vdr-reporting-standard-en-19022024-1.pdf)
- Transportation Environmental Calculator, [https://www.suisseenergie.ch/programmes/calculateur-environnemental-transport/?pk_vid=0b785dce39481c571776159259abdffd](https://www.suisseenergie.ch/programmes/calculateur-environnemental-transport/?pk_vid=0b785dce39481c571776159259abdffd)

