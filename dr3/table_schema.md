---
layout: page
title: Table Schema
subtitle: Third Data Release
---

{: .main_blockquote}
This page gives a schema of the GALAH DR3 catalogues.

* This text gets replaced.
{:toc}

### GALAH DR3 catalogues table schema

For GALAH DR3, we have provided two versions of the [GALAH DR3 catalogue, and several value-added catalogues](/dr3/the_catalogues). The table below collates the available columns across all our catalogues into one table. It gives the catalogues that a given column is found within, and the description, unit, and data type of each column. To save space in the table below, the columns related to abundances have been collapsed in single entries (e.g., `X_fe`), and they are all listed in a table at the bottom of this page.

We strongly recommend also reading the [Recommended columns section of our Best Practices page](/dr3/using_the_data/#recommended-columns). This discusses how some parameters have different values in GALAH DR3 from different methods (e.g., for effective temperature there is `teff`, `irfm_teff`, `init_teff`, `teff_guess`; in this case we recommend `teff`.).

Some notes about the Table Schema of GALAH DR3:
* The `sobject_id` column is the only one found across all the tables, and should be used for joining the catalogues.
* For columns that are listed as being found in multiple catalogues, the same value will be found across all catalogues for a given `sobject_id` (e.g., for a given `sobject_id`, the same `teff` is found in `main_allstar` and `main_allspec`).
* `rv_gaia_dr2` and `dr2_radial_velocity` both refer to the Gaia DR2 radial velocity and are identical for a given `dr3_source_id`.
* Generally we do not recommend values found only in the `main_allspec` catalogue as these are only for expert and diagnostic purposes.

We have shortened the catalogue filenames to save space (i.e., removed the `GALAH_DR3_` and `_v2`).

| Column name | Found in these tables | Description | units | type |
| :------ |:--- | :--- | :--- | :--- |
| `sobject_id` | `main_allspec` `VAC_ages` `VAC_dynamics` `VAC_rv` `VAC_GaiaEDR3` `main_allstar` | GALAH identifier |  | integer |
| `star_id` | `main_allspec` `VAC_GaiaEDR3` `main_allstar` | 2MASS identifier |  | string |
| `dr2_source_id` | `main_allspec` `VAC_GaiaEDR3` `main_allstar` | Gaia DR2 `source_id` |  | integer |
| `dr3_source_id` | `main_allspec` `VAC_GaiaEDR3` `main_allstar` | Gaia DR3 `source_id` |  | integer |
| `survey_name` | `main_allspec` `main_allstar` | Name of survey as part of GALAH+DR3 |  | string |
| `field_id` | `main_allspec` `main_allstar` | GALAH fco field |  | integer |
| `flag_repeat` | `main_allspec` `main_allstar` | Repeat observation flag, indicating if used for clean catalog |  | integer |
| `wg4_field` | `main_allspec` `main_allstar` | GALAH WG4 field |  | string |
| `wg4_pipeline` | `main_allspec` `main_allstar` | SME pipeline version free/lbol/seis |  | string |
| `flag_sp` | `main_allspec` `main_allstar` | Stellar parameter quality flag |  | integer |
| `teff` | `main_allspec` `main_allstar` | Spectroscopic effective temperature (used for fitting) | K | float |
| `e_teff` | `main_allspec` `main_allstar` | Uncertainty `teff` | K | float |
| `irfm_teff` | `main_allspec` `main_allstar` | IRFM temperature (not used for synthesis) | K | float |
| `irfm_ebv` | `main_allspec` `main_allstar` | E(B-V) used for IRFM `teff` estimation | mag | float |
| `irfm_ebv_ref` | `main_allspec` `main_allstar` | Reference `irfm_ebv` |  | string |
| `cov_e_teff` | `main_allspec` | SME covariance fitting uncertainty `teff` | K | float |
| `init_teff` | `main_allspec` | SME initial `teff` | K | float |
| `logg` | `main_allspec` `main_allstar` | Surface gravity (not fitted via spectra if `wg4_pipeline` not free) | log(cm&#8239;s<sup>-2</sup>) | float |
| `e_logg` | `main_allspec` `main_allstar` | Uncertainty `logg` | log(cm&#8239;s<sup>-2</sup>) | float |
| `cov_e_logg` | `main_allspec` | MonteCarlo uncertainty `logg` | log(cm&#8239;s<sup>-2</sup>) | float |
| `init_logg` | `main_allspec` | SME initial `logg` | log(cm&#8239;s<sup>-2</sup>) | float |
| `fe_h` | `main_allspec` `main_allstar` | Fe atomic abundance from Fe lines (final, 1D-NLTE) |  | float |
| `e_fe_h` | `main_allspec` `main_allstar` | Uncertainty `fe_h` |  | float |
| `cov_e_fe_h` | `main_allspec` | SME covariance fitting uncertainty `fe_h` |  | float |
| `flag_fe_h` | `main_allspec` `main_allstar` | Quality flag `fe_h` |  | integer |
| `fe_h_atmo` | `main_allspec` `main_allstar` | sme.feh from stellar parameter run, fitted from H, Ti, Sc, Fe |  | float |
| `e_fe_h_atmo` | `main_allspec` | Uncertainty `fe_h_atmo` |  | float |
| `cov_e_fe_h_atmo` | `main_allspec` | SME covariance fitting uncertainty sme.feh |  | float |
| `init_fe_h_atmo` | `main_allspec` | SME initial sme.feh |  | float |
| `vmic` | `main_allspec` `main_allstar` | Microturbulence velocity (from empirical relation) | km&#8239;s<sup>-1</sup> | float |
| `vbroad` | `main_allspec` `main_allstar` | Broadening velocity (fitted sme.vsini with sme.vmac=0) | km&#8239;s<sup>-1</sup> | float |
| `e_vbroad` | `main_allspec` `main_allstar` | Uncertainty of `vbroad` | km&#8239;s<sup>-1</sup> | float |
| `cov_e_vbroad` | `main_allspec` | SME covariance fitting uncertainty sme.vsini | km&#8239;s<sup>-1</sup> | float |
| `init_vbroad` | `main_allspec` | SME initial broadening velocity | km&#8239;s<sup>-1</sup> | float |
| `mass` | `main_allspec` | Stellar parameter fitting product of stellar mass | solMass | float |
| `lbol` | `main_allspec` | Stellar parameter fitting product of bolometric luminosity | solLum | float |
| `age` | `main_allspec` | Stellar parameter fitting product of stellar age | Gyr | float |
| `chi2_sp` | `main_allspec` `main_allstar` | χ² value of stellar parameter fitting |  | float |
| `alpha_fe` | `main_allspec` `main_allstar` | Combined, weighted alpha-process element abundance |  | float |
| `e_alpha_fe` | `main_allspec` `main_allstar` | Uncertainty of `alpha_fe` |  | float |
| `nr_alpha_fe` | `main_allspec` `main_allstar` | Bitmask of used measurements for `alpha_fe` |  | float |
| `flag_alpha_fe` | `main_allspec` `main_allstar` | Quality flag of measurements for `alpha_fe` |  | integer |
| `flux_A_Fe` | `main_allspec` `main_allstar` | Normalised maximum absorption strength of in iron lines |  | float |
| `chi_A_Fe` | `main_allspec` `main_allstar` | χ² value of iron abundance fitting |  | float |
| `ind_X1234_fe` | `main_allspec` | Individual uncalibrated measurmenet of line/combo X1234 |  | float |
| `ind_cov_e_X1234` | `main_allspec` | SME covariance fitting uncertainty `ind_X1234_fe` |  | float |
| `ind_flag_X1234` | `main_allspec` | Quality flag fit for `ind_X1234_fe` |  | integer |
| `X_fe` | `main_allspec` `main_allstar` | Neutral/ionised X atomic abundance (final, 1D-LTE or NLTE) |  | float |
| `e_X_fe` | `main_allspec` `main_allstar` | Uncertainty `X_fe` |  | float |
| `nr_X_fe` | `main_allspec` `main_allstar` | Bitmask of used X ind lines |  | integer |
| `flag_X_fe` | `main_allspec` `main_allstar` | Quality flag of `X_fe` |  | integer |
| `ra_dr2` | `main_allspec` `main_allstar` | Right Ascension Gaia DR2 | deg | float |
| `dec_dr2` | `main_allspec` `main_allstar` | Declination Gaia DR2 | deg | float |
| `parallax_dr2` | `main_allspec` `main_allstar` | propagated from Gaia DR2 | mas | float |
| `parallax_error_dr2` | `main_allspec` `main_allstar` | propagated from Gaia DR2 | mas | float |
| `r_est_dr2` | `main_allspec` `main_allstar` | propagated from 2018AJ....156...58B | pc | float |
| `r_lo_dr2` | `main_allspec` `main_allstar` | propagated from 2018AJ....156...58B | pc | float |
| `r_hi_dr2` | `main_allspec` `main_allstar` | propagated from 2018AJ....156...58B | pc | float |
| `r_len_dr2` | `main_allspec` `main_allstar` | propagated from 2018AJ....156...58B | pc | float |
| `rv_galah` | `main_allspec` `VAC_rv` `main_allstar` | Best-method radial velocity from GALAH spectra |  | float |
| `e_rv_galah` | `main_allspec` `VAC_rv` `main_allstar` | Uncertainty of `rv_galah` |  | float |
| `rv_gaia_dr2` | `main_allspec` `main_allstar` | propagated from Gaia DR2; identical to `dr2_radial_velocity` | km&#8239;s<sup>-1</sup> | float |
| `e_rv_gaia_dr2` | `main_allspec` `main_allstar` | propagated from Gaia DR2; identical to `dr2_radial_velocity_error` | km&#8239;s<sup>-1</sup> | float |
| `red_flag` | `main_allspec` `main_allstar` | reduction pipeline quality flag |  | integer |
| `ebv` | `main_allspec` `main_allstar` | SFD extinction value | mag | float |
| `snr_c1_iraf` | `main_allspec` `main_allstar` | Average SNR/px CCD1 |  | float |
| `snr_c2_iraf` | `main_allspec` `main_allstar` | Average SNR/px CCD2 |  | float |
| `snr_c3_iraf` | `main_allspec` `main_allstar` | Average SNR/px CCD3 |  | float |
| `snr_c4_iraf` | `main_allspec` `main_allstar` | Average SNR/px CCD4 |  | float |
| `flag_guess` | `main_allspec` `main_allstar` | GUESS reduction pipeline quality flag |  | integer |
| `rv_guess` | `main_allspec` | Reduction pipeline best radial velocity | km&#8239;s<sup>-1</sup> | float |
| `e_rv_guess` | `main_allspec` | Reduction pipeline uncertainty radial velocity | km&#8239;s<sup>-1</sup> | float |
| `teff_guess` | `main_allspec` | Reduction pipeline best teff | K | float |
| `logg_guess` | `main_allspec` | Reduction pipeline best logg | log(cm&#8239;s<sup>-2</sup>) | float |
| `feh_guess` | `main_allspec` | Reduction pipeline best `fe_h` |  | float |
| `rv_5854` | `main_allspec` | Local best fit to RV when fitting A(Ba5854) | km&#8239;s<sup>-1</sup> | float |
| `rv_6708` | `main_allspec` | Local best fit to RV when fitting A(Li6708) | km&#8239;s<sup>-1</sup> | float |
| `rv_6722` | `main_allspec` | Local best fit to RV when fitting A(Si6722) | km&#8239;s<sup>-1</sup> | float |
| `v_jk` | `main_allspec` `main_allstar` | V magnitude estimated from 2MASS J and Ks mag | mag | float |
| `j_m` | `main_allspec` `main_allstar` | propagated from 2MASS | mag | float |
| `j_msigcom` | `main_allspec` `main_allstar` | propagated from 2MASS | mag | float |
| `h_m` | `main_allspec` `main_allstar` | propagated from 2MASS | mag | float |
| `h_msigcom` | `main_allspec` `main_allstar` | propagated from 2MASS | mag | float |
| `ks_m` | `main_allspec` `main_allstar` | propagated from 2MASS | mag | float |
| `ks_msigcom` | `main_allspec` `main_allstar` | propagated from 2MASS | mag | float |
| `ph_qual_tmass` | `main_allspec` `main_allstar` | propagated from 2MASS `ph_qual` |  | string |
| `w2mpro` | `main_allspec` `main_allstar` | propagated from AllWISE | mag | float |
| `w2mpro_error` | `main_allspec` `main_allstar` | propagated from AllWISE | mag | float |
| `ph_qual_wise` | `main_allspec` `main_allstar` | propagated from AllWISE `ph_qual` |  | string |
| `a_ks` | `main_allspec` `main_allstar` | Used Ks band extinction | mag | float |
| `e_a_ks` | `main_allspec` `main_allstar` | Uncertainty of `a_ks` | mag | float |
| `bc_ks` | `main_allspec` `main_allstar` | Used Bolometric Correction for Ks band | mag | float |
| `ruwe_dr2` | `main_allspec` `main_allstar` | propagated from Gaia DR2 |  | float |
| `age_bstep` | `VAC_ages` | Age estimate BSTEP-Mod. |  | float |
| `e_age_bstep` | `VAC_ages` | 1-sigma uncertainty of `age_bstep` |  | float |
| `e16_age_bstep` | `VAC_ages` | 16 percentile value for `age_bstep` |  | float |
| `e50_age_bstep` | `VAC_ages` | 50 percentile value for `age_bstep` |  | float |
| `e84_age_bstep` | `VAC_ages` | 84 percentile value for `age_bstep` |  | float |
| `m_act_bstep` | `VAC_ages` | Actual stellar mass after mass loss BSTEP-Mod. |  | float |
| `e_m_act_bstep` | `VAC_ages` | 1-sigma uncertainty of `m_act_bstep` |  | float |
| `e16_m_act_bstep` | `VAC_ages` | 16 percentile value for `m_act_bstep` |  | float |
| `e50_m_act_bstep` | `VAC_ages` | 50 percentile value for `m_act_bstep` |  | float |
| `e84_m_act_bstep` | `VAC_ages` | 84 percentile value for `m_act_bstep` |  | float |
| `m_ini_bstep` | `VAC_ages` | Initial stellar mass BSTEP-Mod. |  | float |
| `e_m_ini_bstep` | `VAC_ages` | 1-sigma uncertainty of `m_ini_bstep` |  | float |
| `e16_m_ini_bstep` | `VAC_ages` | 16 percentile value for `m_ini_bstep` |  | float |
| `e50_m_ini_bstep` | `VAC_ages` | 50 percentile value for `m_ini_bstep` |  | float |
| `e84_m_ini_bstep` | `VAC_ages` | 84 percentile value for `m_ini_bstep` |  | float |
| `radius_bstep` | `VAC_ages` | Stellar Radius BSTEP-Mod. |  | float |
| `e_radius_bstep` | `VAC_ages` | 1-sigma uncertainty of `radius_bstep` |  | float |
| `e16_radius_bstep` | `VAC_ages` | 16 percentile value for `radius_bstep` |  | float |
| `e50_radius_bstep` | `VAC_ages` | 50 percentile value for `radius_bstep` |  | float |
| `e84_radius_bstep` | `VAC_ages` | 84 percentile value for `radius_bstep` |  | float |
| `is_redclump_bstep` | `VAC_ages` | Probability to be a red clump star (1.0) or not (0.0) BSTEP-Mod. |  | float |
| `e_is_redclump_bstep` | `VAC_ages` | 1-sigma uncertainty of `is_redclump_bstep` |  | float |
| `e16_is_redclump_bstep` | `VAC_ages` | 16 percentile value for `is_redclump_bstep` |  | float |
| `e50_is_redclump_bstep` | `VAC_ages` | 50 percentile value for `is_redclump_bstep` |  | float |
| `e84_is_redclump_bstep` | `VAC_ages` | 84 percentile value for `is_redclump_bstep` |  | float |
| `distance_bstep` | `VAC_ages` | Distance BSTEP-Mod. |  | float |
| `e_distance_bstep` | `VAC_ages` | 1-sigma uncertainty of `distance_bstep` |  | float |
| `e16_distance_bstep` | `VAC_ages` | 16 percentile value for `distance_bstep` |  | float |
| `e50_distance_bstep` | `VAC_ages` | 50 percentile value for `distance_bstep` |  | float |
| `e84_distance_bstep` | `VAC_ages` | 84 percentile value for `distance_bstep` |  | float |
| `ebv_bstep` | `VAC_ages` | Extinction E(B-V) BSTEP-Mod. |  | float |
| `e_ebv_bstep` | `VAC_ages` | 1-sigma uncertainty of `ebv_bstep` |  | float |
| `e16_ebv_bstep` | `VAC_ages` | 16 percentile value for `ebv_bstep` |  | float |
| `e50_ebv_bstep` | `VAC_ages` | 50 percentile value for `ebv_bstep` |  | float |
| `e84_ebv_bstep` | `VAC_ages` | 84 percentile value for `ebv_bstep` |  | float |
| `teff_bstep` | `VAC_ages` | Effective Temperature BSTEP-Mod. |  | float |
| `e_teff_bstep` | `VAC_ages` | 1-sigma uncertainty of `teff_bstep` |  | float |
| `e16_teff_bstep` | `VAC_ages` | 16 percentile value for `teff_bstep` |  | float |
| `e50_teff_bstep` | `VAC_ages` | 50 percentile value for `teff_bstep` |  | float |
| `e84_teff_bstep` | `VAC_ages` | 84 percentile value for `teff_bstep` |  | float |
| `logg_bstep` | `VAC_ages` | Surface gravity BSTEP-Mod. |  | float |
| `e_logg_bstep` | `VAC_ages` | 1-sigma uncertainty of `logg_bstep` |  | float |
| `e16_logg_bstep` | `VAC_ages` | 16 percentile value for `logg_bstep` |  | float |
| `e50_logg_bstep` | `VAC_ages` | 50 percentile value for `logg_bstep` |  | float |
| `e84_logg_bstep` | `VAC_ages` | 84 percentile value for `logg_bstep` |  | float |
| `meh_act_bstep` | `VAC_ages` | Surface effective [M/H] BSTEP-Mod. |  | float |
| `e_meh_act_bstep` | `VAC_ages` | 1-sigma uncertainty of `meh_act_bstep` |  | float |
| `e16_meh_act_bstep` | `VAC_ages` | 16 percentile value for `meh_act_bstep` |  | float |
| `e50_meh_act_bstep` | `VAC_ages` | 50 percentile value for `meh_act_bstep` |  | float |
| `e84_meh_act_bstep` | `VAC_ages` | 84 percentile value for `meh_act_bstep` |  | float |
| `meh_ini_bstep` | `VAC_ages` | Intial effective metallicity [M/H] from isochrones BSTEP-Mod. |  | float |
| `e_meh_ini_bstep` | `VAC_ages` | 1-sigma uncertainty of `meh_ini_bstep` |  | float |
| `e16_meh_ini_bstep` | `VAC_ages` | 16 percentile value for `meh_ini_bstep` |  | float |
| `e50_meh_ini_bstep` | `VAC_ages` | 50 percentile value for `meh_ini_bstep` |  | float |
| `e84_meh_ini_bstep` | `VAC_ages` | 84 percentile value for `meh_ini_bstep` |  | float |
| `log_lum_bstep` | `VAC_ages` | log(Luminosity L/`L_sun`) |  | float |
| `e_log_lum_bstep` | `VAC_ages` | 1-sigma uncertainty of `log_lum_bstep` |  | float |
| `e16_log_lum_bstep` | `VAC_ages` | 16 percentile value for `log_lum_bstep` |  | float |
| `e50_log_lum_bstep` | `VAC_ages` | 50 percentile value for `log_lum_bstep` |  | float |
| `e84_log_lum_bstep` | `VAC_ages` | 84 percentile value for `log_lum_bstep` |  | float |
| `abs_j_bstep` | `VAC_ages` | Absolute Magnitude 2MASS J |  | float |
| `e_abs_j_bstep` | `VAC_ages` | 1-sigma uncertainty of `abs_j_bstep` |  | float |
| `e16_abs_j_bstep` | `VAC_ages` | 16 percentile value for `abs_j_bstep` |  | float |
| `e50_abs_j_bstep` | `VAC_ages` | 50 percentile value for `abs_j_bstep` |  | float |
| `e84_abs_j_bstep` | `VAC_ages` | 84 percentile value for `abs_j_bstep` |  | float |
| `abs_ks_bstep` | `VAC_ages` | Absolute Magnitude 2MASS Ks |  | float |
| `e_abs_ks_bstep` | `VAC_ages` | 1-sigma uncertainty of `abs_ks_bstep` |  | float |
| `e16_abs_ks_bstep` | `VAC_ages` | 16 percentile value for `abs_ks_bstep` |  | float |
| `e50_abs_ks_bstep` | `VAC_ages` | 50 percentile value for `abs_ks_bstep` |  | float |
| `e84_abs_ks_bstep` | `VAC_ages` | 84 percentile value for `abs_ks_bstep` |  | float |
| `use_dist_flag` | `VAC_dynamics` | Dist. Used: BSTEP(0), Photogeom.(1), Geom.(2), Plx(4), n.a.(8) |  | integer |
| `use_rv_flag` | `VAC_dynamics` `VAC_rv` | RV flag: `rv_obst` (0), `rv_sme_v2` (1), Gaia DR2 (2) or n.a. (4) |  | integer |
| `X_XYZ` | `VAC_dynamics` | Best-value heliocentric Galactic rectangular x-coordinate | kpc | float |
| `Y_XYZ` | `VAC_dynamics` | Best-value heliocentric Galactic rectangular y-coordinate | kpc | float |
| `Z_XYZ` | `VAC_dynamics` | Best-value heliocentric Galactic rectangular z-coordinate | kpc | float |
| `U_UVW` | `VAC_dynamics` | Best-value heliocentric Galactic rectangular x-velocity | km&#8239;s<sup>-1</sup> | float |
| `V_UVW` | `VAC_dynamics` | Best-value heliocentric Galactic rectangular y-velocity | km&#8239;s<sup>-1</sup> | float |
| `W_UVW` | `VAC_dynamics` | Best-value heliocentric Galactic rectangular z-velocity | km&#8239;s<sup>-1</sup> | float |
| `R_Rzphi` | `VAC_dynamics` | Best-value Galactocentric Radius | kpc | float |
| `phi_Rzphi` | `VAC_dynamics` | Best-value Galactocentric azimuth | rad | float |
| `z_Rzphi` | `VAC_dynamics` | Best-value Galactocentric height | kpc | float |
| `vR_Rzphi` | `VAC_dynamics` | Best-value Galactocentric radial velocity | km&#8239;s<sup>-1</sup> | float |
| `vT_Rzphi` | `VAC_dynamics` | Best-value Galactocentric tangential velocity | km&#8239;s<sup>-1</sup> | float |
| `vz_Rzphi` | `VAC_dynamics` | Best-value Galactocentric vertical velocity | km&#8239;s<sup>-1</sup> | float |
| `J_R` | `VAC_dynamics` | Best-value radial action | km&#8239;kpc&#8239;s<sup>-1</sup> | float |
| `L_Z` | `VAC_dynamics` | Best-value azimuthal action / angular momentum | km&#8239;kpc&#8239;s<sup>-1</sup> | float |
| `J_Z` | `VAC_dynamics` | Best-value vertical action | km&#8239;kpc&#8239;s<sup>-1</sup> | float |
| `omega_R` | `VAC_dynamics` | Best-value radial orbit frequency | Gyr<sup>-1</sup> | float |
| `omega_phi` | `VAC_dynamics` | Best-value azimuthal orbit frequency | Gyr<sup>-1</sup> | float |
| `omega_z` | `VAC_dynamics` | Best-value vertical orbit frequency | Gyr<sup>-1</sup> | float |
| `angle_R` | `VAC_dynamics` | Best-value radial orbit angle | rad | float |
| `angle_phi` | `VAC_dynamics` | Best-value azimuthal orbit angle | rad | float |
| `angle_z` | `VAC_dynamics` | Best-value vertical orbit angle | rad | float |
| `ecc` | `VAC_dynamics` | Best-value orbit eccentricity |  | float |
| `zmax` | `VAC_dynamics` | Best-value maximum Galactocentric height | kpc | float |
| `R_peri` | `VAC_dynamics` | Best-value Galactocentric pericenter radius | kpc | float |
| `R_ap` | `VAC_dynamics` | Best-value Galactocentric apocenter radius | kpc | float |
| `Energy` | `VAC_dynamics` | Best-value orbit energy | km<sup>-2</sup>&#8239;s<sup>-2</sup> | float |
| `X_XYZ_5` | `VAC_dynamics` | 5th Percentile MC heliocentric Galactic rectangular x-coordinate | kpc | float |
| `X_XYZ_50` | `VAC_dynamics` | 50th Percentile MC heliocentric Galactic rectangular x-coordinate | kpc | float |
| `X_XYZ_95` | `VAC_dynamics` | 95th Percentile MC heliocentric Galactic rectangular x-coordinate | kpc | float |
| `Y_XYZ_5` | `VAC_dynamics` | 5th Percentile MC heliocentric Galactic rectangular y-coordinate | kpc | float |
| `Y_XYZ_50` | `VAC_dynamics` | 50th Percentile MC heliocentric Galactic rectangular y-coordinate | kpc | float |
| `Y_XYZ_95` | `VAC_dynamics` | 95th Percentile MC heliocentric Galactic rectangular y-coordinate | kpc | float |
| `Z_XYZ_5` | `VAC_dynamics` | 5th Percentile MC heliocentric Galactic rectangular z-coordinate | kpc | float |
| `Z_XYZ_50` | `VAC_dynamics` | 50th Percentile MC heliocentric Galactic rectangular z-coordinate | kpc | float |
| `Z_XYZ_95` | `VAC_dynamics` | 95th Percentile MC heliocentric Galactic rectangular z-coordinate | kpc | float |
| `U_UVW_5` | `VAC_dynamics` | 5th Percentile MC heliocentric Galactic rectangular x-velocity | km&#8239;s<sup>-1</sup> | float |
| `U_UVW_50` | `VAC_dynamics` | 50th Percentile MC heliocentric Galactic rectangular x-velocity | km&#8239;s<sup>-1</sup> | float |
| `U_UVW_95` | `VAC_dynamics` | 95th Percentile MC heliocentric Galactic rectangular x-velocity | km&#8239;s<sup>-1</sup> | float |
| `V_UVW_5` | `VAC_dynamics` | 5th Percentile MC heliocentric Galactic rectangular y-velocity | km&#8239;s<sup>-1</sup> | float |
| `V_UVW_50` | `VAC_dynamics` | 50th Percentile MC heliocentric Galactic rectangular y-velocity | km&#8239;s<sup>-1</sup> | float |
| `V_UVW_95` | `VAC_dynamics` | 95th Percentile MC heliocentric Galactic rectangular y-velocity | km&#8239;s<sup>-1</sup> | float |
| `W_UVW_5` | `VAC_dynamics` | 5th Percentile MC heliocentric Galactic rectangular z-velocity | km&#8239;s<sup>-1</sup> | float |
| `W_UVW_50` | `VAC_dynamics` | 50th Percentile MC heliocentric Galactic rectangular z-velocity | km&#8239;s<sup>-1</sup> | float |
| `W_UVW_95` | `VAC_dynamics` | 95th Percentile MC heliocentric Galactic rectangular z-velocity | km&#8239;s<sup>-1</sup> | float |
| `R_Rzphi_5` | `VAC_dynamics` | 5th Percentile MC Galactocentric Radius | kpc | float |
| `R_Rzphi_50` | `VAC_dynamics` | 50th Percentile MC Galactocentric Radius | kpc | float |
| `R_Rzphi_95` | `VAC_dynamics` | 95th Percentile MC Galactocentric Radius | kpc | float |
| `phi_Rzphi_5` | `VAC_dynamics` | 5th Percentile MC Galactocentric azimuth | rad | float |
| `phi_Rzphi_50` | `VAC_dynamics` | 50th Percentile MC Galactocentric azimuth | rad | float |
| `phi_Rzphi_95` | `VAC_dynamics` | 95th Percentile MC Galactocentric azimuth | rad | float |
| `z_Rzphi_5` | `VAC_dynamics` | 5th Percentile MC Galactocentric height | kpc | float |
| `z_Rzphi_50` | `VAC_dynamics` | 50th Percentile MC Galactocentric height | kpc | float |
| `z_Rzphi_95` | `VAC_dynamics` | 95th Percentile MC Galactocentric height | kpc | float |
| `vR_Rzphi_5` | `VAC_dynamics` | 5th Percentile MC Galactocentric radial velocity | km&#8239;s<sup>-1</sup> | float |
| `vR_Rzphi_50` | `VAC_dynamics` | 50th Percentile MC Galactocentric radial velocity | km&#8239;s<sup>-1</sup> | float |
| `vR_Rzphi_95` | `VAC_dynamics` | 95th Percentile MC Galactocentric radial velocity | km&#8239;s<sup>-1</sup> | float |
| `vT_Rzphi_5` | `VAC_dynamics` | 5th Percentile MC Galactocentric tangential velocity | km&#8239;s<sup>-1</sup> | float |
| `vT_Rzphi_50` | `VAC_dynamics` | 50th Percentile MC Galactocentric tangential velocity | km&#8239;s<sup>-1</sup> | float |
| `vT_Rzphi_95` | `VAC_dynamics` | 95th Percentile MC Galactocentric tangential velocity | km&#8239;s<sup>-1</sup> | float |
| `vz_Rzphi_5` | `VAC_dynamics` | 5th Percentile MC Galactocentric vertical velocity | km&#8239;s<sup>-1</sup> | float |
| `vz_Rzphi_50` | `VAC_dynamics` | 50th Percentile MC Galactocentric vertical velocity | km&#8239;s<sup>-1</sup> | float |
| `vz_Rzphi_95` | `VAC_dynamics` | 95th Percentile MC Galactocentric vertical velocity | km&#8239;s<sup>-1</sup> | float |
| `J_R_5` | `VAC_dynamics` | 5th Percentile MC radial action | km&#8239;kpc&#8239;s<sup>-1</sup> | float |
| `J_R_50` | `VAC_dynamics` | 50th Percentile MC radial action | km&#8239;kpc&#8239;s<sup>-1</sup> | float |
| `J_R_95` | `VAC_dynamics` | 95th Percentile MC radial action | km&#8239;kpc&#8239;s<sup>-1</sup> | float |
| `L_Z_5` | `VAC_dynamics` | 5th Percentile MC azimuthal action / angular momentum | km&#8239;kpc&#8239;s<sup>-1</sup> | float |
| `L_Z_50` | `VAC_dynamics` | 50th Percentile MC azimuthal action / angular momentum | km&#8239;kpc&#8239;s<sup>-1</sup> | float |
| `L_Z_95` | `VAC_dynamics` | 95th Percentile MC azimuthal action / angular momentum | km&#8239;kpc&#8239;s<sup>-1</sup> | float |
| `J_Z_5` | `VAC_dynamics` | 5th Percentile MC vertical action | km&#8239;kpc&#8239;s<sup>-1</sup> | float |
| `J_Z_50` | `VAC_dynamics` | 50th Percentile MC vertical action | km&#8239;kpc&#8239;s<sup>-1</sup> | float |
| `J_Z_95` | `VAC_dynamics` | 95th Percentile MC vertical action | km&#8239;kpc&#8239;s<sup>-1</sup> | float |
| `omega_R_5` | `VAC_dynamics` | 5th Percentile MC radial orbit frequency | Gyr<sup>-1</sup> | float |
| `omega_R_50` | `VAC_dynamics` | 50th Percentile MC radial orbit frequency | Gyr<sup>-1</sup> | float |
| `omega_R_95` | `VAC_dynamics` | 95th Percentile MC radial orbit frequency | Gyr<sup>-1</sup> | float |
| `omega_phi_5` | `VAC_dynamics` | 5th Percentile MC azimuthal orbit frequency | Gyr<sup>-1</sup> | float |
| `omega_phi_50` | `VAC_dynamics` | 50th Percentile MC azimuthal orbit frequency | Gyr<sup>-1</sup> | float |
| `omega_phi_95` | `VAC_dynamics` | 95th Percentile MC azimuthal orbit frequency | Gyr<sup>-1</sup> | float |
| `omega_z_5` | `VAC_dynamics` | 5th Percentile MC vertical orbit frequency | Gyr<sup>-1</sup> | float |
| `omega_z_50` | `VAC_dynamics` | 50th Percentile MC vertical orbit frequency | Gyr<sup>-1</sup> | float |
| `omega_z_95` | `VAC_dynamics` | 95th Percentile MC vertical orbit frequency | Gyr<sup>-1</sup> | float |
| `angle_R_5` | `VAC_dynamics` | 5th Percentile MC radial orbit angle | rad | float |
| `angle_R_50` | `VAC_dynamics` | 50th Percentile MC radial orbit angle | rad | float |
| `angle_R_95` | `VAC_dynamics` | 95th Percentile MC radial orbit angle | rad | float |
| `angle_phi_5` | `VAC_dynamics` | 5th Percentile MC azimuthal orbit angle | rad | float |
| `angle_phi_50` | `VAC_dynamics` | 50th Percentile MC azimuthal orbit angle | rad | float |
| `angle_phi_95` | `VAC_dynamics` | 95th Percentile MC azimuthal orbit angle | rad | float |
| `angle_z_5` | `VAC_dynamics` | 5th Percentile MC vertical orbit angle | rad | float |
| `angle_z_50` | `VAC_dynamics` | 50th Percentile MC vertical orbit angle | rad | float |
| `angle_z_95` | `VAC_dynamics` | 95th Percentile MC vertical orbit angle | rad | float |
| `ecc_5` | `VAC_dynamics` | 5th Percentile MC orbit eccentricity |  | float |
| `ecc_50` | `VAC_dynamics` | 50th Percentile MC orbit eccentricity |  | float |
| `ecc_95` | `VAC_dynamics` | 95th Percentile MC orbit eccentricity |  | float |
| `zmax_5` | `VAC_dynamics` | 5th Percentile MC maximum Galactocentric height | kpc | float |
| `zmax_50` | `VAC_dynamics` | 50th Percentile MC maximum Galactocentric height | kpc | float |
| `zmax_95` | `VAC_dynamics` | 95th Percentile MC maximum Galactocentric height | kpc | float |
| `R_peri_5` | `VAC_dynamics` | 5th Percentile MC Galactocentric pericenter radius | kpc | float |
| `R_peri_50` | `VAC_dynamics` | 50th Percentile MC Galactocentric pericenter radius | kpc | float |
| `R_peri_95` | `VAC_dynamics` | 95th Percentile MC Galactocentric pericenter radius | kpc | float |
| `R_ap_5` | `VAC_dynamics` | 5th Percentile MC Galactocentric apocenter radius | kpc | float |
| `R_ap_50` | `VAC_dynamics` | 50th Percentile MC Galactocentric apocenter radius | kpc | float |
| `R_ap_95` | `VAC_dynamics` | 95th Percentile MC Galactocentric apocenter radius | kpc | float |
| `Energy_5` | `VAC_dynamics` | 5th Percentile MC orbit energy | km<sup>-2</sup>&#8239;s<sup>-2</sup> | float |
| `Energy_50` | `VAC_dynamics` | 50th Percentile MC orbit energy | km<sup>-2</sup>&#8239;s<sup>-2</sup> | float |
| `Energy_95` | `VAC_dynamics` | 95th Percentile MC orbit energy | km<sup>-2</sup>&#8239;s<sup>-2</sup> | float |
| `rv_sme_v2` | `VAC_rv` | SME fitted radial velocity from GALAH spectra with correct vbary correction (`vbary_v2`) |  | float |
| `rv_sme_v1` | `VAC_rv` | SME fitted radial velocity from GALAH spectra with wrong vbary correction (`vbary_v1`) |  | float |
| `e_rv_sme` | `VAC_rv` | Uncertainty of `rv_sme_v2` |  | float |
| `cov_e_rv_sme` | `VAC_rv` | SME covariance fitting uncertainty sme.vrad | km&#8239;s<sup>-1</sup> | float |
| `heliocentricJD` | `VAC_rv` | Heliocentric Julian Date |  | float |
| `vbary_v1` | `VAC_rv` | Wrong barycentric correction used for v1 |  | float |
| `vbary_v2` | `VAC_rv` | Correct barycentric correction used for v2 |  | float |
| `rv_obst` | `VAC_rv` | Radial Velocity with grav. redshift correction | km&#8239;s<sup>-1</sup> | float |
| `e_rv_obst` | `VAC_rv` | Uncertainty of `rv_obst` | km&#8239;s<sup>-1</sup> | float |
| `rv_nogr_obst` | `VAC_rv` | Radial Velocity without grav. redshift correction | km&#8239;s<sup>-1</sup> | float |
| `e_rv_nogr_obst` | `VAC_rv` | Uncertainty of `rv_nogr_obst` | km&#8239;s<sup>-1</sup> | float |
| `MJD_local` | `VAC_rv` | Modified Julian Date, Middle of Exposure | d | float |
| `dr2_radial_velocity` | `VAC_rv` `VAC_GaiaEDR3` | Radial velocity from Gaia DR2; identical to `rv_gaia_dr2` | km&#8239;s<sup>-1</sup> | float |
| <small>`dr2_radial_velocity_error`</small> | `VAC_rv` `VAC_GaiaEDR3` | Radial velocity error from Gaia DR2; identical to `e_rv_gaia_dr2` | km&#8239;s<sup>-1</sup> | float |
| `angular_distance` | `VAC_GaiaEDR3` | Angular distance between the two sources | mas | float |
| `magnitude_difference` | `VAC_GaiaEDR3` | G band magnitude difference between the sources | mag | float |
| <small>`proper_motion_propagation`</small> | `VAC_GaiaEDR3` | Flag indicating whether E/DR3 coordinates were proper motion corrected |  | boolean |
| `solution_id` | `VAC_GaiaEDR3` | Solution Identifier |  | integer |
| `designation` | `VAC_GaiaEDR3` | Unique source designation (unique across all Data Releases) |  | string |
| `random_index` | `VAC_GaiaEDR3` | Random index used to select subsets |  | integer |
| `ref_epoch` | `VAC_GaiaEDR3` | Reference epoch | yr | float |
| `ra` | `VAC_GaiaEDR3` | Right ascension | deg | float |
| `ra_error` | `VAC_GaiaEDR3` | Standard error of right ascension | mas | float |
| `dec` | `VAC_GaiaEDR3` | Declination | deg | float |
| `dec_error` | `VAC_GaiaEDR3` | Standard error of declination | mas | float |
| `parallax` | `VAC_GaiaEDR3` | Parallax | mas | float |
| `parallax_error` | `VAC_GaiaEDR3` | Standard error of parallax | mas | float |
| `parallax_over_error` | `VAC_GaiaEDR3` | Parallax divided by its standard error |  | float |
| `pm` | `VAC_GaiaEDR3` | Total proper motion | mas&#8239;yr<sup>-1</sup> | float |
| `pmra` | `VAC_GaiaEDR3` | Proper motion in right ascension direction | mas&#8239;yr<sup>-1</sup> | float |
| `pmra_error` | `VAC_GaiaEDR3` | Standard error of proper motion in right ascension direction | mas&#8239;yr<sup>-1</sup> | float |
| `pmdec` | `VAC_GaiaEDR3` | Proper motion in declination direction | mas&#8239;yr<sup>-1</sup> | float |
| `pmdec_error` | `VAC_GaiaEDR3` | Standard error of proper motion in declination direction | mas&#8239;yr<sup>-1</sup> | float |
| `ra_dec_corr` | `VAC_GaiaEDR3` | Correlation between right ascension and declination |  | float |
| `ra_parallax_corr` | `VAC_GaiaEDR3` | Correlation between right ascension and parallax |  | float |
| `ra_pmra_corr` | `VAC_GaiaEDR3` | Correlation between right ascension and proper motion in right ascension |  | float |
| `ra_pmdec_corr` | `VAC_GaiaEDR3` | Correlation between right ascension and proper motion in declination |  | float |
| `dec_parallax_corr` | `VAC_GaiaEDR3` | Correlation between declination and parallax |  | float |
| `dec_pmra_corr` | `VAC_GaiaEDR3` | Correlation between declination and proper motion in right ascension |  | float |
| `dec_pmdec_corr` | `VAC_GaiaEDR3` | Correlation between declination and proper motion in declination |  | float |
| `parallax_pmra_corr` | `VAC_GaiaEDR3` | Correlation between parallax and proper motion in right ascension |  | float |
| `parallax_pmdec_corr` | `VAC_GaiaEDR3` | Correlation between parallax and proper motion in declination |  | float |
| `pmra_pmdec_corr` | `VAC_GaiaEDR3` | Correlation between proper motion in right ascension and proper motion in declination |  | float |
| `astrometric_n_obs_al` | `VAC_GaiaEDR3` | Total number of observations AL |  | integer |
| `astrometric_n_obs_ac` | `VAC_GaiaEDR3` | Total number of observations AC |  | integer |
| <small>`astrometric_n_good_obs_al`</small> | `VAC_GaiaEDR3` | Number of good observations AL |  | integer |
| <small>`astrometric_n_bad_obs_al`</small> | `VAC_GaiaEDR3` | Number of bad observations AL |  | integer |
| `astrometric_gof_al` | `VAC_GaiaEDR3` | Goodness of fit statistic of model wrt along-scan observations |  | float |
| `astrometric_chi2_al` | `VAC_GaiaEDR3` | AL χ-square value |  | float |
| <small>`astrometric_excess_noise`</small> | `VAC_GaiaEDR3` | Excess noise of the source | mas | float |
| <small>`astrometric_excess_noise_sig`</small> | `VAC_GaiaEDR3` | Significance of excess noise |  | float |
| <small>`astrometric_params_solved`</small> | `VAC_GaiaEDR3` | Which parameters have been solved for? |  | integer |
| <small>`astrometric_primary_flag`</small> | `VAC_GaiaEDR3` | Primary or seconday |  | boolean |
| <small>`nu_eff_used_in_astrometry`</small> | `VAC_GaiaEDR3` | Effective wavenumber of the source used in the astrometric solution | um-1 | float |
| `pseudocolour` | `VAC_GaiaEDR3` | Astrometrically estimated pseudocolour of the source | um-1 | float |
| `pseudocolour_error` | `VAC_GaiaEDR3` | Standard error of the pseudocolour of the source | um-1 | float |
| `ra_pseudocolour_corr` | `VAC_GaiaEDR3` | Correlation between right ascension and pseudocolour |  | float |
| `dec_pseudocolour_corr` | `VAC_GaiaEDR3` | Correlation between declination and pseudocolour |  | float |
| <small>`parallax_pseudocolour_corr`</small> | `VAC_GaiaEDR3` | Correlation between parallax and pseudocolour |  | float |
| `pmra_pseudocolour_corr` | `VAC_GaiaEDR3` | Correlation between proper motion in right asension and pseudocolour |  | float |
| <small>`pmdec_pseudocolour_corr`</small> | `VAC_GaiaEDR3` | Correlation between proper motion in declination and pseudocolour |  | float |
| <small>`astrometric_matched_transits`</small> | `VAC_GaiaEDR3` | Matched FOV transits used in the AGIS solution |  | integer |
| <small>`visibility_periods_used`</small> | `VAC_GaiaEDR3` | Number of visibility periods used in Astrometric solution |  | integer |
| <small>`astrometric_sigma5d_max`</small> | `VAC_GaiaEDR3` | The longest semi-major axis of the 5-d error ellipsoid | mas | float |
| `matched_transits` | `VAC_GaiaEDR3` | The number of transits matched to this source |  | integer |
| `new_matched_transits` | `VAC_GaiaEDR3` | The number of transits newly incorporated into an existing source in the current cycle |  | integer |
| <small>`matched_transits_removed`</small> | `VAC_GaiaEDR3` | The number of transits removed from an existing source in the current cycle |  | integer |
| <small>`ipd_gof_harmonic_amplitude`</small> | `VAC_GaiaEDR3` | Amplitude of the IPD GoF versus position angle of scan |  | float |
| `ipd_gof_harmonic_phase` | `VAC_GaiaEDR3` | Phase of the IPD GoF versus position angle of scan | deg | float |
| `ipd_frac_multi_peak` | `VAC_GaiaEDR3` | Percent of successful-IPD windows with more than one peak |  | integer |
| `ipd_frac_odd_win` | `VAC_GaiaEDR3` | Percent of transits with truncated windows or multiple gate |  | integer |
| `ruwe` | `VAC_GaiaEDR3` | Renormalised unit weight error |  | float |
| <small>`scan_direction_strength_k1`</small> | `VAC_GaiaEDR3` | Degree of concentration of scan directions across the source |  | float |
| <small>`scan_direction_strength_k2`</small> | `VAC_GaiaEDR3` | Degree of concentration of scan directions across the source |  | float |
| <small>`scan_direction_strength_k3`</small> | `VAC_GaiaEDR3` | Degree of concentration of scan directions across the source |  | float |
| <small>`scan_direction_strength_k4`</small> | `VAC_GaiaEDR3` | Degree of concentration of scan directions across the source |  | float |
| `scan_direction_mean_k1` | `VAC_GaiaEDR3` | Mean position angle of scan directions across the source | deg | float |
| `scan_direction_mean_k2` | `VAC_GaiaEDR3` | Mean position angle of scan directions across the source | deg | float |
| `scan_direction_mean_k3` | `VAC_GaiaEDR3` | Mean position angle of scan directions across the source | deg | float |
| `scan_direction_mean_k4` | `VAC_GaiaEDR3` | Mean position angle of scan directions across the source | deg | float |
| `duplicated_source` | `VAC_GaiaEDR3` | Source with multiple source identifiers |  | boolean |
| `phot_g_n_obs` | `VAC_GaiaEDR3` | Number of observations contributing to G photometry |  | integer |
| `phot_g_mean_flux` | `VAC_GaiaEDR3` | G-band mean flux | electron&#8239;s<sup>-1</sup> | float |
| `phot_g_mean_flux_error` | `VAC_GaiaEDR3` | Error on G-band mean flux | electron&#8239;s<sup>-1</sup> | float |
| <small>`phot_g_mean_flux_over_error`</small> | `VAC_GaiaEDR3` | G-band mean flux divided by its error |  | float |
| `phot_g_mean_mag` | `VAC_GaiaEDR3` | G-band mean magnitude | mag | float |
| `phot_bp_n_obs` | `VAC_GaiaEDR3` | Number of observations contributing to BP photometry |  | integer |
| `phot_bp_mean_flux` | `VAC_GaiaEDR3` | Integrated BP mean flux | electron&#8239;s<sup>-1</sup> | float |
| <small>`phot_bp_mean_flux_error`</small> | `VAC_GaiaEDR3` | Error on the integrated BP mean flux | electron&#8239;s<sup>-1</sup> | float |
| <small>`phot_bp_mean_flux_over_error`</small> | `VAC_GaiaEDR3` | Integrated BP mean flux divided by its error |  | float |
| `phot_bp_mean_mag` | `VAC_GaiaEDR3` | Integrated BP mean magnitude | mag | float |
| `phot_rp_n_obs` | `VAC_GaiaEDR3` | Number of observations contributing to RP photometry |  | integer |
| `phot_rp_mean_flux` | `VAC_GaiaEDR3` | Integrated RP mean flux | electron&#8239;s<sup>-1</sup> | float |
| <small>`phot_rp_mean_flux_error`</small> | `VAC_GaiaEDR3` | Error on the integrated RP mean flux | electron&#8239;s<sup>-1</sup> | float |
| <small>`phot_rp_mean_flux_over_error`</small> | `VAC_GaiaEDR3` | Integrated RP mean flux divided by its error |  | float |
| `phot_rp_mean_mag` | `VAC_GaiaEDR3` | Integrated RP mean magnitude | mag | float |
| <small>`phot_bp_n_contaminated_transits`</small> | `VAC_GaiaEDR3` | Number of BP contaminated transits |  | integer |
| <small>`phot_bp_n_blended_transits`</small> | `VAC_GaiaEDR3` | Number of BP blended transits |  | integer |
| <small>`phot_rp_n_contaminated_transits`</small> | `VAC_GaiaEDR3` | Number of RP contaminated transits |  | integer |
| <small>`phot_rp_n_blended_transits`</small> | `VAC_GaiaEDR3` | Number of RP blended transits |  | integer |
| `phot_proc_mode` | `VAC_GaiaEDR3` | Photometry processing mode |  | integer |
| <small>`phot_bp_rp_excess_factor`</small> | `VAC_GaiaEDR3` | BP/RP excess factor |  | float |
| `bp_rp` | `VAC_GaiaEDR3` | BP - RP colour | mag | float |
| `bp_g` | `VAC_GaiaEDR3` | BP - G colour | mag | float |
| `g_rp` | `VAC_GaiaEDR3` | G - RP colour | mag | float |
| `dr2_rv_nb_transits` | `VAC_GaiaEDR3` | Number of transits used to compute radial velocity in Gaia DR2 |  | integer |
| `dr2_rv_template_teff` | `VAC_GaiaEDR3` | Teff of the template used to compute radial velocity in Gaia DR2 | K | float |
| `dr2_rv_template_logg` | `VAC_GaiaEDR3` | logg of the template used to compute radial velocity in Gaia DR2 | log(cm&#8239;s<sup>-2</sup>) | float |
| `dr2_rv_template_fe_h` | `VAC_GaiaEDR3` | Fe/H of the template used to compute radial velocity in Gaia DR2 | dex | float |
| `l` | `VAC_GaiaEDR3` | Galactic longitude | deg | float |
| `b` | `VAC_GaiaEDR3` | Galactic latitude | deg | float |
| `ecl_lon` | `VAC_GaiaEDR3` | Ecliptic longitude | deg | float |
| `ecl_lat` | `VAC_GaiaEDR3` | Ecliptic latitude | deg | float |
| `zpt_ll2020` | `VAC_GaiaEDR3` | Parallax Zeropoint following [Lindegren et al (2020)](https://doi.org/10.1051/0004-6361/202039653) | mas | float |
| `parallax_corr` | `VAC_GaiaEDR3` | Parallax corrected by subtracting `zpt_ll2020` | mas | float |
| `r_med_geo` | `VAC_GaiaEDR3` | The median of the geometric distance posterior. The geometric distance estimate. From [Bailer-Jones et al (2021)](https://dc.zah.uni-heidelberg.de/tableinfo/gedr3dist.main). | pc | float |
| `r_lo_geo` | `VAC_GaiaEDR3` | The 16th percentile of the geometric distance posterior. The lower 1-sigma-like bound on the confidence interval. From [Bailer-Jones et al (2021)](https://dc.zah.uni-heidelberg.de/tableinfo/gedr3dist.main). | pc | float |
| `r_hi_geo` | `VAC_GaiaEDR3` | The 84th percentile of the geometric distance posterior. The upper 1-sigma-like bound on the confidence interval. From [Bailer-Jones et al (2021)](https://dc.zah.uni-heidelberg.de/tableinfo/gedr3dist.main). | pc | float |
| `r_med_photogeo` | `VAC_GaiaEDR3` | The median of the photogeometric distance posterior. The photogeometric distance estimate. From [Bailer-Jones et al (2021)](https://dc.zah.uni-heidelberg.de/tableinfo/gedr3dist.main). | pc | float |
| `r_lo_photogeo` | `VAC_GaiaEDR3` | The 16th percentile of the photogeometric distance posterior. The lower 1-sigma-like bound on the confidence interval. From [Bailer-Jones et al (2021)](https://dc.zah.uni-heidelberg.de/tableinfo/gedr3dist.main). | pc | float |
| `r_hi_photogeo` | `VAC_GaiaEDR3` | The 84th percentile of the photogeometric distance posterior. The upper 1-sigma-like bound on the confidence interval. From [Bailer-Jones et al (2021)](https://dc.zah.uni-heidelberg.de/tableinfo/gedr3dist.main). | pc | float |
| `flag_edr3dist` | `VAC_GaiaEDR3` | Additional information on the solution. Do not use for filtering. Renamed from `flag`. From [Bailer-Jones et al (2021)](https://dc.zah.uni-heidelberg.de/tableinfo/gedr3dist.main). |  | string


### Available abundance columns

To save space in the [table above](#galah-dr3-catalogues-table-schema), the columns related to abundances are collated in single entries (e.g., `X_fe`). Below we list all of the abundance-related columns.

| Placeholder column name | All possible column names | Found in these tables |
| :------ |:--- | :--- |
| `X_fe`<br/><br/>Neutral/ionised X atomic abundance (final, 1D-LTE or NLTE) | `Li_fe` `C_fe` `O_fe` `Na_fe` `Mg_fe` `Al_fe` `Si_fe` `K_fe` `Ca_fe` `Sc_fe` `Sc2_fe` `Ti_fe` `Ti2_fe` `V_fe` `Cr_fe` `Cr2_fe` `Mn_fe` `Co_fe` `Ni_fe` `Cu_fe` `Zn_fe` `Rb_fe` `Sr_fe` `Y_fe` `Zr_fe` `Mo_fe` `Ru_fe` `Ba_fe` `La_fe` `Ce_fe` `Nd_fe` `Sm_fe` `Eu_fe` `Li_fe` `C_fe` `O_fe` `Na_fe` `Mg_fe` `Al_fe` `Si_fe` `K_fe` `Ca_fe` `Sc_fe` `Sc2_fe` `Ti_fe` `Ti2_fe` `V_fe` `Cr_fe` `Cr2_fe` `Mn_fe` `Co_fe` `Ni_fe` `Cu_fe` `Zn_fe` `Rb_fe` `Sr_fe` `Y_fe` `Zr_fe` `Mo_fe` `Ru_fe` `Ba_fe` `La_fe` `Ce_fe` `Nd_fe` `Sm_fe` `Eu_fe` | `main_allspec` `main_allstar` |
| `e_X_fe`<br/><br/>Uncertainty `X_fe` | `e_Li_fe` `e_C_fe` `e_O_fe` `e_Na_fe` `e_Mg_fe` `e_Al_fe` `e_Si_fe` `e_K_fe` `e_Ca_fe` `e_Sc_fe` `e_Sc2_fe` `e_Ti_fe` `e_Ti2_fe` `e_V_fe` `e_Cr_fe` `e_Cr2_fe` `e_Mn_fe` `e_Co_fe` `e_Ni_fe` `e_Cu_fe` `e_Zn_fe` `e_Rb_fe` `e_Sr_fe` `e_Y_fe` `e_Zr_fe` `e_Mo_fe` `e_Ru_fe` `e_Ba_fe` `e_La_fe` `e_Ce_fe` `e_Nd_fe` `e_Sm_fe` `e_Eu_fe` `e_Li_fe` `e_C_fe` `e_O_fe` `e_Na_fe` `e_Mg_fe` `e_Al_fe` `e_Si_fe` `e_K_fe` `e_Ca_fe` `e_Sc_fe` `e_Sc2_fe` `e_Ti_fe` `e_Ti2_fe` `e_V_fe` `e_Cr_fe` `e_Cr2_fe` `e_Mn_fe` `e_Co_fe` `e_Ni_fe` `e_Cu_fe` `e_Zn_fe` `e_Rb_fe` `e_Sr_fe` `e_Y_fe` `e_Zr_fe` `e_Mo_fe` `e_Ru_fe` `e_Ba_fe` `e_La_fe` `e_Ce_fe` `e_Nd_fe` `e_Sm_fe` `e_Eu_fe` | `main_allspec` `main_allstar` |
| `nr_X_fe`<br/><br/>Bitmask of used X ind lines | `nr_Li_fe` `nr_C_fe` `nr_O_fe` `nr_Na_fe` `nr_Mg_fe` `nr_Al_fe` `nr_Si_fe` `nr_K_fe` `nr_Ca_fe` `nr_Sc_fe` `nr_Sc2_fe` `nr_Ti_fe` `nr_Ti2_fe` `nr_V_fe` `nr_Cr_fe` `nr_Cr2_fe` `nr_Mn_fe` `nr_Co_fe` `nr_Ni_fe` `nr_Cu_fe` `nr_Zn_fe` `nr_Rb_fe` `nr_Sr_fe` `nr_Y_fe` `nr_Zr_fe` `nr_Mo_fe` `nr_Ru_fe` `nr_Ba_fe` `nr_La_fe` `nr_Ce_fe` `nr_Nd_fe` `nr_Sm_fe` `nr_Eu_fe` `nr_Li_fe` `nr_C_fe` `nr_O_fe` `nr_Na_fe` `nr_Mg_fe` `nr_Al_fe` `nr_Si_fe` `nr_K_fe` `nr_Ca_fe` `nr_Sc_fe` `nr_Sc2_fe` `nr_Ti_fe` `nr_Ti2_fe` `nr_V_fe` `nr_Cr_fe` `nr_Cr2_fe` `nr_Mn_fe` `nr_Co_fe` `nr_Ni_fe` `nr_Cu_fe` `nr_Zn_fe` `nr_Rb_fe` `nr_Sr_fe` `nr_Y_fe` `nr_Zr_fe` `nr_Mo_fe` `nr_Ru_fe` `nr_Ba_fe` `nr_La_fe` `nr_Ce_fe` `nr_Nd_fe` `nr_Sm_fe` `nr_Eu_fe` | `main_allspec` `main_allstar` |
| `flag_X_fe`<br/><br/>Quality flag of `X_fe` | `flag_Li_fe` `flag_C_fe` `flag_O_fe` `flag_Na_fe` `flag_Mg_fe` `flag_Al_fe` `flag_Si_fe` `flag_K_fe` `flag_Ca_fe` `flag_Sc_fe` `flag_Sc2_fe` `flag_Ti_fe` `flag_Ti2_fe` `flag_V_fe` `flag_Cr_fe` `flag_Cr2_fe` `flag_Mn_fe` `flag_Co_fe` `flag_Ni_fe` `flag_Cu_fe` `flag_Zn_fe` `flag_Rb_fe` `flag_Sr_fe` `flag_Y_fe` `flag_Zr_fe` `flag_Mo_fe` `flag_Ru_fe` `flag_Ba_fe` `flag_La_fe` `flag_Ce_fe` `flag_Nd_fe` `flag_Sm_fe` `flag_Eu_fe` `flag_Li_fe` `flag_C_fe` `flag_O_fe` `flag_Na_fe` `flag_Mg_fe` `flag_Al_fe` `flag_Si_fe` `flag_K_fe` `flag_Ca_fe` `flag_Sc_fe` `flag_Sc2_fe` `flag_Ti_fe` `flag_Ti2_fe` `flag_V_fe` `flag_Cr_fe` `flag_Cr2_fe` `flag_Mn_fe` `flag_Co_fe` `flag_Ni_fe` `flag_Cu_fe` `flag_Zn_fe` `flag_Rb_fe` `flag_Sr_fe` `flag_Y_fe` `flag_Zr_fe` `flag_Mo_fe` `flag_Ru_fe` `flag_Ba_fe` `flag_La_fe` `flag_Ce_fe` `flag_Nd_fe` `flag_Sm_fe` `flag_Eu_fe` | `main_allspec` `main_allstar` |
| `ind_X1234_fe`<br/><br/>Individual uncalibrated measurmenet of line/combo X1234 | `ind_Li6708_fe` `ind_Li6708_NoRV_fe` `ind_C6588_fe` `ind_O_fe` `ind_Na_fe` `ind_Mg5711_fe` `ind_Al_fe` `ind_Si_fe` `ind_K7699_fe` `ind_Ca_fe` `ind_Sc_fe` `ind_Ti4758_fe` `ind_Ti4759_fe` `ind_Ti4778_fe` `ind_Ti4782_fe` `ind_Ti4798_fe` `ind_Ti4802_fe` `ind_Ti4820_fe` `ind_Ti5689_fe` `ind_Ti5716_fe` `ind_Ti5720_fe` `ind_Ti5739_fe` `ind_Ti5866_fe` `ind_Ti6599_fe` `ind_Ti6717_fe` `ind_Ti7853_fe` `ind_Ti4720_fe` `ind_Ti4765_fe` `ind_Ti4799_fe` `ind_Ti4849_fe` `ind_Ti4866_fe` `ind_Ti4874_fe` `ind_V4832_fe` `ind_V4784_fe` `ind_V4797_fe` `ind_Cr_fe` `ind_Mn_fe` `ind_Co4781_fe` `ind_Co4900_fe` `ind_Co5647_fe` `ind_Co6490_fe` `ind_Co6551_fe` `ind_Co6632_fe` `ind_Co6679_fe` `ind_Co7713_fe` `ind_Co7838_fe` `ind_Ni5847_fe` `ind_Ni6586_fe` `ind_Cu5700_fe` `ind_Cu5782_fe` `ind_Zn4722_fe` `ind_Zn4811_fe` `ind_Rb7800_fe` `ind_Sr6550_fe` `ind_Y_fe` `ind_Y4820_fe` `ind_Y4855_fe` `ind_Y4884_fe` `ind_Y5663_fe` `ind_Y5729_fe` `ind_Zr4739_fe` `ind_Zr4772_fe` `ind_Zr4806_fe` `ind_Zr4828_fe` `ind_Zr5681_fe` `ind_Mo5689_fe` `ind_Mo5751_fe` `ind_Mo5858_fe` `ind_Mo6619_fe` `ind_Ru4758_fe` `ind_Ru4869_fe` `ind_Ru5699_fe` `ind_Ba_fe` `ind_La4716_fe` `ind_La4749_fe` `ind_La4804_fe` `ind_La5806_fe` `ind_Ce4774_fe` `ind_Nd4811_fe` `ind_Nd5741_fe` `ind_Nd5770_fe` `ind_Nd5812_fe` `ind_Nd5842_fe` `ind_Sm4720_fe` `ind_Sm4792_fe` `ind_Sm4837_fe` `ind_Sm4848_fe` `ind_Sm4854_fe` `ind_Eu5819_fe` `ind_Eu6645_fe` | `main_allspec` |
| `ind_cov_e_X1234`<br/><br/>SME covariance fitting uncertainty of `ind_X1234_fe` | `ind_cov_e_Li6708` `ind_cov_e_Li6708_NoRV` `ind_cov_e_C6588` `ind_cov_e_O` `ind_cov_e_Na` `ind_cov_e_Mg5711` `ind_cov_e_Al` `ind_cov_e_Si` `ind_cov_e_K7699` `ind_cov_e_Ca` `ind_cov_e_Sc` `ind_cov_e_Ti4758` `ind_cov_e_Ti4759` `ind_cov_e_Ti4778` `ind_cov_e_Ti4782` `ind_cov_e_Ti4798` `ind_cov_e_Ti4802` `ind_cov_e_Ti4820` `ind_cov_e_Ti5689` `ind_cov_e_Ti5716` `ind_cov_e_Ti5720` `ind_cov_e_Ti5739` `ind_cov_e_Ti5866` `ind_cov_e_Ti6599` `ind_cov_e_Ti6717` `ind_cov_e_Ti7853` `ind_cov_e_Ti4720` `ind_cov_e_Ti4765` `ind_cov_e_Ti4799` `ind_cov_e_Ti4849` `ind_cov_e_Ti4866` `ind_cov_e_Ti4874` `ind_cov_e_V4832` `ind_cov_e_V4784` `ind_cov_e_V4797` `ind_cov_e_Cr` `ind_cov_e_Mn` `ind_cov_e_Co4781` `ind_cov_e_Co4900` `ind_cov_e_Co5647` `ind_cov_e_Co6490` `ind_cov_e_Co6551` `ind_cov_e_Co6632` `ind_cov_e_Co6679` `ind_cov_e_Co7713` `ind_cov_e_Co7838` `ind_cov_e_Ni5847` `ind_cov_e_Ni6586` `ind_cov_e_Cu5700` `ind_cov_e_Cu5782` `ind_cov_e_Zn4722` `ind_cov_e_Zn4811` `ind_cov_e_Rb7800` `ind_cov_e_Sr6550` `ind_cov_e_Y` `ind_cov_e_Y4820` `ind_cov_e_Y4855` `ind_cov_e_Y4884` `ind_cov_e_Y5663` `ind_cov_e_Y5729` `ind_cov_e_Zr4739` `ind_cov_e_Zr4772` `ind_cov_e_Zr4806` `ind_cov_e_Zr4828` `ind_cov_e_Zr5681` `ind_cov_e_Mo5689` `ind_cov_e_Mo5751` `ind_cov_e_Mo5858` `ind_cov_e_Mo6619` `ind_cov_e_Ru4758` `ind_cov_e_Ru4869` `ind_cov_e_Ru5699` `ind_cov_e_Ba` `ind_cov_e_La4716` `ind_cov_e_La4749` `ind_cov_e_La4804` `ind_cov_e_La5806` `ind_cov_e_Ce4774` `ind_cov_e_Nd4811` `ind_cov_e_Nd5741` `ind_cov_e_Nd5770` `ind_cov_e_Nd5812` `ind_cov_e_Nd5842` `ind_cov_e_Sm4720` `ind_cov_e_Sm4792` `ind_cov_e_Sm4837` `ind_cov_e_Sm4848` `ind_cov_e_Sm4854` `ind_cov_e_Eu5819` `ind_cov_e_Eu6645` | `main_allspec` |
| `ind_flag_X1234`<br/><br/>Quality flag fit for `ind_X1234_fe` | `ind_flag_Li6708` `ind_flag_Li6708_NoRV` `ind_flag_C6588` `ind_flag_O` `ind_flag_Na` `ind_flag_Mg5711` `ind_flag_Al` `ind_flag_Si` `ind_flag_K7699` `ind_flag_Ca` `ind_flag_Sc` `ind_flag_Ti4758` `ind_flag_Ti4759` `ind_flag_Ti4778` `ind_flag_Ti4782` `ind_flag_Ti4798` `ind_flag_Ti4802` `ind_flag_Ti4820` `ind_flag_Ti5689` `ind_flag_Ti5716` `ind_flag_Ti5720` `ind_flag_Ti5739` `ind_flag_Ti5866` `ind_flag_Ti6599` `ind_flag_Ti6717` `ind_flag_Ti7853` `ind_flag_Ti4720` `ind_flag_Ti4765` `ind_flag_Ti4799` `ind_flag_Ti4849` `ind_flag_Ti4866` `ind_flag_Ti4874` `ind_flag_V4832` `ind_flag_V4784` `ind_flag_V4797` `ind_flag_Cr` `ind_flag_Mn` `ind_flag_Co4781` `ind_flag_Co4900` `ind_flag_Co5647` `ind_flag_Co6490` `ind_flag_Co6551` `ind_flag_Co6632` `ind_flag_Co6679` `ind_flag_Co7713` `ind_flag_Co7838` `ind_flag_Ni5847` `ind_flag_Ni6586` `ind_flag_Cu5700` `ind_flag_Cu5782` `ind_flag_Zn4722` `ind_flag_Zn4811` `ind_flag_Rb7800` `ind_flag_Sr6550` `ind_flag_Y` `ind_flag_Y4820` `ind_flag_Y4855` `ind_flag_Y4884` `ind_flag_Y5663` `ind_flag_Y5729` `ind_flag_Zr4739` `ind_flag_Zr4772` `ind_flag_Zr4806` `ind_flag_Zr4828` `ind_flag_Zr5681` `ind_flag_Mo5689` `ind_flag_Mo5751` `ind_flag_Mo5858` `ind_flag_Mo6619` `ind_flag_Ru4758` `ind_flag_Ru4869` `ind_flag_Ru5699` `ind_flag_Ba` `ind_flag_La4716` `ind_flag_La4749` `ind_flag_La4804` `ind_flag_La5806` `ind_flag_Ce4774` `ind_flag_Nd4811` `ind_flag_Nd5741` `ind_flag_Nd5770` `ind_flag_Nd5812` `ind_flag_Nd5842` `ind_flag_Sm4720` `ind_flag_Sm4792` `ind_flag_Sm4837` `ind_flag_Sm4848` `ind_flag_Sm4854` `ind_flag_Eu5819` `ind_flag_Eu6645` | `main_allspec` |
