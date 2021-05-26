---
layout: page
title: Best practices for GALAH DR3
subtitle: Third Data Release
---

On this page we provide advice and instructions for using the GALAH DR3 catalogues. We would recommend taking the time to read [Buder et al. (2021)](https://arxiv.org/abs/2011.02505), which supplies even more information and quality assessment of GALAH DR3. Sven Buder has created iPython notebooks tutorials for GALAH DR3 which are available here.

<h3> On this page</h3>
* This text gets replaced.
{:toc}

---

### Recommended catalogue

{: .box-success}
We highly recommend using the `galah_dr3.main_star` catalogue if you want to work with the GALAH DR3 stellar parameters and elemental abundances.

The `galah_dr3.main_star` catalogue contains one entry per star and is a cleaned version of the extended `galah_dr3.main_spec`. All the details on acquiring this catalogue can be [found here ](/dr3/get_the_catalogues). If you just want the entire table, it can be directly downloaded from here (it has the file name `GALAH_DR3_main_allstar_v2.fits`), or by using `wget` (removing the `--spider` flag):

```bash
wget --spider https://cloud.datacentral.org.au/teamdata/GALAH/public/GALAH_DR3/GALAH_DR3_main_allstar_v2.fits
```

---

### Recommended flag values

{: .box-success}
We highly recommend only using stars with `flag_sp == 0`, `flag_fe_h == 0`, `flag_X_fe == 0`, and `snr_c3_iraf > 30`.

Every star in the GALAH DR3 catalogues has two main flags:
* `flag_sp`
    - Folds in many potential sources of errors in the input values (e.g., unreliable astrometry, very low signal spectra, reduction problems, possibly binarity)
* `flag_fe_h`
    - Indicates problems with the stellar parameter determination

**By default, we recommend that users only consider stellar parameters (T<sub>eff</sub>, log *g*, [Fe/H], broadening velocity, radial velocity) for stars with `flag_sp == 0` and `flag_fe_h == 0`.**

For every elemental abundance `X_fe` for each star there is a `flag_X_fe`. **We strongly recommend only considering the abundance of element `X` when `flag_X_fe == 0`**. As for all of our previous GALAH releases, we want to stress that we discourage the use of flagged element abundances without consideration of the possible systematics that these flagged measurements can introduce.

Further, we would recommend considering only stars with a signal to noise `snr_c3_iraf > 30`.

---

### Recommended columns

{: .box-success}
For stellar parameters and elemental abundances, use the values found in `galah_dr3.main_star` catalogue.

In the catalogues that constitute GALAH DR3, for many parameters we provide only one value, e.g., for the α-element abundance, we provide one value: `alpha_fe`. However, some parameters have multiple values calculated by different methods. Here we tabulate and discuss these parameters and in most cases make a recommendation on the value to use. Generally we do **not** recommend values found only in the `main_spec` catalogue as these are only for expert use and are typically for diagnostic purposes.

<!--
As well as the `main_star` catalogue, there are a number of value-added catalogues. Details on accessing the data can be found on the Catalogue Data Access page. The value-added catalogues are fully described on the Value-Added Catalogues page. Full details of all the columns and their descriptions is found on the Table Schema page. Briefly the catalogues of GALAH DR3 are:
* `main_star`: The main result catalogue. Our recommended table about stellar parameters and elemental abundance. One entry per star observed. Radial velocity, stellar parameters and abundance data.
* `main_spec`: One entry per observation (about 50000 stars have been observed at least twice). Radial velocity, stellar parameters for each observation. Also contains abundances derived for each individual line.
* `vac_ages`: Ages, distances, luminosities, masses, metallicities, radii and other parameters calculated from isochrones by the Bayesian Stellar Parameter Estimation code (BSTEP) from Sharma et al. (2018).
* `vac_rv`: Collated radial velocity measurements
* `vac_gaiaedr3`: *Gaia* eDR3 data for all stars in GALAH DR3
* `vac_dynamics`: Galactic kinematic and dynamic parameters
 -->


* **For radial velocity, we strongly recommend the `rv_galah` from the `main_star` catalogue**. The source of this value differs for each star. For 83 per cent of stars `rv_galah == rv_obst` (found in the `vac_rv` table), the radial velocity measured by Zwitter et al (2020) from our observed spectra. The remaining stars will have `rv_galah == rv_sme_v2`, the value measured by SME during the analysis process. The `rv_obst` value has errors typically five times smaller than the SME-measured value. Consult the `use_rv_flag` for each star to identify the source of the radial velocity for `rv_galah`. The other radial velocity values available are either from *Gaia* DR2, or are diagnostic values measured during the analysis (e.g., `rv_6708` is the RV measured from just the Li6708 line). See the section of the Value-added catalogues documentation page on the `vac_rv` catalogue for more details.
* **For effective temperature, surface gravity, iron abundance ([Fe/H]), broadening velocity, we strongly recommend `teff`, `logg`, `fe_h`, `vbroad` respectively from the `main_star` catalogue**. These are inferred as part of the spectrum fitting and abundance determination. The other provided values of these are either calculated during an intermediary analysis step (e.g., `teff_guess`), or as part of a value-added catalogues (e.g., `teff_bstep`).
* **For stellar mass and age, we recommend `mass_bstep` and `age_bstep` from the `vac_ages` catalogue**, rather than the `mass` and `age` found in the main_spec table.
* **For distance, we recommend this `distance_bstep` value from the `vac_ages` catalogue**. It was calculated as part of the estimation of age, mass, radius etc found in the `vac_ages` catalogue, and was used for the vast majority of stars (96 per cent) in the calculation of Galactic kinematic and dynamic parameters in `vac_dynamics`. For the other 4 per cent of the stars we mostly use the photogeometric distances `r_med_photogeo` in the `vac_gaiaedr3` catalogue as calculated by Bailer-Jones et al. (2020). The distance used for a given spectrum is provided by the `use_dist_flag` in the `galah_dr3.vac_dynamics` table.s
* **For reddening, we recommend the `ebv` value from the `main_star` catalogue**. This is from Schlegel et al (1998) and was used as part of the estimation of the bolometric corrections.
* For parallax, the GALAH DR3 catalogues has the parallax values from both the *Gaia* DR2 and eDR3 values (the former being called `parallax_dr2` in our catalogues). We have also calculated the eDR3 parallax corrected for the zeropoint offset as prescribed in Lindegren et al (2020), called `parallax_corr` in our tables. We do not have any strong recommendation on the best parallax value to use.
* Distinct from the iron abundance ([Fe/H]) calculated from the spectra, the value-added catalogue of values from BSTEP includes the initial and current metallicity of the star (`meh_ini_bstep` and `meh_act_bstep`). These values were not used as part of the abundance analysis.

This table summarizies the parameters in GALAH DR3 for which there are multiple values for a given star. We have bolded our recommended column.

| Parameter | Recommended value | main_star | main_spec | vac_ages | vac_rv | vac_gaiaedr3 |
| :------ |:--- | :--- | :------ |:--- | :--- | :--- |
| Radial velocity | **`rv_galah`** | **`rv_galah`**,<br/>`rv_gaia_dr2` | **`rv_galah`**,<br/>`rv_gaia_dr2`,<br/>`rv_guess`,<br/>`rv_5854`,<br/>`rv_6708`,<br/>`rv_6722` |  | **`rv_galah`**,<br/>`rv_sme_v2`,<br/>`rv_sme_v1`,<br/>`rv_obst`,<br/>`rv_nogr_obst`,<br/>`dr2_radial_velocity` | `dr2_radial_velocity` |
| Effective Temperature | **`teff`** | **`teff`**,<br/>`irfm_teff` | **`teff`**,<br/>`irfm_teff`,<br/>`init_teff`,<br/>`teff_guess` | `teff_bstep` |  |  |
| Surface gravity | **`logg`** | **`logg`** | **`logg`**,<br/>`init_logg`,<br/>`logg_guess` | `logg_bstep` |  |  |
| [Fe/H] | **`fe_h`** |  **`fe_h`**,<br/>`fe_h_atmo` |  **`fe_h`**,<br/>`fe_h_atmo`,<br/>`init_fe_h_atmo`,<br/>`feh_guess` |  |  |  |
| Broadening velocity | **`vbroad`** | **`vbroad`**  | **`vbroad`**,<br/>`init_vbroad` |  |  |  |
| Stellar mass | **`m_act_bstep`** |  | `mass` | **`m_act_bstep`**,<br/>`m_ini_bstep` |  |  |
| Stellar age | **`age_bstep`** |  | `age` | **`age_bstep`** |  |  |
| Distance | **Consult the `use_dist_flag` for each star** | `r_est_dr2` | `r_est_dr2` | `distance_bstep` |  | `r_med_geo`,<br/>`r_med_photogeo` |
| E(B-V) | **`ebv`** | **`ebv`**,<br/>`irfm_ebv` | **`ebv`**,<br/>`irfm_ebv` | `ebv_bstep` |  |  |
| Parallax |  | `parallax_dr2` | `parallax_dr2` |  |  | `parallax`,<br/>`parallax_corr` |
| Metallicity |  |  |  | `meh_act_bstep`,<br/>`meh_ini_bstep` |  |  |

---

### How to join tables in GALAH DR3

{: .box-success}
Join GALAH DR3 tables using the `sobject_id`.

The catalogues of GALAH DR3 must be joined or cross-matched using the `sobject_id`. Do not use the `star_id` or *Gaia* `source_id` joining catalogues. These value-added catalogues are based upon the extended catalogue which contains measurements per observed spectrum. About 50000 stars were observed multiple times, and therefore have multiple observed spectra. The `sobject_id` column is our internal ID for each observation and using this column for joining will ensure that you are matching information derived from the same spectrum. For instance, to join the `galah_dr3.main_star` to the value-added catalogue of ages (`galah_dr3.vac_ages`), the following ADQL query could be used:

```sql
SELECT
  TOP 100
  g_ms.source_id, g_ages.sobject_id, g_ages.age_bstep, g_ages.e_age_bstep
  FROM galah_dr3.main_star AS g_ms
  JOIN galah_dr3.vac_ages AS g_ages
  	ON g_ms.sobject_id = g_ages.sobject_id
```
