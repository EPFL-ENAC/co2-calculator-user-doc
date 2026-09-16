### 1. Contexte du projet
Faisant partie de l’administration fédérale décentralisée, l’EPFL doit atteindre des objectifs de réduction des émissions de gaz à effet de serre ambitieux. En tant qu’institution académique, la part la plus importante de son empreinte environnementale vient de ses activités de recherche. Les laboratoires consomment en effet environ dix fois plus d'énergie que les bureaux classiques en raison par exemple de leurs besoins spécifiques en matière de ventilation, de l'utilisation d'équipements très gourmands ou encore pour la gestion des données dans les centres de calcul haute performance [1]. Au-delà de la consommation d’énergie, les achats ou les voyages pour ne citer qu’eux représentent une part importante des émissions de CO₂ et un défi important en termes de réduction.

[1] Freese, T., Elzinga, N., Heinemann, M., Lerch, M. M., & Feringa, B. L. (2024). The relevance of sustainable laboratory practices. RSC Sustainability, 2(5), 1300-1336.

### 2. D’un prototype à un déploiement à large échelle  
Afin de mieux comprendre en donnant des ordres de grandeur et de mieux quantifier l’empreinte carbone des laboratoires, un prototype du calculateur CO₂ a été développé en 2019 au sein de la Faculté des Sciences de la vie (SV) de l’EPFL. 

Sa conception repose sur une approche collaborative avec des laboratoires et plateformes de la faculté, le bureau Durabilité SV, des services centraux de la faculté et de l’EPFL, de l’association étudiante Zero Emission Group et d’externes en particulier le cabinet de conseil Quantis. Ce prototype a ensuite été testé dans une trentaine de laboratoires de l’EPFL, ouvrant la voie au développement d’un outil déployé à l’échelle de l’ensemble des facultés. 

Plus d’informations : **[Calculateur CO₂ SV](https://www.epfl.ch/schools/sv/fr/science-de-la-vie/a-propos/bureau-de-durabilite/calculateur-CO₂/)**

L’évolution du projet s’inscrit dans un dialogue continu avec des initiatives externes, notamment **[Labos1point5](https://labos1point5.org/)**, ainsi que plusieurs réseaux et conférences internationales. Ces échanges ont permis d’aligner l’outil avec les standards scientifiques et internationaux. Par ailleurs, il intègre les recommandations issues de différents consortiums de recherche, dont certaines initiatives du programme SCENE, ainsi que l’évolution des exigences en matière de durabilité dans les demandes de financement.

En 2025, le développement de la version open-source de l’outil calculateur CO₂ a été lancé par la Durabilité EPFL, en collaboration étroite avec le service IT de la faculté de l’environnement naturel, architectural et construit **[(ENAC‑IT)](https://www.epfl.ch/schools/enac/fr/a-propos/enac-it/)** et la Direction des systèmes d’information **[(DSI)](https://www.epfl.ch/about/vice-presidencies/fr/vice-presidence-pour-les-operations-vpo/dsi/)**.

Un travail spécifique a également été mené avec le Swiss Data Science Center **[(SDSC)](https://www.epfl.ch/research/domains/sdsc/)**, afin d’adapter la typologie des achats EPFL à la classification utilisée par le Labo 1point5 qui nous partage sa base de facteurs d’émissions (UNSPSC vers NACRES), facilitant ainsi l’analyse des émissions liées aux achats. 

Enfin, l’outil développé par l’EPFL, est conçu pour s’adapter aux spécificités des autres institutions académiques en particulier suisses.

### 3. L’outil et ses fonctionnalités  

L’outil calculateur CO₂ possède trois espaces de travail : 

#### *3.1 Espace Calculateur CO₂*

Cet espace permet d’évaluer l’empreinte carbone de l’unité chaque année, sur la base de l’année civile antérieure (du 1er janvier au 31 décembre) et des modules suivants :

- **Personnel** : ce module permet d’estimer l’empreinte carbone relative aux catégories additionnelles qui s’affiche dans la page résultats (Alimentation, Pendularité, Déchets).

- **Émissions de procédés** : ce module permet d’estimer les émissions de gaz à effet de serre liées aux procédures expérimentales et aux fuites d’équipements. 

- **Bâtiments** : ce module permet d’estimer l'empreinte carbone liée aux émissions de combustion d'énergie (au cas où l’unité utilise une source d'énergie non-centralisée) ainsi que celles liées au bâtiment (chauffage, climatisation, ventilation et éclairage).

- **Équipements** : ce module permet d’estimer l'empreinte carbone liée à la consommation électrique des équipements (scientifiques, IT, etc.) en usage actif et standby.

- **Clouds externes et IA** : ce module permet d’estimer l'empreinte carbone liée à l'utilisation de services de clouds externes et d'intelligence artificielle (IA).

- **Voyages professionnels** : ce module permet d’estimer et à visualiser l'empreinte carbone des voyages professionnels en avion et en train.

- **Achats** : ce module permet d’estimer l'empreinte carbone liée aux achats de l’unité, article par article, à partir des données d'approvisionnement enregistrées dans le système de facturation.

- **Infrastructures de recherche EPFL** : ce module permet d’estimer l'empreinte carbone liée à l'utilisation des infrastructures de recherche internes EPFL par votre unité.

Les utilisatrices et utilisateurs principaux ont accès et peuvent voir tous les modules ci-dessus, alors que les utilisatrices et utilisateurs standards ne peuvent remplir que les modules Clouds externes et IA ainsi que Voyages professionnels. Ces personnes peuvent cependant visualiser les résultats agrégés des autres modules dans la page Résultats, une fois que ceux-ci ont été validés. 

Cet espace permet en outre de suivre l’évolution des émissions de l’unité dans le temps. 

#### *3.2 Espace planificateur de projet CO₂*

L’espace planificateur de projet CO₂ permet d'estimer l'empreinte carbone de différents projets, que ce soient pour des demandes de financement ou des projets passés, en cours ou futurs, en s’appuyant sur les données remontant du calculateur CO₂. 

***Demande de financement***

L’estimation de l’empreinte carbone d’un projet spécifique à une demande de financement peut être effectuée par des utilisateurs et utilisatrices standard ou principaux. 

En plus de saisir le budget total et le budget par module, les utilisatrices et utilisateurs doivent ajouter manuellement les données relatives à la demande de financement pour certains modules.

Pour les utilisatrices et utilisateurs principaux, les données de certains modules remontent automatiquement depuis le calculateur CO₂ (Émissions de procédés, Bâtiments, Équipements, Clouds externes et IA), d’autres sont à saisir (Personnel, Voyages professionnels, Achats, Infrastructures de recherche EPFL). Afin de simplifier la saisie, le module Équipements permet d’appliquer un pourcentage global d’utilisation plutôt que de renseigner chaque équipement individuellement. De même, le module Achats offre deux méthodes d’estimation : sur la base d’un budget global ou d’un budget par catégorie d’achat.

Pour les utilisatrices et utilisateurs standards, les données doivent être ajoutées manuellement pour chaque module.  Ces choix différents de remontées des données ont notamment été réalisés afin de garantir la protection des données personnelles. 

L’estimation peut également être rendue visible à l’ensemble des membres de l’unité, indépendamment de leur rôle (utilisatrice et utilisateur principal et standard). 

L’année de référence détermine les facteurs d’émission utilisés par le planificateur de projet CO₂ pour calculer les émissions attribuables au projet.

***Détail par année***

Pour les utilisatrices et utilisateurs principaux, l’estimation de l’empreinte carbone d’un projet, qu’il soit passé, en cours ou futur, est réalisée grâce à la remontée automatique des données depuis le calculateur CO₂.

Afin d’obtenir une estimation de l’empreinte carbone du projet par année, les utilisatrices et utilisateurs principaux peuvent indiquer la part que représente le projet par rapport aux activités totales de l’unité pour l’année de référence. Pour ce faire, il suffit d’utiliser le curseur présent dans le tableau de chaque module et de renseigner, dans la colonne « % de l’année de référence », le poids relatif du projet.

Pour les utilisatrices et utilisateurs standards, il est également possible d’estimer l’empreinte carbone d’un projet, qu’il soit passé, en cours ou futur. Toutefois, contrairement aux utilisatrices et utilisateurs principaux, cette estimation ne bénéficie pas de la remontée automatique des données depuis le calculateur CO₂, afin de garantir la protection des données personnelles. Les données doivent être ajoutées manuellement pour chaque module. 

Pour cette même raison, le détail annuel d’un projet n’est pas accessible à l’ensemble des membres de l’unité, puisqu’il repose sur des données issues du calculateur CO₂. L’accès à cette section est réservé aux personnes accréditées en tant qu’utilisatrices ou utilisateurs principaux.

Comme alternative, il est possible de télécharger le rapport PDF du projet et de le partager avec les membres de l’unité.

#### *3.3 Explorateur CO₂*

L’explorateur CO₂ permet d’estimer l'empreinte carbone d’éléments ou d’actions spécifiques. Il facilite l’évaluation de différents scénarios et offre la possibilité de télécharger les résultats dans un rapport PDF.

L’exploration est possible pour tous les modules présents dans le calculateur CO₂ et est accessible pour tous types d’utilisateurs (utilisatrices et utilisateurs principaux et standards). 


### 4. Objectifs de l’outil
L’outil calculateur CO₂ open-source remplit les objectifs suivants :

- Proposer une approche cohérente pour identifier et visualiser les principales sources d’émissions liées aux activités des laboratoires et leurs impacts.
- Identifier les profils d’émissions carbone propres à chaque type de laboratoire.
- Estimer l’empreinte carbone d’un projet de recherche (demande de financement ou détail par année de projet) ou d’élément ou d’actions (nouvel achat, futurs voyages professionnels, consommation électrique d’un équipement, etc.). 
- Fournir un outil d'aide à la décision pour prendre des mesures ciblées visant à réduire l'empreinte carbone.
- Satisfaire les futures exigences européennes et nationales concernant l’évaluation de l’impact environnemental des projets de recherche.
- Anticiper les évolutions légales contraignantes en dotant l’EPFL d’outil permettant de comprendre, cibler et diminuer ses émissions carbones.

### 5. Stratégie Climat & Durabilité EPFL 2030 et initiative Green Labs
Le calculateur CO₂ s’inscrit pleinement dans la stratégie environnementale de l’École :

- La **[Stratégie Climat & Durabilité EPFL 2030](https://www.epfl.ch/about/sustainability/fr/strategie/)** ;
- L’initiative **[Green Labs](https://www.epfl.ch/about/sustainability/fr/recherche-et-innovation/green-labs/)** ;
- Les futures exigences internationales et nationales concernant l’évaluation de l’impact environnemental des projets de recherche.

La **[Stratégie Climat & Durabilité EPFL 2030](https://www.epfl.ch/about/sustainability/fr/strategie/)** fixe des objectifs ambitieux en intégrant la durabilité dans les missions fondamentales de l’École : l’enseignement, la recherche et l’innovation. Elle prévoit également des mesures visant à réduire les impacts environnementaux liés au fonctionnement de l’institution. 

Ces objectifs incluent notamment :

- Une réduction globale de 40 % des émissions de gaz à effet de serre d’ici 2030 par rapport à 2019 ;
- Une réduction de 50 % des émissions liées à l’énergie par rapport à 2006 ;
- Une réduction de 30 % des émissions liées aux voyages aériens par rapport à 2019 (objectifs définis au niveau fédéral). 

Depuis l’entrée en vigueur, le 1er janvier 2025, de la loi sur le climat et l’innovation et de l’ordonnance sur la protection du climat, l’EPFL vise également l’atteinte du net zéro pour les scopes 1 et 2 (énergie), et, dans la mesure du possible, pour le scope 3 (émissions indirectes) à l’horizon 2040.

Dans ce contexte, le calculateur CO₂ permet d’estimer l’empreinte carbone au niveau des unités de recherche. Les données peuvent ensuite être agrégées à différents niveaux (instituts, facultés,). 

L’initiative **[Green Labs](https://www.epfl.ch/about/sustainability/fr/recherche-et-innovation/green-labs/)**, inscrite dans cette stratégie a pour objectif de promouvoir des pratiques de recherche responsables sur les plans environnemental et social, sans compromettre la qualité scientifique et en respectant les limites planétaires. Elle vise à quantifier, analyser et optimiser les processus opérationnels des activités de recherche 


 <img width="1152" height="507" alt="image" src="https://github.com/user-attachments/assets/664aaca1-8502-42b9-96f6-faf1415ffe2d" />

      Figure 1 : Approche Green Labs EPFL

Le calculateur CO₂ permet d’anticiper les obligations futures en matière de suivi et de compte rendu des émissions carbones liées aux activités de recherche.

En complément, l’espace planificateur de projet CO₂ permet d’estimer l’empreinte carbone d’un projet lié à une demande de financement, passé, en cours ou futur et l’espace explorateur CO₂ permet d’estimer l’empreinte carbone d’une action spécifique, par exemple un voyage professionnel, l’utilisation d’un équipement scientifique, etc.
