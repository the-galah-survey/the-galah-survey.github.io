---
layout: page
title: Table Schema
subtitle: Third Data Release
---

{: .main_blockquote}
This page gives the schema (or data model) for the [GALAH DR3 main and value-added catalogues](/dr3/the_catalogues).

{: .box-warning}
We strongly recommend reading the [recommended columns section of our Best Practices page](/dr3/using_the_data/#recommended-columns). This discusses how some parameters have different values in GALAH DR3 from different methods (e.g., for effective temperature there is `teff`, `irfm_teff`, `init_teff`, `teff_guess`; in this case we recommend `teff`.).

{: .box-warning}
The `sobject_id` column should be used for joining the catalogues.

* This text gets replaced.
{:toc}

---

### `GALAH_DR3_main_allstar_v2` and `GALAH_DR3_main_allspec_v2`

Unless otherwise noted, all columns are found in both `GALAH_DR3_main_allstar_v2` and `GALAH_DR3_main_allspec_v2`. To save space in the table below, the columns related to abundances have been collapsed in single entries (e.g., `X_fe`), and they are all listed in a table at the bottom of this page.


| Column name | Description | units | type |
| :------ |:--- | :--- | :--- |
| `sobject_id` | GALAH identifier |  | integer |
| `star_id` | 2MASS identifier |  | string |
| `dr2_source_id` | Gaia DR2 `source_id` |  | integer |
| `dr3_source_id` | Gaia DR3 `source_id` |  | integer |
| `survey_name` | Name of survey as part of GALAH+DR3 |  | string |
| `field_id` | GALAH field identifer |  | integer |
| `flag_repeat` | [Repeat observation flag](/dr3/flags/#red_flag), indicating if used for clean catalog |  | integer |
| `wg4_field` | GALAH WG4 field |  | string |
| `wg4_pipeline` | SME pipeline version `free`/`lbol`/`seis` |  | string |
| `flag_sp` | [Stellar parameter quality flag](/dr3/flags/#flag_sp) |  | integer |
| `teff` | Spectroscopic effective temperature (used for fitting) | K | float |
| `e_teff` | Uncertainty `teff` | K | float |
| `irfm_teff` | IRFM temperature (not used for synthesis) | K | float |
| `irfm_ebv` | E(B-V) used for IRFM `teff` estimation | mag | float |
| `irfm_ebv_ref` | Reference `irfm_ebv` |  | string |
| `cov_e_teff` | SME covariance fitting uncertainty `teff`. Only in `main_allspec`. | K | float |
| `init_teff` | SME initial `teff`. Only in `main_allspec`. | K | float |
| `logg` | Surface gravity (not fitted via spectra if `wg4_pipeline` not free) | log(cm&#8239;s<sup>-2</sup>) | float |
| `e_logg` | Uncertainty `logg` | log(cm&#8239;s<sup>-2</sup>) | float |
| `cov_e_logg` | MonteCarlo uncertainty `logg`. Only in `main_allspec`. | log(cm&#8239;s<sup>-2</sup>) | float |
| `init_logg` | SME initial `logg`. Only in `main_allspec`. | log(cm&#8239;s<sup>-2</sup>) | float |
| `fe_h` | Fe atomic abundance from Fe lines (final, 1D-NLTE) |  | float |
| `e_fe_h` | Uncertainty `fe_h` |  | float |
| `cov_e_fe_h` | SME covariance fitting uncertainty `fe_h`. Only in `main_allspec`. |  | float |
| `flag_fe_h` | [Quality flag `fe_h`](/dr3/flags/#flag_fe_h) |  | integer |
| `fe_h_atmo` | sme.feh from stellar parameter run, fitted from H, Ti, Sc, Fe |  | float |
| `e_fe_h_atmo` | Uncertainty `fe_h_atmo`. Only in `main_allspec`. |  | float |
| `cov_e_fe_h_atmo` | SME covariance fitting uncertainty sme.feh. Only in `main_allspec`. |  | float |
| `init_fe_h_atmo` | SME initial sme.feh. Only in `main_allspec`. |  | float |
| `vmic` | Microturbulence velocity (from empirical relation) | km&#8239;s<sup>-1</sup> | float |
| `vbroad` | Broadening velocity (fitted sme.vsini with sme.vmac=0) | km&#8239;s<sup>-1</sup> | float |
| `e_vbroad` | Uncertainty of `vbroad` | km&#8239;s<sup>-1</sup> | float |
| `cov_e_vbroad` | SME covariance fitting uncertainty sme.vsini. Only in `main_allspec`. | km&#8239;s<sup>-1</sup> | float |
| `init_vbroad` | SME initial broadening velocity. Only in `main_allspec`. | km&#8239;s<sup>-1</sup> | float |
| `mass` | Stellar parameter fitting product of stellar mass. Only in `main_allspec`. | M<sub>&#9737;</sub> | float |
| `lbol` | Stellar parameter fitting product of bolometric luminosity. Only in `main_allspec`. | L<sub>&#9737;</sub> | float |
| `age` | Stellar parameter fitting product of stellar age. Only in `main_allspec`. | Gyr | float |
| `chi2_sp` | χ² value of stellar parameter fitting |  | float |
| `alpha_fe` | Combined, weighted α-process element abundance |  | float |
| `e_alpha_fe` | Uncertainty of `alpha_fe` |  | float |
| `nr_alpha_fe` | Bitmask of used measurements for `alpha_fe` |  | float |
| `flag_alpha_fe` | [Quality flag of measurements for `alpha_fe`](/dr3/flags/#flag_x_fe) |  | integer |
| `flux_A_Fe` | Normalised maximum absorption strength of in iron lines |  | float |
| `chi_A_Fe` | χ² value of iron abundance fitting |  | float |
| `ind_X1234_fe` | Individual uncalibrated measurmenet of line/combo X1234. Only in `main_allspec`. |  | float |
| `ind_cov_e_X1234` | SME covariance fitting uncertainty `ind_X1234_fe`. Only in `main_allspec`. |  | float |
| `ind_flag_X1234` | [Quality flag fit for `ind_X1234_fe`](/dr3/flags/#ind_flag_x1234). Only in `main_allspec`. |  | integer |
| `X_fe` | Neutral/ionised X atomic abundance (final, 1D-LTE or NLTE) |  | float |
| `e_X_fe` | Uncertainty `X_fe` |  | float |
| `nr_X_fe` | Bitmask of used X ind lines |  | integer |
| `flag_X_fe` | [Quality flag of `X_fe`](/dr3/flags/#flag_x_fe) |  | integer |
| `ra_dr2` | Right Ascension propagated from Gaia DR2. Original name `ra`. | deg | float |
| `dec_dr2` | Declination propagated from Gaia DR2. Original name `dec`. | deg | float |
| `parallax_dr2` | Parallax propagated from Gaia DR2. Original name `parallax`. | mas | float |
| `parallax_error_dr2` | Parallax error propagated from Gaia DR2. Original name `parallax_error`. | mas | float |
| `r_est_dr2` | Estimated distance propagated from [Bailer-Jones *et al.* (2018)](https://ui.adsabs.harvard.edu/abs/2018AJ....156...58B/abstract). Original name `r_est`. | pc | float |
| `r_lo_dr2` | Lower bound on the confidence interval of the estimated distance propagated from [Bailer-Jones *et al.* (2018)](https://ui.adsabs.harvard.edu/abs/2018AJ....156...58B/abstract). Original name `r_lo`. | pc | float |
| `r_hi_dr2` |  Upper bound on the confidence interval of the estimated distance propagated from [Bailer-Jones *et al.* (2018)](https://ui.adsabs.harvard.edu/abs/2018AJ....156...58B/abstract). Original name `r_hi`. | pc | float |
| `r_len_dr2` | Length scale used in the prior for the distance estimation propagated from [Bailer-Jones *et al.* (2018)](https://ui.adsabs.harvard.edu/abs/2018AJ....156...58B/abstract). Original name `r_len`. | pc | float |
| `rv_galah` | Best-method radial velocity from GALAH spectra | km&#8239;s<sup>-1</sup> | float |
| `e_rv_galah` | Uncertainty of `rv_galah` | km&#8239;s<sup>-1</sup> | float |
| `rv_gaia_dr2` | Radial velocity propagated from Gaia DR2; identical to `dr2_radial_velocity` | km&#8239;s<sup>-1</sup> | float |
| `e_rv_gaia_dr2` | Radial velocity error propagated from Gaia DR2; identical to `dr2_radial_velocity_error` | km&#8239;s<sup>-1</sup> | float |
| `red_flag` | [Reduction pipeline quality flag](/dr3/flags/#red_flag) |  | integer |
| `ebv` | [Schlegel et al. (1998)](https://doi.org/10.1086/305772) extinction value | mag | float |
| `snr_c1_iraf` | Average SNR/px CCD1 |  | float |
| `snr_c2_iraf` | Average SNR/px CCD2 |  | float |
| `snr_c3_iraf` | Average SNR/px CCD3 |  | float |
| `snr_c4_iraf` | Average SNR/px CCD4 |  | float |
| `flag_guess` | [GUESS reduction pipeline quality flag](/dr3/flags/#red_flag) |  | integer |
| `rv_guess` | Reduction pipeline best radial velocity. Only in `main_allspec`. | km&#8239;s<sup>-1</sup> | float |
| `e_rv_guess` | Reduction pipeline uncertainty radial velocity. Only in `main_allspec`. | km&#8239;s<sup>-1</sup> | float |
| `teff_guess` | Reduction pipeline best T<sub>eff</sub>. Only in `main_allspec`. | K | float |
| `logg_guess` | Reduction pipeline best log*g*. Only in `main_allspec`. | log(cm&#8239;s<sup>-2</sup>) | float |
| `feh_guess` | Reduction pipeline best [Fe/H]. Only in `main_allspec`. |  | float |
| `rv_5854` | Local best fit to RV when fitting A(Ba5854). Only in `main_allspec`. | km&#8239;s<sup>-1</sup> | float |
| `rv_6708` | Local best fit to RV when fitting A(Li6708). Only in `main_allspec`. | km&#8239;s<sup>-1</sup> | float |
| `rv_6722` | Local best fit to RV when fitting A(Si6722). Only in `main_allspec`. | km&#8239;s<sup>-1</sup> | float |
| `v_jk` | V magnitude estimated from 2MASS J and K<sub>s</sub> mag | mag | float |
| `j_m` | J magnitude propagated from 2MASS | mag | float |
| `j_msigcom` | J magnitude uncertainty propagated from 2MASS | mag | float |
| `h_m` | Band H magnitude propagated from 2MASS | mag | float |
| `h_msigcom` | H magnitude uncertainty propagated from 2MASS | mag | float |
| `ks_m` | Band K<sub>s</sub> magnitude propagated from 2MASS | mag | float |
| `ks_msigcom` | K<sub>s</sub> magnitude uncertainty magnitude propagated from 2MASS | mag | float |
| `ph_qual_tmass` | JHK<sub>s</sub> Photometric quality flag propagated from 2MASS. Renamed from `ph_qual` in original catalogue. |  | string |
| `w2mpro` | W2 profile-fitting magnitude propagated from AllWISE | mag | float |
| `w2mpro_error` | Error on W2 profile-fitting magnitude propagated from AllWISE | mag | float |
| `ph_qual_wise` | Photometric quality flag propagated from AllWISE. Renamed from `ph_qual` in original catalogue. |  | string |
| `a_ks` | Used K<sub>s</sub> band extinction | mag | float |
| `e_a_ks` | Uncertainty of `a_ks` | mag | float |
| `bc_ks` | Used Bolometric Correction for K<sub>s</sub> band | mag | float |
| `ruwe_dr2` | Renormalised unit weight error propagated from Gaia DR2. Renamed from `ruwe` in original catalogue. |  | float |

#### Abundance columns

To save space in the [table above](#galah_dr3_main_allstar_v2-and-galah_dr3_main_allspec_v2), the columns related to abundances are collated in single entries (e.g., `X_fe`). Below we list all of the abundance-related columns.

| Placeholder column name | All possible column names
| :------ |:--- | :--- |
| `X_fe`<br/><br/>Neutral/ionised X atomic abundance (final, 1D-LTE or NLTE) | `Li_fe` `C_fe` `O_fe` `Na_fe` `Mg_fe` `Al_fe` `Si_fe` `K_fe` `Ca_fe` `Sc_fe` `Sc2_fe` `Ti_fe` `Ti2_fe` `V_fe` `Cr_fe` `Cr2_fe` `Mn_fe` `Co_fe` `Ni_fe` `Cu_fe` `Zn_fe` `Rb_fe` `Sr_fe` `Y_fe` `Zr_fe` `Mo_fe` `Ru_fe` `Ba_fe` `La_fe` `Ce_fe` `Nd_fe` `Sm_fe` `Eu_fe` `Li_fe` `C_fe` `O_fe` `Na_fe` `Mg_fe` `Al_fe` `Si_fe` `K_fe` `Ca_fe` `Sc_fe` `Sc2_fe` `Ti_fe` `Ti2_fe` `V_fe` `Cr_fe` `Cr2_fe` `Mn_fe` `Co_fe` `Ni_fe` `Cu_fe` `Zn_fe` `Rb_fe` `Sr_fe` `Y_fe` `Zr_fe` `Mo_fe` `Ru_fe` `Ba_fe` `La_fe` `Ce_fe` `Nd_fe` `Sm_fe` `Eu_fe` |
| `e_X_fe`<br/><br/>Uncertainty `X_fe` | `e_Li_fe` `e_C_fe` `e_O_fe` `e_Na_fe` `e_Mg_fe` `e_Al_fe` `e_Si_fe` `e_K_fe` `e_Ca_fe` `e_Sc_fe` `e_Sc2_fe` `e_Ti_fe` `e_Ti2_fe` `e_V_fe` `e_Cr_fe` `e_Cr2_fe` `e_Mn_fe` `e_Co_fe` `e_Ni_fe` `e_Cu_fe` `e_Zn_fe` `e_Rb_fe` `e_Sr_fe` `e_Y_fe` `e_Zr_fe` `e_Mo_fe` `e_Ru_fe` `e_Ba_fe` `e_La_fe` `e_Ce_fe` `e_Nd_fe` `e_Sm_fe` `e_Eu_fe` `e_Li_fe` `e_C_fe` `e_O_fe` `e_Na_fe` `e_Mg_fe` `e_Al_fe` `e_Si_fe` `e_K_fe` `e_Ca_fe` `e_Sc_fe` `e_Sc2_fe` `e_Ti_fe` `e_Ti2_fe` `e_V_fe` `e_Cr_fe` `e_Cr2_fe` `e_Mn_fe` `e_Co_fe` `e_Ni_fe` `e_Cu_fe` `e_Zn_fe` `e_Rb_fe` `e_Sr_fe` `e_Y_fe` `e_Zr_fe` `e_Mo_fe` `e_Ru_fe` `e_Ba_fe` `e_La_fe` `e_Ce_fe` `e_Nd_fe` `e_Sm_fe` `e_Eu_fe` |
| `nr_X_fe`<br/><br/>Bitmask of used X ind lines | `nr_Li_fe` `nr_C_fe` `nr_O_fe` `nr_Na_fe` `nr_Mg_fe` `nr_Al_fe` `nr_Si_fe` `nr_K_fe` `nr_Ca_fe` `nr_Sc_fe` `nr_Sc2_fe` `nr_Ti_fe` `nr_Ti2_fe` `nr_V_fe` `nr_Cr_fe` `nr_Cr2_fe` `nr_Mn_fe` `nr_Co_fe` `nr_Ni_fe` `nr_Cu_fe` `nr_Zn_fe` `nr_Rb_fe` `nr_Sr_fe` `nr_Y_fe` `nr_Zr_fe` `nr_Mo_fe` `nr_Ru_fe` `nr_Ba_fe` `nr_La_fe` `nr_Ce_fe` `nr_Nd_fe` `nr_Sm_fe` `nr_Eu_fe` `nr_Li_fe` `nr_C_fe` `nr_O_fe` `nr_Na_fe` `nr_Mg_fe` `nr_Al_fe` `nr_Si_fe` `nr_K_fe` `nr_Ca_fe` `nr_Sc_fe` `nr_Sc2_fe` `nr_Ti_fe` `nr_Ti2_fe` `nr_V_fe` `nr_Cr_fe` `nr_Cr2_fe` `nr_Mn_fe` `nr_Co_fe` `nr_Ni_fe` `nr_Cu_fe` `nr_Zn_fe` `nr_Rb_fe` `nr_Sr_fe` `nr_Y_fe` `nr_Zr_fe` `nr_Mo_fe` `nr_Ru_fe` `nr_Ba_fe` `nr_La_fe` `nr_Ce_fe` `nr_Nd_fe` `nr_Sm_fe` `nr_Eu_fe` |
| `flag_X_fe`<br/><br/>[Quality flag of `X_fe`](/dr3/flags/#flag_x_fe) | `flag_Li_fe` `flag_C_fe` `flag_O_fe` `flag_Na_fe` `flag_Mg_fe` `flag_Al_fe` `flag_Si_fe` `flag_K_fe` `flag_Ca_fe` `flag_Sc_fe` `flag_Sc2_fe` `flag_Ti_fe` `flag_Ti2_fe` `flag_V_fe` `flag_Cr_fe` `flag_Cr2_fe` `flag_Mn_fe` `flag_Co_fe` `flag_Ni_fe` `flag_Cu_fe` `flag_Zn_fe` `flag_Rb_fe` `flag_Sr_fe` `flag_Y_fe` `flag_Zr_fe` `flag_Mo_fe` `flag_Ru_fe` `flag_Ba_fe` `flag_La_fe` `flag_Ce_fe` `flag_Nd_fe` `flag_Sm_fe` `flag_Eu_fe` `flag_Li_fe` `flag_C_fe` `flag_O_fe` `flag_Na_fe` `flag_Mg_fe` `flag_Al_fe` `flag_Si_fe` `flag_K_fe` `flag_Ca_fe` `flag_Sc_fe` `flag_Sc2_fe` `flag_Ti_fe` `flag_Ti2_fe` `flag_V_fe` `flag_Cr_fe` `flag_Cr2_fe` `flag_Mn_fe` `flag_Co_fe` `flag_Ni_fe` `flag_Cu_fe` `flag_Zn_fe` `flag_Rb_fe` `flag_Sr_fe` `flag_Y_fe` `flag_Zr_fe` `flag_Mo_fe` `flag_Ru_fe` `flag_Ba_fe` `flag_La_fe` `flag_Ce_fe` `flag_Nd_fe` `flag_Sm_fe` `flag_Eu_fe` |
| `ind_X1234_fe`<br/><br/>Individual uncalibrated measurmenet of line/combo X1234 | `ind_Li6708_fe` `ind_Li6708_NoRV_fe` `ind_C6588_fe` `ind_O_fe` `ind_Na_fe` `ind_Mg5711_fe` `ind_Al_fe` `ind_Si_fe` `ind_K7699_fe` `ind_Ca_fe` `ind_Sc_fe` `ind_Ti4758_fe` `ind_Ti4759_fe` `ind_Ti4778_fe` `ind_Ti4782_fe` `ind_Ti4798_fe` `ind_Ti4802_fe` `ind_Ti4820_fe` `ind_Ti5689_fe` `ind_Ti5716_fe` `ind_Ti5720_fe` `ind_Ti5739_fe` `ind_Ti5866_fe` `ind_Ti6599_fe` `ind_Ti6717_fe` `ind_Ti7853_fe` `ind_Ti4720_fe` `ind_Ti4765_fe` `ind_Ti4799_fe` `ind_Ti4849_fe` `ind_Ti4866_fe` `ind_Ti4874_fe` `ind_V4832_fe` `ind_V4784_fe` `ind_V4797_fe` `ind_Cr_fe` `ind_Mn_fe` `ind_Co4781_fe` `ind_Co4900_fe` `ind_Co5647_fe` `ind_Co6490_fe` `ind_Co6551_fe` `ind_Co6632_fe` `ind_Co6679_fe` `ind_Co7713_fe` `ind_Co7838_fe` `ind_Ni5847_fe` `ind_Ni6586_fe` `ind_Cu5700_fe` `ind_Cu5782_fe` `ind_Zn4722_fe` `ind_Zn4811_fe` `ind_Rb7800_fe` `ind_Sr6550_fe` `ind_Y_fe` `ind_Y4820_fe` `ind_Y4855_fe` `ind_Y4884_fe` `ind_Y5663_fe` `ind_Y5729_fe` `ind_Zr4739_fe` `ind_Zr4772_fe` `ind_Zr4806_fe` `ind_Zr4828_fe` `ind_Zr5681_fe` `ind_Mo5689_fe` `ind_Mo5751_fe` `ind_Mo5858_fe` `ind_Mo6619_fe` `ind_Ru4758_fe` `ind_Ru4869_fe` `ind_Ru5699_fe` `ind_Ba_fe` `ind_La4716_fe` `ind_La4749_fe` `ind_La4804_fe` `ind_La5806_fe` `ind_Ce4774_fe` `ind_Nd4811_fe` `ind_Nd5741_fe` `ind_Nd5770_fe` `ind_Nd5812_fe` `ind_Nd5842_fe` `ind_Sm4720_fe` `ind_Sm4792_fe` `ind_Sm4837_fe` `ind_Sm4848_fe` `ind_Sm4854_fe` `ind_Eu5819_fe` `ind_Eu6645_fe` |
| `ind_cov_e_X1234`<br/><br/>SME covariance fitting uncertainty of `ind_X1234_fe` | `ind_cov_e_Li6708` `ind_cov_e_Li6708_NoRV` `ind_cov_e_C6588` `ind_cov_e_O` `ind_cov_e_Na` `ind_cov_e_Mg5711` `ind_cov_e_Al` `ind_cov_e_Si` `ind_cov_e_K7699` `ind_cov_e_Ca` `ind_cov_e_Sc` `ind_cov_e_Ti4758` `ind_cov_e_Ti4759` `ind_cov_e_Ti4778` `ind_cov_e_Ti4782` `ind_cov_e_Ti4798` `ind_cov_e_Ti4802` `ind_cov_e_Ti4820` `ind_cov_e_Ti5689` `ind_cov_e_Ti5716` `ind_cov_e_Ti5720` `ind_cov_e_Ti5739` `ind_cov_e_Ti5866` `ind_cov_e_Ti6599` `ind_cov_e_Ti6717` `ind_cov_e_Ti7853` `ind_cov_e_Ti4720` `ind_cov_e_Ti4765` `ind_cov_e_Ti4799` `ind_cov_e_Ti4849` `ind_cov_e_Ti4866` `ind_cov_e_Ti4874` `ind_cov_e_V4832` `ind_cov_e_V4784` `ind_cov_e_V4797` `ind_cov_e_Cr` `ind_cov_e_Mn` `ind_cov_e_Co4781` `ind_cov_e_Co4900` `ind_cov_e_Co5647` `ind_cov_e_Co6490` `ind_cov_e_Co6551` `ind_cov_e_Co6632` `ind_cov_e_Co6679` `ind_cov_e_Co7713` `ind_cov_e_Co7838` `ind_cov_e_Ni5847` `ind_cov_e_Ni6586` `ind_cov_e_Cu5700` `ind_cov_e_Cu5782` `ind_cov_e_Zn4722` `ind_cov_e_Zn4811` `ind_cov_e_Rb7800` `ind_cov_e_Sr6550` `ind_cov_e_Y` `ind_cov_e_Y4820` `ind_cov_e_Y4855` `ind_cov_e_Y4884` `ind_cov_e_Y5663` `ind_cov_e_Y5729` `ind_cov_e_Zr4739` `ind_cov_e_Zr4772` `ind_cov_e_Zr4806` `ind_cov_e_Zr4828` `ind_cov_e_Zr5681` `ind_cov_e_Mo5689` `ind_cov_e_Mo5751` `ind_cov_e_Mo5858` `ind_cov_e_Mo6619` `ind_cov_e_Ru4758` `ind_cov_e_Ru4869` `ind_cov_e_Ru5699` `ind_cov_e_Ba` `ind_cov_e_La4716` `ind_cov_e_La4749` `ind_cov_e_La4804` `ind_cov_e_La5806` `ind_cov_e_Ce4774` `ind_cov_e_Nd4811` `ind_cov_e_Nd5741` `ind_cov_e_Nd5770` `ind_cov_e_Nd5812` `ind_cov_e_Nd5842` `ind_cov_e_Sm4720` `ind_cov_e_Sm4792` `ind_cov_e_Sm4837` `ind_cov_e_Sm4848` `ind_cov_e_Sm4854` `ind_cov_e_Eu5819` `ind_cov_e_Eu6645` |
| `ind_flag_X1234`<br/><br/>[Quality flag fit for `ind_X1234_fe`](/dr3/flags/#ind_flag_x1234) | `ind_flag_Li6708` `ind_flag_Li6708_NoRV` `ind_flag_C6588` `ind_flag_O` `ind_flag_Na` `ind_flag_Mg5711` `ind_flag_Al` `ind_flag_Si` `ind_flag_K7699` `ind_flag_Ca` `ind_flag_Sc` `ind_flag_Ti4758` `ind_flag_Ti4759` `ind_flag_Ti4778` `ind_flag_Ti4782` `ind_flag_Ti4798` `ind_flag_Ti4802` `ind_flag_Ti4820` `ind_flag_Ti5689` `ind_flag_Ti5716` `ind_flag_Ti5720` `ind_flag_Ti5739` `ind_flag_Ti5866` `ind_flag_Ti6599` `ind_flag_Ti6717` `ind_flag_Ti7853` `ind_flag_Ti4720` `ind_flag_Ti4765` `ind_flag_Ti4799` `ind_flag_Ti4849` `ind_flag_Ti4866` `ind_flag_Ti4874` `ind_flag_V4832` `ind_flag_V4784` `ind_flag_V4797` `ind_flag_Cr` `ind_flag_Mn` `ind_flag_Co4781` `ind_flag_Co4900` `ind_flag_Co5647` `ind_flag_Co6490` `ind_flag_Co6551` `ind_flag_Co6632` `ind_flag_Co6679` `ind_flag_Co7713` `ind_flag_Co7838` `ind_flag_Ni5847` `ind_flag_Ni6586` `ind_flag_Cu5700` `ind_flag_Cu5782` `ind_flag_Zn4722` `ind_flag_Zn4811` `ind_flag_Rb7800` `ind_flag_Sr6550` `ind_flag_Y` `ind_flag_Y4820` `ind_flag_Y4855` `ind_flag_Y4884` `ind_flag_Y5663` `ind_flag_Y5729` `ind_flag_Zr4739` `ind_flag_Zr4772` `ind_flag_Zr4806` `ind_flag_Zr4828` `ind_flag_Zr5681` `ind_flag_Mo5689` `ind_flag_Mo5751` `ind_flag_Mo5858` `ind_flag_Mo6619` `ind_flag_Ru4758` `ind_flag_Ru4869` `ind_flag_Ru5699` `ind_flag_Ba` `ind_flag_La4716` `ind_flag_La4749` `ind_flag_La4804` `ind_flag_La5806` `ind_flag_Ce4774` `ind_flag_Nd4811` `ind_flag_Nd5741` `ind_flag_Nd5770` `ind_flag_Nd5812` `ind_flag_Nd5842` `ind_flag_Sm4720` `ind_flag_Sm4792` `ind_flag_Sm4837` `ind_flag_Sm4848` `ind_flag_Sm4854` `ind_flag_Eu5819` `ind_flag_Eu6645` |

---

### `VAC_ages`

| Column name | Description | units | type |
| :------ |:--- | :--- | :--- |
| `sobject_id` | GALAH identifier |  | integer |
| `age_bstep` | Age estimate BSTEP-Mod. | Gyr | float |
| `e_age_bstep` | 1-sigma uncertainty of `age_bstep` | Gyr | float |
| `e16_age_bstep` | 16 percentile value for `age_bstep` | Gyr | float |
| `e50_age_bstep` | 50 percentile value for `age_bstep` | Gyr | float |
| `e84_age_bstep` | 84 percentile value for `age_bstep` | Gyr | float |
| `m_act_bstep` | Actual stellar mass after mass loss BSTEP-Mod. | M<sub>&#9737;</sub> | float |
| `e_m_act_bstep` | 1-sigma uncertainty of `m_act_bstep` | M<sub>&#9737;</sub> | float |
| `e16_m_act_bstep` | 16 percentile value for `m_act_bstep` | M<sub>&#9737;</sub> | float |
| `e50_m_act_bstep` | 50 percentile value for `m_act_bstep` | M<sub>&#9737;</sub> | float |
| `e84_m_act_bstep` | 84 percentile value for `m_act_bstep` | M<sub>&#9737;</sub> | float |
| `m_ini_bstep` | Initial stellar mass BSTEP-Mod. | M<sub>&#9737;</sub> | float |
| `e_m_ini_bstep` | 1-sigma uncertainty of `m_ini_bstep` | M<sub>&#9737;</sub> | float |
| `e16_m_ini_bstep` | 16 percentile value for `m_ini_bstep` | M<sub>&#9737;</sub> | float |
| `e50_m_ini_bstep` | 50 percentile value for `m_ini_bstep` | M<sub>&#9737;</sub> | float |
| `e84_m_ini_bstep` | 84 percentile value for `m_ini_bstep` | M<sub>&#9737;</sub> | float |
| `radius_bstep` | Stellar Radius BSTEP-Mod. | R<sub>&#9737;</sub> | float |
| `e_radius_bstep` | 1-sigma uncertainty of `radius_bstep` | R<sub>&#9737;</sub> | float |
| `e16_radius_bstep` | 16 percentile value for `radius_bstep` | R<sub>&#9737;</sub> | float |
| `e50_radius_bstep` | 50 percentile value for `radius_bstep` | R<sub>&#9737;</sub> | float |
| `e84_radius_bstep` | 84 percentile value for `radius_bstep` | R<sub>&#9737;</sub> | float |
| `is_redclump_bstep` | Probability to be a red clump star (1.0) or not (0.0) BSTEP-Mod. |  | float |
| `e_is_redclump_bstep` | 1-sigma uncertainty of `is_redclump_bstep` |  | float |
| `e16_is_redclump_bstep` | 16 percentile value for `is_redclump_bstep` |  | float |
| `e50_is_redclump_bstep` | 50 percentile value for `is_redclump_bstep` |  | float |
| `e84_is_redclump_bstep` | 84 percentile value for `is_redclump_bstep` |  | float |
| `distance_bstep` | Distance BSTEP-Mod. | kpc | float |
| `e_distance_bstep` | 1-sigma uncertainty of `distance_bstep` | kpc | float |
| `e16_distance_bstep` | 16 percentile value for `distance_bstep` | kpc | float |
| `e50_distance_bstep` | 50 percentile value for `distance_bstep` | kpc | float |
| `e84_distance_bstep` | 84 percentile value for `distance_bstep` | kpc | float |
| `ebv_bstep` | Extinction E(B-V) BSTEP-Mod. | mag | float |
| `e_ebv_bstep` | 1-sigma uncertainty of `ebv_bstep` | mag | float |
| `e16_ebv_bstep` | 16 percentile value for `ebv_bstep` | mag | float |
| `e50_ebv_bstep` | 50 percentile value for `ebv_bstep` | mag | float |
| `e84_ebv_bstep` | 84 percentile value for `ebv_bstep` | mag | float |
| `teff_bstep` | Effective Temperature BSTEP-Mod. | K | float |
| `e_teff_bstep` | 1-sigma uncertainty of `teff_bstep` | K | float |
| `e16_teff_bstep` | 16 percentile value for `teff_bstep` | K | float |
| `e50_teff_bstep` | 50 percentile value for `teff_bstep` | K | float |
| `e84_teff_bstep` | 84 percentile value for `teff_bstep` | K | float |
| `logg_bstep` | Surface gravity BSTEP-Mod. | log(cm&#8239;s<sup>-2</sup>) | float |
| `e_logg_bstep` | 1-sigma uncertainty of `logg_bstep` | log(cm&#8239;s<sup>-2</sup>) | float |
| `e16_logg_bstep` | 16 percentile value for `logg_bstep` | log(cm&#8239;s<sup>-2</sup>) | float |
| `e50_logg_bstep` | 50 percentile value for `logg_bstep` | log(cm&#8239;s<sup>-2</sup>) | float |
| `e84_logg_bstep` | 84 percentile value for `logg_bstep` | log(cm&#8239;s<sup>-2</sup>) | float |
| `meh_act_bstep` | Surface effective [M/H] BSTEP-Mod. |  | float |
| `e_meh_act_bstep` | 1-sigma uncertainty of `meh_act_bstep` |  | float |
| `e16_meh_act_bstep` | 16 percentile value for `meh_act_bstep` |  | float |
| `e50_meh_act_bstep` | 50 percentile value for `meh_act_bstep` |  | float |
| `e84_meh_act_bstep` | 84 percentile value for `meh_act_bstep` |  | float |
| `meh_ini_bstep` | Intial effective metallicity [M/H] from isochrones BSTEP-Mod. |  | float |
| `e_meh_ini_bstep` | 1-sigma uncertainty of `meh_ini_bstep` |  | float |
| `e16_meh_ini_bstep` | 16 percentile value for `meh_ini_bstep` |  | float |
| `e50_meh_ini_bstep` | 50 percentile value for `meh_ini_bstep` |  | float |
| `e84_meh_ini_bstep` | 84 percentile value for `meh_ini_bstep` |  | float |
| `log_lum_bstep` | log(Luminosity L/L<sub>Sun</sub>) |  | float |
| `e_log_lum_bstep` | 1-sigma uncertainty of `log_lum_bstep` |  | float |
| `e16_log_lum_bstep` | 16 percentile value for `log_lum_bstep` |  | float |
| `e50_log_lum_bstep` | 50 percentile value for `log_lum_bstep` |  | float |
| `e84_log_lum_bstep` | 84 percentile value for `log_lum_bstep` |  | float |
| `abs_j_bstep` | Absolute Magnitude 2MASS J | mag | float |
| `e_abs_j_bstep` | 1-sigma uncertainty of `abs_j_bstep` | mag | float |
| `e16_abs_j_bstep` | 16 percentile value for `abs_j_bstep` | mag | float |
| `e50_abs_j_bstep` | 50 percentile value for `abs_j_bstep` | mag | float |
| `e84_abs_j_bstep` | 84 percentile value for `abs_j_bstep` | mag | float |
| `abs_ks_bstep` | Absolute Magnitude 2MASS K<sub>s</sub> | mag | float |
| `e_abs_ks_bstep` | 1-sigma uncertainty of `abs_ks_bstep` | mag | float |
| `e16_abs_ks_bstep` | 16 percentile value for `abs_ks_bstep` | mag | float |
| `e50_abs_ks_bstep` | 50 percentile value for `abs_ks_bstep` | mag | float |
| `e84_abs_ks_bstep` | 84 percentile value for `abs_ks_bstep` | mag | float |

---

### `VAC_dynamics`

| Column name | Description | units | type |
| :------ |:--- | :--- | :--- |
| `sobject_id` | GALAH identifier |  | integer |
| `use_dist_flag` | [Distance value was used in the Galactic orbit calculations](/dr3/flags/#use_dist_flag): 0: `distance_bstep`; 1: `r_med_photogeo`; 2: `r_med_geo`; 4: `parallax`; 8: No distance. |  | integer |
| `use_rv_flag` | [Radial velocity value has been used for `rv_galah`](/dr3/flags/#use_rv_flag): `rv_obst` (0), `rv_sme_v2` (1), Gaia DR2 (2) or n.a. (4) |  | integer |
| `X_XYZ` | Best-value heliocentric Galactic rectangular x-coordinate | kpc | float |
| `Y_XYZ` | Best-value heliocentric Galactic rectangular y-coordinate | kpc | float |
| `Z_XYZ` | Best-value heliocentric Galactic rectangular z-coordinate | kpc | float |
| `U_UVW` | Best-value heliocentric Galactic rectangular x-velocity | km&#8239;s<sup>-1</sup> | float |
| `V_UVW` | Best-value heliocentric Galactic rectangular y-velocity | km&#8239;s<sup>-1</sup> | float |
| `W_UVW` | Best-value heliocentric Galactic rectangular z-velocity | km&#8239;s<sup>-1</sup> | float |
| `R_Rzphi` | Best-value Galactocentric Radius | kpc | float |
| `phi_Rzphi` | Best-value Galactocentric azimuth | rad | float |
| `z_Rzphi` | Best-value Galactocentric height | kpc | float |
| `vR_Rzphi` | Best-value Galactocentric radial velocity | km&#8239;s<sup>-1</sup> | float |
| `vT_Rzphi` | Best-value Galactocentric tangential velocity | km&#8239;s<sup>-1</sup> | float |
| `vz_Rzphi` | Best-value Galactocentric vertical velocity | km&#8239;s<sup>-1</sup> | float |
| `J_R` | Best-value radial action | km&#8239;kpc&#8239;s<sup>-1</sup> | float |
| `L_Z` | Best-value azimuthal action / angular momentum | km&#8239;kpc&#8239;s<sup>-1</sup> | float |
| `J_Z` | Best-value vertical action | km&#8239;kpc&#8239;s<sup>-1</sup> | float |
| `omega_R` | Best-value radial orbit frequency | Gyr<sup>-1</sup> | float |
| `omega_phi` | Best-value azimuthal orbit frequency | Gyr<sup>-1</sup> | float |
| `omega_z` | Best-value vertical orbit frequency | Gyr<sup>-1</sup> | float |
| `angle_R` | Best-value radial orbit angle | rad | float |
| `angle_phi` | Best-value azimuthal orbit angle | rad | float |
| `angle_z` | Best-value vertical orbit angle | rad | float |
| `ecc` | Best-value orbit eccentricity |  | float |
| `zmax` | Best-value maximum Galactocentric height | kpc | float |
| `R_peri` | Best-value Galactocentric pericenter radius | kpc | float |
| `R_ap` | Best-value Galactocentric apocenter radius | kpc | float |
| `Energy` | Best-value orbit energy | km<sup>-2</sup>&#8239;s<sup>-2</sup> | float |
| `X_XYZ_5` | 5th Percentile MC heliocentric Galactic rectangular x-coordinate (`X_XYZ`) | kpc | float |
| `X_XYZ_50` | 50th Percentile MC heliocentric Galactic rectangular x-coordinate (`X_XYZ`) | kpc | float |
| `X_XYZ_95` | 95th Percentile MC heliocentric Galactic rectangular x-coordinate (`X_XYZ`) | kpc | float |
| `Y_XYZ_5` | 5th Percentile MC heliocentric Galactic rectangular y-coordinate (`Y_XYZ`) | kpc | float |
| `Y_XYZ_50` | 50th Percentile MC heliocentric Galactic rectangular y-coordinate (`Y_XYZ`) | kpc | float |
| `Y_XYZ_95` | 95th Percentile MC heliocentric Galactic rectangular y-coordinate (`Y_XYZ`) | kpc | float |
| `Z_XYZ_5` | 5th Percentile MC heliocentric Galactic rectangular z-coordinate (`Z_XYZ`) | kpc | float |
| `Z_XYZ_50` | 50th Percentile MC heliocentric Galactic rectangular z-coordinate (`Z_XYZ`) | kpc | float |
| `Z_XYZ_95` | 95th Percentile MC heliocentric Galactic rectangular z-coordinate (`Z_XYZ`) | kpc | float |
| `U_UVW_5` | 5th Percentile MC heliocentric Galactic rectangular x-velocity (`U_UVW`) | km&#8239;s<sup>-1</sup> | float |
| `U_UVW_50` | 50th Percentile MC heliocentric Galactic rectangular x-velocity (`U_UVW`) | km&#8239;s<sup>-1</sup> | float |
| `U_UVW_95` | 95th Percentile MC heliocentric Galactic rectangular x-velocity (`U_UVW`) | km&#8239;s<sup>-1</sup> | float |
| `V_UVW_5` | 5th Percentile MC heliocentric Galactic rectangular y-velocity (`V_UVW`) | km&#8239;s<sup>-1</sup> | float |
| `V_UVW_50` | 50th Percentile MC heliocentric Galactic rectangular y-velocity (`V_UVW`) | km&#8239;s<sup>-1</sup> | float |
| `V_UVW_95` | 95th Percentile MC heliocentric Galactic rectangular y-velocity (`V_UVW`) | km&#8239;s<sup>-1</sup> | float |
| `W_UVW_5` | 5th Percentile MC heliocentric Galactic rectangular z-velocity (`W_UVW`) | km&#8239;s<sup>-1</sup> | float |
| `W_UVW_50` | 50th Percentile MC heliocentric Galactic rectangular z-velocity (`W_UVW`) | km&#8239;s<sup>-1</sup> | float |
| `W_UVW_95` | 95th Percentile MC heliocentric Galactic rectangular z-velocity (`W_UVW`) | km&#8239;s<sup>-1</sup> | float |
| `R_Rzphi_5` | 5th Percentile MC Galactocentric Radius (`R_Rzphi`) | kpc | float |
| `R_Rzphi_50` | 50th Percentile MC Galactocentric Radius (`R_Rzphi`) | kpc | float |
| `R_Rzphi_95` | 95th Percentile MC Galactocentric Radius (`R_Rzphi`) | kpc | float |
| `phi_Rzphi_5` | 5th Percentile MC Galactocentric azimuth (`phi_Rzphi`) | rad | float |
| `phi_Rzphi_50` | 50th Percentile MC Galactocentric azimuth (`phi_Rzphi`) | rad | float |
| `phi_Rzphi_95` | 95th Percentile MC Galactocentric azimuth (`phi_Rzphi`) | rad | float |
| `z_Rzphi_5` | 5th Percentile MC Galactocentric height (`z_Rzphi`) | kpc | float |
| `z_Rzphi_50` | 50th Percentile MC Galactocentric height (`z_Rzphi`) | kpc | float |
| `z_Rzphi_95` | 95th Percentile MC Galactocentric height (`z_Rzphi`) | kpc | float |
| `vR_Rzphi_5` | 5th Percentile MC Galactocentric radial velocity (`vR_Rzphi`) | km&#8239;s<sup>-1</sup> | float |
| `vR_Rzphi_50` | 50th Percentile MC Galactocentric radial velocity (`vR_Rzphi`) | km&#8239;s<sup>-1</sup> | float |
| `vR_Rzphi_95` | 95th Percentile MC Galactocentric radial velocity (`vR_Rzphi`) | km&#8239;s<sup>-1</sup> | float |
| `vT_Rzphi_5` | 5th Percentile MC Galactocentric tangential velocity (`vT_Rzphi`) | km&#8239;s<sup>-1</sup> | float |
| `vT_Rzphi_50` | 50th Percentile MC Galactocentric tangential velocity (`vT_Rzphi`) | km&#8239;s<sup>-1</sup> | float |
| `vT_Rzphi_95` | 95th Percentile MC Galactocentric tangential velocity (`vT_Rzphi`) | km&#8239;s<sup>-1</sup> | float |
| `vz_Rzphi_5` | 5th Percentile MC Galactocentric vertical velocity (`vz_Rzphi`) | km&#8239;s<sup>-1</sup> | float |
| `vz_Rzphi_50` | 50th Percentile MC Galactocentric vertical velocity (`vz_Rzphi`) | km&#8239;s<sup>-1</sup> | float |
| `vz_Rzphi_95` | 95th Percentile MC Galactocentric vertical velocity (`vz_Rzphi`) | km&#8239;s<sup>-1</sup> | float |
| `J_R_5` | 5th Percentile MC radial action (`J_R`) | km&#8239;kpc&#8239;s<sup>-1</sup> | float |
| `J_R_50` | 50th Percentile MC radial action (`J_R`) | km&#8239;kpc&#8239;s<sup>-1</sup> | float |
| `J_R_95` | 95th Percentile MC radial action (`J_R`) | km&#8239;kpc&#8239;s<sup>-1</sup> | float |
| `L_Z_5` | 5th Percentile MC azimuthal action / angular momentum (`L_Z`) | km&#8239;kpc&#8239;s<sup>-1</sup> | float |
| `L_Z_50` | 50th Percentile MC azimuthal action / angular momentum (`L_Z`) | km&#8239;kpc&#8239;s<sup>-1</sup> | float |
| `L_Z_95` | 95th Percentile MC azimuthal action / angular momentum (`L_Z`) | km&#8239;kpc&#8239;s<sup>-1</sup> | float |
| `J_Z_5` | 5th Percentile MC vertical action (`J_Z`) | km&#8239;kpc&#8239;s<sup>-1</sup> | float |
| `J_Z_50` | 50th Percentile MC vertical action (`J_Z`) | km&#8239;kpc&#8239;s<sup>-1</sup> | float |
| `J_Z_95` | 95th Percentile MC vertical action (`J_Z`) | km&#8239;kpc&#8239;s<sup>-1</sup> | float |
| `omega_R_5` | 5th Percentile MC radial orbit frequency (`omega_R`) | Gyr<sup>-1</sup> | float |
| `omega_R_50` | 50th Percentile MC radial orbit frequency (`omega_R`) | Gyr<sup>-1</sup> | float |
| `omega_R_95` | 95th Percentile MC radial orbit frequency (`omega_R`) | Gyr<sup>-1</sup> | float |
| `omega_phi_5` | 5th Percentile MC azimuthal orbit frequency (`omega_phi`) | Gyr<sup>-1</sup> | float |
| `omega_phi_50` | 50th Percentile MC azimuthal orbit frequency (`omega_phi`) | Gyr<sup>-1</sup> | float |
| `omega_phi_95` | 95th Percentile MC azimuthal orbit frequency (`omega_phi`) | Gyr<sup>-1</sup> | float |
| `omega_z_5` | 5th Percentile MC vertical orbit frequency (`omega_z`) | Gyr<sup>-1</sup> | float |
| `omega_z_50` | 50th Percentile MC vertical orbit frequency (`omega_z`) | Gyr<sup>-1</sup> | float |
| `omega_z_95` | 95th Percentile MC vertical orbit frequency (`omega_z`) | Gyr<sup>-1</sup> | float |
| `angle_R_5` | 5th Percentile MC radial orbit angle (`angle_R`) | rad | float |
| `angle_R_50` | 50th Percentile MC radial orbit angle (`angle_R`) | rad | float |
| `angle_R_95` | 95th Percentile MC radial orbit angle (`angle_R`) | rad | float |
| `angle_phi_5` | 5th Percentile MC azimuthal orbit angle (`angle_phi`) | rad | float |
| `angle_phi_50` | 50th Percentile MC azimuthal orbit angle (`angle_phi`) | rad | float |
| `angle_phi_95` | 95th Percentile MC azimuthal orbit angle (`angle_phi`) | rad | float |
| `angle_z_5` | 5th Percentile MC vertical orbit angle (`angle_z`) | rad | float |
| `angle_z_50` | 50th Percentile MC vertical orbit angle (`angle_z`) | rad | float |
| `angle_z_95` | 95th Percentile MC vertical orbit angle (`angle_z`) | rad | float |
| `ecc_5` | 5th Percentile MC orbit eccentricity (`ecc`) |  | float |
| `ecc_50` | 50th Percentile MC orbit eccentricity (`ecc`) |  | float |
| `ecc_95` | 95th Percentile MC orbit eccentricity (`ecc`) |  | float |
| `zmax_5` | 5th Percentile MC maximum Galactocentric height (`zmax`) | kpc | float |
| `zmax_50` | 50th Percentile MC maximum Galactocentric height (`zmax`) | kpc | float |
| `zmax_95` | 95th Percentile MC maximum Galactocentric height (`zmax`) | kpc | float |
| `R_peri_5` | 5th Percentile MC Galactocentric pericenter radius (`R_peri`) | kpc | float |
| `R_peri_50` | 50th Percentile MC Galactocentric pericenter radius (`R_peri`) | kpc | float |
| `R_peri_95` | 95th Percentile MC Galactocentric pericenter radius (`R_peri`) | kpc | float |
| `R_ap_5` | 5th Percentile MC Galactocentric apocenter radius (`R_ap`) | kpc | float |
| `R_ap_50` | 50th Percentile MC Galactocentric apocenter radius (`R_ap`) | kpc | float |
| `R_ap_95` | 95th Percentile MC Galactocentric apocenter radius (`R_ap`) | kpc | float |
| `Energy_5` | 5th Percentile MC orbit energy (`Energy`) | km<sup>-2</sup>&#8239;s<sup>-2</sup> | float |
| `Energy_50` | 50th Percentile MC orbit energy (`Energy`) | km<sup>-2</sup>&#8239;s<sup>-2</sup> | float |
| `Energy_95` | 95th Percentile MC orbit energy (`Energy`) | km<sup>-2</sup>&#8239;s<sup>-2</sup> | float |

---

### `VAC_rv`

| Column name | Description | units | type |
| :------ |:--- | :--- | :--- |
| `sobject_id` | GALAH identifier |  | integer |
| `use_rv_flag` | [Radial velocity value has been used for `rv_galah`](/dr3/flags/#use_rv_flag): `rv_obst` (0), `rv_sme_v2` (1), Gaia DR2 (2) or n.a. (4) |  | integer |
| `rv_galah` | Best-method radial velocity from GALAH spectra | km&#8239;s<sup>-1</sup> | float |
| `e_rv_galah` | Uncertainty of `rv_galah` | km&#8239;s<sup>-1</sup> | float |
| `rv_sme_v2` | SME fitted radial velocity from GALAH spectra with correct `vbary` correction (`vbary_v2`) | km&#8239;s<sup>-1</sup> | float |
| `rv_sme_v1` | SME fitted radial velocity from GALAH spectra with wrong `vbary` correction (`vbary_v1`) | km&#8239;s<sup>-1</sup> | float |
| `e_rv_sme` | Uncertainty of `rv_sme_v2` | km&#8239;s<sup>-1</sup> | float |
| `cov_e_rv_sme` | SME covariance fitting uncertainty sme.vrad | km&#8239;s<sup>-1</sup> | float |
| `heliocentricJD` | Heliocentric Julian Date |  | float |
| `vbary_v1` | Wrong barycentric correction used for the original GALAH DR3 | km&#8239;s<sup>-1</sup> | float |
| `vbary_v2` | Correct barycentric correction used for the updated GALAH DR3 | km&#8239;s<sup>-1</sup> | float |
| `rv_obst` | Radial Velocity with gravitational redshift correction | km&#8239;s<sup>-1</sup> | float |
| `e_rv_obst` | Uncertainty of `rv_obst` | km&#8239;s<sup>-1</sup> | float |
| `rv_nogr_obst` | Radial Velocity without gravitational redshift correction | km&#8239;s<sup>-1</sup> | float |
| `e_rv_nogr_obst` | Uncertainty of `rv_nogr_obst` | km&#8239;s<sup>-1</sup> | float |
| `MJD_local` | Modified Julian Date at middle of exposure | d | float |
| `dr2_radial_velocity` | Radial velocity from Gaia DR2; identical to `rv_gaia_dr2` | km&#8239;s<sup>-1</sup> | float |
| `dr2_radial_velocity_error` | Radial velocity error from Gaia DR2; identical to `e_rv_gaia_dr2` | km&#8239;s<sup>-1</sup> | float |

---

### `VAC_GaiaEDR3`

Unless otherwise stated, all values are from [gaiaedr3.gaia_source](https://gea.esac.esa.int/archive/documentation/GEDR3/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html).

| Column name | Description | units | type |
| :------ |:--- | :--- | :--- |
| `star_id` | 2MASS identifier |  | string |
| `sobject_id` | GALAH identifier |  | integer |
| `dr2_source_id` | Gaia DR2 `source_id` |  | integer |
| `dr3_source_id` | Gaia DR3 `source_id` |  | integer |
| `angular_distance` | Angular distance between the two sources. Propagated from [edr3.dr2_neighbourhood](https://gea.esac.esa.int/archive/documentation/GEDR3/Gaia_archive/chap_datamodel/sec_dm_auxiliary_tables/ssec_dm_dr2_neighbourhood.html) | mas | float |
| `magnitude_difference` | G band magnitude difference between the sources. Propagated from [edr3.dr2_neighbourhood](https://gea.esac.esa.int/archive/documentation/GEDR3/Gaia_archive/chap_datamodel/sec_dm_auxiliary_tables/ssec_dm_dr2_neighbourhood.html) | mag | float |
| `proper_motion_propagation` | [Flag indicating whether E/DR3 coordinates were proper motion corrected](/dr3/flags/#flags-from-gaia-catalogues). Propagated from [edr3.dr2_neighbourhood](https://gea.esac.esa.int/archive/documentation/GEDR3/Gaia_archive/chap_datamodel/sec_dm_auxiliary_tables/ssec_dm_dr2_neighbourhood.html) |  | boolean |
| `solution_id` | Solution Identifier |  | integer |
| `designation` | Unique source designation (unique across all Data Releases) |  | string |
| `random_index` | Random index used to select subsets |  | integer |
| `ref_epoch` | Reference epoch | yr | float |
| `ra` | Right ascension | deg | float |
| `ra_error` | Standard error of right ascension | mas | float |
| `dec` | Declination | deg | float |
| `dec_error` | Standard error of declination | mas | float |
| `parallax` | Parallax | mas | float |
| `parallax_error` | Standard error of parallax | mas | float |
| `parallax_over_error` | Parallax divided by its standard error |  | float |
| `pm` | Total proper motion | mas&#8239;yr<sup>-1</sup> | float |
| `pmra` | Proper motion in right ascension direction | mas&#8239;yr<sup>-1</sup> | float |
| `pmra_error` | Standard error of proper motion in right ascension direction | mas&#8239;yr<sup>-1</sup> | float |
| `pmdec` | Proper motion in declination direction | mas&#8239;yr<sup>-1</sup> | float |
| `pmdec_error` | Standard error of proper motion in declination direction | mas&#8239;yr<sup>-1</sup> | float |
| `ra_dec_corr` | Correlation between right ascension and declination |  | float |
| `ra_parallax_corr` | Correlation between right ascension and parallax |  | float |
| `ra_pmra_corr` | Correlation between right ascension and proper motion in right ascension |  | float |
| `ra_pmdec_corr` | Correlation between right ascension and proper motion in declination |  | float |
| `dec_parallax_corr` | Correlation between declination and parallax |  | float |
| `dec_pmra_corr` | Correlation between declination and proper motion in right ascension |  | float |
| `dec_pmdec_corr` | Correlation between declination and proper motion in declination |  | float |
| `parallax_pmra_corr` | Correlation between parallax and proper motion in right ascension |  | float |
| `parallax_pmdec_corr` | Correlation between parallax and proper motion in declination |  | float |
| `pmra_pmdec_corr` | Correlation between proper motion in right ascension and proper motion in declination |  | float |
| `astrometric_n_obs_al` | Total number of observations AL |  | integer |
| `astrometric_n_obs_ac` | Total number of observations AC |  | integer |
| `astrometric_n_good_obs_al` | Number of good observations AL |  | integer |
| `astrometric_n_bad_obs_al` | Number of bad observations AL |  | integer |
| `astrometric_gof_al` | Goodness of fit statistic of model wrt along-scan observations |  | float |
| `astrometric_chi2_al` | AL χ-square value |  | float |
| `astrometric_excess_noise` | Excess noise of the source | mas | float |
| `astrometric_excess_noise_sig` | Significance of excess noise |  | float |
| `astrometric_params_solved` | Which parameters have been solved for? |  | integer |
| `astrometric_primary_flag` | Primary or seconday |  | boolean |
| `nu_eff_used_in_astrometry` | Effective wavenumber of the source used in the astrometric solution | um&#8239;s<sup>-1</sup> | float |
| `pseudocolour` | Astrometrically estimated pseudocolour of the source | um&#8239;s<sup>-1</sup> | float |
| `pseudocolour_error` | Standard error of the pseudocolour of the source | um&#8239;s<sup>-1</sup> | float |
| `ra_pseudocolour_corr` | Correlation between right ascension and pseudocolour |  | float |
| `dec_pseudocolour_corr` | Correlation between declination and pseudocolour |  | float |
| `parallax_pseudocolour_corr` | Correlation between parallax and pseudocolour |  | float |
| `pmra_pseudocolour_corr` | Correlation between proper motion in right asension and pseudocolour |  | float |
| `pmdec_pseudocolour_corr` | Correlation between proper motion in declination and pseudocolour |  | float |
| `astrometric_matched_transits` | Matched FOV transits used in the AGIS solution |  | integer |
| `visibility_periods_used` | Number of visibility periods used in Astrometric solution |  | integer |
| `astrometric_sigma5d_max` | The longest semi-major axis of the 5-d error ellipsoid | mas | float |
| `matched_transits` | The number of transits matched to this source |  | integer |
| `new_matched_transits` | The number of transits newly incorporated into an existing source in the current cycle |  | integer |
| `matched_transits_removed` | The number of transits removed from an existing source in the current cycle |  | integer |
| `ipd_gof_harmonic_amplitude` | Amplitude of the IPD GoF versus position angle of scan |  | float |
| `ipd_gof_harmonic_phase` | Phase of the IPD GoF versus position angle of scan | deg | float |
| `ipd_frac_multi_peak` | Percent of successful-IPD windows with more than one peak |  | integer |
| `ipd_frac_odd_win` | Percent of transits with truncated windows or multiple gate |  | integer |
| `ruwe` | Renormalised unit weight error |  | float |
| `scan_direction_strength_k1` | Degree of concentration of scan directions across the source |  | float |
| `scan_direction_strength_k2` | Degree of concentration of scan directions across the source |  | float |
| `scan_direction_strength_k3` | Degree of concentration of scan directions across the source |  | float |
| `scan_direction_strength_k4` | Degree of concentration of scan directions across the source |  | float |
| `scan_direction_mean_k1` | Mean position angle of scan directions across the source | deg | float |
| `scan_direction_mean_k2` | Mean position angle of scan directions across the source | deg | float |
| `scan_direction_mean_k3` | Mean position angle of scan directions across the source | deg | float |
| `scan_direction_mean_k4` | Mean position angle of scan directions across the source | deg | float |
| `duplicated_source` | Source with multiple source identifiers |  | boolean |
| `phot_g_n_obs` | Number of observations contributing to G photometry |  | integer |
| `phot_g_mean_flux` | G-band mean flux | electron&#8239;s<sup>-1</sup> | float |
| `phot_g_mean_flux_error` | Error on G-band mean flux | electron&#8239;s<sup>-1</sup> | float |
| `phot_g_mean_flux_over_error` | G-band mean flux divided by its error |  | float |
| `phot_g_mean_mag` | G-band mean magnitude | mag | float |
| `phot_bp_n_obs` | Number of observations contributing to BP photometry |  | integer |
| `phot_bp_mean_flux` | Integrated BP mean flux | electron&#8239;s<sup>-1</sup> | float |
| `phot_bp_mean_flux_error` | Error on the integrated BP mean flux | electron&#8239;s<sup>-1</sup> | float |
| `phot_bp_mean_flux_over_error` | Integrated BP mean flux divided by its error |  | float |
| `phot_bp_mean_mag` | Integrated BP mean magnitude | mag | float |
| `phot_rp_n_obs` | Number of observations contributing to RP photometry |  | integer |
| `phot_rp_mean_flux` | Integrated RP mean flux | electron&#8239;s<sup>-1</sup> | float |
| `phot_rp_mean_flux_error` | Error on the integrated RP mean flux | electron&#8239;s<sup>-1</sup> | float |
| `phot_rp_mean_flux_over_error` | Integrated RP mean flux divided by its error |  | float |
| `phot_rp_mean_mag` | Integrated RP mean magnitude | mag | float |
| `phot_bp_n_contaminated_transits` | Number of BP contaminated transits |  | integer |
| `phot_bp_n_blended_transits` | Number of BP blended transits |  | integer |
| `phot_rp_n_contaminated_transits` | Number of RP contaminated transits |  | integer |
| `phot_rp_n_blended_transits` | Number of RP blended transits |  | integer |
| `phot_proc_mode` | Photometry processing mode |  | integer |
| `phot_bp_rp_excess_factor` | BP/RP excess factor |  | float |
| `bp_rp` | BP - RP colour | mag | float |
| `bp_g` | BP - G colour | mag | float |
| `g_rp` | G - RP colour | mag | float |
| `dr2_radial_velocity` | Radial velocity from Gaia DR2; identical to `rv_gaia_dr2` | km&#8239;s<sup>-1</sup> | float |
| `dr2_radial_velocity_error` | Radial velocity error from Gaia DR2; identical to `e_rv_gaia_dr2` | km&#8239;s<sup>-1</sup> | float |
| `dr2_rv_nb_transits` | Number of transits used to compute radial velocity in Gaia DR2 |  | integer |
| `dr2_rv_template_teff` | T<sub>eff</sub> of the template used to compute radial velocity in Gaia DR2 | K | float |
| `dr2_rv_template_logg` | log*g* of the template used to compute radial velocity in Gaia DR2 | log(cm&#8239;s<sup>-2</sup>) | float |
| `dr2_rv_template_fe_h` | [Fe/H] of the template used to compute radial velocity in Gaia DR2 | dex | float |
| `l` | Galactic longitude | deg | float |
| `b` | Galactic latitude | deg | float |
| `ecl_lon` | Ecliptic longitude | deg | float |
| `ecl_lat` | Ecliptic latitude | deg | float |
| `zpt_ll2020` | Parallax Zeropoint following [Lindegren *et al.* (2020)](https://doi.org/10.1051/0004-6361/202039653) | mas | float |
| `parallax_corr` | `parallax` corrected by subtracting `zpt_ll2020` | mas | float |
| `r_med_geo` | The median of the geometric distance posterior. The geometric distance estimate. Propagated from [BJ+21](https://dc.zah.uni-heidelberg.de/tableinfo/gedr3dist.main). | pc | float |
| `r_lo_geo` | The 16th percentile of the geometric distance posterior. The lower 1-sigma-like bound on the confidence interval. Propagated from [BJ+21](https://dc.zah.uni-heidelberg.de/tableinfo/gedr3dist.main). | pc | float |
| `r_hi_geo` | The 84th percentile of the geometric distance posterior. The upper 1-sigma-like bound on the confidence interval. Propagated from [BJ+21](https://dc.zah.uni-heidelberg.de/tableinfo/gedr3dist.main). | pc | float |
| `r_med_photogeo` | The median of the photogeometric distance posterior. The photogeometric distance estimate. Propagated from [BJ+21](https://dc.zah.uni-heidelberg.de/tableinfo/gedr3dist.main). | pc | float |
| `r_lo_photogeo` | The 16th percentile of the photogeometric distance posterior. The lower 1-sigma-like bound on the confidence interval. Propagated from [BJ+21](https://dc.zah.uni-heidelberg.de/tableinfo/gedr3dist.main). | pc | float |
| `r_hi_photogeo` | The 84th percentile of the photogeometric distance posterior. The upper 1-sigma-like bound on the confidence interval. Propagated from [BJ+21](https://dc.zah.uni-heidelberg.de/tableinfo/gedr3dist.main). | pc | float |
| `flag_edr3dist` | Additional information on the solution. Do not use for filtering. Propagated from [BJ+21](https://dc.zah.uni-heidelberg.de/tableinfo/gedr3dist.main); original name `flag`.  |  | string |


### `GALAH_DR3_VAC_li_allstar_v2` and `GALAH_DR3_VAC_li_allspec_v2`

Both `GALAH_DR3_VAC_li_allstar_v2` and `GALAH_DR3_VAC_li_allspec_v2` share the same columns. 


| Column name | Description | units | type |
| :------ |:--- | :--- | :--- |
| `sobject_id` | Spectrum ID from GALAH DR3 |  | Integer |
| `star_id` | Star ID from GALAH DR3 |  | String |
| `fwhm_broad` | Width of the lines measured from broad region, NaN if poorly constrained | km&#8239;s<sup>-1</sup> | Float |
| `sigma_Li` | WWidth of the breidablik Li line, NaN if outside grid | km&#8239;s<sup>-1</sup> | Float |
| `vbroad_DR3` | Rotational broadening from GALAH DR3 (no instrumental profile) | km&#8239;s<sup>-1</sup> | Float |
| `delta_rv_6708` | Relative vrad compared to GALAH DR3 measured from the broad region, measured from Li region if poorly constrained | km&#8239;s<sup>-1</sup> | Float |
| `rv_DR3` | v$_{rad} from GALAH DR3 | km&#8239;s<sup>-1</sup> | Float |
| `EW` | Measured Li EW | m&#8491; | Float | 
| `e_EW_low` | Lower error in Li EW ($\sigma_{l}^{EW}$) | m&#8491; | Float | 
| `e_EW_upp` | Upper error in Li EW ($\sigma_{u}^{EW}$) | m&#8491; | Float | 
| `e_EW_norris` | Error using formula from Norris et al. (2001) | m&#8491; | Float | 
| `ALi` | 3D NLTE A(Li) detections | dex | Float | 
| `ALi_upp_lim` | 3D NLTE A(Li) upper limit corresponding to 2$\sigma_{l}^{EW}$ | dex | Float | 
| `e_ALi_low` | Lower error in A(Li) associated with $\sigma_{l}^{EW}$ | dex | Float | 
| `e_ALi_upp` | Upper error in A(Li) associated with $\sigma_{u}^{EW}$ | dex | Float | 
| `e_ALi_teff` | Error in A(Li) associated with $\sigma_{T_{eff}}$ | dex | Float | 
| `flag_ALi` | Bitmask flag for abundances and EW calculated in this catalogue |  | Integer | 
| `ALi_DR3` | 1D NLTE A(Li) detections and upper limits from GALAH DR3 | dex | Float | 
| `e_ALi_DR3` | $\sigma_{A(Li)}$ from GALAH DR3 | dex | Float | 
| `flag_ALi_DR3` | Bitmask flag for A(Li) from GALAH DR3 | dex | Integer | 
| `teff_DR3` | T$_{eff}$ from GALAH DR3 | K | Float |
| `e_teff_DR3` | $\sigma_{T_{eff}}$ from GALAH DR3 | K | Float |
| `logg_DR3` | log(g) from GALAH DR3 | log(cm&#8239;s<sup>-2</sup>) | Float |
| `e_logg_DR3` | $\sigma_{log(g)}$ from GALAH DR3 | log(cm&#8239;s<sup>-2</sup>) | Float |
| `flag_sp_DR3` | Bitmask flag for T$_{eff}$ and log(g) from GALAH DR3 |  | Int |
| `fe_h_DR3` | [Fe/H] from GALAH DR3 | dex | Float |
| `e_fe_h_DR3` | $\sigma_{[Fe/H]}$ from GALAH DR3 | dex | Float |
| `flag_fe_h_DR3` | Bitmask flag for metallicity from GALAH DR3 |  | Integer |
| `snr_DR3` | S/N of the spectra from GALAH DR3 |  | Float |
