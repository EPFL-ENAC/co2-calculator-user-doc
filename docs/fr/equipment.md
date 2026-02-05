
# Documentation module : consommation électrique des équipements

<p><b>1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Données collectées</b></p>

<p>L’inventaire des équipements disponible sur Sesame permet d’effectuer la liste des équipements scientifiques (&gt;10'000 CHF), des équipements IT et autres par laboratoire: <a href="https://sesame.epfl.ch/#Shell-home">https://sesame.epfl.ch/#Shell-home</a></p>

<p><b>2.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Méthodologie</b></p>

<p>La puissance moyenne « actif » et « veille » de chaque équipement est multipliée par les heures d’utilisation hebdomadaires, par le nombre de semaines travaillées et par le facteur d’émission de l’électricité suisse :</p>

$$
E_i\;[\mathrm{kWh/an}] = \frac{\big(P_{i,\mathrm{actif}}\;[\mathrm{W}]\cdot h_{i,\mathrm{actif}}\;[\mathrm{h/sem}] + P_{i,\mathrm{veille}}\;[\mathrm{W}]\cdot h_{i,\mathrm{veille}}\;[\mathrm{h/sem}]\big)\cdot 47\;[\mathrm{sem/an}]}{1000}
$$

$$
\mathrm{GES}_i\;[\mathrm{kg\,CO_2\,eq/an}] = E_i\;[\mathrm{kWh/an}]\cdot FE\;[\mathrm{kg\,CO_2\,eq/kWh}]
$$

<p><b>Définitions</b></p>

- <em>P<sub>i,actif</sub></em> et <em>P<sub>i,veille</sub></em> : puissances moyennes « actif » et « veille » (W), déterminées par l’équipe durabilité EPFL (mesures directes ou littérature) — valeurs présentées dans le tableau ci‑dessous.
- <em>h<sub>i,actif</sub></em> et <em>h<sub>i,veille</sub></em> : heures hebdomadaires d’utilisation « actif » et « veille » (h/sem), saisies par l’utilisateur.
- 47 : nombre de semaines travaillées par an.
- <em>FE</em> : facteur d’émission de l’électricité (0.125 kg CO<sub>2</sub> eq/kWh, KBOB 2002).

## Tableau des puissances moyennes des équipements
??? abstract "Tableau des puissances moyennes des équipements"
    {{ read_csv('../includes/table_factor.csv') }}

<p><b>3.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Facteurs d’émissions</b></p>

<p>Seul le facteur d’émission 0.125&nbsp;kg CO<sub>2</sub>&nbsp;eq / kWh (KBOB 2002) est utilisé dans ce module.</p>

## 4. Upload CSV

Il est possible d’uploader un fichier CSV contenant équipements. Le format du fichier doit être le suivant :

header:

```
name,equipment_class,sub_class,active_usage_hours,passive_usage_hours
```

name, equipment_class are mandatory else the entry will be ignored. sub-class, active_usage_hours and passive_usage_hours are optional, if not provided, they have to be completed in the module interface.

All fields are separated by a comma and no spaces must be used after and before the commas.

Example of valid CSV content :

```
 Thermostast Numérique,Agitator / Incubator,Refrigerated incubators,40,128
 ```

The equipment_class must be one of the following : 
??? abstract "Classes et sous classes d’équipements scientifiques"

    - Power supplies 

    - Amplifiers 

    - Signal analysis 

    - Signal generators 

    - Oscilloscopes 

    - Agitator / Incubator: 
    Simple agitators/incubators
    Refrigerated incubators
    30 to 37°C incubators
    Bench agitators (vortex, rockers, platforms, magnetic agitators, thermomixers…)
    CO2 incubators
    Climate chambers
    Water-baths, bead-baths, dry-baths
    Agitation heating plates

    - Centrifugation: 
    Ultra centrifuges
    High-speed floor-standing centrifuges
    Large refrigerated bench top centrifuges
    Large bench top centrifuges
    1.5mL refrigerated bench top centrifuges
    1.5mL bench top centrifuges
    Mini centrifuges

    - Vacuum chamber 

    - Chromatographs (HPLC, etc.): 
    FPLC
    HPLC

    - Cell counter (FACS) 

    - Cryogenics 

    - Cryostats 

    - Cytometer 

    - Evaporator: 
    Vacuum evaporators
    Rotary vacuum evaporators

    - Drying ovens 

    - Laminar flow hood: 
    Old 180cm laminar flow hoods (>15yo)
    Old 120cm laminar flow hoods (>15yo)
    Recent 180cm laminar flow hoods (<15yo)
    Recent 150cm laminar flow hoods  (<15yo)

    - Lab ovens 

    - Lyophilisator: 
    Speed vacuum concentrators
    Lyophilisator (> 1kW)

    - Microtomes 

    - PCR / QPCR: 
    PCR
    QPCR

    - Sequencers 

    - Deposition and engraving systems 

    - Other biological, chem. and phys. equip.: 
    Sonicators, homogenizers
    Transfection systems, electroporators, gene pulsers
    Water purifiers
    Spectrophotometers, fluorimeters, luminometers
    Plate readers
    Plate washers
    Imaging systems, geldocs
    Microwaves
    Refrigerated baths, chillers
    Ultrasound baths
    Bioruptors
    Emulsiflexes
    Crushers
    Euthanasia boxes
    Stimulators
    Pipette pullers
    UV irradiators
    Pipetting robots
    Syringe pumps and injectors
    Gel dryers
    O2 concentrator generators
    Other devices

    - Milling machine 

    - Chemical reactors 

    - Other stewardship equipment 

    - Other measuring equipment 

    - Pneumatic tables 

    - Potentiostat 

    - Probes 

    - Laser-scanning microscope 

    - AFM microscopes 

    - Optical microscopes: 
    Average confocal microscopes
    Microscopes with incubation chamber
    FL microscopes
    Simple microscopes, reversed microscopes, and binocular lenses,…

    - Stereo microscopes 

    - Other microscopy equipment 

    - Gas analyser 

    - Scales 

    - Lab cameras 

    - Spectrometers 

    - Diffractometers 

    - Lasers 

    - Light sources: 
    Light sources for microscope
    Insect UV lights

    - Acoustics 

    - EEG /ECG / EMG 

    - Micromanipulator 

    - Coaters 

    - 3D printer 

    - Driller 

    - Pumps: 
    Vaccum mechanical pumps (> 500W)
    Vaccum diaphragm pumps (< 500W)
    Laboratory suction pumps (< 100W)
    Peristaltic pumps

    - Robots 

    - Autoclaves: 
    Bench top autoclaves
    Autoclaves (150 L)

    - CPG mobile equipment: 
    CPG ventilation motors
    Other CPG mobile equipment

    - Other infrastructure equipment: 
    Distillation equipment
    Washers

??? abstract "Classes et sous classes d’équipements IT"

    - Servers 

    - Desktop 

    - Laptop 

    - Monitors 

    - Printers 

    - Scanners 

    - Telecom 

    - Beamer 

    - Cameras 

    - HF Microphones 

    - Videoconferencing 

    - Hoods 

    - Kitchen freezer 

    - Other electrotechnical equip. 

    - Other IT / telecom  equipment 

    - Photo camera 

    - Screens 

    - Other audiovisual equipment 

    - Special furniture 

    - CPG fixed equipment 

    - Vehicles 

    - Tablet 

    - Software 

    - Network 

    - Components 

??? abstract "Classes et sous classes d’équipements autres"

    - Lab Freezer / Frigde: 
    Old -80°C freezers (>12yo)
    Recent -80°C freezers (<12yo)
    Small +4°C or -20°C freezers (< 150L)
    Big +4°C or -20°C freezers (> 150L)
    Refrigerated display cabinets (fixed or mobile, 1-2m3)
    Cold rooms (20m2)
    Ice machines
