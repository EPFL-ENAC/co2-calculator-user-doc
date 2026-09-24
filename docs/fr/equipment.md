### 1.	Contexte 
Des milliers d’équipements scientifiques, informatiques et autres sont répertoriés à l’EPFL dans l’inventaire des équipements. L’analyse de cette liste, combinée aux données de consommation électrique associées à leur utilisation, permet d’estimer les émissions de gaz à effet de serre liées à leur consommation électrique (Scope 2).

### 2.	Données collectées
#### *2.1 Espace Calculateur CO₂*

L’inventaire des équipements disponible sur le portail de gestion interne du personnel permet de connaitre la liste des équipements scientifiques (>10’000 CHF), des équipements IT et autres par unité.  

Les colonnes suivantes sont saisies manuellement : 

- Usage actif et usage standby : Il est recommandé de faire une estimation conservatrice (qui n'est pas sous-estimée). Si la puissance moyenne active ou standby de votre équipement est différente de celle utilisée par défaut, merci de contacter l’équipe dédiée à l’adresse suivante: [CO₂calculator@epfl.ch](mailto:CO₂calculator@epfl.ch).
- Sous-classe : La saisie de la sous-classe pour les équipements est faite manuellement là où cette information est nécessaire, notamment lorsque la ligne s’affiche en beige. 
- Classe : La mise à jour de la classe est possible si celle de votre inventaire n'est pas appropriée. Attention cela ne mettra pas à jour l’inventaire.

#### *2.2 Espace Planificateur de projet CO₂*

***Demande de financement***

Pour les utilisatrices et utilisateurs principaux, les données du module Équipement remontent automatiquement depuis le calculateur CO₂. Pour chaque équipement, il est possible de définir un pourcentage de référence afin d’estimer la part des émissions des équipements venant de l’inventaire interne attribuable au projet et selon l’année. Un pourcentage global peut également être appliqué à l’ensemble du module afin d’éviter la saisie du pourcentage de référence par ligne d’équipement. 

Pour les utilisatrices et utilisateurs standards, les données du calculateur CO₂ ne remontent pas automatiquement. Les informations relatives aux équipements doivent donc être saisies manuellement.

***Détail par année***

Pour les utilisatrices et utilisateurs principaux, les données du module Équipements remontent automatiquement depuis le calculateur CO₂. Pour chaque équipement, il est possible de définir un pourcentage de référence afin d’estimer la part des émissions des équipements venant de l’inventaire interne attribuable au projet et selon l’année. Un pourcentage global peut également être appliqué à l’ensemble du module afin d’éviter la saisie du pourcentage de référence par ligne d’équipement.

Pour les utilisatrices et utilisateurs standards, les données du calculateur CO₂ ne remontent pas automatiquement. Les informations relatives aux équipements doivent donc être saisies manuellement.

#### *2.3 Espace Explorateur CO₂*

Afin d’explorer l’empreinte carbone du module Équipements, les utilisatrices et utilisateurs peuvent saisir manuellement les données liées à l’utilisation des équipements. 

<a id="facteurs"></a>
### 3.	Facteurs d’émissions
Seul le facteur d’émission 0.097 kg CO₂-eq/kWh (BAFU, 2025) est utilisé dans ce module.

<a id="methodologie"></a>
### 4.	Méthodologie
L’empreinte carbone $CF_{equipment}$ est calculée comme le produit de la puissance moyenne active et standby de l’équipement, les heures d’utilisation de chaque mode d’utilisation annuelle ainsi que le facteur d’émission de l’électricité suisse tel que :

$$
CF_{equipment} = \frac{P_{equipment,active} \cdot H_{active} + P_{equipment,standby} \cdot H_{standby}}{1000}
\cdot Weeksperyear
\cdot EF_{electricity}
$$

Où : 

- $equipment$ : équipement utilisé dans l’unité
- $active,stanby$ : mode d’utilisation d’équipement
- $P_{equipment,active}$ et $P_{equipment,standby}$ : puissances moyennes en mode active et standby pour l’équipement exprimé en W et déterminées par l’équipe durabilité EPFL par mesure directe ou revue de littérature (voir section 7 Annexe)
- $H_{equipment,active}$  et $H_{equipment,standby}$ : temps d’utilisations en mode active et standby pour l’équipement en h/week déterminée par l’utilisateur·rice Weeksperyear : 47 semaines travaillées par an
- $EF_{electricity}$ : facteur d’émission 0.097 kg CO₂-eq/kWh (BAFU, 2025)

Dans l’espace Planificateur de projet CO₂, dans la section demande de financement et détail par année, les utilisatrices et utilisateurs principaux peuvent définir, pour chaque année, soit un pourcentage de référence pour chaque ligne d’équipement, soit un pourcentage global applicable à l’ensemble du module. Ces pourcentages permettent d’estimer la part des émissions des équipements attribuable au projet. 


### 5. Limites
- Le temps d’utilisation utilisé par défaut étant basé sur des estimations génériques, ces données doivent être mises à jour pour être plus réalistes et donc plus précises.
- Les puissances de chaque équipements ont été déterminées par la Durabilité EPFL par prise de mesure directe ou trouvée dans les revues de littérature. Ces données ne sont pas forcément représentatives de l’équipement utilisé, auquel cas il est recommandé de contacter l’équipe dédiée à l’adresse suivante : [CO₂calculator@epfl.ch](mailto:CO₂calculator@epfl.ch) pour effectuer la mise à jour.
- Le facteur d’émission 0.097 kg CO₂-eq/kWh est représentatif d’une moyenne annuelle, et non du mix électrique au moment de l’utilisation de l’équipement.

### 6. Références
- Corporate Footprint Calculator v 1.0, [https://www.itinero.admin.ch/fr/feuilles-de-route-zero-net#Corporate-Footprint-Calculator](https://www.itinero.admin.ch/fr/feuilles-de-route-zero-net#Corporate-Footprint-Calculator)
- BAFU 2025, [https://nexus.openlca.org/database/BAFU](https://nexus.openlca.org/database/BAFU)
