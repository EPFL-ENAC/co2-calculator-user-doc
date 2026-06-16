## 4.6 Voyages professionnels  

### 1.	Contexte
Les déplacements professionnels à l’EPFL sont effectués principalement en avion et en train. Les déplacements professionnels en avion sont réservés via l’agence de voyages de l’EPFL (LEX 5.6.2) et les données contenant les informations nécessaires au calcul de l’empreinte carbone sont donc récoltées automatiquement et utilisées dans ce module. Si des déplacements en avion ont été réservés hors agence de voyage central, ils peuvent être saisis manuellement. Les voyages en train doivent systématiquement être saisis manuellement. 

### 2.	Données collectées
Les données relatives aux voyages en avion sont communiquées par l’agence de voyages central de EPFL, et contiennent des informations précises relatives aux déplacements comme la date, la durée, le départ et la destination, la classe, la distance, le numéro de vol, etc. Ces données sont analysées et complétées à l’aide de l’API Atmosfair pour le calcul de l’empreinte carbone par vol en kg CO₂-eq. 

-> Plus d'information concernant la [méthodologie de calcul Atmosfair](https://www.atmosfair.de/en/standards/emissions_calculation/)

Pour les déplacements en train ou en avion réservés hors agence central, les données doivent être saisies manuellement : ville de départ et d’arrivée, le mode de transport (avion ou train) ainsi que le nombre de voyageurs et la classe. 

### 3.	Facteurs d’émissions

Pour les vols réservés via l’agence de voyage, les facteurs d’émissions de l’impact des vols proviennent d’[Atmosfair](https://www.atmosfair.de/en/standards/emissions_calculation/).  Ces facteurs prennent en compte les caractéristiques spécifiques du vol, telles que la distance, la classe mais aussi le type d'avion, le nombre de passagers, l'altitude, le charge de fret, etc. Tous ces aspects sont pris en compte pour définir la quantité d’émissions relatives au déplacement. Le RFI utilisé dans l’empreinte carbone est de 2.7.

Pour les vols et trains saisis manuellement, les facteurs d’émissions en kg CO₂-eq/km parcourus proviennent du [calculateur environnemental transport](https://www.suisseenergie.ch/programmes/calculateur-environnemental-transport/?pk_vid=0b785dce39481c571776159259abdffd), développé par SuisseÉnergie. 

Les facteurs en kg CO₂-eq / km pour les avions dépendent notamment de la géographie du vol (Europe ou intercontinental) et de la classe (économique, business, etc.).

Pour les trains, ces facteurs dépendent de la géographie (Suisse, Allemagne, Autriche, Italie, France ou reste du monde). Une moyenne du trafic régional et longue distance est prise en compte.


### 4.	Méthodologie

Les déplacements en avion réservés via l’agence de voyage central EPFL sont remontés automatiquement dans l’outil, avec l’estimation des émissions associées. 

En ce qui concerne les déplacements en avion réservés hors de l’agence de voyage central et les déplacements en train, les données sont saisies manuellement. 

***Sous-module Avions (saisie manuelle)***

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

***Sous-module Trains (saisie manuelle)***

L’empreinte carbone de chaque voyage $CF_{train}$ est calculée comme le produit de la distance entre ville de départ et l’arrivé et le facteur d’émission associé tel que : 

$$
CF_{train} = Distance \cdot EF_{train}
$$

Où : 
- $Distance$ : distance entre le point de départ et arrivé en km
- $EF_{train}$  : facteur d’émission du voyage en train en kg CO₂-eq/km


Le calculateur additionne alors l’impact total des déplacements professionnels :  déplacements en avion effectués via l’agence de voyage central et déplacements en avion et en train saisis manuellement. 



### 5. Limites
- Ce module présente un degré de confiance élevé, car les données relatives aux déplacements en avion sont collectées par l’agence de voyages, permettant d’avoir des données sources robustes, précises et presque complètes (on estime que 90 % des voyages en avion du personnel sont couverts). De plus, les facteurs d’émission utilisés pour ces déplacements proviennent de la base de données Atmosfair, qui les adapte en fonction de paramètres très précis du vol, tels que la distance, la classe, mais aussi le taux de remplissage de l’avion, la charge de fret, le modèle d’avion, etc.
- Pour tous les autres déplacements, les données étant saisies manuellement, a qualité des résultats finaux dépend donc de la qualité des données entrées. 


### 6. Références
- Méthodologie Atmosfair [https://www.atmosfair.de/wp-content/uploads/flight-emissionscalculator-documentation-calculationmethodology.pdf](https://www.atmosfair.de/wp-content/uploads/flight-emissionscalculator-documentation-calculationmethodology.pdf) et [https://www.atmosfair.de/wp-content/uploads/vdr-reporting-standard-en-19022024-1.pdf](https://www.atmosfair.de/wp-content/uploads/vdr-reporting-standard-en-19022024-1.pdf)
- Mobitool v3.1, [https://www.suisseenergie.ch/programmes/calculateur-environnemental-transport/?pk_vid=0b785dce39481c571776159259abdffd](https://www.suisseenergie.ch/programmes/calculateur-environnemental-transport/?pk_vid=0b785dce39481c571776159259abdffd)

