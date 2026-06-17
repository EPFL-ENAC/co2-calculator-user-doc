### 1.	Contexte 
Certaines activités de laboratoire émettent directement des gaz, comme par exemple du CO₂ utilisé dans certains laboratoires SV ou le SF₆ comme fluide frigorigène. Ce sont les émissions de procédés. Ce module vise à capturer ces émissions directes (Scope 1).

### 2.	Données collectées 
Les quantités de gaz émises par les émissions de procédés sont saisies manuellement.

<a id="facteurs"></a>
### 3.	Facteurs d’émission
Pour le CO₂, CH₄, N₂O, les valeurs IPCC AR5 sont utilisées (GHG Protocol, 2024). Pour les fluides frigorigènes, les facteurs d’émissions transmis par le Labos 1point5 (2021, 2022) sont utilisés (voir tableaux des facteurs d’émissions dans la section 7 Annexe). Ces facteurs sont aussi basés sur IPCC AR5. 

<a id="methodologie"></a>
### 4.	Méthodologie
L’empreinte carbone de chaque émission de procédés $CF_{{process~emission}}$ est calculée comme le produit de la consommation d’émission de procédé en kg et le facteur d’émission correspondant.

$$
CF_{process~emission} = Q_{{process_{type}}} \cdot EF_{{process_{type}}}
$$

Où : 

- ${process_{type}}$ : voir le Tableau 1 dans la section 7 (Annexe)
- $Q_{process_{type}}$ : quantité d’émission de procédé (kg), saisie manuellement 
- $EF_{process_{type}}$ : facteur d’émission selon le type d'émission de procédé (kg CO₂-eq / kg)

Le total des émissions de l'ensemble de chaque élément s'affiche en t CO₂-eq une fois le module validé.

### 5.	Limites 
Le module Émissions de procédés doit être rempli manuellement. La qualité des résultats dépend donc directement de la qualité des données entrées. Ces chiffres peuvent être estimés ou mesurés selon les données à disposition.

### 6.	Références
- Greenhouse Gas Protocol (2024) : [IPCC Global Warming Potential Values](https://ghgprotocol.org/sites/default/files/2024-08/Global-Warming-Potential-Values%20%28August%202024%29.pdf)
- Labos 1point5 :  [Facteurs d'emission - version de juin 2021](http://apps.labos1point5.org/static/carbon/FacteursEmission_GES1point5_Juin2021.pdf) et  [Facteurs d'emission biens et services - version de janvier 2022](https://apps.labos1point5.org/static/carbon/FacteursEmission_BiensEtServices_janvier2022_FR.pdf).
- Pour les biens et services vous pouvez également consulter une discussion plus détaillée dans [De Paepe 2023](https://www.biorxiv.org/content/10.1101/2023.04.04.535626v3).

### 7.	Annexe
| Gaz émis               | Sous-catégorie | Unité              | Unité eq CO₂ |
|------------------------|----------------|--------------------|-------------|
| CO₂                    |                | kg CO₂-eq / kg     | 1           |
| CH₄ fossil             |                | kg CO₂-eq / kg     | 30          |
| N₂O                    |                | kg CO₂-eq / kg     | 265         |
|                | NF3                | kg CO₂-eq / kg     | 16100       |
| Fluides frigorigènes   | R116           | kg CO₂-eq / kg     | 11100       |
| Fluides frigorigènes   | R125           | kg CO₂-eq / kg     | 3170        |
| Fluides frigorigènes   | R134a          | kg CO₂-eq / kg     | 1300        |
| Fluides frigorigènes   | R14            | kg CO₂-eq / kg     | 6630        |
| Fluides frigorigènes   | R143a          | kg CO₂-eq / kg     | 4800        |
| Fluides frigorigènes   | R152a          | kg CO₂-eq / kg     | 138         |
| Fluides frigorigènes   | R218           | kg CO₂-eq / kg     | 8900        |
| Fluides frigorigènes   | R227ea         | kg CO₂-eq / kg     | 2640        |
| Fluides frigorigènes   | R23            | kg CO₂-eq / kg     | 12400       |
| Fluides frigorigènes   | R318           | kg CO₂-eq / kg     | 9540        |
| Fluides frigorigènes   | R32            | kg CO₂-eq / kg     | 677         |
| Fluides frigorigènes   | R404a          | kg CO₂-eq / kg     | 3943        |
| Fluides frigorigènes   | R407a          | kg CO₂-eq / kg     | 1923        |
| Fluides frigorigènes   | R407c          | kg CO₂-eq / kg     | 1624        |
| Fluides frigorigènes   | R407f          | kg CO₂-eq / kg     | 1674        |
| Fluides frigorigènes   | R410a          | kg CO₂-eq / kg     | 1924        |
| Fluides frigorigènes   | R417a          | kg CO₂-eq / kg     | 2127        |
| Fluides frigorigènes   | R422a          | kg CO₂-eq / kg     | 2844        |
| Fluides frigorigènes   | R422d          | kg CO₂-eq / kg     | 2473        |
| Fluides frigorigènes   | R427a          | kg CO₂-eq / kg     | 2024        |
| Fluides frigorigènes   | R4310mee       | kg CO₂-eq / kg     | 1650        |
| Fluides frigorigènes   | R507           | kg CO₂-eq / kg     | 3985        |
| Fluides frigorigènes   | R507a          | kg CO₂-eq / kg     | 2235        |
| Fluides frigorigènes   | R5114          | kg CO₂-eq / kg     | 7910        |
| Fluides frigorigènes   | SF6            | kg CO₂-eq / kg     | 23500       |
| Fluides frigorigènes   | R11            | kg CO₂-eq / kg     | 4660        |
| Fluides frigorigènes   | R113           | kg CO₂-eq / kg     | 5820        |
| Fluides frigorigènes   | R114           | kg CO₂-eq / kg     | 8590        |
| Fluides frigorigènes   | R115           | kg CO₂-eq / kg     | 7670        |
| Fluides frigorigènes   | R12            | kg CO₂-eq / kg     | 10200       |
| Fluides frigorigènes   | R122           | kg CO₂-eq / kg     | 59          |
| Fluides frigorigènes   | R122a          | kg CO₂-eq / kg     | 258         |
| Fluides frigorigènes   | R123           | kg CO₂-eq / kg     | 79          |
| Fluides frigorigènes   | R123a          | kg CO₂-eq / kg     | 370         |
| Fluides frigorigènes   | R124           | kg CO₂-eq / kg     | 527         |
| Fluides frigorigènes   | R13            | kg CO₂-eq / kg     | 13900       |
| Fluides frigorigènes   | R132c          | kg CO₂-eq / kg     | 338         |
| Fluides frigorigènes   | R141b          | kg CO₂-eq / kg     | 782         |
| Fluides frigorigènes   | R142b          | kg CO₂-eq / kg     | 1980        |
| Fluides frigorigènes   | R21            | kg CO₂-eq / kg     | 148         |
| Fluides frigorigènes   | R22            | kg CO₂-eq / kg     | 1760        |
| Fluides frigorigènes   | R225ca         | kg CO₂-eq / kg     | 127         |
| Fluides frigorigènes   | R225cb         | kg CO₂-eq / kg     | 525         |
| Fluides frigorigènes   | R290           | kg CO₂-eq / kg     | 3           |
| Fluides frigorigènes   | R401a          | kg CO₂-eq / kg     | 1130        |
| Fluides frigorigènes   | R408a          | kg CO₂-eq / kg     | 3257        |
| Fluides frigorigènes   | R502           | kg CO₂-eq / kg     | 4786        |

    Tableau 1: facteurs d’émissions Biens et services (Labos1point5, 2022).  

