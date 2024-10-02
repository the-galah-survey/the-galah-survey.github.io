---
layout: page
title: Table Schema
subtitle: Fourth Data Release
---

{: .main_blockquote}
This page gives the schema (or data model) for the [GALAH DR4 main and value-added catalogues](/dr4/the_catalogues).

{: .box-warning}
We strongly recommend reading the [recommended columns section of our Best Practices page](/dr4/using_the_data/#recommended-columns). T

{: .box-warning}
The `sobject_id` column should be used for joining the catalogues.

* This text gets replaced.
{:toc}

---

### `galah_dr4_allstar_240705` and `galah_dr4_allspec_240705`

Unless otherwise noted, all columns are found in both `galah_dr4_allstar_240705` and `galah_dr4_allspec_240705`. To save space in the table below, the columns related to abundances have been collapsed in single entries (e.g., `X_fe`), and they are all listed in a table at the bottom of this page.


| Column name | Description | units | type |
| :------ |:--- | :--- | :--- |
| `sobject_id` | GALAH identifier|meta.id | integer |
| `tmass_id` | 2MASS identifier|meta.id.cross | string |
| `gaiadr3_source_id` | Gaia DR3 source_id|meta.id.cross | integer |
| `survey_name` | HERMES-2dF Survey/Program/Pointing (other if not available)|meta.id | string |
| `field_id` | GALAH Field ID (-1 if not available)|meta.number | integer |
| `setup` | Analysis setup: single/binary/coadds|meta.version | string |
| `mjd` | Modified Julian Date|time.epoch | float |
| `ra` | Gaia DR3 Right ascension|pos.eq.ra;meta.main | float |
| `dec` | Gaia DR3 Declination|pos.eq.dec;meta.main | float |
| `flag_sp` | Major spectroscopic quality bitmask flag|meta.code.qual,stat.fit | integer |
| `flag_sp_fit` | Major spectroscopic fitting quality bitmask flag|meta.code.qual,stat.fit | integer |
| `opt_loop` | Nr of optimisation loops used for fitting|meta.modelled | integer |
| `flag_red` | Quality bitmask flag of reduction pipeline|meta.code.qual,stat.fit | integer |
| `snr_px_ccd1` | Average signal-to-noise ratio (per pixel) of CCD1|stat.snr | float |
| `snr_px_ccd2` | Average signal-to-noise ratio (per pixel) of CCD2|stat.snr | float |
| `snr_px_ccd3` | Average signal-to-noise ratio (per pixel) of CCD3|stat.snr | float |
| `snr_px_ccd4` | Average signal-to-noise ratio (per pixel) of CCD4|stat.snr | float |
| `chi2_sp` | Chi2 value of spectroscopic fitting|stat.fit.chi2 | float |
| `px_used_perc` | Percentage of spectrum used for spectroscopic fit|fit.param | integer |
| `model_name` | Neural network model used for creating synthetic spectra|meta.modelled | string |
| `closest_model` | Neural network model closest for Teff/logg/[Fe/H] combination|meta.modelled | string |
| `comp_time` | Computation time spent on spectrum|meta.number | float |
| `fit_global_rv` | Are spectra coadded (without RV shifts) and then a global RV fitted?|meta.modelled | boolean |
| `rv_comp_nr` | Number of peaks in RV cross-correlation function (CCF), only in `allspec` table |meta.number | integer |
| `rv_comp_1` | Radial velocity of primary source|spect.dopplerVeloc.opt | float |
| `e_rv_comp_1` | Uncertainty of rv_comp_1|stat.error;spect.dopplerVeloc.opt | float |
| `rv_comp_1_p` | Prominence of rv_comp_1 in CCF, only in `allspec` table |stat.param | float |
| `rv_comp_2` | Radial velocity of potential secondary source|spect.dopplerVeloc.opt | float |
| `e_rv_comp_2` | Uncertainty of rv_comp_2, only in `allstar` table|stat.error;spect.dopplerVeloc.opt | float |
| `rv_comp_2_h` | Height of rv_comp_2 in CCF, only in `allspec` table |stat.param | float |
| `rv_comp_2_p` | Prominence of rv_comp_2o in CCF, only in `allspec` table |stat.param | float |
| `rv_gaia_dr3` | Radial velocity in Gaia DR3|spect.dopplerVeloc.opt | float |
| `e_rv_gaia_dr3` | Uncertainty of rv_gaia_dr3|stat.error;spect.dopplerVeloc.opt | float |
| `v_bary_eff` | Barycentric velocity applied to reduced spectra|arith.factor;phys.veloc | float |
| `teff` | Spectroscopic effective temperature (used for fitting)|phys.temperature.effective | float |
| `e_teff` | Uncertainty teff|stat.error;phys.temperature.effective | float |
| `logg` | Surface gravity adjusted via parallax information|phys.gravity | float |
| `e_logg` | Uncertainty logg_plx|stat.error;phys.gravity | float |
| `fe_h` | Abundance of Fe and all other elements not fitted in GALAH (Fe: 1D-NLTE)|phys.abund.Fe | float |
| `e_fe_h` | Uncertainty fe_h|stat.error;phys.abund.Fe | float |
| `flag_fe_h` | Quality flag fe_h|meta.code.qual,stat.fit | integer |
| `vmic` | Microturbulence velocity (fitted)|phys.veloc.microTurb | float |
| `e_vmic` | Uncertainty vmic|stat.error;phys.veloc.microTurb | float |
| `vsini` | Broadening velocity (fitted sme.vsini with sme.vmac=0)|phys.veloc.rotat | float |
| `e_vsini` | Uncertainty of vsini|stat.error;phys.veloc.rotat | float |
| `nn_li_fe` | Neural Network Elemental abundance for [Li/Fe], only in `allstar` table |phys.abund | float |
| `nn_e_li_fe` | Uncertainty nn_li_fe, only in `allstar` table |phys.abund | float |
| `nn_flag_li_fe` | Quality bitmask flag of nn_li_fe, only in `allstar` table|meta.code.qual,stat.fit | integer |
| `li_fe` | Elemental abundance for [Li/Fe], only in `allspec` table |phys.abund | float |
| `e_li_fe` | Uncertainty Li_fe, only in `allspec` table |stat.error;phys.abund | float |
| `flag_li_fe` | Quality bitmask flag of Li_fe, only in `allspec` table |meta.code.qual,stat.fit | integer |
| `X_fe` | Elemental abundance for [X/Fe]|phys.abund | float |
| `e_X_fe` | Uncertainty X_fe|stat.error;phys.abund | float |
| `flag_X_fe` | [Quality bitmask flag of `X_fe`](/dr4/flags/#flag_x_fe) |meta.code.qual,stat.fit | integer |
| `mass` | Mass used for calculating logg(plx), only in `allstar` table |fit.param;phys.mass | float |
| `age` | Age estimated when calculating mass, only in `allstar` table |fit.param;time.age | float |
| `bc_ks` | Bolometric Correction of Ks, BC(Ks), used for calculating logg(plx)|phot.mag.bc;em.IR.K | float |
| `a_ks` | Attenuation in Ks-band A(Ks) used for calculating logg(plx)|phys.absorption.gal | float |
| `lbol` | Bolometric Luminosity used for calculating logg(plx)|fit.param;phys.luminosity | float |
| `r_med` | Median Distance used for calculating logg(plx)|pos.distance | float |
| `r_lo` | Lower Limit Distance used for calculating logg(plx)|stat.error;stat.min;pos.distance | float |
| `r_hi` | Higher Limit Distance used for calculating logg(plx)|stat.error;stat.max;pos.distance | float |
| `sb2_rv_16` | 16th perc. radial velocity of fit to syn-obs residuals|stat.error;spect.dopplerVeloc.opt | float |
| `sb2_rv_50` | 50th perc. radial velocity of fit to syn-obs residuals|spect.dopplerVeloc.opt | float |
| `sb2_rv_84` | 84th perc. radial velocity of fit to syn-obs residuals|stat.error;spect.dopplerVeloc.opt | float |
| `ew_h_beta` | Equivalent Width of observed Hbeta core|fit.param;spect.line.eqWidth | float |
| `ew_h_alpha` | Equivalent Width of observed Halpha core|fit.param;spect.line.eqWidth | float |
| `res_h_beta` | Residual Equivalent Width of syn-obs residuals at Hbeta core|fit.param;spect.line.eqWidth | float |
| `res_h_alpha` | Residual Equivalent Width of syn-obs residuals at Halpha core|fit.param;spect.line.eqWidth | float |
| `ew_k_is` | Equivalent Width of fit for K7699 Interstellar Line|fit.param;spect.line.eqWidth | float |
| `sigma_k_is` | Sigma auf Gaussian fit for K7699 Interstellar Line|fit.param | float |
| `rv_k_is` | Radial velocity of fit to syn-obs residuals around K7699 line|fit.param;spect.dopplerVeloc.opt | float |
| `ew_dib5780` | Equivalent Width of fit for 5780 Diffiuse Interstellar Band|fit.param;spect.line.eqWidth | float |
| `sigma_dib5780` | Sigma auf Gaussian fit for 5780 DIB|fit.param | float |
| `rv_dib5780` | Radial velocity of fit to syn-obs residuals around 5780 DIB|fit.param;spect.dopplerVeloc.opt | float |
| `ew_dib5797` | Equivalent Width of fit for 5797 Diffiuse Interstellar Band|fit.param;spect.line.eqWidth | float |
| `sigma_dib5797` | Sigma auf Gaussian fit for 5797 DIB|fit.param | float |
| `rv_dib5797` | Radial velocity of fit to syn-obs residuals around 5797 DIB|fit.param;spect.dopplerVeloc.opt | float |
| `ew_dib6613` | Equivalent Width of fit for 6613 Diffiuse Interstellar Band|fit.param;spect.line.eqWidth | float |
| `sigma_dib6613` | Sigma auf Gaussian fit for 6613 DIB|fit.param | float |
| `rv_dib6613` | Radial velocity of fit to syn-obs residuals around 6613 DIB|fit.param;spect.dopplerVeloc.opt | float |
| `logg_spec` | Spectroscopic surface gravity (used for fitting), only in `allspec` table |phys.gravity | float |
| `e_logg_spec` | Uncertainty logg_spec, only in `allspec` table |stat.error;phys.gravity | float |
| `ebv` | Extinction E(B-V)|phys.absorption.gal | float |
| `phot_g_mean_mag` | Gaia DR3 G-band mean magnitude|phot.mag;em.opt | float |
| `phot_bp_mean_mag` | Gaia DR3 Integrated BP mean magnitude, only in `allspec` table |phot.mag;em.opt.B | float |
| `bp_rp` | Gaia DR3 BP - RP colour|phot.color;em.opt.B;em.opt.R | float |
| `j_m` | 2MASS J-band magnitude, only in `allstar` table |phot.mag;em.IR.J | float |
| `j_msigcom` | 2MASS Uncertainty of j_m, only in `allstar` table |stat.error;phot.mag;em.IR.J | float |
| `h_m` | 2MASS H-band magnitude|phot.mag;em.IR.H | float |
| `h_msigcom` | 2MASS Uncertainty of h_m|stat.error;phot.mag;em.IR.H | float |
| `ks_m` | 2MASS Ks-band magnitude|phot.mag;em.IR.K | float |
| `ks_msigcom` | 2MASS Uncertainty of ks_m|stat.error;phot.mag;em.IR.K | float |
| `W2mag` | AllWISE W2-band magnitude|phot.mag;em.IR.4-8um | float |
| `e_W2mag` | AllWISE uncertainty of W2mag|stat.error;phot.mag | float |
| `ruwe` | Gaia DR3 Renormalised unit weight error|stat.error | float |
| `parallax` | Astrometric parallax used for GALAH DR4|pos.parallax.trig | float |
| `parallax_error` | Gaia DR3 Standard error of parallax|stat.error;pos.parallax.trig | float |
| `e_parallax` | Uncertainty of astrometric parallax used for GALAH DR4, only in `allspec` table |stat.error;pos.parallax.trig | float |
| `parallax_gaia_edr3` | Parallax reported with corrections by Gaia EDR3, only in `allspec` table |pos.parallax.trig | float
| `e_parallax_gaia_edr3` | Uncertainty of parallax reported with corrections by Gaia EDR3, only in `allspec` table |stat.error;pos.parallax.trig | float |
| `ew_li` | Equivalent width of LiI 6708 line region|spect.line.eqWidth | float |
| `e_ew_li_low` | Lower uncertainty limit of ew_li|stat.error;spect.line.eqWidth | float |
| `e_ew_li_upp` | Upper uncertainty limit of ew_li|stat.error;spect.line.eqWidth | float |
| `a_li` | Absolute Lithium abundance|phys.abund | float |
| `a_li_upp_lim` | Upper limit of a_li|stat.error;phys.abund | float |
| `e_a_li_low` | Lower uncertainty of a_li|stat.error;phys.abund | float |
| `e_a_li_upp` | Upper uncertainty of a_li|stat.error;phys.abund | float |
| `e_a_li_teff` | Teff-correlated uncertainty of a_li|stat.error;phys.abund | float |
| `flag_a_li` | Quality bitmask flag of a_li|meta.code.qual,stat.fit | integer |


#### Abundance columns

To save space in the [table above](#galah_dr4_main_allstar-and-galah_dr4_main_allspec), the columns related to abundances are collated in single entries (e.g., `X_fe`). Below we list all of the abundance-related columns.

| Placeholder column name | All possible column names
| :------ |:--- | :--- |
| `X_fe`<br/><br/>Neutral/ionised X atomic abundance | `li_fe` `c_fe` `n_fe` `o_fe` `na_fe` `mg_fe` `al_fe` `si_fe` `k_fe` `ca_fe` `sc_fe` `ti_fe` `v_fe` `cr_fe` `mn_fe` `co_fe` `ni_fe` `cu_fe` `zn_fe` `rb_fe` `sr_fe` `y_fe` `zr_fe` `mo_fe` `ru_fe` `ba_fe` `la_fe` `ce_fe` `nd_fe` `sm_fe` `eu_fe` |
| `e_X_fe`<br/><br/>Uncertainty `X_fe` | `e_li_fe` `e_c_fe` `e_n_fe` `e_o_fe` `e_na_fe` `e_mg_fe` `e_al_fe` `e_si_fe` `e_k_fe` `e_ca_fe` `e_sc_fe` `e_ti_fe` `e_v_fe` `e_cr_fe` `e_mn_fe` `e_co_fe` `e_ni_fe` `e_cu_fe` `e_zn_fe` `e_rb_fe` `e_sr_fe` `e_y_fe` `e_zr_fe` `e_mo_fe` `e_ru_fe` `e_ba_fe` `e_la_fe` `e_ce_fe` `e_nd_fe` `e_sm_fe` `e_eu_fe` |
| `flag_X_fe`<br/><br/>[Quality flag of `X_fe`](/dr4/flags/#flag_x_fe) | `flag_li_fe` `flag_c_fe` `flag_n_fe` `flag_o_fe` `flag_na_fe` `flag_mg_fe` `flag_al_fe` `flag_si_fe` `flag_k_fe` `flag_ca_fe` `flag_sc_fe` `flag_ti_fe` `flag_v_fe` `flag_cr_fe` `flag_mn_fe` `flag_co_fe` `flag_ni_fe` `flag_cu_fe` `flag_zn_fe` `flag_rb_fe` `flag_sr_fe` `flag_y_fe` `flag_zr_fe` `flag_mo_fe` `flag_ru_fe` `flag_ba_fe` `flag_la_fe` `flag_ce_fe` `flag_nd_fe` `flag_sm_fe` `flag_eu_fe` |

---

### `galah_dr4_vac_wise_tmass_gaiadr3_240705`

| Column name | Description | units | type |
| :------ |:--- | :--- | :--- |
| `sobject_id` | GALAH identifier|meta.id | integer |
| `tmass_id` | 2MASS identifier|meta.id.cross | string |
| `tmass_ph_qual` | 2MASS Photometric quality flag. Three character flag, one character per ba|meta.code.qual;phot | string |
| `raj2000` | 2MASS J2000 right ascension with respect to the ICRS|pos.eq.ra;meta.main | float |
| `dej2000` | 2MASS J2000 declination with respect to the ICRS|pos.eq.dec;meta.main | float |
| `j_m` | 2MASS J-band magnitude|phot.mag;em.IR.J | float |
| `j_msigcom` | 2MASS Uncertainty of j_m|stat.error;phot.mag;em.IR.J | float |
| `h_m` | 2MASS H-band magnitude|phot.mag;em.IR.H | float |
| `h_msigcom` | 2MASS Uncertainty of h_m|stat.error;phot.mag;em.IR.H | float |
| `ks_m` | 2MASS Ks-band magnitude|phot.mag;em.IR.K | float |
| `ks_msigcom` | 2MASS Uncertainty of ks_m|stat.error;phot.mag;em.IR.K | float |
| `wise_id` | AllWISE Sexagesimal, equatorial position-based source name in the form:?hhmm|meta.id.cross | string |
| `W1mag` | AllWISE W1 magnitude measured with profile-fitting photometry, or the magnit|phot.mag;em.IR.3-4um | float |
| `e_W1mag` | AllWISE W1 profile-fit photometric measurement uncertainty in mag units. Thi|stat.error;phot.mag | float |
| `W2mag` | AllWISE W2-band magnitude|phot.mag;em.IR.4-8um | float |
| `e_W2mag` | AllWISE uncertainty of W2mag|stat.error;phot.mag | float |
| `W3mag` | AllWISE W3 magnitude measured with profile-fitting photometry, or the magnit|phot.mag;em.IR.8-15um | float |
| `e_W3mag` | AllWISE W3 profile-fit photometric measurement uncertainty in mag units. Thi|stat.error;phot.mag | float |
| `W4mag` | AllWISE W4 magnitude measured with profile-fitting photometry, or the magnit|phot.mag;em.IR.15-30um | float |
| `e_W4mag` | AllWISE W4 profile-fit photometric measurement uncertainty in mag units. Thi|stat.error;phot.mag | float |
| `wise_ph_qual` | AllWISE Photometric quality flag.  ?Four character flag, one character per b|meta.code.qual;phot | string |
| `r_med_geo` | Bailer-Jones+ (2021) The median of the geometric distance posterior. The geometric distan|pos.distance | float |
| `r_lo_geo` | Bailer-Jones+ (2021) The 16th percentile of the geometric distance posterior. The lower 1|pos.distance;stat.min | float |
| `r_hi_geo` | Bailer-Jones+ (2021) The 84th percentile of the geometric distance posterior. The upper 1|pos.distance;stat.max | float |
| `r_med_photogeo` | Bailer-Jones+ (2021) The median of the photogeometric distance posterior. The photogeomet|pos.distance | float |
| `r_lo_photogeo` | Bailer-Jones+ (2021) The 16th percentile of the photogeometric distance posterior. The lo|pos.distance;stat.min | float |
| `r_hi_photogeo` | Bailer-Jones+ (2021) The 84th percentile of the photogeometric distance posterior. The up|pos.distance;stat.max | float |
| `calj_flag`| Bailer-Jones+ (2021) Additional information on the solution. Do not use for filtering (se|meta.code | string |
| `solution_id` | Gaia DR3 Solution Identifier|meta.version | integer |
| `designation` | Gaia DR3 Unique source designation (unique across all Data Releases)|meta.id;meta.main | string |
| `source_id` | Gaia DR3 Unique source identifier (unique within a particular Data Release)|meta.id | integer |
| `random_index` | Gaia DR3 Random index for use when selecting subsets|meta.code | integer |
| `ref_epoch` | Gaia DR3 Reference epoch|meta.ref;time.epoch | float |
| `ra` | Gaia DR3 Right ascension|pos.eq.ra;meta.main | float |
| `ra_error` | Gaia DR3 Standard error of right ascension|stat.error;pos.eq.ra | float |
| `dec` | Gaia DR3 Declination|pos.eq.dec;meta.main | float |
| `dec_error` | Gaia DR3 Standard error of declination|stat.error;pos.eq.dec | float |
| `parallax` | Astrometric parallax used for GALAH DR4|pos.parallax.trig | float |
| `parallax_error` | Gaia DR3 Standard error of parallax|stat.error;pos.parallax.trig | float |
| `parallax_over_error` | Gaia DR3 Parallax divided by its standard error|stat.snr;pos.parallax.trig | float |
| `pm` | Gaia DR3 Total proper motion|pos.pm;pos.eq | float |
| `pmra` | Gaia DR3 Proper motion in right ascension direction|pos.pm;pos.eq.ra | float |
| `pmra_error` | Gaia DR3 Standard error of proper motion in right ascension direction|stat.error;pos.pm;pos.eq.ra | float |
| `pmdec` | Gaia DR3 Proper motion in declination direction|pos.pm;pos.eq.dec | float |
| `pmdec_error` | Gaia DR3 Standard error of proper motion in declination direction|stat.error;pos.pm;pos.eq.dec | float |
| `ra_dec_corr` | Gaia DR3 Correlation between right ascension and declination|stat.correlation | float |
| `ra_parallax_corr` | Gaia DR3 Correlation between right ascension and parallax|stat.correlation | float |
| `ra_pmra_corr` | Gaia DR3 Correlation between right ascension and proper motion in right ascen|stat.correlation | float |
| `ra_pmdec_corr` | Gaia DR3 Correlation between right ascension and proper motion in declination|stat.correlation | float |
| `dec_parallax_corr` | Gaia DR3 Correlation between declination and parallax|stat.correlation | float |
| `dec_pmra_corr` | Gaia DR3 Correlation between declination and proper motion in right ascension|stat.correlation | float |
| `dec_pmdec_corr` | Gaia DR3 Correlation between declination and proper motion in declination|stat.correlation | float |
| `parallax_pmra_corr` | Gaia DR3 Correlation between parallax and proper motion in right ascension|stat.correlation | float |
| `parallax_pmdec_corr` | Gaia DR3 Correlation between parallax and proper motion in declination|stat.correlation | float |
| `pmra_pmdec_corr` | Gaia DR3 Correlation between proper motion in right ascension and proper moti|stat.correlation | float |
| `astrometric_n_obs_al` | Gaia DR3 Total number of observations in the along-scan (AL) direction|meta.number | integer |
| `astrometric_n_obs_ac` | Gaia DR3 Total number of observations in the across-scan (AC) direction|meta.number | integer |
| `astrometric_n_good_obs_al` | Gaia DR3 Number of good observations in the along-scan (AL) direction|meta.number | integer |
| `astrometric_n_bad_obs_al`| Gaia DR3 Number of bad observations in the along-scan (AL) direction|meta.number | integer |
| `astrometric_gof_al` | Gaia DR3 Goodness of fit statistic of model wrt along-scan observations|stat.fit.goodness | float |
| `astrometric_chi2_al` | Gaia DR3 AL chi-square value|stat.fit.chi2 | float |
| `astrometric_excess_noise` | Gaia DR3 Excess noise of the source|stat.value | float |
| `astrometric_excess_noise_sig` | Gaia DR3 Significance of excess noise|stat.value | float |
| `astrometric_params_solved` | Gaia DR3 Which parameters have been solved for?|meta.number | integer |
| `astrometric_primary_flag` | Gaia DR3 Primary or seconday|meta.code | boolean |
| `nu_eff_used_in_astrometry` | Gaia DR3 Effective wavenumber of the source used in the astrometric solution|em.wavenumber | float |
| `pseudocolour` | Gaia DR3 Astrometrically estimated pseudocolour of the source|em.wavenumber | float |
| `pseudocolour_error` | Gaia DR3 Standard error of the pseudocolour of the source|stat.error;em.wavenumber | float |
| `ra_pseudocolour_corr` | Gaia DR3 Correlation between right ascension and pseudocolour|stat.correlation;em.wavenumber;pos.eq.ra | float |
| `dec_pseudocolour_corr` | Gaia DR3 Correlation between declination and pseudocolour|stat.correlation;em.wavenumber;pos.eq.dec | float |
| `parallax_pseudocolour_corr` | Gaia DR3 Correlation between parallax and pseudocolour|stat.correlation;em.wavenumber;pos.parallax | float |
| `pmra_pseudocolour_corr` | Gaia DR3 Correlation between proper motion in right asension and pseudocolour|stat.correlation;em.wavenumber;pos.pm;pos.eq.ra | float |
| `pmdec_pseudocolour_corr` | Gaia DR3 Correlation between proper motion in declination and pseudocolour|stat.correlation;em.wavenumber;pos.pm;pos.eq.dec | float |
| `astrometric_matched_transits` | Gaia DR3 Matched FOV transits used in the AGIS solution|meta.number | integer |
| `visibility_periods_used` | Gaia DR3 Number of visibility periods used in Astrometric solution|meta.number | integer |
| `astrometric_sigma5d_max` | Gaia DR3 The longest semi-major axis of the 5-d error ellipsoid|stat;pos.errorEllipse | float |
| `matched_transits` | Gaia DR3 The number of transits matched to this source|meta.number | integer |
| `new_matched_transits` | Gaia DR3 The number of transits newly incorporated into an existing source in|meta.number | integer |
| `matched_transits_removed` | Gaia DR3 The number of transits removed from an existing source in the curren|meta.number | integer |
| `ipd_gof_harmonic_amplitude` | Gaia DR3 Amplitude of the IPD GoF versus position angle of scan|stat.value | float |
| `ipd_gof_harmonic_phase` | Gaia DR3 Phase of the IPD GoF versus position angle of scan|pos.posAng;stat.value | float |
| `ipd_frac_multi_peak` | Gaia DR3 Percent of successful-IPD windows with more than one peak|stat.value | integer |
| `ipd_frac_odd_win` | Gaia DR3 Percent of transits with truncated windows or multiple gate|stat.value | integer |
| `ruwe` | Gaia DR3 Renormalised unit weight error|stat.error | float |
| `scan_direction_strength_k1` | Gaia DR3 Degree of concentration of scan directions across the source|stat.value | float |
| `scan_direction_strength_k2` | Gaia DR3 Degree of concentration of scan directions across the source|stat.value | float |
| `scan_direction_strength_k3` | Gaia DR3 Degree of concentration of scan directions across the source|stat.value | float |
| `scan_direction_strength_k4` | Gaia DR3 Degree of concentration of scan directions across the source|stat.value | float |
| `scan_direction_mean_k1` | Gaia DR3 Mean position angle of scan directions across the source|pos.posAng;stat.mean | float |
| `scan_direction_mean_k2` | Gaia DR3 Mean position angle of scan directions across the source|pos.posAng;stat.mean | float |
| `scan_direction_mean_k3` | Gaia DR3 Mean position angle of scan directions across the source|pos.posAng;stat.mean | float |
| `scan_direction_mean_k4` | Gaia DR3 Mean position angle of scan directions across the source|pos.posAng;stat.mean | float |
| `duplicated_source` | Gaia DR3 Source with multiple source identifiers|meta.code.status | boolean |
| `phot_g_n_obs` | Gaia DR3 Number of observations contributing to G photometry|meta.number | integer |
| `phot_g_mean_flux` | Gaia DR3 G-band mean flux|phot.flux;em.opt | float |
| `phot_g_mean_flux_error` | Gaia DR3 Error on G-band mean flux|stat.error;phot.flux;em.opt | float |
| `phot_g_mean_flux_over_error` | Gaia DR3 G-band mean flux divided by its error|stat.snr;phot.flux;em.opt | float |
| `phot_g_mean_mag` | Gaia DR3 G-band mean magnitude|phot.mag;em.opt | float |
| `phot_bp_n_obs` | Gaia DR3 Number of observations contributing to BP photometry|meta.number | integer |
| `phot_bp_mean_flux` | Gaia DR3 Integrated BP mean flux|phot.flux;em.opt.B | float |
| `phot_bp_mean_flux_error` | Gaia DR3 Error on the integrated BP mean flux|stat.error;phot.flux;em.opt.B | float |
| `phot_bp_mean_flux_over_error` | Gaia DR3 Integrated BP mean flux divided by its error|stat.snr;phot.flux;em.opt.B | float |
| `phot_bp_mean_mag` | Gaia DR3 Integrated BP mean magnitude|phot.mag;em.opt.B | float |
| `phot_rp_n_obs` | Gaia DR3 Number of observations contributing to RP photometry|meta.number | integer |
| `phot_rp_mean_flux` | Gaia DR3 Integrated RP mean flux|phot.flux;em.opt.R | float |
| `phot_rp_mean_flux_error` | Gaia DR3 Error on the integrated RP mean flux|stat.error;phot.flux;em.opt.R | float |
| `phot_rp_mean_flux_over_error` | Gaia DR3 Integrated RP mean flux divided by its error|stat.snr;phot.flux;em.opt.R | float |
| `phot_rp_mean_mag` | Gaia DR3 Integrated RP mean magnitude|phot.mag;em.opt.R | float |
| `phot_bp_rp_excess_factor` | Gaia DR3 BP/RP excess factor|arith.factor;phot.flux;em.opt | float |
| `phot_bp_n_contaminated_transits` | Gaia DR3 Number of BP contaminated transits|meta.number | integer |
| `phot_bp_n_blended_transits` | Gaia DR3 Number of BP blended transits|meta.number | integer |
| `phot_rp_n_contaminated_transits` | Gaia DR3 Number of RP contaminated transits|meta.number | integer |
| `phot_rp_n_blended_transits` | Gaia DR3 Number of RP blended transits|meta.number | integer |
| `phot_proc_mode` | Gaia DR3 Photometry processing mode|meta.code | integer |
| `bp_rp` | Gaia DR3 BP - RP colour|phot.color;em.opt.B;em.opt.R | float |
| `bp_g` | Gaia DR3 BP - G colour|phot.color;em.opt.B;em.opt | float |
| `g_rp` | Gaia DR3 G - RP colour|phot.color;em.opt;em.opt.R | float |
| `radial_velocity` | Gaia DR3 Radial velocity|spect.dopplerVeloc.opt;em.opt.I | float |
| `radial_velocity_error` | Gaia DR3 Radial velocity error|stat.error;spect.dopplerVeloc.opt;em.opt.I | float |
| `rv_method_used` | Gaia DR3 Method used to obtain the radial velocity|meta.code.class | integer |
| `rv_nb_transits` | Gaia DR3 Number of transits used to compute the radial velocity|meta.number | integer |
| `rv_nb_deblended_transits` | Gaia DR3 Number of valid transits that have undergone deblending|meta.number | integer |
| `rv_visibility_periods_used` | Gaia DR3 Number of visibility periods used to estimate the radial velocity|meta.number | integer |
| `rv_expected_sig_to_noise` | Gaia DR3 Expected signal to noise ratio in the combination of the spectra use|stat.snr | float |
| `rv_renormalised_gof` | Gaia DR3 Radial velocity renormalised goodness of fit|stat.fit.goodness | float |
| `rv_chisq_pvalue` | Gaia DR3 P-value for constancy based on a chi-squared criterion|stat.fit.param | float |
| `rv_time_duration` | Gaia DR3 Time coverage of the radial velocity time series|time.duration | float |
| `rv_amplitude_robust` | Gaia DR3 Total amplitude in the radial velocity time series after outlier rem|stat.error;spect.dopplerVeloc.opt;em.opt.I | float |
| `rv_template_teff` | Gaia DR3 Teff of the template used to compute the radial velocity|stat.fit.param | float |
| `rv_template_logg` | Gaia DR3 Logg of the template used to compute the radial velocity|stat.fit.param | float |
| `rv_template_fe_h` | Gaia DR3 [Fe/H] of the template used to compute the radial velocityy|stat.fit.param | float |
| `rv_atm_param_origin` | Gaia DR3 Origin of the atmospheric parameters associated to the template|meta.code.class | integer |
| `vbroad` | Gaia DR3 Spectral line broadening parameter|spect.dopplerVeloc.opt;em.opt.I | float |
| `vbroad_error` | Gaia DR3 Uncertainty on the spectral line broadening|stat.error;spect.dopplerVeloc.opt;em.opt.I | float |
| `vbroad_nb_transits` | Gaia DR3 Number of transits used to compute vbroad|meta.number | integer |
| `grvs_mag` | Gaia DR3 Integrated Grvs magnitude|phot.mag;em.opt | float |
| `grvs_mag_error` | Gaia DR3 Grvs magnitude uncertainty|stat.error;phot.mag;em.opt | float |
| `grvs_mag_nb_transits` | Gaia DR3 Number of transits used to compute Grvs|meta.number | integer |
| `rvs_spec_sig_to_noise` | Gaia DR3 Signal to noise ratio in the mean RVS spectrum|stat.snr | float |
| `phot_variable_flag` | Gaia DR3 Photometric variability flag|meta.code;src.var | string |
| `l` | Gaia DR3 Galactic longitude|pos.galactic.lon | float |
| `b` | Gaia DR3 Galactic latitude|pos.galactic.lat | float |
| `ecl_lon` | Gaia DR3 Ecliptic longitude|pos.ecliptic.lon | float |
| `ecl_lat` | Gaia DR3 Ecliptic latitude|pos.ecliptic.lat | float |
| `in_qso_candidates` | Gaia DR3 Flag indicating the availability of additional information in the QS|meta.code.status | boolean |
| `in_galaxy_candidates` | Gaia DR3 Flag indicating the availability of additional information in the ga|meta.code.status | boolean |
| `non_single_star` | Gaia DR3 Flag indicating the availability of additional information in the va|meta.code.status | integer |
| `has_xp_continuous` | Gaia DR3 Flag indicating the availability of mean BP/RP spectrum in continuou|meta.code.status | boolean |
| `has_xp_sampled` | Gaia DR3 Flag indicating the availability of mean BP/RP spectrum in sampled f|meta.code.status | boolean |
| `has_rvs` | Gaia DR3 Flag indicating the availability of mean RVS spectrum for this sourc|meta.code.status | boolean |
| `has_epoch_photometry` | Gaia DR3 Flag indicating the availability of epoch photometry for this source|meta.code.status | boolean |
| `has_epoch_rv` | Gaia DR3 Flag indicating the availability of epoch radial velocity for this s|meta.code.status | boolean |
| `has_mcmc_gspphot` | Gaia DR3 Flag indicating the availability of GSP-Phot MCMC samples for this s|meta.code.status | boolean |
| `has_mcmc_msc` | Gaia DR3 Flag indicating the availability of MSC MCMC samples for this source|meta.code.status | boolean |
| `in_andromeda_survey` | Gaia DR3 Flag indicating that the source is present in the Gaia Andromeda Pho|meta.code.status | boolean |
| `classprob_dsc_combmod_quasar` | Gaia DR3 Probability from DSC-Combmod of being a quasar (data used: BP/RP spe|stat.probability | float |
| `classprob_dsc_combmod_galaxy` | Gaia DR3 Probability from DSC-Combmod of being a galaxy (data used: BP/RP spe|stat.probability | float |
| `classprob_dsc_combmod_star` | Gaia DR3 Probability from DSC-Combmod of being a single star (but not a white|stat.probability | float |
| `teff_gspphot` | Gaia DR3 Effective temperature from GSP-Phot Aeneas best library using BP/RP|phys.temperature.effective | float |
| `teff_gspphot_lower` | Gaia DR3 Lower confidence level (16%) of effective temperature from GSP-Phot|phys.temperature.effective;stat.min | float |
| `teff_gspphot_upper` | Gaia DR3 Upper confidence level (84%) of effective temperature from GSP-Phot|phys.temperature.effective;stat.max | float |
| `logg_gspphot` | Gaia DR3 Surface gravity from GSP-Phot Aeneas best library using BP/RP spectr|phys.gravity | float |
| `logg_gspphot_lower` | Gaia DR3 Lower confidence level (16%) of surface gravity from GSP-Phot Aeneas|phys.gravity;stat.min | float |
| `logg_gspphot_upper` | Gaia DR3 Upper confidence level (84%) of surface gravity from GSP-Phot Aeneas|phys.gravity;stat.max | float |
| `mh_gspphot` | Gaia DR3 Iron abundance from GSP-Phot Aeneas best library using BP/RP spectra|phys.abund.Z | float |
| `mh_gspphot_lower` | Gaia DR3 Lower confidence level (16%) of iron abundance from GSP-Phot Aeneas|phys.abund.Z;stat.min | float |
| `mh_gspphot_upper` | Gaia DR3 Upper confidence level (84%) of iron abundance from GSP-Phot Aeneas|phys.abund.Z;stat.max | float |
| `distance_gspphot` | Gaia DR3 Distance from GSP-Phot Aeneas best library using BP/RP spectra|pos.distance;pos.eq | float |
| `distance_gspphot_lower` | Gaia DR3 Lower confidence level (16%) of distance from GSP-Phot Aeneas best l|pos.distance;pos.eq | float |
| `distance_gspphot_upper` | Gaia DR3 Upper confidence level (84%) of distance from GSP-Phot Aeneas best l|pos.distance;pos.eq | float |
| `azero_gspphot` | Gaia DR3 Monochromatic extinction $A_0$ at 547.7nm from GSP-Phot Aeneas best|phys.absorption;em.opt | float |
| `azero_gspphot_lower` | Gaia DR3 Lower confidence level (16%) of monochromatic extinction $A_0$ at 54|phys.absorption;em.opt | float |
| `azero_gspphot_upper` | Gaia DR3 Upper confidence level (84%) of monochromatic extinction $A_0$ at 54|phys.absorption;em.opt | float |
| `ag_gspphot` | Gaia DR3 Extinction in G band from GSP-Phot Aeneas best library using BP/RP s|phys.absorption;em.opt | float |
| `ag_gspphot_lower` | Gaia DR3 Lower confidence level (16%) of extinction in G band from GSP-Phot A|phys.absorption;em.opt | float |
| `ag_gspphot_upper` | Gaia DR3 Upper confidence level (84%) of extinction in G band from GSP-Phot A|phys.absorption;em.opt | float |
| `ebpminrp_gspphot` | Gaia DR3 Reddening $E(G_{\rm BP} - G_{\rm RP})$ from GSP-Phot Aeneas best lib|phot.color.excess | float |
| `ebpminrp_gspphot_lower` | Gaia DR3 Lower confidence level (16%) of reddening  $E(G_{\rm BP} - G_{\rm RP|phot.color.excess;stat.min | float |
| `ebpminrp_gspphot_upper` | Gaia DR3 Upper confidence level (84%) of reddening  $E(G_{\rm BP} - G_{\rm RP|phot.color.excess;stat.max | float |
| `libname_gspphot` | Gaia DR3 Name of library that achieves the highest mean log-posterior in MCMC|meta.note | string |
| `ebv` | Extinction E(B-V)|phys.absorption.gal | float |
| `phot_g_mean_mag_error` | Gaia DR3 G-band mean magnitude error|stat.error;phot.mag;em.opt | float |
| `phot_bp_mean_mag_error` | Integrated BP mean magnitude error|stat.error;phot.mag;em.opt.B | float |
| `phot_rp_mean_mag_error` | Integrated RP mean magnitude error|stat.error;phot.mag;em.opt.R | float |
| `plx_zpt_corr` | Lindegren+ (2021) Gaia DR3 parallax zeropoint correction|stat.error | float |
| `parallax_raw` | Gaia DR3 Raw Parallax (before plx_zpt_corr)|pos.parallax.trig | float |
| `parallax_error_raw` | Gaia DR3 Raw Parallax (before plx_zpt_corr)|stat.error;pos.parallax.trig | float |

---

### `galah_dr4_vac_dynamics_240705`

| Column name | Description | units | type |
| `sobject_id` | GALAH identifier|meta.id | integer |
| `tmass_id` | 2MASS identifier|meta.id.cross | string |
| `gaiadr3_source_id` | Gaia DR3 source_id|meta.id.cross | integer |
| `ra` | Gaia DR3 Right ascension|pos.eq.ra;meta.main | float |
| `dec` | Gaia DR3 Declination|pos.eq.dec;meta.main | float |
| `r_med` | Median Distance used for calculating logg(plx)|pos.distance | float |
| `pmra` | Gaia DR3 Proper motion in right ascension direction|pos.pm;pos.eq.ra | float |
| `pmdec` | Gaia DR3 Proper motion in declination direction|pos.pm;pos.eq.dec | float |
| `rv` | Radial velocity used for orbit estimation|arith.factor;spect.dopplerVeloc | float |
| `X_XYZ` | Best-value heliocentric Galactic rectangular x-coordinate|pos.cartesian.x;pos.heliocentric | float |
| `Y_XYZ` | Best-value heliocentric Galactic rectangular y-coordinate|pos.cartesian.y;pos.heliocentric | float |
| `Z_XYZ` | Best-value heliocentric Galactic rectangular z-coordinate|pos.cartesian.z;pos.heliocentric | float |
| `U_UVW` | Best-value heliocentric Galactic rectangular x-velocity|phys.vel.orbital;pos.heliocentric | float |
| `V_UVW` | Best-value heliocentric Galactic rectangular y-velocity|phys.vel.orbital;pos.heliocentric | float |
| `W_UVW` | Best-value heliocentric Galactic rectangular z-velocity|phys.vel.orbital;pos.heliocentric | float |
| `R_Rzphi` | Best-value Galactocentric Radius|pos.galactocentric | float |
| `phi_Rzphi` | Best-value Galactocentric azimuth|pos.galactocentric | float |
| `z_Rzphi` | Best-value Galactocentric height|pos.galactocentric | float |
| `vR_Rzphi` | Best-value Galactocentric radial velocity|phys.vel.orbital;pos.galactocentric | float |
| `vT_Rzphi` | Best-value Galactocentric tangential velocity|phys.vel.orbital;pos.galactocentric | float |
| `vz_Rzphi` | Best-value Galactocentric vertical velocity|phys.vel.orbital;pos.galactocentric | float |
| `J_R` | Best-value radial action|src.orbital | float |
| `L_Z` | Best-value azimuthal action / angular momentum|src.orbital;phys.angMomentum | float |
| `J_Z` | Best-value vertical action|src.orbital | float |
| `omega_R` | Radial orbit frequency|src.orbital | float |
| `omega_phi` | Azimuthal orbit frequency|src.orbital | float |
| `omega_z` | Vertical orbit frequency|src.orbital | float |
| `angle_R` | Radial orbit angle|src.orbital | float |
| `angle_phi` | Azimuthal orbit angle|src.orbital | float |
| `angle_z` | Vertical orbit angle|src.orbital | float |
| `ecc` | Best-value orbit eccentricity|src.orbital.eccentricity | float |
| `zmax` | Best-value maximum Galactocentric height|src.orbital | float |
| `R_peri` | Best-value Galactocentric pericenter radius|src.orbital | float |
| `R_ap` | Best-value Galactocentric apocenter radius|src.orbital | float |
| `Energy` | Best-value orbit energy|src.orbital;phys.energy | float |

### `galah_dr4_vac_3dnlte_a_li_240705`

| Column name | Description | units | type |
| :------ |:--- | :--- | :--- |
| `sobject_id` | GALAH identifier|meta.id | integer |
| `tmass_id` | 2MASS identifier|meta.id.cross | string |
| `teff` | Spectroscopic effective temperature (used for fitting)|phys.temperature.effective | float |
| `e_teff` | Uncertainty teff|stat.error;phys.temperature.effective | float |
| `logg` | Surface gravity adjusted via parallax information|phys.gravity | float |
| `e_logg` | Uncertainty logg_plx|stat.error;phys.gravity | float |
| `fe_h` | Abundance of Fe and all other elements not fitted in GALAH (Fe: 1D-NLTE)|phys.abund.Fe | float |
| `e_fe_h` | Uncertainty fe_h|stat.error;phys.abund.Fe | float |
| `EW` | Equivalent width of LiI 6708 line region|spect.line.eqWidth | float |
| `e_EW_low` | Lower uncertainty limit of ew_li|stat.error;spect.line.eqWidth | float |
| `e_EW_upp` | Upper uncertainty limit of ew_li|stat.error;spect.line.eqWidth | float |
| `e_EW_norris` | Norris uncertainty limit of ew_li|stat.error;spect.line.eqWidth | float |
| `ALi` | Absolute Lithium abundance|phys.abund | float |
| `ALi_upp_lim` | Upper limit of a_li|stat.error;phys.abund | float |
| `e_ALi_low` | Lower uncertainty of a_li|stat.error;phys.abund | float |
| `e_ALi_upp` | Upper uncertainty of a_li|stat.error;phys.abund | float |
| `e_ALi_teff` | Teff-correlated uncertainty of a_li|stat.error;phys.abund | float |
| `minchisq` | A_Li fitting minimum chi2|stat.fit.chi2 | float |
| `flag_sp` | Major spectroscopic quality bitmask flag|meta.code.qual,stat.fit | integer |
| `flag_fe_h` | Quality flag fe_h|meta.code.qual,stat.fit | integer |
| `flag_ALi` | Quality bitmask flag of a_li|meta.code.qual,stat.fit | integer |
| `fwhm_li` | FWHM of LiI 6708 line fit|spect.line.width;stat.fwhm | float |
| `rv` | Radial velocity used for orbit estimation|arith.factor;spect.dopplerVeloc | float |
| `snr` | SNR of LiI 6708 line fit|stat.snr | float |
| `CN1` | CN1 of LiI 6708 line fit|spect.line.eqWidth | float |
| `Fe` | Fe of LiI 6708 line fit|spect.line.eqWidth | float |
| `CN2` | CN2 of LiI 6708 line fit|spect.line.eqWidth | float |
| `V/Ce` | V/Ce of LiI 6708 line fit|spect.line.eqWidth | float |
| `Quest1` | ?1 of LiI 6708 line fit|spect.line.eqWidth | float |
| `Quest2` | ?2 of LiI 6708 line fit|spect.line.eqWidth | float |
