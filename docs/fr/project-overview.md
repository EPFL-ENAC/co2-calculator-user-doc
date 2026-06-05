# 2.	Aperçu du projet  
## 2.1 Contexte du projet
Faisant partie de l’administration fédérale décentralisée, l’EPFL doit atteindre des objectifs de réduction des émissions de gaz à effet de serre ambitieux. En tant qu’institution académique, la part la plus importante de son empreinte environnementale vient de ses activités de recherche. Les laboratoires consomment en effet environ dix fois plus d'énergie que les bureaux classiques en raison par exemple de leurs besoins spécifiques en matière de ventilation, de l'utilisation d'équipements très gourmands ou encore pour la gestion des données dans les centres de calcul haute performance [1]. Au-delà de la consommation d’énergie, les achats ou les voyages pour ne citer qu’eux représentent une part importante des émissions de CO₂ et un défi important en termes de réduction.

[1] Freese, T., Elzinga, N., Heinemann, M., Lerch, M. M., & Feringa, B. L. (2024). The relevance of sustainable laboratory practices. RSC Sustainability, 2(5), 1300-1336.

## 2.2 D’un prototype à un déploiement à large échelle  
Afin de mieux comprendre en donnant des ordres de grandeur et de mieux quantifier l’empreinte carbone des laboratoires, un prototype du calculateur CO₂ a été développé en 2019 au sein de la Faculté des Sciences de la vie (SV) de l’EPFL. 

Sa conception repose sur une approche collaborative avec des laboratoires et plateformes de la faculté, le bureau Durabilité SV, des services centraux de la faculté et de l’EPFL, de l’association étudiante Zero Emission Group et d’externes en particulier le cabinet de conseil Quantis. Ce prototype a ensuite été testé dans une trentaine de laboratoires de l’EPFL, ouvrant la voie au développement d’un outil déployé à l’échelle de l’ensemble des facultés. 

Plus d’informations : **[Calculateur CO₂ SV](https://www.epfl.ch/schools/sv/fr/science-de-la-vie/a-propos/bureau-de-durabilite/calculateur-co2/)**

L’évolution du projet s’inscrit dans un dialogue continu avec des initiatives externes, notamment **[Labos1point5](https://labos1point5.org/)**, ainsi que plusieurs réseaux et conférences internationales. Ces échanges ont permis d’aligner l’outil avec les standards scientifiques et internationaux. Par ailleurs, il intègre les recommandations issues de différents consortiums de recherche, dont certaines initiatives du programme SCENE, ainsi que l’évolution des exigences en matière de durabilité dans les demandes de financement.

En 2025, le développement de la version open-source de l’outil calculateur CO₂ a été lancé par la Durabilité EPFL, en collaboration étroite avec le service IT de la faculté de l’environnement naturel, architectural et construit **[(ENAC‑IT)](https://www.epfl.ch/schools/enac/fr/a-propos/enac-it/)** et la Direction des systèmes d’information **[(DSI)](https://www.epfl.ch/about/vice-presidencies/fr/vice-presidence-pour-les-operations-vpo/dsi/)**.

Un travail spécifique a également été mené avec le Swiss Data Science Center **[(SDSC)](https://www.epfl.ch/research/domains/sdsc/)**, afin d’adapter la typologie des achats EPFL à la classification utilisée par le Labo 1point5 qui nous partage sa base de facteurs d’émissions (UNSPSC vers NACRES), facilitant ainsi l’analyse des émissions liées aux achats. 

Enfin, l’outil développé par l’EPFL, est conçu pour s’adapter aux spécificités des autres institutions académiques en particulier suisses.

## 2.3 L’outil et ses fonctionnalités  

L’outil calculateur CO₂ possède deux espaces de travail : 

#### *Espace Calculateur CO₂*

Cet espace permet d’évaluer l’empreinte carbone de l’unité chaque année, sur la base de l’année civile antérieure (du 1er janvier au 31 décembre) et des modules suivants :
- **Émissions de procédés**
- **Bâtiments**
- **Équipements**
- **Clouds externes et IA**
- **Voyages professionnels**
- **Achats**
- **Infrastructures de recherche EPFL**
- **Catégories additionnelles** - *Pendularité, Alimentation, Déchets, Constructions et rénovations*

Cet espace permet en outre de suivre l’évolution des émissions de l’unité dans le temps. 

#### *Espace Simulateur CO₂*

L’espace Simulateur CO₂ possède deux fonctionnalités. 
La première fonctionnalité *Explorer* permet d’estimer l’empreinte d’un ou plusieurs modules spécifiques. La simulation est possible pour les modules suivants : 
- **Émissions de procédés**
- **Équipements**
- **Achats**
- **Voyages professionnels**
- **Clouds externes & IA**

La deuxième fonctionnalité *Planifier* permet d’estimer l’empreinte d’un projet de recherche en cours ou à venir. Il est particulièrement pertinent par exemple pour la demande d’une subvention ou d’une demande de fonds. 

Dans la majorité des modules de cet espace, les données remontent automatiquement depuis le calculateur CO₂ ne nécessitant qu’une validation, et seulement dans certains cas une saisie manuelle des informations doit être effectuée. 

## 2.4 Objectifs de l’outil
L’outil calculateur CO₂ open-source remplit les objectifs suivants :

- Proposer une approche cohérente pour identifier et visualiser les principales sources d’émissions liées aux activités des laboratoires et leurs impacts.
- Identifier les profils d’émissions carbone propres à chaque type de laboratoire.
- Estimer l’empreinte carbone d’un module (nouvel achat, futurs voyages professionnels, consommation électrique d’un équipement, etc.) ou d’un projet de recherche en cours ou à venir.
- Fournir un outil d'aide à la décision pour prendre des mesures ciblées visant à réduire l'empreinte carbone.
- Satisfaire les futures exigences européennes et nationales concernant l’évaluation de l’impact environnemental des projets de recherche.
- Anticiper les évolutions légales contraignantes en dotant l’EPFL d’outil permettant de comprendre, cibler et diminuer ses émissions carbones.

## 2.5 Stratégie Climat & Durabilité EPFL 2030 et initiative GreenLabs
Le calculateur CO₂ s’inscrit pleinement dans la stratégie environnementale de l’École :
- La **[Stratégie Climat & Durabilité EPFL 2030](https://www.epfl.ch/about/sustainability/fr/strategie/)** ;
- L’initiative **[GreenLabs](https://www.epfl.ch/about/sustainability/fr/recherche-et-innovation/green-labs/)**
- Les futures exigences internationales et nationales concernant l’évaluation de l’impact environnemental des projets de recherche.

La **[Stratégie Climat & Durabilité EPFL 2030](https://www.epfl.ch/about/sustainability/fr/strategie/)** fixe des objectifs ambitieux en intégrant la durabilité dans les missions fondamentales de l’École : l’enseignement, la recherche et l’innovation. Elle prévoit également des mesures visant à réduire les impacts environnementaux liés au fonctionnement de l’institution. Ces objectifs incluent notamment :
- Une réduction globale de 40 % des émissions de gaz à effet de serre d’ici 2030 par rapport à 2019 ;
- Une réduction de 50 % des émissions liées à l’énergie par rapport à 2006 ;
- Une réduction de 30 % des émissions liées aux voyages aériens par rapport à 2019 (objectifs définis au niveau fédéral). 

Depuis l’entrée en vigueur, le 1er janvier 2025, de la loi sur le climat et l’innovation et de l’ordonnance sur la protection du climat, l’EPFL vise également l’atteinte du net zéro pour les scopes 1 et 2 (énergie), et, dans la mesure du possible, pour le scope 3 (émissions indirectes) à l’horizon 2040.

Dans ce contexte, le calculateur CO₂ permet d’estimer l’empreinte carbone au niveau des unités de recherche. Les données peuvent ensuite être agrégées à différents niveaux (instituts, facultés,). 

L’initiative **[GreenLabs](https://www.epfl.ch/about/sustainability/fr/recherche-et-innovation/green-labs/)**, inscrite dans cette stratégie a pour objectif de promouvoir des pratiques de recherche responsables sur les plans environnemental et social, sans compromettre la qualité scientifique et en respectant les limites planétaires. Elle vise à quantifier, analyser et optimiser les processus opérationnels des activités de recherche 


 <img width="384" height="172" alt="image" src="https://github.com/user-attachments/assets/664aaca1-8502-42b9-96f6-faf1415ffe2d" />

      Figure 1 : Approche GreenLabs EPFL

Le calculateur CO₂ permet d’anticiper les obligations futures en matière de suivi et de compte rendu des émissions carbones liées aux activités de recherche.

En complément, l’espace *Simulation CO₂* permet d’estimer l’empreinte carbone d’un ou plusieurs modules (par exemple : achat d’équipement, voyages professionnels, consommation électrique d’un équipement supplémentaire) ou d’un projet de recherche, et ainsi d’orienter les décisions à l’échelle d’un projet de recherche ou d’un module spécifique.



