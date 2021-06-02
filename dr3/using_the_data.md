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
We highly recommend using the `GALAH_DR3_main_allstar_v2.fits` catalogue if you want to work with the GALAH DR3 stellar parameters and elemental abundances.

{: .box-warning}
For more information, see our [Catalogue documentation](/dr3/the_catalogues).

The `GALAH_DR3_main_allstar_v2.fits` catalogue contains one entry per star and is a cleaned version of the extended `GALAH_DR3_main_allspec_v2.fits`. All the details on acquiring this catalogue can be [found here ](/dr3/the_catalogues). If you just want the entire table, it can be directly [directly downloaded from here](https://cloud.datacentral.org.au/teamdata/GALAH/public/GALAH_DR3), or by using `wget` (removing the `--spider` flag):

```bash
wget --spider https://cloud.datacentral.org.au/teamdata/GALAH/public/GALAH_DR3/GALAH_DR3_main_allstar_v2.fits
```

---

### Recommended flag values

{: .box-success}
Overall, we make three recommendations: (1) `snr_c3_iraf > 30`; (2) only stellar parameters for stars with `flag_sp == 0`, `flag_fe_h == 0`; (3) only elemental abundances with `flag_X_fe == 0`.

{: .box-warning}
For more information, see our [Flag bitmask documentation](/dr3/flags).

**We would recommend considering only stars with a signal to noise `snr_c3_iraf > 30`.**

Every star in the `GALAH_DR3_main_allstar_v2.fits` catalogue has two main flags:
* `flag_sp`
    - Folds in many potential sources of errors in the input values (e.g., unreliable astrometry, very low signal spectra, reduction problems, possibly binarity).
* `flag_fe_h`
    - Indicates problems with the stellar parameter determination.

**By default, we recommend that users only consider stellar parameters (T<sub>eff</sub>, log *g*, [Fe/H], broadening velocity, radial velocity) for stars with `flag_sp == 0` and `flag_fe_h == 0`.**

For every elemental abundance `X_fe` for each star in `GALAH_DR3_main_allstar_v2.fits` catalogue there is one flag:
* `flag_X_fe`
    - Indicates problems with the elemental abundance determination.

**We strongly recommend only considering the abundance of element `X` when `flag_X_fe == 0`**. As for all of our previous GALAH releases, we want to stress that we discourage the use of element abundances with `flag_X_fe > 0` without consideration of the possible systematics that these flagged measurements can introduce.

---

### Recommended columns

{: .box-success}
For stellar parameters and elemental abundances, use the values found in `GALAH_DR3_main_allstar_v2` catalogue. We do **not** recommend values found only in the `GALAH_DR3_main_allspec_v2` catalogue as these are only for expert use and are typically for diagnostic purposes.

{: .box-warning}
For more information, see our [Table scheme documentation](/dr3/table_schema).

In the catalogues that constitute GALAH DR3, for many parameters we provide only one value (e.g., for the α-element abundance, `alpha_fe`). However, some parameters have multiple values calculated by different methods. In this section, we discuss these parameters and in most cases make a recommendation on the value to use.

* **For radial velocity, we strongly recommend the `rv_galah`**.
    - The source of this value differs for each star. For 83 per cent of stars `rv_galah == rv_obst` (found in the `vac_rv` table), the radial velocity measured by Zwitter et al (2020) from our observed spectra. The remaining stars will have `rv_galah == rv_sme_v2`, the value measured by SME during the analysis process. The `rv_obst` value has errors typically five times smaller than the SME-measured value. Consult the `use_rv_flag` for each star to identify the source of the radial velocity for `rv_galah`.
    - The other radial velocity values available are either from *Gaia* DR2, or are diagnostic values measured during the analysis (e.g., `rv_6708` is the RV measured from just the Li6708 line). See the section of the Value-added catalogues documentation page on the `GALAH_DR3_VAC_rv_v2` table for more details.
* **For effective temperature, surface gravity, iron abundance ([Fe/H]), broadening velocity, we strongly recommend `teff`, `logg`, `fe_h`, `vbroad` respectively from the `GALAH_DR3_main_allstar_v2` catalogue**.
    - These are inferred as part of the spectrum fitting and abundance determination.
    - The other provided values of these are either calculated during an intermediary analysis step (e.g., `teff_guess`), or as part of a value-added catalogues (e.g., `teff_bstep`).
* **For stellar mass and age, we recommend `mass_bstep` and `age_bstep` from the `GALAH_DR3_VAC_ages_v2` table**.
    - Do not use the `mass` and `age` found in the main_spec table.
* **For heliocentric distance, we recommend `distance_bstep` value from the `GALAH_DR3_VAC_ages_v2` table**.
    - `distance_bstep` was calculated as part of the estimation of age, mass, radius etc found in the `GALAH_DR3_VAC_ages_v2` catalogue.
    - `distance_bstep` was used for the vast majority of stars (96 per cent) in the calculation of Galactic kinematic and dynamic parameters in `GALAH_DR3_VAC_dynamics_v2`. For the other 4 per cent of the stars we mostly use the photogeometric distances `r_med_photogeo` in the `GALAH_DR3_VAC_GaiaEDR3_v2` table as calculated by [Bailer-Jones et al. (2020)](https://doi.org/10.3847/1538-3881/abd806). The distance used for a given spectrum is provided by the `use_dist_flag` in the `GALAH_DR3_VAC_dynamics_v2` table.
* **For reddening, we recommend the `ebv` value from the `GALAH_DR3_main_allstar_v2` table**.
    - This is from Schlegel et al (1998) and was used as part of the estimation of the bolometric corrections.
* For parallax, the GALAH DR3 catalogues has the parallax values from both the *Gaia* DR2 and eDR3 values (the former being called `parallax_dr2` in our catalogues). We have also calculated the eDR3 parallax corrected for the zeropoint offset as prescribed in [Lindegren et al (2020)](https://doi.org/10.1051/0004-6361/202039653 ), called `parallax_corr` in our tables. We do not have any strong recommendation on the best parallax value to use.
* Distinct from the iron abundance ([Fe/H]) calculated from the spectra, the `GALAH_DR3_VAC_ages_v2` table includes the initial and current metallicity of the star (`meh_ini_bstep` and `meh_act_bstep`) as calculated by BSTEP. These values were not used as part of the abundance analysis.

This table summarizies the parameters in GALAH DR3 for which there are multiple values for a given star. We have bolded our recommended column.

| Parameter and<br/>recommended value | `main_allstar` | `main_allspec` | `VAC_ages` | `VAC_rv` | `VAC_GaiaEDR3` |
| :------ |:--- | :--- | :------ |:--- | :--- | :--- |
| Radial velocity:<br/>**`rv_galah`** | **`rv_galah`**,<br/>`rv_gaia_dr2` | **`rv_galah`**,<br/>`rv_gaia_dr2`,<br/>`rv_guess`,<br/>`rv_5854`,<br/>`rv_6708`,<br/>`rv_6722` |  | **`rv_galah`**,<br/>`rv_sme_v2`,<br/>`rv_sme_v1`,<br/>`rv_obst`,<br/>`rv_nogr_obst`,<br/>`dr2_radial_velocity` | `dr2_radial_velocity` |
| Effective Temperature:<br/>**`teff`** | **`teff`**,<br/>`irfm_teff` | **`teff`**,<br/>`irfm_teff`,<br/>`init_teff`,<br/>`teff_guess` | `teff_bstep` |  |  |
| Surface gravity:<br/>**`logg`** | **`logg`** | **`logg`**,<br/>`init_logg`,<br/>`logg_guess` | `logg_bstep` |  |  |
| [Fe/H]:<br/>**`fe_h`** |  **`fe_h`**,<br/>`fe_h_atmo` |  **`fe_h`**,<br/>`fe_h_atmo`,<br/>`init_fe_h_atmo`,<br/>`feh_guess` |  |  |  |
| Broadening velocity:<br/>**`vbroad`** | **`vbroad`**  | **`vbroad`**,<br/>`init_vbroad` |  |  |  |
| Stellar mass:<br/>**`m_act_bstep`** |  | `mass` | **`m_act_bstep`**,<br/>`m_ini_bstep` |  |  |
| Stellar age:<br/>**`age_bstep`** |  | `age` | **`age_bstep`** |  |  |
| Distance:<br/>**`distance_bstep`** | `r_est_dr2` | `r_est_dr2` | **`distance_bstep`** |  | `r_med_geo`,<br/>`r_med_photogeo` |
| E(B-V):<br/>**`ebv`** | **`ebv`**,<br/>`irfm_ebv` | **`ebv`**,<br/>`irfm_ebv` | `ebv_bstep` |  |  |
| Parallax  | `parallax_dr2` | `parallax_dr2` |  |  | `parallax`,<br/>`parallax_corr` |
| Metallicity |  |  | `meh_act_bstep`,<br/>`meh_ini_bstep` |  |  |


---

### Joining GALAH DR3 catalogues

{: .box-success}
Join GALAH DR3 tables using the `sobject_id`.

The catalogues of GALAH DR3 must be joined or cross-matched using the `sobject_id`. Do not use the `star_id` or *Gaia* `source_id` joining catalogues. These value-added catalogues are based upon the extended catalogue which contains measurements per observed spectrum. About 50000 stars were observed multiple times, and therefore have multiple observed spectra. The `sobject_id` column is our internal ID for each observation and using this column for joining will ensure that you are matching information derived from the same spectrum. For instance, to join the `GALAH_DR3_main_allstar_v2` and `GALAH_DR3_VAC_ages_v2` catalogues, [using the Data Central](https://datacentral.org.au/services/query/), the following ADQL query could be used:

```sql
-- Join GALAH_DR3_main_allstar_v2 and GALAH_DR3_VAC_ages_v2
-- and get the effective temperature, surface gravity,
-- iron abundance, and age of each star.
SELECT
  TOP 100
  g_ms.source_id, g_ms.teff, g_ms.logg, g_ms.fe_h,
  g_ages.sobject_id, g_ages.age_bstep, g_ages.e_age_bstep
  -- GALAH_DR3_main_allstar_v2 is galah_dr3.main_star
  FROM galah_dr3.main_star AS g_ms
  -- GALAH_DR3_VAC_ages_v2 is galah_dr3.vac_ages
  JOIN galah_dr3.vac_ages AS g_ages
  	ON g_ms.sobject_id = g_ages.sobject_id
```
