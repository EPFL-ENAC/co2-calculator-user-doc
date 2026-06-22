### 1.	Context
Professional travel at EPFL is mainly undertaken by plane and train. Professional plane trips are booked through EPFL’s travel agency (LEX 5.6.2), and the data containing the information required to calculate the carbon footprint is therefore collected automatically and used in this module. If planes have been booked outside the central travel agency, they must be entered manually. Train journeys must be entered manually.

### 2.	Data collected 
Data relating to air travel is provided by EPFL’s central travel agency and contains specific details such as the date, duration, departure and destination, class, distance, plane number, etc. This set of data is supplemented using the Atmosfair API to calculate the carbon footprint per flight in kg CO₂-eq.  
-> More information about the [Atmosfair calculation methodology](https://www.atmosfair.de/en/standards/emissions_calculation/)

For plane or train travel booked outside the central agency, the data must be entered manually: departure and arrival cities, travel dates, as well as the number of passengers and class. 

### 3.	Emission factors 

--- 

For flights booked via the travel agency, the emission factors for plane carbon footprint come from Atmosfair database. These factors consider the specific characteristics of the plane, such as distance, class, as well as aircraft type, number of passengers, altitude, cargo load, etc. All these aspects are considered when determining the quantity of emissions associated with the journey. The radiative forcing index (RFI) used in the carbon footprint is 2.7.

For plane and train travels entered manually, the emission factors in kg CO₂-eq/km travelled come from Mobitool database. 

- The flight emission factors in kg CO₂-eq/km depend on the destination (Europe or intercontinental) and the class (economy, professional, etc.)
- For train travels, these factors depend on the country railways (Switzerland, Germany, Austria, Italy, France or the rest of the world. An average of regional and long-distance traffic is considered.

### 4.	Methodology

Les déplacements en avion réservés via l’agence de voyage central EPFL sont remontés automatiquement dans l’outil, avec l’estimation des émissions associées. 

En ce qui concerne les déplacements en avion réservés hors de l’agence de voyage central et les déplacements en train, les données sont saisies manuellement. 

***Plane sub-module (manual entry)***

L’empreinte carbone de chaque voyage $CF_{plane}$ est calculée comme le produit de la distance entre ville de départ et l’arrivé, le facteur d’émission associé, et le multiplicateur de forçage radiatif tel que :

$$
CF_{plane} = Distance \cdot EF_{classe} \cdot RFI
$$

Où : 

- $Distance$ : distance entre le point de départ et d’arrivée en km
- $classe$ : classe d'un billet
- $EF_{classe}$  : facteur d’émission de l’avion selon la classe en kg CO₂-eq/km
- $RFI$ : en anglais « radiative forcing index » qui représente le multiplicateur de forçage radiatif . 

Ici, un RFI de 2.7 est considéré. 

***Train sub-module (manual entry)***

L’empreinte carbone de chaque voyage $CF_{train}$ est calculée comme le produit de la distance entre ville de départ et l’arrivé et le facteur d’émission associé tel que : 

$$
CF_{train} = Distance \cdot EF_{train}
$$

Où : 
- $Distance$ : distance entre le point de départ et arrivé en km
- $EF_{train}$  : facteur d’émission du voyage en train en kg CO₂-eq/km


Le calculateur additionne alors l’impact total des déplacements professionnels :  déplacements en avion effectués via l’agence de voyage central et déplacements en avion et en train saisis manuellement. 



### 5. Limitations
- Ce module présente un degré de confiance élevé, car les données relatives aux déplacements en avion sont collectées par l’agence de voyages, permettant d’avoir des données sources robustes, précises et presque complètes (on estime que 90 % des voyages en avion du personnel sont couverts). De plus, les facteurs d’émission utilisés pour ces déplacements proviennent de la base de données Atmosfair, qui les adapte en fonction de paramètres très précis du vol, tels que la distance, la classe, mais aussi le taux de remplissage de l’avion, la charge de fret, le modèle d’avion, etc.
- Pour tous les autres déplacements, les données étant saisies manuellement, a qualité des résultats finaux dépend donc de la qualité des données entrées. 


### 6. References
- Méthodologie Atmosfair [https://www.atmosfair.de/wp-content/uploads/flight-emissionscalculator-documentation-calculationmethodology.pdf](https://www.atmosfair.de/wp-content/uploads/flight-emissionscalculator-documentation-calculationmethodology.pdf) et [https://www.atmosfair.de/wp-content/uploads/vdr-reporting-standard-en-19022024-1.pdf](https://www.atmosfair.de/wp-content/uploads/vdr-reporting-standard-en-19022024-1.pdf)
- Mobitool v3.1, [https://www.suisseenergie.ch/programmes/calculateur-environnemental-transport/?pk_vid=0b785dce39481c571776159259abdffd](https://www.suisseenergie.ch/programmes/calculateur-environnemental-transport/?pk_vid=0b785dce39481c571776159259abdffd)

