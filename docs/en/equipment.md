
# Documentation module: consommation électrique des équipements

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
