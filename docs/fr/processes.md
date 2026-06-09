## 4.2 Émissions de procédés

### 1.	Contexte 
Certaines activités de laboratoire émettent directement des gaz, comme par exemple du CO₂ utilisé dans certains laboratoires SV ou le SF₆ comme fluide frigorigène. Ce sont les émissions de procédés. Ce module vise à capturer ces émissions directes (Scope 1).

### 2.	Données collectées 
Les quantités de gaz émises par les émissions de procédés sont saisies manuellement.

### 3.	Facteurs d’émission
Pour le CO₂, CH₄, N₂O, les valeurs IPCC AR5 sont utilisées (GHG Protocol, 2024). Pour les fluides frigorigènes, les facteurs d’émissions transmis par le Labos 1point5 (2021, 2022) sont utilisés (voir tableaux des facteurs d’émissions dans la section 7 Annexe). Ces facteurs sont aussi basés sur IPCC AR5. 

### 4.	Méthodologie
L’empreinte carbone de chaque émission de procédés $$CF_{\{process_emission}}$$ est calculée comme le produit de la consommation d’émission de procédé en kg et le facteur d’émission correspondant.

$$
CF_{\{process\_emission}} = Q_{\{process\_type}} \cdot EF_{\{process\_type}}
$$

Où :
- $\{process\_type}$ : voir le Tableau 1 dans la section 7 (Annexe)  
- $Q_{\{process\_type}}$ : quantité d’émission de procédé (kg), saisie manuellement  
- $EF_{\{process\_type}}$ : facteur d’émission (kg CO₂-eq / kg)

Le total des émissions de l'ensemble de chaque élément s'affiche en t CO2-eq une fois le module validé.

### 5.	Limites 
Le module Émissions de procédés doit être rempli manuellement. La qualité des résultats dépend donc directement de la qualité des données entrées. Ces chiffres peuvent être estimés ou mesurés selon les données à disposition.

### 6.	Références
- Greenhouse Gas Protocol (2024) : [IPCC Global Warming Potential Values](https://ghgprotocol.org/sites/default/files/2024-08/Global-Warming-Potential-Values%20%28August%202024%29.pdf)
- Labos 1point5 :  [Facteurs d'emission - version de juin 2021](http://apps.labos1point5.org/static/carbon/FacteursEmission_GES1point5_Juin2021.pdf) et  [Facteurs d'emission biens et services - version de janvier 2022](https://apps.labos1point5.org/static/carbon/FacteursEmission_BiensEtServices_janvier2022_FR.pdf).
- Pour les biens et services vous pouvez également consulter une discussion plus détaillée dans [De Paepe 2023](https://www.biorxiv.org/content/10.1101/2023.04.04.535626v3).

### 7.	Annexe

