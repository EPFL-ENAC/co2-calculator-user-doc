### 1.	Context
The use of external clouds and artificial intelligence (AI) within the scientific community has been rising sharply in recent years. In this module, the external clouds considered are those providing external storage and/or computing services, such as AWS (Amazon), GCP (Google), etc. Data on the use of external AI (agents such as ChatGPT – OpenAI, Claude – Anthropic, etc.) is entered manually. 

The use of EPFL’s internal IT facilities is covered in the EPFL Research Facilities module. It is important to note that these platforms have a lower environmental impact than external clouds, given Switzerland’s energy consumption mix and the sustainable management of computing infrastructure (e.g. longer lifespan of computing clusters).

### 2.	Data collected 
Usage data for external clouds and AI must be entered manually. 


***External clouds sub-module***

The name of the cloud provider, the type of service used (storage or computing) and the amount invoiced must be entered. 

***AI sub-module***

The carbon quantification of AI usage in the calculator focuses on the voluntary use of specific AI tools. The name of the AI provider, the type of service used (text, image or code generation), the number of FTEs using it and the frequency of use (equivalent to a full-time position) must be entered. It is important to note that AI is currently found in all major software and digital services. Standard web searches also incorporate automated AI; for example, Google uses its Gemini AI in every internet search. It is therefore impossible to quantify all AI-related uses.

### 3.	Emission factors 
***External clouds sub-module***

The carbon footprint figures are taken from an EPFL study on the environmental impact of data centers carried out in 2023.

In this first version, usages are not differentiated (compute and storage) and all cloud providers have the same emission factor. This factor is 0.259 kg CO₂-eq/EUR.

***AI sub-module***

The assessment of the impacts of different usage types is constantly evolving, which is why this version of the tool offers the following usage types: text generation, code generation and image generation.


|                              | Text generation (i.e., an article summary (250 output tokens)  | Code generation (i.e., assistance with writing application code – 5,000 output tokens) | Image generation |
|------------------------------|---------------------------------------------|-------------------------------------|--------------------|
| Emission factors (kg CO₂-eq) | 7.5 × 10⁻⁶                                  | 1.5 × 10⁻⁴                          | 3.0 × 10⁻⁴         |


- Text generation: the generic factor was determined using the factors proposed by the [EcoLogits Calculator](https://ecologits.ai/latest/methodology/) for writing an article abstract (250 tokens in output). According to the study by L uccion i 2024, the same range of impacts is found for a single text generation iteration: between 3 and 10 mg CO₂-eq.
- Code generation: Code generation is generally more token-intensive than simple text generation. According to the categories defined by Ecologits, the orders of magnitude range between:
    - A short interaction with a chatbot (around 400 tokens), and
    - The generation of code for a complete application (up to 15,000 tokens).

Comparable orders of magnitude are observed for commercial AI:
  - Copilot: approximately 1,000 to 3,000 tokens per query
  - ChatGPT: approximately 200 to 2,000 tokens per query
  - Euria: from a few dozen to around a hundred tokens per request 

In the CO₂ calculator tool, the assumption used for code generation assistance is a consumption of approximately 5,000 tokens per request. This value corresponds to several rounds of interaction with an AI to resolve a specific coding issue. This assumption results in a multiplier of 20 compared to text generation, for which a value of 250 tokens is used.

- Image generation: the estimate of emissions associated with image generation is based on the study by Luccioni (2024). This study shows that, on average, image generation emits around 40 times more than text generation, with reference values of approximately 5 mg CO₂-eq for text generation and 200 mg CO₂-eq for image generation. Considering the different models evaluated in the study as well as the variability observed between the first and the third quartile, image generation is estimated to generate emissions ranging from 0.15 g CO₂-eq to 5 g CO₂-eq per image.

### 4.	Methodology 

***External clouds sub-module***

The carbon footprint is calculated using a monetary ratio based on the name of the cloud provider and the type of usage. The carbon footprint associated with the use of each external cloud provider $CF_{external~cloud}$ is calculated as the product of the amount spent and the specific usage emission factor, such as:

$$
CF_{external~cloud}= Amount_{provider,type} \cdot EF_{provider,type}
$$

Where: 

- $provider$: external cloud provider (AWS, Alibaba Cloud, Azure, GCP, Huawei, OVH, Wasabi).
- $type$: type of service used (compute, storage).
- $Amount_{\text{external cloud provider}}$: amount spent with an external cloud provider in Swiss francs, euros or US dollars.
- $EF_{\text{external cloud provider}}$: emission factor in kg CO₂-eq per currency.


***AI sub-module***

The carbon footprint is calculated based on the number of FTEs in the unit and the frequency of use. Emissions factors related to AI usage are aggregated by service type. The carbon footprint of usage for each AI provider for a given usage type $CF_{AI}$ is calculated as the product of the number of FTE, the number of uses per day, and the usage emissions factor: 

$$
CF_{AI} 
=FTE_{AI_{provider,type}} \cdot Frequency_{AI_{provider,type}} \cdot EF_{AI_{provider,type}}
$$

Where: 

- $AI_{provider}$: AI service provider. 
- $type$: type of service used (text, code or image generation).
- $FTE_{AI_{provider,type}}$: number of FTEs for a type of service provided by a provider.
- $Frequency_{AI_{provider,type}}$: number of uses per FTE per day for a type of service provided by a provider. This is the frequency of use per FTE per day reported by users multiplied by 235 (5 days × 47 working weeks).
- $EF_{AI_{provider,type}}$: emission factor for the use of a service type provided by a supplier in kg CO₂-eq).


### 5. Limitations
- The amount used relative to the number of TB stored, CPU/GPU computing hours, or tokens used (in the case of AI) is not specified. The methodology will be refined during the second iteration.
- Location is not requested as this information is not always readily available. Furthermore, this would require providing country-specific factors (carbon intensity of electricity). The methodology will be refined in the second iteration.
- The AI impact calculation is aggregated by type of use. No distinction is made between different AI providers or different types of models.
- In some cases, certain benefits or resources are provided to research teams for the use of external cloud services: Amazon, for example, with its AWS Cloud Credits for Research programme. This could potentially skew carbon footprint calculations. 


### 6. References 
- Luccioni (2024) : Luccioni et al, Power Hungry Processing: Watts Driving the Cost of AI Deployment?, CVoR Issued. November 6, 2024. [DOI: 10.1145/3630106.3658542](https://dl.acm.org/doi/10.1145/3630106.3658542)
- Ecologits Calculator : [https://huggingface.co/spaces/genai-impact/ecologits-calculator](https://huggingface.co/spaces/genai-impact/ecologits-calculator)
- Environemental mix for external cloud use : Etude 2023 EPFL Data Center impacts
- Text generation : [Ecologits](https://huggingface.co/spaces/genai-impact/ecologits-calculator), [Luccioni 2024](https://dl.acm.org/doi/10.1145/3630106.3658542)
- Text generation vs. code writing assistance: [Ecologits, prompt sur différents AI](https://huggingface.co/spaces/genai-impact/ecologits-calculator)
- Text generation vs. image generation : [Luccioni 2024](https://dl.acm.org/doi/10.1145/3630106.3658542)
