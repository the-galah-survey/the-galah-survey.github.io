---
layout: page
title: GALAH DR3 catalogues
subtitle: Third Data Release
---

{: .main_blockquote}
This page describes the catalogues of GALAH DR3 and how to get them.

* This text gets replaced.
{:toc}

---

### GALAH DR3 Main Catalogues

We provide two versions of the GALAH DR3 catalogue (`GALAH_DR3_main_xx.fits`)

#### Recommended catalogue of stellar parameters and abundances
##### [Download `GALAH_DR3_main_allstar_v2.fits`](https://cloud.datacentral.org.au/teamdata/GALAH/public/GALAH_DR3/) (833 MB)
 {:.no_toc}

{: .box-warning}
Strongly recommend the use of this table for most science cases interested in stellar parameters and abundances.

The `GALAH_DR3_main_allstar_v2` is our main results catalogue. It contains results for 588,571 stars observed as part of the GALAH, K2-HERMES, TESS-HERMES, and other related surveys that used the HERMES spectrograph on the Anglo-Australian Telescope between November 2013 and February 2019. For all targets we provide stellar parameters, radial velocities, and elemental abundances.

We recommend this catalogue for most science cases as it contains only one entry **per star** (about 50000 stars were observed multiple times; if you are interested in the per observation results, see the [`GALAH_DR3_main_allspec_v2` catalogue](#extended-catalogue-of-stellar-parameters-and-abundances)). The full list of columns is on the [Table Schema documentation](/dr3/table_schema). For each star we provide:
* Star identifers:
    - the GALAH observation ID (`sobject_id`)
    - 2MASS identifier (`star_id`)
    - Gaia DR2 and eDR3 `source_id` (`dr2_source_id` and `dr3_source_id` respectively)
* Stellar parameters (and their errors):
    - Effective temperature (`teff`, `irfm_teff`), surface gravity (`logg`), iron abundance (`fe_h`), overall α-abundance (`alpha_fe`)
    - Microturbulence (`vmic`) and broadening velocities (`vbroad`)
* Barycentric radial velocity of the star (`rv_galah`)
* Elemental abundances (and their errors) for:
    - These all take the form `X_fe`, where `X` is the element's chemical symbol
    - light elements: Li, C, O
    - odd-Z elements: Na, Al, K
    - α-elements: Mg, Si, Ca, Ti (and TiII)
    - iron-peak elements: Sc, V, Cr, Mn, Co, Ni, Cu, Zn
    - light and heavy slow neutron capture elements: Y, Ba, La, Rb, Mo, Ru, Nd, Sm
    - rapid neutron capture element: Eu
* Flagging information:
    - Please read our [GALAH DR3 Best Practices page](/dr3/using_the_data) for recommendations on flags.
    - Two overall flags: a stellar parameter quality flag (`flag_sp`) and a iron abundance quality flag (`flag_fe_h`)
    - Quality flags for `alpha_fe` (`flag_alpha_fe`)
    - Intermediary analysis flags: reduction pipeline quality flag (`red_flag`); GUESS reduction pipeline quality flag (`flag_guess`)
    - Repeat observation flag, indicating if used for clean catalog (`flag_repeat`)
* Other useful information:
    - The internal survey name (`survey_name`), observation field identifer (`field_id`)
    - Signal-to-noise for the spectrum from each camera (`snr_c1_iraf`, `snr_c2_iraf`, `snr_c3_iraf`, `snr_c3_iraf`)
* Photometry:
    - V magnitude estimated from 2MASS *J* and *K*<sub>s</sub> mag (`v_jk`)
    - 2MASS (`j_m`, `h_m`, `ks_m`)
    - WISE (`w2mpro`)
* Gaia DR2 data:
    - `ra_dr2`, `dec_dr2`, `parallax_dr2`, `rv_gaia_dr2`, `ruwe_dr2`

#### Extended catalogue of stellar parameters and abundances
##### [Download `GALAH_DR3_main_allspec_v2.fits`](https://cloud.datacentral.org.au/teamdata/GALAH/public/GALAH_DR3/) (2.1 GB)
 {:.no_toc}

{: .box-warning}
`GALAH_DR3_main_allspec_v2` is not recommended for most science cases. It is an extended version of the [`GALAH_DR3_main_allstar_v2`](#recommended-catalogue-of-stellar-parameters-and-abundances). It contains results **per spectra** (rather than per star) and includes extra columns for individual spectra lines.

The `GALAH_DR3_main_allspec_v2` catalogue has results for 678,423 spectra acquired as part of the GALAH, K2-HERMES, TESS-HERMES, and other related surveys that used the HERMES spectrograph on the Anglo-Australian Telescope between November 2013 and February 2019. As with the `GALAH_DR3_main_allstar_v2`, for all spectra we provide stellar parameters, radial velocities, and elemental abundances. For the full list of columns, see the [Table Schema page](/dr3/table_schema).

As well as the information included in `GALAH_DR3_main_allstar_v2`, the `GALAH_DR3_main_allspec_v2` catalogue has:
* Elemental abundances (and their errors) for individual spectral lines
    - These all take the form `ind_X1234_fe`, where `X1234` is the element's chemical symbol and the wavelength
* Diagnostic information from the analysis pipeline
    - Results from our initial GUESS pipeline (`rv_guess`, `teff_guess`, `logg_guess`, `feh_guess`)
    - Radial velocities of individual spectral lines (`rv_5854`, `rv_6708`, `rv_6722`)

---

### GALAH DR3 Value-Added Catalogues

#### Gaia eDR3 data for all stars in GALAH DR3
##### [Download `GALAH_DR3_VAC_GaiaEDR3_v2.fits`](https://cloud.datacentral.org.au/teamdata/GALAH/public/GALAH_DR3/) (338 MB)
 {:.no_toc}
This provides a cross-match GALAH DR3 and Gaia eDR3. This catalogue contains an entry for every star in GALAH DR3 that we identified a match in Gaia eDR3. The full list of columns is on the [Table Schema documentation](/dr3/table_schema). The `GALAH_DR3_VAC_GaiaEDR3_v2` catalogue consists of:
* GALAH DR3 `sobject_id` and `star_id`
* All columns from [`gaiaedr3.gaia_source`](https://gea.esac.esa.int/archive/documentation/GEDR3/Gaia_archive/chap_datamodel/sec_dm_main_tables/ssec_dm_gaia_source.html) (with `source_id` renamed `dr3_source_id`)
* All columns from [`gaiaedr3.dr2_neighbourhood`](https://gea.esac.esa.int/archive/documentation/GEDR3/Gaia_archive/chap_datamodel/sec_dm_auxiliary_tables/ssec_dm_dr2_neighbourhood.html):
    - e.g., `angular_distance`, `magnitude_difference`, `proper_motion_propagation`
* Photogeometric and Geometric Distances from [Bailer-Jones *et al.* (2020)](https://www2.mpia-hd.mpg.de/homes/calj/gedr3_distances/main.html)
* Zeropoints from [Lindegren *et al.* (2020)](https://arxiv.org/abs/2012.01742)

Some notes and caveats about the cross-match between GALAH DR3 and Gaia eDR3:
* This cross-match used the previously identified Gaia DR2 `source_id` for each GALAH DR3 star, and the `gaiaedr3.dr2_neighbourhood` table created by the Gaia team. The Gaia DR2 `source_id` had been found using the `gaiadr2.tmass_best_neighbour` table and the 2MASS ID of each GALAH star. In the future, we suggest to perform this crossmatch via GALAH's 2MASS ID and the yet-to-come match of Gaia EDR3 and 2MASS identifiers.
* All `GALAH_DR3_VAC_GaiaEDR3_v2` entries have an angular distance between their Gaia DR2 and eDR3 sources smaller than 160 mas, and 99.9 per cent are within 20 mas.
* There is a Gaia eDR3 source for every entry in the `GALAH_DR3_main_allstar_v2` table.
    - There are 111 entries in the `GALAH_DR3_main_allspec_v2` table that lack a Gaia `source_id` as we have not attempted to find them in Gaia eDR3 and they never had a Gaia DR2 `source_id`. Of these 38 are bright stars and do have a parallax from Hipparcos.
* 17654 stars had more than one Gaia eDR3 match (98 per cent of these had only two matches, and the remainder with 3 or 4 matches). For simplicity we have chosen the closest match in angular distance between the Gaia DR2 and Gaia eDR3 position as reported by the `gaiaedr3.dr2_neighbourhood`.
    - For over 99 per cent of ~18000 stars, the closest match had an angular distance <10 mas, and second closest match was >600 mas.
    - There is likely source confusion for <100 stars. For instance, for 57 of the ~18000 stars with multiple matches in the `gaiaedr3.dr2_neighbourhood` table, the second closest match in angular distance has a smaller magnitude difference between Gaia DR2 and eDR3.

---

#### Ages, masses, distances and other parameters estimated by BSTEP
##### [Download `GALAH_DR3_VAC_ages_v2.fits`](https://cloud.datacentral.org.au/teamdata/GALAH/public/GALAH_DR3/) (362 MB)
 {:.no_toc}
This catalogue uses the Bayesian Stellar Parameter Estimation code (BSTEP) from [Sharma *et al.* (2018)](http://doi.org/10.1093/mnras/stx2582) to provide  a Bayesian estimate of intrinsic stellar parameters from observed parameters by making use of stellar isochrones. The full list of columns is on the [Table Schema documentation](/dr3/table_schema).

For each star, we give the following parameters found by BSTEP:
* distance (`distance_bstep`)
* age (`age_bstep`)
* initial and current mass (`m_ini_bstep` and `m_act_bstep`)
* stellar radius (`radius_bstep`)
* stellar luminosity (`log_lum_bstep`)
* a probability of whether this is a red clump star (`is_redclump_bstep`)
* the reddening (`ebv_bstep`)
* absolute *J* and *K<sub>S</sub>* magnitudes (`abs_j_bstep` and `abs_ks_bstep`)
* effective temperature (`teff_bstep`)
* surface gravity (`logg_bstep`)
* initial and current metallicity (`meh_ini_bstep` and `meh_act_bstep`)

For each estimated parameter we also report the 1-sigma uncertainty (prefix `e_`), and the 16th (`e16_`), 50th (`e50_`), and 84th (`e84_`) percentiles.

{: .box-warning}
As discussed on our [Best Practices page](/dr3/using_the_data), we recommend the ages, masses, and distances from BSTEP as our best values for these parameters.  We do not recommend using BSTEP values for stellar parameters like effective temperature and surface gravity.

For details of the adopted priors see [Sharma *et al.* (2018)](https://doi.org/10.1093/mnras/stx2582). Briefly, a flat prior on age and metallicity was used and for density distribution of stars a combination of an exponential stellar disc and a diffuse stellar halo was used. For results presented in this paper, we use the PARSEC release v1.2S + COLIBRI stellar isochrone ([Marigo *et al.* 2017](https://doi.org/10.3847/1538-4357/835/1/77)). We use the following observables, T<sub>eff</sub> , log *g*, [Fe/H], [α/Fe] , 2MASS *J* and *K<sub>S</sub>* photometry, and parallax from Gaia. The effective observed metallicity, log(Z/Z<sub>⊙</sub>), was estimated from [Fe/H] and [α/Fe] using the formula by [Salaris (2006)](https://books.google.de/books?id=A5DvAAAAMAAJ). This was compared with the surface metallicity reported by the isochrones, which takes the evolutionary changes in surface metallicity Z into account.

---

#### Galactic kinematic and dynamic information
##### [Download `GALAH_DR3_VAC_dynamics_v2.fits`](https://cloud.datacentral.org.au/teamdata/GALAH/public/GALAH_DR3/) (554 MB)
{:.no_toc}

We provide a value-added-catalog with kinematic and dynamic information, that builds upon the 5D astrometric information by Gaia eDR3, and primarily radial velocities determined from GALAH spectra. The full list of columns is on the [Table Schema documentation](/dr3/table_schema). This catalogue provides:

* Heliocentric cartesian coordinate (`X_XYZ`, `Y_XYZ`, `Z_XYZ`) and velocity frames (`U_UVW`, `V_UVW`, `W_UVW`)
* Galactocentric cylindrical coordinate (`R_Rzphi`, `z_Rzphi`, `phi_Rzphi`) and velocity frames (`vR_Rzphi`, `vz_Rzphi`, `vT_Rzphi`)
    - Note that we report `vT_Rzphi` rather than `vR_Rzphi`. The initial release of this table did report `vphi_Rzphi`. We changed to `vT_Rzphi` because due to the normalisation within galpy the notation was confusing.
    - If `vphi_Rzphi` is desired, it can be calculated as `vphi_Rzphi = vT_Rzphi * (8.21 kpc) / R_Rzphi`
* Orbital angles (`angle_R`, `angle_phi`, `angle_z`) and frequencies (`omega_R`, `omega_phi`, `omega_z`)
* Actions (`J_R`, `L_Z`, `J_Z`)
* eccentricity (`ecc`)
* Maximum Galactocentric orbit height (`zmax`), pericenter and apocenter radii (`R_peri`, `R_ap`)
* Orbit energies (`Energy`)

For each estimated parameter we also report a mean value and the 5th, 50th, and 95th percentiles (these have the suffixes `_5`, `_50`, `_95`).

For the calculation of orbit information we use version 1.6 of the Python package `galpy` ([Bovy 2015](http://doi.org/10.1088/0067-0049/216/2/29)). To estimate actions, eccentricity, maximum orbit Galactocentric height, and apocenter/pericenter radii, we use the Staeckel fudge via the galpy module `actionAngleStaeckel` with a focus of 0.45. We use the following potentials and observed properties of the Galaxy:
* The best fitting axisymmetric potential by McMillan (2017);
* A solar radius of 8.21 kpc, consistent with the latest measurement by Gravity Collaboration *et al.* (2019) of 8.178 ± 0.013(stat.) ± 0.022(sys.) kpc;
* A circular velocity at this radius of 233.1 km/s;
* The total motion of the Sun in the V-direction of 248.27 km/s by evaluation the proper motion measurements from Reid & Brunthaler (2004) at our chosen Solar radius;
* The Sun placed 25 pc above the plane (Jurić *et al.* 2008);
* The peculiar solar velocities U = 11.1 km/s and W=7.25 km/s by Schönrich *et al.* (2020) but V=15.17 km/s.

The input values for each star were:
* Sky positions (`ra`, `dec`) and proper motions (`pmra`, `pmdec`) from Gaia eDR3 (see the [`GALAH_DR3_VAC_GaiaEDR3_v2` catalogue above](#gaia-edr3-data-for-all-stars-in-galah-dr3).)
* Radial velocities from GALAH DR3 (`rv_galah`)
  - See the value-added catalogue of [Collated radial velocity measurements below](#collated-radial-velocity-measurements).
* Distances from GALAH (`distance_bstep`)
  - See the [BSTEP catalogue above](#ages-masses-distances-and-other-parameters-estimated-by-bstep)

---

#### Collated radial velocity measurements
##### [Download `GALAH_DR3_VAC_rv_v2.fits`](https://cloud.datacentral.org.au/teamdata/GALAH/public/GALAH_DR3/) (67 MB)
{:.no_toc}

This catalogue collates several radial velocities measurements for each star. The full list of columns is on the [Table Schema documentation](/dr3/table_schema).

* `rv_obst` and `rv_nogr_obst` (and their error columns)
    - [Zwitter *et al.* (2020)](https://arxiv.org/abs/2012.12201) created essentially noiseless observed spectra from the median spectra for all GALAH DR3 stars belonging to the same bin with a width of 50 K in temperature, 0.2 dex in gravity, and 0.1 dex in metallicity. The observed spectra are then cross-correlated with these noiseless spectra to measure radial velocities with a typical accuracy of 0.1 km/s. The `rv_nogr_obst` reports the value without the gravitational redshift correction.
* `rv_sme_v2` (and its error columns)
    - The radial velocity calculated by SME as part of the stellar parameter and abundance determination.
    - There is also a `rv_sme_v1` column which was the value found in the original GALAH DR3 release which had an incorrect barycentric correction.
* `dr2_radial_velocity` (and its error columns)
    - Radial velocity from Gaia DR2
    - This value is also listed as `rv_gaia_dr2` in `GALAH_DR3_main_allstar_v2` and `GALAH_DR3_main_allspec_v2`.

The `rv_galah` in `GALAH_DR3_main_allstar_v2`, `GALAH_DR3_main_allspec_v2`, and `GALAH_DR3_VAC_rv_v2` reports our best value for the radial velocity of each spectrum. The method used for a given spectrum is provided by the `use_rv_flag` in the `GALAH_DR3_VAC_rv_v2` and `GALAH_DR3_VAC_dynamics_v2` catalogues: (0) `rv_obst` (83% of spectra); (1) `rv_sme_v2` (13% of spectra); (2) `dr2_radial_velocity` (2% of spectra); or (4) no value (2% of spectra).

----

#### FGK binary stars
Binary stellar systems represent a significant fraction of stars in our Galaxy. Therefore, their effect on observations, as well as their impact on the Galactic environment, have to be properly taken into account when studying Galactic structure and evolution. To this end, we present a sample of 12760 binary systems for which the properties of their stellar components were derived in a separate analysis from the main DR3 analysis.

The details of the analysis are described in [Traven *et al.* (2020)](https://doi.org/10.1051/0004-6361/202037484), and the catalogue of derived parameters is [available at CDS](http://cdsarc.u-strasbg.fr/viz-bin/cat/J/A+A/638/A145).

---

#### List of all possible GALAH fields and field configurations
##### [Download `target/galahfco_3_public.txt`](https://cloud.datacentral.org.au/teamdata/GALAH/public/GALAH_DR3/) (934 KB)
 {:.no_toc}

This lists all 7993 possible fields in the current target selection catalogue of the GALAH survey. For a given field centre (i.e., a given `ra`, `dec`) there is an associated unique identifer (`field_id`). For a given `field_id`, there can be one or more possible observable fields --- for instance if the target density is high enough, or there are bright and faint fields. Each possible configuration has a unique identifer of `fco_id`.

* Field configuration identifier: `fco_id`
* Unique field identifier: `field_id` (and `parent` for legacy reasons)
* Field centre location (`ra`, `dec`)
* Field radius in degrees (`radius`)
* The subsurvey name (`progname`)
    - Possible values: `bright`, `galah`, `galah_faint`, `galah_ufaint`, `k2`, `ocluster`, `repeat0`, `tess`
* Magnitude range of the field (`vmin` and `vmax`)
* Magnitude used to set exposure time (`vexp`)
* The selection function (`selfunc`)
* Magnitude used for complicated selection functions (`vsplit`)
* Internal use only values (`active`, `name`, `priority`, `special`, `max_observed`)

---

### Getting the catalogues

{: .box-warning}
We recommend the `GALAH_DR3_main_allstar_v2.fits` catalogue if you want our best effort stellar parameters and elemental abundances. This catalogue can be [directly downloaded from Data Central](https://cloud.datacentral.org.au/teamdata/GALAH/public/GALAH_DR3).<br/><br/>
Please read our [best practices for using GALAH DR3](/dr3/using_the_data).

There are two methods for accessing these catalogues depending on your requirements

#### Downloading the FITS files

The catalogues can be [downloaded from Data Central](https://cloud.datacentral.org.au/teamdata/GALAH/public/GALAH_DR3/) as FITS files, or using the following command (removing the `--spider` flag and replacing with the appropriate file name as listed below):

```bash
# Download the galah_dr3.main_star catalogue
wget --spider https://cloud.datacentral.org.au/teamdata/GALAH/public/GALAH_DR3/GALAH_DR3_main_allstar_v2.fits
```

#### ADQL query

{: .box-error}
The versions served by Data Central are currently our initial DR3 release and contain some minor errors.

The catalogues can be accessed using the [query services provided by Data Central](https://datacentral.org.au/services/query/). For example, if you are interested in all of the entries for stars likely to be members of the globular cluster ω&nbsp;Centauri, these could be found using a query like:

```sql
SELECT
   TOP 100
   *
   FROM galah_dr3.main_star -- GALAH_DR3_main_allstar_v2
   WHERE
      1=CONTAINS(POINT('ICRS', ra, dec),
                 CIRCLE('ICRS', 201.6836, -47.5068, 1.0 ))
   AND sqrt(power(pmra-(-3.2),2)+power(pmdec-(-6.9),2)) < 1.5
   AND rv_galah > 170
```

---
