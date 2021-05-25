---
layout: page
title: Table Schema
subtitle: Third Data Release
---

For GALAH DR3, we have provided two versions of the GALAH DR3 catalogue, and several value-added catalogues. These are described in detail on the Catalogue Data Access and Using the GALAH Catalogues pages. The table below collates the available columns across these catalogues into one table. It gives the catalogues that a given column is found within, and the description, unit, and data type of each column. To save space in the table below, the columns related to abundances have been collapsed in single entries (e.g., `X_fe`), and they are all listed in a table at the bottom of this page.

Items of note:

* The `sobject_id` column is the only one found across all the tables, and should be used for joining the catalogues.
* For columns that are listed as being found in multiple catalogues, the same value will be found across all catalogues for a given `sobject_id` (e.g., for a given `sobject_id`, the same `teff` is found in `main_star` and `main_spec`).
* For parameters that have multiple options (e.g., effective temperature with possible values of `teff`, `irfm_teff`, `init_teff`, `teff_guess`, `teff_bstep`), consult the Using GALAH Data page, which gives our recommendation for the value to use.
* `rv_gaia_dr2` and `dr_radial_velocity` both refer to the Gaia DR2 radial velocity and are identical for a given `dr3_source_id`.
* Generally we do not recommend values found only in the main_spec catalogue as these are only for expert use and are for diagnostic purposes.


### GALAH DR3 catalogues table schema

| Column name | Found in these tables | Description | units | type |
| :------ |:--- | :--- | :--- | :--- |
| `sobject_id` | `main_spec`, `vac_ages`, `vac_dynamics`, `vac_rv`, `vac_gaiaedr3`, `main_star` | GALAH identifier |  | integer |
| `star_id` | `main_spec`, `vac_gaiaedr3`, `main_star` | 2MASS identifier |  | string |
| `dr2_source_id` | `main_spec`, `vac_gaiaedr3`, `main_star` | Gaia DR2 `source_id` |  | integer |
| `dr3_source_id` | `main_spec`, `vac_gaiaedr3`, `main_star` | Gaia DR3 `source_id` |  | integer |
| `survey_name` | `main_spec`, `main_star` | Name of survey as part of GALAH+DR3 |  | string |
| `field_id` | `main_spec`, `main_star` | GALAH fco field |  | integer |
| `flag_repeat` | `main_spec`, `main_star` | Repeat observation flag, indicating if used for clean catalog |  | integer |
| `wg4_field` | `main_spec`, `main_star` | GALAH WG4 field |  | string |
| `wg4_pipeline` | `main_spec`, `main_star` | SME pipeline version free/lbol/seis |  | string |
| `flag_sp` | `main_spec`, `main_star` | Stellar parameter quality flag |  | integer |
| `teff` | `main_spec`, `main_star` | Spectroscopic effective temperature (used for fitting) | K | float |
| `e_teff` | `main_spec`, `main_star` | Uncertainty `teff` | K | float |
| `irfm_teff` | `main_spec`, `main_star` | IRFM temperature (not used for synthesis) | K | float |
| `irfm_ebv` | `main_spec`, `main_star` | E(B-V) used for IRFM `teff` estimation | mag | float |
| `irfm_ebv_ref` | `main_spec`, `main_star` | Reference `irfm_ebv` |  | string |
| `cov_e_teff` | `main_spec` | SME covariance fitting uncertainty `teff` | K | float |
| `init_teff` | `main_spec` | SME initial `teff` | K | float |
| `logg` | `main_spec`, `main_star` | Surface gravity (not fitted via spectra if `wg4_pipeline` not free) | log(cm.s**-2) | float |
| `e_logg` | `main_spec`, `main_star` | Uncertainty `logg` | log(cm.s**-2) | float |
| `cov_e_logg` | `main_spec` | MonteCarlo uncertainty `logg` | log(cm.s**-2) | float |
| `init_logg` | `main_spec` | SME initial `logg` | log(cm.s**-2) | float |
| `fe_h` | `main_spec`, `main_star` | Fe atomic abundance from Fe lines (final, 1D-NLTE) |  | float |
| `e_fe_h` | `main_spec`, `main_star` | Uncertainty `fe_h` |  | float |
| `cov_e_fe_h` | `main_spec` | SME covariance fitting uncertainty `fe_h` |  | float |
| `flag_fe_h` | `main_spec`, `main_star` | Quality flag `fe_h` |  | integer |
| `fe_h_atmo` | `main_spec`, `main_star` | sme.feh from stellar parameter run, fitted from H, Ti, Sc, Fe |  | float |
| `e_fe_h_atmo` | `main_spec` | Uncertainty `fe_h_atmo` |  | float |
| `cov_e_fe_h_atmo` | `main_spec` | SME covariance fitting uncertainty sme.feh |  | float |
| `init_fe_h_atmo` | `main_spec` | SME initial sme.feh |  | float |
| `vmic` | `main_spec`, `main_star` | Microturbulence velocity (from empirical relation) | km s-1 | float |
| `vbroad` | `main_spec`, `main_star` | Broadening velocity (fitted sme.vsini with sme.vmac=0) | km s-1 | float |
| `e_vbroad` | `main_spec`, `main_star` | Uncertainty of `vbroad` | km s-1 | float |
| `cov_e_vbroad` | `main_spec` | SME covariance fitting uncertainty sme.vsini | km s-1 | float |
| `init_vbroad` | `main_spec` | SME initial broadening velocity | km s-1 | float |
| `mass` | `main_spec` | Stellar parameter fitting product of stellar mass | solMass | float |
| `lbol` | `main_spec` | Stellar parameter fitting product of bolometric luminosity | solLum | float |
| `age` | `main_spec` | Stellar parameter fitting product of stellar age | Gyr | float |
| `chi2_sp` | `main_spec`, `main_star` | χ² value of stellar parameter fitting |  | float |
| `alpha_fe` | `main_spec`, `main_star` | Combined, weighted alpha-process element abundance |  | float |
| `e_alpha_fe` | `main_spec`, `main_star` | Uncertainty of `alpha_fe` |  | float |
| `nr_alpha_fe` | `main_spec`, `main_star` | Bitmask of used measurements for `alpha_fe` |  | float |
| `flag_alpha_fe` | `main_spec`, `main_star` | Quality flag of measurements for `alpha_fe` |  | integer |
| `flux_A_Fe` | `main_spec`, `main_star` | Normalised maximum absorption strength of in iron lines |  | float |
| `chi_A_Fe` | `main_spec`, `main_star` | χ² value of iron abundance fitting |  | float |
| `ind_X1234_fe` | `main_spec` | Individual uncalibrated measurmenet of line/combo X1234 |  | float |
| `ind_cov_e_X1234` | `main_spec` | SME covariance fitting uncertainty `ind_X1234_fe` |  | float |
| `ind_flag_X1234` | `main_spec` | Quality flag fit for `ind_X1234_fe` |  | integer |
| `X_fe` | `main_spec`, `main_star` | Neutral/ionised X atomic abundance (final, 1D-LTE or NLTE) |  | float |
| `e_X_fe` | `main_spec`, `main_star` | Uncertainty `X_fe` |  | float |
| `nr_X_fe` | `main_spec`, `main_star` | Bitmask of used X ind lines |  | integer |
| `flag_X_fe` | `main_spec`, `main_star` | Quality flag of `X_fe` |  | integer |
| `ra_dr2` | `main_spec`, `main_star` | Right Ascension Gaia DR2 | deg | float |
| `dec_dr2` | `main_spec`, `main_star` | Declination Gaia DR2 | deg | float |
| `parallax_dr2` | `main_spec`, `main_star` | propagated from Gaia DR2 | mas | float |
| `parallax_error_dr2` | `main_spec`, `main_star` | propagated from Gaia DR2 | mas | float |
| `r_est_dr2` | `main_spec`, `main_star` | propagated from 2018AJ....156...58B | pc | float |
| `r_lo_dr2` | `main_spec`, `main_star` | propagated from 2018AJ....156...58B | pc | float |
| `r_hi_dr2` | `main_spec`, `main_star` | propagated from 2018AJ....156...58B | pc | float |
| `r_len_dr2` | `main_spec`, `main_star` | propagated from 2018AJ....156...58B | pc | float |
| `rv_galah` | `main_spec`, `vac_rv`, `main_star` | Best-method radial velocity from GALAH spectra |  | float |
| `e_rv_galah` | `main_spec`, `vac_rv`, `main_star` | Uncertainty of `rv_galah` |  | float |
| `rv_gaia_dr2` | `main_spec`, `main_star` | propagated from Gaia DR2; identical to `dr2_radial_velocity` | km s-1 | float |
| `e_rv_gaia_dr2` | `main_spec`, `main_star` | propagated from Gaia DR2; identical to `dr2_radial_velocity_error` | km s-1 | float |
| `red_flag` | `main_spec`, `main_star` | reduction pipeline quality flag |  | integer |
| `ebv` | `main_spec`, `main_star` | SFD extinction value | mag | float |
| `snr_c1_iraf` | `main_spec`, `main_star` | Average SNR/px CCD1 |  | float |
| `snr_c2_iraf` | `main_spec`, `main_star` | Average SNR/px CCD2 |  | float |
| `snr_c3_iraf` | `main_spec`, `main_star` | Average SNR/px CCD3 |  | float |
| `snr_c4_iraf` | `main_spec`, `main_star` | Average SNR/px CCD4 |  | float |
| `flag_guess` | `main_spec`, `main_star` | GUESS reduction pipeline quality flag |  | integer |
| `rv_guess` | `main_spec` | Reduction pipeline best radial velocity | km s-1 | float |
| `e_rv_guess` | `main_spec` | Reduction pipeline uncertainty radial velocity | km s-1 | float |
| `teff_guess` | `main_spec` | Reduction pipeline best teff | K | float |
| `logg_guess` | `main_spec` | Reduction pipeline best logg | log(cm.s**-2) | float |
| `feh_guess` | `main_spec` | Reduction pipeline best `fe_h` |  | float |
| `rv_5854` | `main_spec` | Local best fit to RV when fitting A(Ba5854) | km s-1 | float |
| `rv_6708` | `main_spec` | Local best fit to RV when fitting A(Li6708) | km s-1 | float |
| `rv_6722` | `main_spec` | Local best fit to RV when fitting A(Si6722) | km s-1 | float |
| `v_jk` | `main_spec`, `main_star` | V magnitude estimated from 2MASS J and Ks mag | mag | float |
| `j_m` | `main_spec`, `main_star` | propagated from 2MASS | mag | float |
| `j_msigcom` | `main_spec`, `main_star` | propagated from 2MASS | mag | float |
| `h_m` | `main_spec`, `main_star` | propagated from 2MASS | mag | float |
| `h_msigcom` | `main_spec`, `main_star` | propagated from 2MASS | mag | float |
| `ks_m` | `main_spec`, `main_star` | propagated from 2MASS | mag | float |
| `ks_msigcom` | `main_spec`, `main_star` | propagated from 2MASS | mag | float |
| `ph_qual_tmass` | `main_spec`, `main_star` | propagated from 2MASS `ph_qual` |  | string |
| `w2mpro` | `main_spec`, `main_star` | propagated from AllWISE | mag | float |
| `w2mpro_error` | `main_spec`, `main_star` | propagated from AllWISE | mag | float |
| `ph_qual_wise` | `main_spec`, `main_star` | propagated from AllWISE `ph_qual` |  | string |
| `a_ks` | `main_spec`, `main_star` | Used Ks band extinction | mag | float |
| `e_a_ks` | `main_spec`, `main_star` | Uncertainty of `a_ks` | mag | float |
| `bc_ks` | `main_spec`, `main_star` | Used Bolometric Correction for Ks band | mag | float |
| `ruwe_dr2` | `main_spec`, `main_star` | propagated from Gaia DR2 |  | float |
| `age_bstep` | `vac_ages` | Age estimate BSTEP-Mod. |  | float |
| `e_age_bstep` | `vac_ages` | 1-sigma uncertainty of `age_bstep` |  | float |
| `e16_age_bstep` | `vac_ages` | 16 percentile value for `age_bstep` |  | float |
| `e50_age_bstep` | `vac_ages` | 50 percentile value for `age_bstep` |  | float |
| `e84_age_bstep` | `vac_ages` | 84 percentile value for `age_bstep` |  | float |
| `m_act_bstep` | `vac_ages` | Actual stellar mass after mass loss BSTEP-Mod. |  | float |
| `e_m_act_bstep` | `vac_ages` | 1-sigma uncertainty of `m_act_bstep` |  | float |
| `e16_m_act_bstep` | `vac_ages` | 16 percentile value for `m_act_bstep` |  | float |
| `e50_m_act_bstep` | `vac_ages` | 50 percentile value for `m_act_bstep` |  | float |
| `e84_m_act_bstep` | `vac_ages` | 84 percentile value for `m_act_bstep` |  | float |
| `m_ini_bstep` | `vac_ages` | Initial stellar mass BSTEP-Mod. |  | float |
| `e_m_ini_bstep` | `vac_ages` | 1-sigma uncertainty of `m_ini_bstep` |  | float |
| `e16_m_ini_bstep` | `vac_ages` | 16 percentile value for `m_ini_bstep` |  | float |
| `e50_m_ini_bstep` | `vac_ages` | 50 percentile value for `m_ini_bstep` |  | float |
| `e84_m_ini_bstep` | `vac_ages` | 84 percentile value for `m_ini_bstep` |  | float |
| `radius_bstep` | `vac_ages` | Stellar Radius BSTEP-Mod. |  | float |
| `e_radius_bstep` | `vac_ages` | 1-sigma uncertainty of `radius_bstep` |  | float |
| `e16_radius_bstep` | `vac_ages` | 16 percentile value for `radius_bstep` |  | float |
| `e50_radius_bstep` | `vac_ages` | 50 percentile value for `radius_bstep` |  | float |
| `e84_radius_bstep` | `vac_ages` | 84 percentile value for `radius_bstep` |  | float |
| `is_redclump_bstep` | `vac_ages` | Probability to be a red clump star (1.0) or not (0.0) BSTEP-Mod. |  | float |
| `e_is_redclump_bstep` | `vac_ages` | 1-sigma uncertainty of `is_redclump_bstep` |  | float |
| `e16_is_redclump_bstep` | `vac_ages` | 16 percentile value for `is_redclump_bstep` |  | float |
| `e50_is_redclump_bstep` | `vac_ages` | 50 percentile value for `is_redclump_bstep` |  | float |
| `e84_is_redclump_bstep` | `vac_ages` | 84 percentile value for `is_redclump_bstep` |  | float |
| `distance_bstep` | `vac_ages` | Distance BSTEP-Mod. |  | float |
| `e_distance_bstep` | `vac_ages` | 1-sigma uncertainty of `distance_bstep` |  | float |
| `e16_distance_bstep` | `vac_ages` | 16 percentile value for `distance_bstep` |  | float |
| `e50_distance_bstep` | `vac_ages` | 50 percentile value for `distance_bstep` |  | float |
| `e84_distance_bstep` | `vac_ages` | 84 percentile value for `distance_bstep` |  | float |
| `ebv_bstep` | `vac_ages` | Extinction E(B-V) BSTEP-Mod. |  | float |
| `e_ebv_bstep` | `vac_ages` | 1-sigma uncertainty of `ebv_bstep` |  | float |
| `e16_ebv_bstep` | `vac_ages` | 16 percentile value for `ebv_bstep` |  | float |
| `e50_ebv_bstep` | `vac_ages` | 50 percentile value for `ebv_bstep` |  | float |
| `e84_ebv_bstep` | `vac_ages` | 84 percentile value for `ebv_bstep` |  | float |
| `teff_bstep` | `vac_ages` | Effective Temperature BSTEP-Mod. |  | float |
| `e_teff_bstep` | `vac_ages` | 1-sigma uncertainty of `teff_bstep` |  | float |
| `e16_teff_bstep` | `vac_ages` | 16 percentile value for `teff_bstep` |  | float |
| `e50_teff_bstep` | `vac_ages` | 50 percentile value for `teff_bstep` |  | float |
| `e84_teff_bstep` | `vac_ages` | 84 percentile value for `teff_bstep` |  | float |
| `logg_bstep` | `vac_ages` | Surface gravity BSTEP-Mod. |  | float |
| `e_logg_bstep` | `vac_ages` | 1-sigma uncertainty of `logg_bstep` |  | float |
| `e16_logg_bstep` | `vac_ages` | 16 percentile value for `logg_bstep` |  | float |
| `e50_logg_bstep` | `vac_ages` | 50 percentile value for `logg_bstep` |  | float |
| `e84_logg_bstep` | `vac_ages` | 84 percentile value for `logg_bstep` |  | float |
| `meh_act_bstep` | `vac_ages` | Surface effective [M/H] BSTEP-Mod. |  | float |
| `e_meh_act_bstep` | `vac_ages` | 1-sigma uncertainty of `meh_act_bstep` |  | float |
| `e16_meh_act_bstep` | `vac_ages` | 16 percentile value for `meh_act_bstep` |  | float |
| `e50_meh_act_bstep` | `vac_ages` | 50 percentile value for `meh_act_bstep` |  | float |
| `e84_meh_act_bstep` | `vac_ages` | 84 percentile value for `meh_act_bstep` |  | float |
| `meh_ini_bstep` | `vac_ages` | Intial effective metallicity [M/H] from isochrones BSTEP-Mod. |  | float |
| `e_meh_ini_bstep` | `vac_ages` | 1-sigma uncertainty of `meh_ini_bstep` |  | float |
| `e16_meh_ini_bstep` | `vac_ages` | 16 percentile value for `meh_ini_bstep` |  | float |
| `e50_meh_ini_bstep` | `vac_ages` | 50 percentile value for `meh_ini_bstep` |  | float |
| `e84_meh_ini_bstep` | `vac_ages` | 84 percentile value for `meh_ini_bstep` |  | float |
| `log_lum_bstep` | `vac_ages` | log(Luminosity L/`L_sun`) |  | float |
| `e_log_lum_bstep` | `vac_ages` | 1-sigma uncertainty of `log_lum_bstep` |  | float |
| `e16_log_lum_bstep` | `vac_ages` | 16 percentile value for `log_lum_bstep` |  | float |
| `e50_log_lum_bstep` | `vac_ages` | 50 percentile value for `log_lum_bstep` |  | float |
| `e84_log_lum_bstep` | `vac_ages` | 84 percentile value for `log_lum_bstep` |  | float |
| `abs_j_bstep` | `vac_ages` | Absolute Magnitude 2MASS J |  | float |
| `e_abs_j_bstep` | `vac_ages` | 1-sigma uncertainty of `abs_j_bstep` |  | float |
| `e16_abs_j_bstep` | `vac_ages` | 16 percentile value for `abs_j_bstep` |  | float |
| `e50_abs_j_bstep` | `vac_ages` | 50 percentile value for `abs_j_bstep` |  | float |
| `e84_abs_j_bstep` | `vac_ages` | 84 percentile value for `abs_j_bstep` |  | float |
| `abs_ks_bstep` | `vac_ages` | Absolute Magnitude 2MASS Ks |  | float |
| `e_abs_ks_bstep` | `vac_ages` | 1-sigma uncertainty of `abs_ks_bstep` |  | float |
| `e16_abs_ks_bstep` | `vac_ages` | 16 percentile value for `abs_ks_bstep` |  | float |
| `e50_abs_ks_bstep` | `vac_ages` | 50 percentile value for `abs_ks_bstep` |  | float |
| `e84_abs_ks_bstep` | `vac_ages` | 84 percentile value for `abs_ks_bstep` |  | float |
| `use_dist_flag` | `vac_dynamics` | Dist. Used: BSTEP(0), Photogeom.(1), Geom.(2), Plx(4), n.a.(8) |  | integer |
| `use_rv_flag` | `vac_dynamics`, `vac_rv` | RV flag: `rv_obst` (0), `rv_sme_v2` (1), Gaia DR2 (2) or n.a. (4) |  | integer |
| `X_XYZ` | `vac_dynamics` | Best-value heliocentric Galactic rectangular x-coordinate | kpc | float |
| `Y_XYZ` | `vac_dynamics` | Best-value heliocentric Galactic rectangular y-coordinate | kpc | float |
| `Z_XYZ` | `vac_dynamics` | Best-value heliocentric Galactic rectangular z-coordinate | kpc | float |
| `U_UVW` | `vac_dynamics` | Best-value heliocentric Galactic rectangular x-velocity | km s-1 | float |
| `V_UVW` | `vac_dynamics` | Best-value heliocentric Galactic rectangular y-velocity | km s-1 | float |
| `W_UVW` | `vac_dynamics` | Best-value heliocentric Galactic rectangular z-velocity | km s-1 | float |
| `R_Rzphi` | `vac_dynamics` | Best-value Galactocentric Radius | kpc | float |
| `phi_Rzphi` | `vac_dynamics` | Best-value Galactocentric azimuth | rad | float |
| `z_Rzphi` | `vac_dynamics` | Best-value Galactocentric height | kpc | float |
| `vR_Rzphi` | `vac_dynamics` | Best-value Galactocentric radial velocity | km s-1 | float |
| `vT_Rzphi` | `vac_dynamics` | Best-value Galactocentric tangential velocity | km s-1 | float |
| `vz_Rzphi` | `vac_dynamics` | Best-value Galactocentric vertical velocity | km s-1 | float |
| `J_R` | `vac_dynamics` | Best-value radial action | km kpc s-1 | float |
| `L_Z` | `vac_dynamics` | Best-value azimuthal action / angular momentum | km kpc s-1 | float |
| `J_Z` | `vac_dynamics` | Best-value vertical action | km kpc s-1 | float |
| `omega_R` | `vac_dynamics` | Best-value radial orbit frequency | Gyr-1 | float |
| `omega_phi` | `vac_dynamics` | Best-value azimuthal orbit frequency | Gyr-1 | float |
| `omega_z` | `vac_dynamics` | Best-value vertical orbit frequency | Gyr-1 | float |
| `angle_R` | `vac_dynamics` | Best-value radial orbit angle | rad | float |
| `angle_phi` | `vac_dynamics` | Best-value azimuthal orbit angle | rad | float |
| `angle_z` | `vac_dynamics` | Best-value vertical orbit angle | rad | float |
| ecc | `vac_dynamics` | Best-value orbit eccentricity |  | float |
| zmax | `vac_dynamics` | Best-value maximum Galactocentric height | kpc | float |
| `R_peri` | `vac_dynamics` | Best-value Galactocentric pericenter radius | kpc | float |
| `R_ap` | `vac_dynamics` | Best-value Galactocentric apocenter radius | kpc | float |
| Energy | `vac_dynamics` | Best-value orbit energy | km-2 s-2 | float |
| `X_XYZ_5` | `vac_dynamics` | 5th Percentile MC heliocentric Galactic rectangular x-coordinate | kpc | float |
| `X_XYZ_50` | `vac_dynamics` | 50th Percentile MC heliocentric Galactic rectangular x-coordinate | kpc | float |
| `X_XYZ_95` | `vac_dynamics` | 95th Percentile MC heliocentric Galactic rectangular x-coordinate | kpc | float |
| `Y_XYZ_5` | `vac_dynamics` | 5th Percentile MC heliocentric Galactic rectangular y-coordinate | kpc | float |
| `Y_XYZ_50` | `vac_dynamics` | 50th Percentile MC heliocentric Galactic rectangular y-coordinate | kpc | float |
| `Y_XYZ_95` | `vac_dynamics` | 95th Percentile MC heliocentric Galactic rectangular y-coordinate | kpc | float |
| `Z_XYZ_5` | `vac_dynamics` | 5th Percentile MC heliocentric Galactic rectangular z-coordinate | kpc | float |
| `Z_XYZ_50` | `vac_dynamics` | 50th Percentile MC heliocentric Galactic rectangular z-coordinate | kpc | float |
| `Z_XYZ_95` | `vac_dynamics` | 95th Percentile MC heliocentric Galactic rectangular z-coordinate | kpc | float |
| `U_UVW_5` | `vac_dynamics` | 5th Percentile MC heliocentric Galactic rectangular x-velocity | km s-1 | float |
| `U_UVW_50` | `vac_dynamics` | 50th Percentile MC heliocentric Galactic rectangular x-velocity | km s-1 | float |
| `U_UVW_95` | `vac_dynamics` | 95th Percentile MC heliocentric Galactic rectangular x-velocity | km s-1 | float |
| `V_UVW_5` | `vac_dynamics` | 5th Percentile MC heliocentric Galactic rectangular y-velocity | km s-1 | float |
| `V_UVW_50` | `vac_dynamics` | 50th Percentile MC heliocentric Galactic rectangular y-velocity | km s-1 | float |
| `V_UVW_95` | `vac_dynamics` | 95th Percentile MC heliocentric Galactic rectangular y-velocity | km s-1 | float |
| `W_UVW_5` | `vac_dynamics` | 5th Percentile MC heliocentric Galactic rectangular z-velocity | km s-1 | float |
| `W_UVW_50` | `vac_dynamics` | 50th Percentile MC heliocentric Galactic rectangular z-velocity | km s-1 | float |
| `W_UVW_95` | `vac_dynamics` | 95th Percentile MC heliocentric Galactic rectangular z-velocity | km s-1 | float |
| `R_Rzphi_5` | `vac_dynamics` | 5th Percentile MC Galactocentric Radius | kpc | float |
| `R_Rzphi_50` | `vac_dynamics` | 50th Percentile MC Galactocentric Radius | kpc | float |
| `R_Rzphi_95` | `vac_dynamics` | 95th Percentile MC Galactocentric Radius | kpc | float |
| `phi_Rzphi_5` | `vac_dynamics` | 5th Percentile MC Galactocentric azimuth | rad | float |
| `phi_Rzphi_50` | `vac_dynamics` | 50th Percentile MC Galactocentric azimuth | rad | float |
| `phi_Rzphi_95` | `vac_dynamics` | 95th Percentile MC Galactocentric azimuth | rad | float |
| `z_Rzphi_5` | `vac_dynamics` | 5th Percentile MC Galactocentric height | kpc | float |
| `z_Rzphi_50` | `vac_dynamics` | 50th Percentile MC Galactocentric height | kpc | float |
| `z_Rzphi_95` | `vac_dynamics` | 95th Percentile MC Galactocentric height | kpc | float |
| `vR_Rzphi_5` | `vac_dynamics` | 5th Percentile MC Galactocentric radial velocity | km s-1 | float |
| `vR_Rzphi_50` | `vac_dynamics` | 50th Percentile MC Galactocentric radial velocity | km s-1 | float |
| `vR_Rzphi_95` | `vac_dynamics` | 95th Percentile MC Galactocentric radial velocity | km s-1 | float |
| `vT_Rzphi_5` | `vac_dynamics` | 5th Percentile MC Galactocentric tangential velocity | km s-1 | float |
| `vT_Rzphi_50` | `vac_dynamics` | 50th Percentile MC Galactocentric tangential velocity | km s-1 | float |
| `vT_Rzphi_95` | `vac_dynamics` | 95th Percentile MC Galactocentric tangential velocity | km s-1 | float |
| `vz_Rzphi_5` | `vac_dynamics` | 5th Percentile MC Galactocentric vertical velocity | km s-1 | float |
| `vz_Rzphi_50` | `vac_dynamics` | 50th Percentile MC Galactocentric vertical velocity | km s-1 | float |
| `vz_Rzphi_95` | `vac_dynamics` | 95th Percentile MC Galactocentric vertical velocity | km s-1 | float |
| `J_R_5` | `vac_dynamics` | 5th Percentile MC radial action | km kpc s-1 | float |
| `J_R_50` | `vac_dynamics` | 50th Percentile MC radial action | km kpc s-1 | float |
| `J_R_95` | `vac_dynamics` | 95th Percentile MC radial action | km kpc s-1 | float |
| `L_Z_5` | `vac_dynamics` | 5th Percentile MC azimuthal action / angular momentum | km kpc s-1 | float |
| `L_Z_50` | `vac_dynamics` | 50th Percentile MC azimuthal action / angular momentum | km kpc s-1 | float |
| `L_Z_95` | `vac_dynamics` | 95th Percentile MC azimuthal action / angular momentum | km kpc s-1 | float |
| `J_Z_5` | `vac_dynamics` | 5th Percentile MC vertical action | km kpc s-1 | float |
| `J_Z_50` | `vac_dynamics` | 50th Percentile MC vertical action | km kpc s-1 | float |
| `J_Z_95` | `vac_dynamics` | 95th Percentile MC vertical action | km kpc s-1 | float |
| `omega_R_5` | `vac_dynamics` | 5th Percentile MC radial orbit frequency | Gyr-1 | float |
| `omega_R_50` | `vac_dynamics` | 50th Percentile MC radial orbit frequency | Gyr-1 | float |
| `omega_R_95` | `vac_dynamics` | 95th Percentile MC radial orbit frequency | Gyr-1 | float |
| `omega_phi_5` | `vac_dynamics` | 5th Percentile MC azimuthal orbit frequency | Gyr-1 | float |
| `omega_phi_50` | `vac_dynamics` | 50th Percentile MC azimuthal orbit frequency | Gyr-1 | float |
| `omega_phi_95` | `vac_dynamics` | 95th Percentile MC azimuthal orbit frequency | Gyr-1 | float |
| `omega_z_5` | `vac_dynamics` | 5th Percentile MC vertical orbit frequency | Gyr-1 | float |
| `omega_z_50` | `vac_dynamics` | 50th Percentile MC vertical orbit frequency | Gyr-1 | float |
| `omega_z_95` | `vac_dynamics` | 95th Percentile MC vertical orbit frequency | Gyr-1 | float |
| `angle_R_5` | `vac_dynamics` | 5th Percentile MC radial orbit angle | rad | float |
| `angle_R_50` | `vac_dynamics` | 50th Percentile MC radial orbit angle | rad | float |
| `angle_R_95` | `vac_dynamics` | 95th Percentile MC radial orbit angle | rad | float |
| `angle_phi_5` | `vac_dynamics` | 5th Percentile MC azimuthal orbit angle | rad | float |
| `angle_phi_50` | `vac_dynamics` | 50th Percentile MC azimuthal orbit angle | rad | float |
| `angle_phi_95` | `vac_dynamics` | 95th Percentile MC azimuthal orbit angle | rad | float |
| `angle_z_5` | `vac_dynamics` | 5th Percentile MC vertical orbit angle | rad | float |
| `angle_z_50` | `vac_dynamics` | 50th Percentile MC vertical orbit angle | rad | float |
| `angle_z_95` | `vac_dynamics` | 95th Percentile MC vertical orbit angle | rad | float |
| `ecc_5` | `vac_dynamics` | 5th Percentile MC orbit eccentricity |  | float |
| `ecc_50` | `vac_dynamics` | 50th Percentile MC orbit eccentricity |  | float |
| `ecc_95` | `vac_dynamics` | 95th Percentile MC orbit eccentricity |  | float |
| `zmax_5` | `vac_dynamics` | 5th Percentile MC maximum Galactocentric height | kpc | float |
| `zmax_50` | `vac_dynamics` | 50th Percentile MC maximum Galactocentric height | kpc | float |
| `zmax_95` | `vac_dynamics` | 95th Percentile MC maximum Galactocentric height | kpc | float |
| `R_peri_5` | `vac_dynamics` | 5th Percentile MC Galactocentric pericenter radius | kpc | float |
| `R_peri_50` | `vac_dynamics` | 50th Percentile MC Galactocentric pericenter radius | kpc | float |
| `R_peri_95` | `vac_dynamics` | 95th Percentile MC Galactocentric pericenter radius | kpc | float |
| `R_ap_5` | `vac_dynamics` | 5th Percentile MC Galactocentric apocenter radius | kpc | float |
| `R_ap_50` | `vac_dynamics` | 50th Percentile MC Galactocentric apocenter radius | kpc | float |
| `R_ap_95` | `vac_dynamics` | 95th Percentile MC Galactocentric apocenter radius | kpc | float |
| `Energy_5` | `vac_dynamics` | 5th Percentile MC orbit energy | km-2 s-2 | float |
| `Energy_50` | `vac_dynamics` | 50th Percentile MC orbit energy | km-2 s-2 | float |
| `Energy_95` | `vac_dynamics` | 95th Percentile MC orbit energy | km-2 s-2 | float |
| `rv_sme_v2` | `vac_rv` | SME fitted radial velocity from GALAH spectra with correct vbary correction (`vbary_v2`) |  | float |
| `rv_sme_v1` | `vac_rv` | SME fitted radial velocity from GALAH spectra with wrong vbary correction (`vbary_v1`) |  | float |
| `e_rv_sme` | `vac_rv` | Uncertainty of `rv_galah` |  | float |
| `cov_e_rv_sme` | `vac_rv` | SME covariance fitting uncertainty sme.vrad | km s-1 | float |
| heliocentricJD | `vac_rv` | Heliocentric Julian Date |  | float |
| `vbary_v1` | `vac_rv` | Wrong barycentric correction used for v1 |  | float |
| `vbary_v2` | `vac_rv` | Correct barycentric correction used for v2 |  | float |
| `rv_obst` | `vac_rv` | Radial Velocity with grav. redshift correction | km s-1 | float |
| `e_rv_obst` | `vac_rv` | Uncertainty of `rv_obst` | km s-1 | float |
| `rv_nogr_obst` | `vac_rv` | Radial Velocity without grav. redshift correction | km s-1 | float |
| `e_rv_nogr_obst` | `vac_rv` | Uncertainty of `rv_nogr_obst` | km s-1 | float |
| `MJD_local` | `vac_rv` | Modified Julian Date, Middle of Exposure | d | float |
| `dr2_radial_velocity` | `vac_rv`, `vac_gaiaedr3` | Radial velocity from Gaia DR2; identical to `rv_gaia_dr2` | km s-1 | float |
| `dr2_radial_velocity_error` | `vac_rv`, `vac_gaiaedr3` | Radial velocity error from Gaia DR2; identical to `e_rv_gaia_dr2` | km s-1 | float |
| `angular_distance` | `vac_gaiaedr3` | Angular distance between the two sources | mas | float |
| `magnitude_difference` | `vac_gaiaedr3` | G band magnitude difference between the sources | mag | float |
| `proper_motion_propagation` | `vac_gaiaedr3` | Flag indicating whether E/DR3 coordinates were proper motion corrected |  | boolean |
| `solution_id` | `vac_gaiaedr3` | Solution Identifier |  | integer |
| designation | `vac_gaiaedr3` | Unique source designation (unique across all Data Releases) |  | string |
| `random_index` | `vac_gaiaedr3` | Random index used to select subsets |  | integer |
| `ref_epoch` | `vac_gaiaedr3` | Reference epoch | yr | float |
| ra | `vac_gaiaedr3` | Right ascension | deg | float |
| `ra_error` | `vac_gaiaedr3` | Standard error of right ascension | mas | float |
| dec | `vac_gaiaedr3` | Declination | deg | float |
| `dec_error` | `vac_gaiaedr3` | Standard error of declination | mas | float |
| parallax | `vac_gaiaedr3` | Parallax | mas | float |
| `parallax_error` | `vac_gaiaedr3` | Standard error of parallax | mas | float |
| `parallax_over_error` | `vac_gaiaedr3` | Parallax divided by its standard error |  | float |
| pm | `vac_gaiaedr3` | Total proper motion | mas yr-1 | float |
| pmra | `vac_gaiaedr3` | Proper motion in right ascension direction | mas yr-1 | float |
| `pmra_error` | `vac_gaiaedr3` | Standard error of proper motion in right ascension direction | mas yr-1 | float |
| pmdec | `vac_gaiaedr3` | Proper motion in declination direction | mas yr-1 | float |
| `pmdec_error` | `vac_gaiaedr3` | Standard error of proper motion in declination direction | mas yr-1 | float |
| `ra_dec_corr` | `vac_gaiaedr3` | Correlation between right ascension and declination |  | float |
| `ra_parallax_corr` | `vac_gaiaedr3` | Correlation between right ascension and parallax |  | float |
| `ra_pmra_corr` | `vac_gaiaedr3` | Correlation between right ascension and proper motion in right ascension |  | float |
| `ra_pmdec_corr` | `vac_gaiaedr3` | Correlation between right ascension and proper motion in declination |  | float |
| `dec_parallax_corr` | `vac_gaiaedr3` | Correlation between declination and parallax |  | float |
| `dec_pmra_corr` | `vac_gaiaedr3` | Correlation between declination and proper motion in right ascension |  | float |
| `dec_pmdec_corr` | `vac_gaiaedr3` | Correlation between declination and proper motion in declination |  | float |
| `parallax_pmra_corr` | `vac_gaiaedr3` | Correlation between parallax and proper motion in right ascension |  | float |
| `parallax_pmdec_corr` | `vac_gaiaedr3` | Correlation between parallax and proper motion in declination |  | float |
| `pmra_pmdec_corr` | `vac_gaiaedr3` | Correlation between proper motion in right ascension and proper motion in declination |  | float |
| `astrometric_n_obs_al` | `vac_gaiaedr3` | Total number of observations AL |  | integer |
| `astrometric_n_obs_ac` | `vac_gaiaedr3` | Total number of observations AC |  | integer |
| `astrometric_n_good_obs_al` | `vac_gaiaedr3` | Number of good observations AL |  | integer |
| `astrometric_n_bad_obs_al` | `vac_gaiaedr3` | Number of bad observations AL |  | integer |
| `astrometric_gof_al` | `vac_gaiaedr3` | Goodness of fit statistic of model wrt along-scan observations |  | float |
| `astrometric_chi2_al` | `vac_gaiaedr3` | AL χ-square value |  | float |
| `astrometric_excess_noise` | `vac_gaiaedr3` | Excess noise of the source | mas | float |
| `astrometric_excess_noise_sig` | `vac_gaiaedr3` | Significance of excess noise |  | float |
| `astrometric_params_solved` | `vac_gaiaedr3` | Which parameters have been solved for? |  | integer |
| `astrometric_primary_flag` | `vac_gaiaedr3` | Primary or seconday |  | boolean |
| `nu_eff_used_in_astrometry` | `vac_gaiaedr3` | Effective wavenumber of the source used in the astrometric solution | um-1 | float |
| `pseudocolour` | `vac_gaiaedr3` | Astrometrically estimated pseudocolour of the source | um-1 | float |
| `pseudocolour_error` | `vac_gaiaedr3` | Standard error of the pseudocolour of the source | um-1 | float |
| `ra_pseudocolour_corr` | `vac_gaiaedr3` | Correlation between right ascension and pseudocolour |  | float |
| `dec_pseudocolour_corr` | `vac_gaiaedr3` | Correlation between declination and pseudocolour |  | float |
| `parallax_pseudocolour_corr` | `vac_gaiaedr3` | Correlation between parallax and pseudocolour |  | float |
| `pmra_pseudocolour_corr` | `vac_gaiaedr3` | Correlation between proper motion in right asension and pseudocolour |  | float |
| `pmdec_pseudocolour_corr` | `vac_gaiaedr3` | Correlation between proper motion in declination and pseudocolour |  | float |
| `astrometric_matched_transits` | `vac_gaiaedr3` | Matched FOV transits used in the AGIS solution |  | integer |
| `visibility_periods_used` | `vac_gaiaedr3` | Number of visibility periods used in Astrometric solution |  | integer |
| `astrometric_sigma5d_max` | `vac_gaiaedr3` | The longest semi-major axis of the 5-d error ellipsoid | mas | float |
| `matched_transits` | `vac_gaiaedr3` | The number of transits matched to this source |  | integer |
| `new_matched_transits` | `vac_gaiaedr3` | The number of transits newly incorporated into an existing source in the current cycle |  | integer |
| `matched_transits_removed` | `vac_gaiaedr3` | The number of transits removed from an existing source in the current cycle |  | integer |
| `ipd_gof_harmonic_amplitude` | `vac_gaiaedr3` | Amplitude of the IPD GoF versus position angle of scan |  | float |
| `ipd_gof_harmonic_phase` | `vac_gaiaedr3` | Phase of the IPD GoF versus position angle of scan | deg | float |
| `ipd_frac_multi_peak` | `vac_gaiaedr3` | Percent of successful-IPD windows with more than one peak |  | integer |
| `ipd_frac_odd_win` | `vac_gaiaedr3` | Percent of transits with truncated windows or multiple gate |  | integer |
| `ruwe` | `vac_gaiaedr3` | Renormalised unit weight error |  | float |
| `scan_direction_strength_k1` | `vac_gaiaedr3` | Degree of concentration of scan directions across the source |  | float |
| `scan_direction_strength_k2` | `vac_gaiaedr3` | Degree of concentration of scan directions across the source |  | float |
| `scan_direction_strength_k3` | `vac_gaiaedr3` | Degree of concentration of scan directions across the source |  | float |
| `scan_direction_strength_k4` | `vac_gaiaedr3` | Degree of concentration of scan directions across the source |  | float |
| `scan_direction_mean_k1` | `vac_gaiaedr3` | Mean position angle of scan directions across the source | deg | float |
| `scan_direction_mean_k2` | `vac_gaiaedr3` | Mean position angle of scan directions across the source | deg | float |
| `scan_direction_mean_k3` | `vac_gaiaedr3` | Mean position angle of scan directions across the source | deg | float |
| `scan_direction_mean_k4` | `vac_gaiaedr3` | Mean position angle of scan directions across the source | deg | float |
| `duplicated_source` | `vac_gaiaedr3` | Source with multiple source identifiers |  | boolean |
| `phot_g_n_obs` | `vac_gaiaedr3` | Number of observations contributing to G photometry |  | integer |
| `phot_g_mean_flux` | `vac_gaiaedr3` | G-band mean flux | 'electron'.s**-1 | float |
| `phot_g_mean_flux_error` | `vac_gaiaedr3` | Error on G-band mean flux | 'electron'.s**-1 | float |
| `phot_g_mean_flux_over_error` | `vac_gaiaedr3` | G-band mean flux divided by its error |  | float |
| `phot_g_mean_mag` | `vac_gaiaedr3` | G-band mean magnitude | mag | float |
| `phot_bp_n_obs` | `vac_gaiaedr3` | Number of observations contributing to BP photometry |  | integer |
| `phot_bp_mean_flux` | `vac_gaiaedr3` | Integrated BP mean flux | 'electron'.s**-1 | float |
| `phot_bp_mean_flux_error` | `vac_gaiaedr3` | Error on the integrated BP mean flux | 'electron'.s**-1 | float |
| `phot_bp_mean_flux_over_error` | `vac_gaiaedr3` | Integrated BP mean flux divided by its error |  | float |
| `phot_bp_mean_mag` | `vac_gaiaedr3` | Integrated BP mean magnitude | mag | float |
| `phot_rp_n_obs` | `vac_gaiaedr3` | Number of observations contributing to RP photometry |  | integer |
| `phot_rp_mean_flux` | `vac_gaiaedr3` | Integrated RP mean flux | 'electron'.s**-1 | float |
| `phot_rp_mean_flux_error` | `vac_gaiaedr3` | Error on the integrated RP mean flux | 'electron'.s**-1 | float |
| `phot_rp_mean_flux_over_error` | `vac_gaiaedr3` | Integrated RP mean flux divided by its error |  | float |
| `phot_rp_mean_mag` | `vac_gaiaedr3` | Integrated RP mean magnitude | mag | float |
| `phot_bp_n_contaminated_transits` | `vac_gaiaedr3` | Number of BP contaminated transits |  | integer |
| `phot_bp_n_blended_transits` | `vac_gaiaedr3` | Number of BP blended transits |  | integer |
| `phot_rp_n_contaminated_transits` | `vac_gaiaedr3` | Number of RP contaminated transits |  | integer |
| `phot_rp_n_blended_transits` | `vac_gaiaedr3` | Number of RP blended transits |  | integer |
| `phot_proc_mode` | `vac_gaiaedr3` | Photometry processing mode |  | integer |
| `phot_bp_rp_excess_factor` | `vac_gaiaedr3` | BP/RP excess factor |  | float |
| `bp_rp` | `vac_gaiaedr3` | BP - RP colour | mag | float |
| `bp_g` | `vac_gaiaedr3` | BP - G colour | mag | float |
| `g_rp` | `vac_gaiaedr3` | G - RP colour | mag | float |
| `dr2_rv_nb_transits` | `vac_gaiaedr3` | Number of transits used to compute radial velocity in Gaia DR2 |  | integer |
| `dr2_rv_template_teff` | `vac_gaiaedr3` | Teff of the template used to compute radial velocity in Gaia DR2 | K | float |
| `dr2_rv_template_logg` | `vac_gaiaedr3` | logg of the template used to compute radial velocity in Gaia DR2 | log(cm.s**-2) | float |
| `dr2_rv_template_fe_h` | `vac_gaiaedr3` | Fe/H of the template used to compute radial velocity in Gaia DR2 | dex | float |
| `l` | `vac_gaiaedr3` | Galactic longitude | deg | float |
| `b` | `vac_gaiaedr3` | Galactic latitude | deg | float |
| `ecl_lon` | `vac_gaiaedr3` | Ecliptic longitude | deg | float |
| `ecl_lat` | `vac_gaiaedr3` | Ecliptic latitude | deg | float |
| `zpt_ll2020` | `vac_gaiaedr3` | Parallax Zeropoint following [Lindegren et al (2020)](https://doi.org/10.1051/0004-6361/202039653) | mas | float |
| `parallax_corr` | `vac_gaiaedr3` | Parallax corrected by subtracting `zpt_ll2020` | mas | float |
| `r_med_geo` | `vac_gaiaedr3` | The median of the geometric distance posterior. The geometric distance estimate. | pc | float |
| `r_lo_geo` | `vac_gaiaedr3` | The 16th percentile of the geometric distance posterior. The lower 1-sigma-like bound on the confidence interval. | pc | float |
| `r_hi_geo` | `vac_gaiaedr3` | The 84th percentile of the geometric distance posterior. The upper 1-sigma-like bound on the confidence interval. | pc | float |
| `r_med_photogeo` | `vac_gaiaedr3` | The median of the photogeometric distance posterior. The photogeometric distance estimate. | pc | float |
| `r_lo_photogeo` | `vac_gaiaedr3` | The 16th percentile of the photogeometric distance posterior. The lower 1-sigma-like bound on the confidence interval. | pc | float |
| `r_hi_photogeo` | `vac_gaiaedr3` | The 84th percentile of the photogeometric distance posterior. The upper 1-sigma-like bound on the confidence interval. | pc | float |
| `flag_edr3dist` | `vac_gaiaedr3` | Additional information on the solution. Do not use for filtering (see table note in the reference URL). |  | string


### Available abundance columns

To save space in the [table above](#galah-dr3-catalogues-table-schema), the columns related to abundances were collapsed in single entries (e.g., `X_fe`). Below we list all of the abundance-related columns.

| Placeholder column name | All possible column names | Found in these tables |
| :------ |:--- | :--- |
| `X_fe` | `Li_fe`, `C_fe`, `O_fe`, `Na_fe`, `Mg_fe`, `Al_fe`, `Si_fe`, `K_fe`, `Ca_fe`, `Sc_fe`, `Sc2_fe`, `Ti_fe`, `Ti2_fe`, `V_fe`, `Cr_fe`, `Cr2_fe`, `Mn_fe`, `Co_fe`, `Ni_fe`, `Cu_fe`, `Zn_fe`, `Rb_fe`, `Sr_fe`, `Y_fe`, `Zr_fe`, `Mo_fe`, `Ru_fe`, `Ba_fe`, `La_fe`, `Ce_fe`, `Nd_fe`, `Sm_fe`, `Eu_fe`, `Li_fe`, `C_fe`, `O_fe`, `Na_fe`, `Mg_fe`, `Al_fe`, `Si_fe`, `K_fe`, `Ca_fe`, `Sc_fe`, `Sc2_fe`, `Ti_fe`, `Ti2_fe`, `V_fe`, `Cr_fe`, `Cr2_fe`, `Mn_fe`, `Co_fe`, `Ni_fe`, `Cu_fe`, `Zn_fe`, `Rb_fe`, `Sr_fe`, `Y_fe`, `Zr_fe`, `Mo_fe`, `Ru_fe`, `Ba_fe`, `La_fe`, `Ce_fe`, `Nd_fe`, `Sm_fe`, `Eu_fe` | `main_spec`, `main_star` |
| `e_X_fe` | `e_Li_fe`, `e_C_fe`, `e_O_fe`, `e_Na_fe`, `e_Mg_fe`, `e_Al_fe`, `e_Si_fe`, `e_K_fe`, `e_Ca_fe`, `e_Sc_fe`, `e_Sc2_fe`, `e_Ti_fe`, `e_Ti2_fe`, `e_V_fe`, `e_Cr_fe`, `e_Cr2_fe`, `e_Mn_fe`, `e_Co_fe`, `e_Ni_fe`, `e_Cu_fe`, `e_Zn_fe`, `e_Rb_fe`, `e_Sr_fe`, `e_Y_fe`, `e_Zr_fe`, `e_Mo_fe`, `e_Ru_fe`, `e_Ba_fe`, `e_La_fe`, `e_Ce_fe`, `e_Nd_fe`, `e_Sm_fe`, `e_Eu_fe`, `e_Li_fe`, `e_C_fe`, `e_O_fe`, `e_Na_fe`, `e_Mg_fe`, `e_Al_fe`, `e_Si_fe`, `e_K_fe`, `e_Ca_fe`, `e_Sc_fe`, `e_Sc2_fe`, `e_Ti_fe`, `e_Ti2_fe`, `e_V_fe`, `e_Cr_fe`, `e_Cr2_fe`, `e_Mn_fe`, `e_Co_fe`, `e_Ni_fe`, `e_Cu_fe`, `e_Zn_fe`, `e_Rb_fe`, `e_Sr_fe`, `e_Y_fe`, `e_Zr_fe`, `e_Mo_fe`, `e_Ru_fe`, `e_Ba_fe`, `e_La_fe`, `e_Ce_fe`, `e_Nd_fe`, `e_Sm_fe`, `e_Eu_fe` | `main_spec`, `main_star` |
| `nr_X_fe` | `nr_Li_fe`, `nr_C_fe`, `nr_O_fe`, `nr_Na_fe`, `nr_Mg_fe`, `nr_Al_fe`, `nr_Si_fe`, `nr_K_fe`, `nr_Ca_fe`, `nr_Sc_fe`, `nr_Sc2_fe`, `nr_Ti_fe`, `nr_Ti2_fe`, `nr_V_fe`, `nr_Cr_fe`, `nr_Cr2_fe`, `nr_Mn_fe`, `nr_Co_fe`, `nr_Ni_fe`, `nr_Cu_fe`, `nr_Zn_fe`, `nr_Rb_fe`, `nr_Sr_fe`, `nr_Y_fe`, `nr_Zr_fe`, `nr_Mo_fe`, `nr_Ru_fe`, `nr_Ba_fe`, `nr_La_fe`, `nr_Ce_fe`, `nr_Nd_fe`, `nr_Sm_fe`, `nr_Eu_fe`, `nr_Li_fe`, `nr_C_fe`, `nr_O_fe`, `nr_Na_fe`, `nr_Mg_fe`, `nr_Al_fe`, `nr_Si_fe`, `nr_K_fe`, `nr_Ca_fe`, `nr_Sc_fe`, `nr_Sc2_fe`, `nr_Ti_fe`, `nr_Ti2_fe`, `nr_V_fe`, `nr_Cr_fe`, `nr_Cr2_fe`, `nr_Mn_fe`, `nr_Co_fe`, `nr_Ni_fe`, `nr_Cu_fe`, `nr_Zn_fe`, `nr_Rb_fe`, `nr_Sr_fe`, `nr_Y_fe`, `nr_Zr_fe`, `nr_Mo_fe`, `nr_Ru_fe`, `nr_Ba_fe`, `nr_La_fe`, `nr_Ce_fe`, `nr_Nd_fe`, `nr_Sm_fe`, `nr_Eu_fe` | `main_spec`, `main_star` |
| `flag_X_fe` | `flag_Li_fe`, `flag_C_fe`, `flag_O_fe`, `flag_Na_fe`, `flag_Mg_fe`, `flag_Al_fe`, `flag_Si_fe`, `flag_K_fe`, `flag_Ca_fe`, `flag_Sc_fe`, `flag_Sc2_fe`, `flag_Ti_fe`, `flag_Ti2_fe`, `flag_V_fe`, `flag_Cr_fe`, `flag_Cr2_fe`, `flag_Mn_fe`, `flag_Co_fe`, `flag_Ni_fe`, `flag_Cu_fe`, `flag_Zn_fe`, `flag_Rb_fe`, `flag_Sr_fe`, `flag_Y_fe`, `flag_Zr_fe`, `flag_Mo_fe`, `flag_Ru_fe`, `flag_Ba_fe`, `flag_La_fe`, `flag_Ce_fe`, `flag_Nd_fe`, `flag_Sm_fe`, `flag_Eu_fe`, `flag_Li_fe`, `flag_C_fe`, `flag_O_fe`, `flag_Na_fe`, `flag_Mg_fe`, `flag_Al_fe`, `flag_Si_fe`, `flag_K_fe`, `flag_Ca_fe`, `flag_Sc_fe`, `flag_Sc2_fe`, `flag_Ti_fe`, `flag_Ti2_fe`, `flag_V_fe`, `flag_Cr_fe`, `flag_Cr2_fe`, `flag_Mn_fe`, `flag_Co_fe`, `flag_Ni_fe`, `flag_Cu_fe`, `flag_Zn_fe`, `flag_Rb_fe`, `flag_Sr_fe`, `flag_Y_fe`, `flag_Zr_fe`, `flag_Mo_fe`, `flag_Ru_fe`, `flag_Ba_fe`, `flag_La_fe`, `flag_Ce_fe`, `flag_Nd_fe`, `flag_Sm_fe`, `flag_Eu_fe` | `main_spec`, `main_star` |
| `ind_X1234_fe` | `ind_Li6708_fe`, `ind_Li6708_NoRV_fe`, `ind_C6588_fe`, `ind_O_fe`, `ind_Na_fe`, `ind_Mg5711_fe`, `ind_Al_fe`, `ind_Si_fe`, `ind_K7699_fe`, `ind_Ca_fe`, `ind_Sc_fe`, `ind_Ti4758_fe`, `ind_Ti4759_fe`, `ind_Ti4778_fe`, `ind_Ti4782_fe`, `ind_Ti4798_fe`, `ind_Ti4802_fe`, `ind_Ti4820_fe`, `ind_Ti5689_fe`, `ind_Ti5716_fe`, `ind_Ti5720_fe`, `ind_Ti5739_fe`, `ind_Ti5866_fe`, `ind_Ti6599_fe`, `ind_Ti6717_fe`, `ind_Ti7853_fe`, `ind_Ti4720_fe`, `ind_Ti4765_fe`, `ind_Ti4799_fe`, `ind_Ti4849_fe`, `ind_Ti4866_fe`, `ind_Ti4874_fe`, `ind_V4832_fe`, `ind_V4784_fe`, `ind_V4797_fe`, `ind_Cr_fe`, `ind_Mn_fe`, `ind_Co4781_fe`, `ind_Co4900_fe`, `ind_Co5647_fe`, `ind_Co6490_fe`, `ind_Co6551_fe`, `ind_Co6632_fe`, `ind_Co6679_fe`, `ind_Co7713_fe`, `ind_Co7838_fe`, `ind_Ni5847_fe`, `ind_Ni6586_fe`, `ind_Cu5700_fe`, `ind_Cu5782_fe`, `ind_Zn4722_fe`, `ind_Zn4811_fe`, `ind_Rb7800_fe`, `ind_Sr6550_fe`, `ind_Y_fe`, `ind_Y4820_fe`, `ind_Y4855_fe`, `ind_Y4884_fe`, `ind_Y5663_fe`, `ind_Y5729_fe`, `ind_Zr4739_fe`, `ind_Zr4772_fe`, `ind_Zr4806_fe`, `ind_Zr4828_fe`, `ind_Zr5681_fe`, `ind_Mo5689_fe`, `ind_Mo5751_fe`, `ind_Mo5858_fe`, `ind_Mo6619_fe`, `ind_Ru4758_fe`, `ind_Ru4869_fe`, `ind_Ru5699_fe`, `ind_Ba_fe`, `ind_La4716_fe`, `ind_La4749_fe`, `ind_La4804_fe`, `ind_La5806_fe`, `ind_Ce4774_fe`, `ind_Nd4811_fe`, `ind_Nd5741_fe`, `ind_Nd5770_fe`, `ind_Nd5812_fe`, `ind_Nd5842_fe`, `ind_Sm4720_fe`, `ind_Sm4792_fe`, `ind_Sm4837_fe`, `ind_Sm4848_fe`, `ind_Sm4854_fe`, `ind_Eu5819_fe`, `ind_Eu6645_fe` | `main_spec` |
| `ind_cov_e_X1234` | `ind_cov_e_Li6708`, `ind_cov_e_Li6708_NoRV`, `ind_cov_e_C6588`, `ind_cov_e_O`, `ind_cov_e_Na`, `ind_cov_e_Mg5711`, `ind_cov_e_Al`, `ind_cov_e_Si`, `ind_cov_e_K7699`, `ind_cov_e_Ca`, `ind_cov_e_Sc`, `ind_cov_e_Ti4758`, `ind_cov_e_Ti4759`, `ind_cov_e_Ti4778`, `ind_cov_e_Ti4782`, `ind_cov_e_Ti4798`, `ind_cov_e_Ti4802`, `ind_cov_e_Ti4820`, `ind_cov_e_Ti5689`, `ind_cov_e_Ti5716`, `ind_cov_e_Ti5720`, `ind_cov_e_Ti5739`, `ind_cov_e_Ti5866`, `ind_cov_e_Ti6599`, `ind_cov_e_Ti6717`, `ind_cov_e_Ti7853`, `ind_cov_e_Ti4720`, `ind_cov_e_Ti4765`, `ind_cov_e_Ti4799`, `ind_cov_e_Ti4849`, `ind_cov_e_Ti4866`, `ind_cov_e_Ti4874`, `ind_cov_e_V4832`, `ind_cov_e_V4784`, `ind_cov_e_V4797`, `ind_cov_e_Cr`, `ind_cov_e_Mn`, `ind_cov_e_Co4781`, `ind_cov_e_Co4900`, `ind_cov_e_Co5647`, `ind_cov_e_Co6490`, `ind_cov_e_Co6551`, `ind_cov_e_Co6632`, `ind_cov_e_Co6679`, `ind_cov_e_Co7713`, `ind_cov_e_Co7838`, `ind_cov_e_Ni5847`, `ind_cov_e_Ni6586`, `ind_cov_e_Cu5700`, `ind_cov_e_Cu5782`, `ind_cov_e_Zn4722`, `ind_cov_e_Zn4811`, `ind_cov_e_Rb7800`, `ind_cov_e_Sr6550`, `ind_cov_e_Y`, `ind_cov_e_Y4820`, `ind_cov_e_Y4855`, `ind_cov_e_Y4884`, `ind_cov_e_Y5663`, `ind_cov_e_Y5729`, `ind_cov_e_Zr4739`, `ind_cov_e_Zr4772`, `ind_cov_e_Zr4806`, `ind_cov_e_Zr4828`, `ind_cov_e_Zr5681`, `ind_cov_e_Mo5689`, `ind_cov_e_Mo5751`, `ind_cov_e_Mo5858`, `ind_cov_e_Mo6619`, `ind_cov_e_Ru4758`, `ind_cov_e_Ru4869`, `ind_cov_e_Ru5699`, `ind_cov_e_Ba`, `ind_cov_e_La4716`, `ind_cov_e_La4749`, `ind_cov_e_La4804`, `ind_cov_e_La5806`, `ind_cov_e_Ce4774`, `ind_cov_e_Nd4811`, `ind_cov_e_Nd5741`, `ind_cov_e_Nd5770`, `ind_cov_e_Nd5812`, `ind_cov_e_Nd5842`, `ind_cov_e_Sm4720`, `ind_cov_e_Sm4792`, `ind_cov_e_Sm4837`, `ind_cov_e_Sm4848`, `ind_cov_e_Sm4854`, `ind_cov_e_Eu5819`, `ind_cov_e_Eu6645` | `main_spec` |
| `ind_flag_X1234` | `ind_flag_Li6708`, `ind_flag_Li6708_NoRV`, `ind_flag_C6588`, `ind_flag_O`, `ind_flag_Na`, `ind_flag_Mg5711`, `ind_flag_Al`, `ind_flag_Si`, `ind_flag_K7699`, `ind_flag_Ca`, `ind_flag_Sc`, `ind_flag_Ti4758`, `ind_flag_Ti4759`, `ind_flag_Ti4778`, `ind_flag_Ti4782`, `ind_flag_Ti4798`, `ind_flag_Ti4802`, `ind_flag_Ti4820`, `ind_flag_Ti5689`, `ind_flag_Ti5716`, `ind_flag_Ti5720`, `ind_flag_Ti5739`, `ind_flag_Ti5866`, `ind_flag_Ti6599`, `ind_flag_Ti6717`, `ind_flag_Ti7853`, `ind_flag_Ti4720`, `ind_flag_Ti4765`, `ind_flag_Ti4799`, `ind_flag_Ti4849`, `ind_flag_Ti4866`, `ind_flag_Ti4874`, `ind_flag_V4832`, `ind_flag_V4784`, `ind_flag_V4797`, `ind_flag_Cr`, `ind_flag_Mn`, `ind_flag_Co4781`, `ind_flag_Co4900`, `ind_flag_Co5647`, `ind_flag_Co6490`, `ind_flag_Co6551`, `ind_flag_Co6632`, `ind_flag_Co6679`, `ind_flag_Co7713`, `ind_flag_Co7838`, `ind_flag_Ni5847`, `ind_flag_Ni6586`, `ind_flag_Cu5700`, `ind_flag_Cu5782`, `ind_flag_Zn4722`, `ind_flag_Zn4811`, `ind_flag_Rb7800`, `ind_flag_Sr6550`, `ind_flag_Y`, `ind_flag_Y4820`, `ind_flag_Y4855`, `ind_flag_Y4884`, `ind_flag_Y5663`, `ind_flag_Y5729`, `ind_flag_Zr4739`, `ind_flag_Zr4772`, `ind_flag_Zr4806`, `ind_flag_Zr4828`, `ind_flag_Zr5681`, `ind_flag_Mo5689`, `ind_flag_Mo5751`, `ind_flag_Mo5858`, `ind_flag_Mo6619`, `ind_flag_Ru4758`, `ind_flag_Ru4869`, `ind_flag_Ru5699`, `ind_flag_Ba`, `ind_flag_La4716`, `ind_flag_La4749`, `ind_flag_La4804`, `ind_flag_La5806`, `ind_flag_Ce4774`, `ind_flag_Nd4811`, `ind_flag_Nd5741`, `ind_flag_Nd5770`, `ind_flag_Nd5812`, `ind_flag_Nd5842`, `ind_flag_Sm4720`, `ind_flag_Sm4792`, `ind_flag_Sm4837`, `ind_flag_Sm4848`, `ind_flag_Sm4854`, `ind_flag_Eu5819`, `ind_flag_Eu6645` | `main_spec` |
