## 4.5 Clouds externes et IA

### 1.	Contexte 
L’usage des clouds externes et de l’intelligence artificielle (IA) au sein de la communauté scientifique est en nette augmentation depuis quelques années. Dans ce module, les clouds externes pris en considération sont ceux des services de stockage et/ou de calculs externes, tels que AWS – Amazon, GCP – Google, etc.). Les données de Ll’utilisation de l’IA externe (agents tels que ChatGPT – OpenAI, Claude – Anthropic, etc.) sont saisies manuellement. 

L’utilisation des plateformes informatiques interne de l’EPFL est considérée dans le module Infrastructures de recherches. Il est important de noter que ces plateformes comportent un impact environnemental plus faible que les clouds externes au vu du mix de consommation énergétique Suisse et une maîtrise durable des infrastructures de calcul (durée de vie plus grande des clusters de calcul par exemple).

### 2.	Données collectées
Les données d’utilisation de Clouds externes et d’IA sont saisies manuellement.

***Sous-module Clouds externes***
Le nom du fournisseur cloud, le type de service utilisé (stockage ou calcul) et le montant facturé doivent être saisis. 

***Sous-module IA***
La quantification carbone de l’utilisation de l’IA dans le calculateur est centrée sur l’utilisation volontaire d'outils d'IA spécifiques. Le nom du fournisseur IA, le type de service utilisé (génération de texte, d’image ou de code), le nombre d’EPT l’utilisant et la fréquence d’utilisation (équivalent à un temps plein) doivent être saisis. Il est important de relever que l’IA se retrouve actuellement dans l’ensemble des principaux logiciels et services numériques. La recherche web standard intègre également l’IA automatisée comme par exemple, Google avec son IA Gemini dans chaque recherche sur internet. Il est donc impossible de quantifier l’ensemble des utilisations liée à l’IA. 


### 3.	Facteurs d’émissions
***Sous-module Clouds externes***
Les ratios monétaires sont issus d’une étude d’impact des datacenters de l’EPFL réalisée en 2023.

Dans cette première version, les usages ne sont pas différenciés (compute et storage) et tous les fournisseurs de clouds ont le même facteur d’émissions. Ce dernier est de 0.259 kg CO2-eq/EUR.

***Sous-module IA***
L’évaluation des impacts des différents types d’usage est en constante évolution, c’est pourquoi cette version de l’outil propose comme type d’usage : la génération de texte, de code et d’image. 

- Génération de texte : le facteur générique a été déterminé en utilisant les facteurs proposés par EcoLogits Calculator  pour l’écriture d’un résumé d’un article (250 tokens en output). Selon l’étude de Luccioni 2024, on retrouve la même plage d’impacts pour une itération de génération de texte : entre 3 et 10 mg CO2-eq.
- Génération de code : La génération de code est généralement plus intensive en tokens que la génération de texte simple. Selon les catégories définies par Ecologits, les ordres de grandeur se situent entre :
  - Une interaction courte avec un chatbot (environ 400 tokens), et
  - La génération du code d’une application complète (jusqu’à 15 000 tokens).

Des ordres de grandeur comparables sont observés pour les IA commerciales :

  - Copilot : environ 1 000 à 3 000 tokens par requête
  - ChatGPT : environ 200 à 2 000 tokens par requête
  - Euria : de quelques dizaines à une centaine de tokens par requête 

Dans l’outil calculateur CO₂, l’hypothèse retenue pour l’aide à la génération de code est une consommation d’environ 5 000 tokens par demande. Cette valeur correspond à plusieurs allers‑retours avec une IA pour résoudre un problème de code spécifique. Cette hypothèse se traduit par un facteur multiplicatif de 20 par rapport à la génération de texte, pour laquelle une valeur de 250 tokens est utilisée.

- Génération d’image : l’estimation des émissions liées à la génération d’images s’appuie sur l’étude de Luccioni (2024). Cette étude montre que, en moyenne, la génération d’images est environ 40 fois plus émettrice que la génération de texte, avec des valeurs de référence d’environ 5 mg CO₂-eq pour une génération de texte et 200 mg CO₂-eq pour une génération d’image. En tenant compte des différents modèles évalués dans l’étude ainsi que de la variabilité observée entre le premier et le troisième quartile, la génération d’images est estimée comme générant des émissions comprises entre 0.15 g CO₂-eq et 5 g CO₂-eq par image.

### 4.	Méthodologie
### 5. Limites
### 6. Références
### 7. Annexe
