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

Dans cette première version, les usages ne sont pas différenciés (compute et storage) et tous les fournisseurs de clouds ont le même facteur d’émissions. Ce dernier est de 0.259 kg CO₂-eq/EUR.

***Sous-module IA***

L’évaluation des impacts des différents types d’usage est en constante évolution, c’est pourquoi cette version de l’outil propose comme type d’usage : la génération de texte, de code et d’image. 


|                              | Génération de texte (ex. résumé d'article ~250 tokens) | Génération de code (ex. aide à l'écriture de code d'une application ~5000 tokens) | Génération d'image |
|------------------------------|---------------------------------------------|-------------------------------------|--------------------|
| Facteur d’émission (kg CO₂-eq) | 7.5 × 10⁻⁶                                  | 1.5 × 10⁻⁴                          | 3.0 × 10⁻⁴         |



- Génération de texte : le facteur générique a été déterminé en utilisant les facteurs proposés par [EcoLogits Calculator](https://ecologits.ai/latest/methodology/) pour l’écriture d’un résumé d’un article (250 tokens en output). Selon l’étude de Luccioni 2024, on retrouve la même plage d’impacts pour une itération de génération de texte : entre 3 et 10 mg CO₂-eq.
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

***Sous-module Clouds externes***

Le calcul de l’empreinte carbone est effectué à partir d’un ratio monétaire et en fonction du nom du fournisseur cloud et du type d’utilisation. L’empreinte carbone liée à l’usage de chaque fournisseur cloud externe $CF_{external~cloud}$ est calculée comme le produit du montant dépensé et du facteur d’émission d’utilisation spécifique tel que :

$$
CF_{external~cloud}= Amount_{provider,type} \cdot EF_{provider,type}
$$

Où : 

- $provider$ : fournisseur de cloud externe (AWS, Alibaba Cloud, Azure, GCP, Huawei, OVH, Wasabi)
- $type$ : type de service utilisé (compute, storage)
- $Amount_{\text{external cloud provider}}$ : montant dépensé auprès d'un fournisseur de cloud externe en franc suisse, euro, ou dollar américain.
- $EF_{\text{external cloud provider}}$ : facteur d’émission en kg CO₂-eq par devise.

***Sous-module IA***

Le calcul de l’empreinte carbone est effectué à partir du nombre d’EPT dans l’unité et de la fréquence d’utilisation. Les facteurs d’émission liés à l’utilisation d’IA sont agrégés par type de service. L’empreinte carbone d’usage de chaque fournisseur IA sur un type d’utilisation $CF_{AI}$ est calculée comme le produit du nombre d’EPT, du nombre d’utilisation par jours, et du facteur d’émission d’utilisation :

$$
CF_{AI} 
=EPT_{AI_{provider,type}} \cdot Frequency_{AI_{provider,type}} \cdot EF_{AI_{provider,type}}
$$

Où : 

- $AI_{provider}$ : fournisseur du service d’IA
- $type$ : type de service utilisé (génération de texte, de code ou d’image(
- $EPT_{AI_{provider,type}}$ : nombre d’EPT pour un type de service fourni par un fournisseur
- $Frequency_{AI_{provider,type}}$ : nombre d’utilisation par EPT par jour pour un type de service fourni par un fournisseur. Il s’agit de la fréquence d’utilisation par EPT par jour renseignée par les utilisateur·rices multipliés par 235 (5 jours x 47 semaines travaillées).
- $EF_{AI_{provider,type}}$ : facteur d’émission d’utilisation d'un type de service fourni par un fournisseur en kg CO₂-eq)



### 5. Limites
- La quantité utilisée par rapport au nombre de TB stockés ou d’heures de calcul CPU/GPU, ou de tokens utilisés (dans le cas de l’IA) n’est pas renseignée. La méthodologie sera affinée dans une deuxième itération.
- La localisation n’est pas demandée car cette information n’est pas toujours aisément disponible. De plus, cela nécessiterait de fournir les facteurs associés aux pays (intensité carbone de l’électricité). La méthodologie sera affinée dans une deuxième itération.
- Le calcul d’impact de l’IA est agrégé par type d’utilisation. Pas de différence entre les différents fournisseurs IA, ni les différents types de modèles.
- Il arrive que certaines avantages ou mises à disposition soient données aux équipes de recherche pour une utilisation de cloud externe : Amazon avec son AWS Cloud Credits for Research program. Ceci pourrait potentiellement fausser les calculs d’empreinte carbone. 

### 6. Références
- Luccioni (2024) : Luccioni et al, Power Hungry Processing: Watts Driving the Cost of AI Deployment?, CVoR Issued. November 6, 2024. [DOI: 10.1145/3630106.3658542](https://dl.acm.org/doi/10.1145/3630106.3658542)
- Ecologits Calculator : [https://huggingface.co/spaces/genai-impact/ecologits-calculator](https://huggingface.co/spaces/genai-impact/ecologits-calculator)
- Environemental mix for external cloud use : Etude 2023 EPFL Data Center impacts
- Génération de texte : [Ecologits](https://huggingface.co/spaces/genai-impact/ecologits-calculator), [Luccioni 2024](https://dl.acm.org/doi/10.1145/3630106.3658542)
- Génération de texte VS assistance écriture de code : [Ecologits, prompt sur différents IA](https://huggingface.co/spaces/genai-impact/ecologits-calculator)
- Génération de texte VS génération d’image : [Luccioni 2024](https://dl.acm.org/doi/10.1145/3630106.3658542)
