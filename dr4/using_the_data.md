---
layout: page
title: Best practices for GALAH DR4
subtitle: Fourth Data Release
---


{: .main_blockquote}
On this page we provide advice and instructions for using the GALAH DR4 catalogues. We would recommend taking the time to read [Buder *et al.* (2021)](https://doi.org/10.1093/mnras/stab1242), which supplies even more information and quality assessment for GALAH DR4. 

* This text gets replaced.
{:toc}

---

### Recommended catalogue

{: .box-success}
We highly recommend using the `GALAH_DR4_main_allstar.fits` catalogue if you want to work with the GALAH DR4 stellar parameters and elemental abundances.

{: .box-warning}
For more information, see our [Catalogue documentation](/dr4/the_catalogues).

If your science case contains stellar parameters and elemental abundances, then we recommend the `GALAH_DR4_main_allstar.fits` catalogue. It contains one entry per star.

There is an extended version called `GALAH_DR4_main_allspec.fits` that contains one entry per observation. This table is for expert use only.

Consult the [catalogue documentation](/dr4/the_catalogues) for details on the catalogues and acquiring them. If you just want the entire `GALAH_DR4_main_allstar` catalogue, it can be directly [directly downloaded](https://cloud.datacentral.org.au/teamdata/GALAH/public/GALAH_DR4/catalogs/), or with `wget` (removing the `--spider` flag):

```bash
wget --spider https://cloud.datacentral.org.au/teamdata/GALAH/public/GALAH_DR4/catalogs/GALAH_DR4_main_allstar.fits
```

---

### Recommended flag values

{: .box-success}
Overall, we make three recommendations: (1) `snr_px_ccd3 > 30`; (2) only stellar parameters for stars with `flag_sp == 0`; (3) only elemental abundances with `flag_X_fe == 0`.

{: .box-warning}
For more information, see our [Flag bitmask documentation](/dr4/flags).

The main recommended `GALAH_DR4_main_allstar` catalogue contains a number of flags. For most science cases, the most important to consider is the spectroscopic quality flag (`flag_sp`). `flag_sp` folds in many potential sources of errors in the input values (e.g., missing data, very low signal spectra, poor analysis results, possible binarity). **By default, we recommend that users only consider stellar parameters (T<sub>eff</sub>, log *g*, [Fe/H], broadening velocity, radial velocity) for stars with `flag_sp == 0`.**

For the abundance information there are similar flags. For each indivudual elemental abundance `X_fe` there is a `flag_X_fe` that indicates problems with the elemental abundance determination. **We strongly recommend only considering the abundance of element `X` when `flag_X_fe == 0`**. As for all of our previous GALAH releases, we want to stress that we discourage the use of element abundances with `flag_X_fe > 0` without consideration of the possible systematics that these flagged measurements can introduce.

**We would recommend considering only stars with a red camera signal to noise per pixel `snr_px_ccd3 > 30`.**

---

### Recommended columns

{: .box-success}
For stellar parameters and elemental abundances, use the values found in `GALAH_DR4_main_allstar` catalogue. We do **not** recommend values found only in the `GALAH_DR4_main_allspec` catalogue as these are meant for expert use and are typically for diagnostic purposes.

{: .box-warning}
For more information, see our [Table schema documentation](/dr4/table_schema).

In the catalogues that constitute GALAH DR4, for many parameters we provide only one value, e.g., for the overall α-element abundance there is just `alpha_fe`. However, some parameters have multiple values calculated by different methods. In this section, we discuss these parameters and in most cases make a recommendation on the value to use.

* **For stellar luminosity, mass and age, we recommend `log_lum_bstep`, `mass_bstep` and `age_bstep` respectively from the `GALAH_DR3_VAC_ages_v2` table**.
    - Do not use the `lbol`, `mass` and `age` found in the `GALAH_DR3_main_allspec_v2` catalogue.
* **For heliocentric distance, we recommend `distance_bstep` value from the `GALAH_DR3_VAC_ages_v2` table**.
    - `distance_bstep` was calculated as part of the estimation of age, mass, radius etc found in the `GALAH_DR3_VAC_ages_v2` catalogue.
    - `distance_bstep` was used for the vast majority of stars (96 per cent) in the calculation of Galactic kinematic and dynamic parameters in `GALAH_DR3_VAC_dynamics_v2`. For the other 4 per cent of the stars we mostly use the photogeometric distances `r_med_photogeo` in the `GALAH_DR3_VAC_GaiaEDR3_v2` table as calculated by [Bailer-Jones *et al.* (2020)](https://doi.org/10.3847/1538-3881/abd806). The distance used for a given spectrum is provided by the `use_dist_flag` in the `GALAH_DR3_VAC_dynamics_v2` table.
* **For reddening, we recommend the `ebv` value from the `GALAH_DR3_main_allstar_v2` table**.
    - This is from [Schlegel *et al.* (1998)](https://doi.org/10.1086/305772) and was used as part of the estimation of the bolometric corrections.
* Distinct from the iron abundance ([Fe/H]) calculated from the spectra, the `GALAH_DR3_VAC_ages_v2` table includes the initial and current metallicity of the star (`meh_ini_bstep` and `meh_act_bstep`) as calculated by BSTEP. These values were not used as part of the abundance analysis.

This table summarizies the parameters in GALAH DR4 for which there are multiple values for a given star. We have bolded our recommended column.

| Parameter and<br/>recommended value | `main_allstar` | `main_allspec` | `VAC_ages` | `VAC_rv` | `VAC_GaiaEDR3` |
| :------ |:--- | :--- | :------ |:--- | :--- | :--- |
| Radial velocity:<br/>**`rv_galah`** | **`rv_galah`**,<br/>`rv_gaia_dr2` | **`rv_galah`**,<br/>`rv_gaia_dr2`,<br/>`rv_guess`,<br/>`rv_5854`,<br/>`rv_6708`,<br/>`rv_6722` |  | **`rv_galah`**,<br/>`rv_sme_v2`,<br/>`rv_sme_v1`,<br/>`rv_obst`,<br/>`rv_nogr_obst`,<br/>`dr2_radial_velocity` | `dr2_radial_velocity` |
| Effective Temperature:<br/>**`teff`** | **`teff`**,<br/>`irfm_teff` | **`teff`**,<br/>`irfm_teff`,<br/>`init_teff`,<br/>`teff_guess` | `teff_bstep` |  |  |
| Surface gravity:<br/>**`logg`** | **`logg`** | **`logg`**,<br/>`init_logg`,<br/>`logg_guess` | `logg_bstep` |  |  |
| [Fe/H]:<br/>**`fe_h`** |  **`fe_h`**,<br/>`fe_h_atmo` |  **`fe_h`**,<br/>`fe_h_atmo`,<br/>`init_fe_h_atmo`,<br/>`feh_guess` |  |  |  |
| Broadening velocity:<br/>**`vbroad`** | **`vbroad`**  | **`vbroad`**,<br/>`init_vbroad` |  |  |  |
| Stellar luminosity:<br/>**`log_lum_bstep`** |  | `lbol` | **`log_lum_bstep`** |  |  |
| Stellar mass:<br/>**`m_act_bstep`** |  | `mass` | **`m_act_bstep`**,<br/>`m_ini_bstep` |  |  |
| Stellar age:<br/>**`age_bstep`** |  | `age` | **`age_bstep`** |  |  |
| Distance:<br/>**`distance_bstep`** | `r_est_dr2` | `r_est_dr2` | **`distance_bstep`** |  | `r_med_geo`,<br/>`r_med_photogeo` |
| E(B-V):<br/>**`ebv`** | **`ebv`**,<br/>`irfm_ebv` | **`ebv`**,<br/>`irfm_ebv` | `ebv_bstep` |  |  |
| Parallax  | `parallax_dr2` | `parallax_dr2` |  |  | `parallax`,<br/>`parallax_corr` |
| Metallicity |  |  | `meh_act_bstep`,<br/>`meh_ini_bstep` |  |  |


---

### Joining GALAH DR4 catalogues

{: .box-success}
Join GALAH DR4 tables using the `sobject_id`.

The catalogues of GALAH DR4 must be joined or cross-matched using the `sobject_id`. The value-added catalogues are based on the extended catalogue which contains measurements per observed spectrum. 110,923 stars were observed multiple times, and therefore have multiple observed spectra. The `sobject_id` column is our internal ID for each observation and using this column for joining will ensure that you are matching information derived from the same spectrum.

For instance, to join the `GALAH_DR4_main_allstar` and `GALAH_DR4_VAC_dynamics` catalogues [using Data Central](https://datacentral.org.au/services/query/), the following ADQL query could be used:

```sql
SELECT
  TOP 100
  g_ms.dr3_source_id, g_ms.teff, g_ms.logg, g_ms.fe_h,
  g_ages.sobject_id, g_ages.age_bstep, g_ages.e_age_bstep
  FROM galah_dr3p2.main_star AS g_ms
  JOIN galah_dr3p2.vac_dyn AS g_dyn
  	ON g_ms.sobject_id = g_dyn.sobject_id
```

{: .box-warning}
Data Central's ADQL engine does not like column name clashes. So if you are merging tables, it is necessary to explicitly list the columns of interest.
