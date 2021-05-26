---
layout: page
title: Value-added catalogues
subtitle: Third Data Release
---

<h3> On this page</h3>
* This text gets replaced.
{:toc}
* [`galah_dr3.vac_gaiaedr3`](#galah_dr3vac_gaiaedr3)
    - *Gaia* eDR3 data for all stars in GALAH DR3
* [`galah_dr3.vac_ages`](#galah_dr3vac_ages)
    - Stellar ages, masses, distances and other parameters estimated using isochrones
* [`galah_dr3.vac_dynamics`](#galah_dr3vac_dynamics)
    - Galactic kinematic and dynamic parameters
* [`galah_dr3.vac_rv`](#galah_dr3vac_rv)
    - Collated radial velocity measurements
* FGK binary stars
    - Identification of likely for double-lined spectroscopic binaries.
* [`galah_dr3.vac_galahfco`](#galah_dr3vac_galahfco)
    - List of fields and field configurations. Each field has a unique ra, dec coordinates and field_id. Multiple configurtations can have same field_id.

### `galah_dr3.vac_gaiaedr3`
#### Gaia eDR3 data for all stars in GALAH DR3
This provides a cross-match GALAH DR3 and Gaia eDR3. This catalogue contains an entry for every star in GALAH DR3 that we identified a match in Gaia eDR3. The `vac_gaiaedr3` catalogue consists of:
* GALAH DR3 `sobject_id` and `star_id`
* All columns from `gaiaedr3.gaia_source` (with `source_id` renamed `dr3_source_id`)
* All columns from `gaiaedr3.dr2_neighbourhood`:
    - e.g., `angular_distance`, `magnitude_difference`, `proper_motion_propagation`
* Photogeometric and Geometric Distances from [Bailer-Jones et al. (2020)](https://arxiv.org/abs/2012.05220)
* Zeropoints from [Lindegren et al. (2020)](https://arxiv.org/abs/2012.01742)

Some notes and caveats about the cross-match between GALAH DR3 and Gaia eDR3:
* This cross-match used the previously identified Gaia DR2 `source_id` for each GALAH DR3 star, and the `gaiaedr3.dr2_neighbourhood` table created by the Gaia team. The Gaia DR2 `source_id` had been found using the `gaiadr2.tmass_best_neighbour` table and the 2MASS ID of each GALAH star. In the future, we suggest to perform this crossmatch via GALAH's 2MASS ID and the yet-to-come match of Gaia EDR3 and 2MASS identifiers.
* All `galah_dr3.vac_gaiaedr3` entries have an angular distance between their Gaia DR2 and eDR3 sources smaller than 160 mas, and 99.9 per cent are within 20 mas.
* There is a Gaia eDR3 source for every entry in the `galah_dr3.main_star` table.
    - There are 111 entries in the `galah_dr3.main_spec` table that lack a Gaia `source_id` as we have not attempted to find them in Gaia eDR3 and they never had a Gaia DR2 `source_id`. Of these 38 are bright stars and do have a parallax from Hipparcos.
* 17654 stars had more than one Gaia eDR3 match (98 per cent two matches and the remainder with 3 or 4 matches). For simplicity we have chosen the match with the smallest angular distances between the Gaia DR2 and Gaia eDR3 position as reported by the `gaiaedr3.dr2_neighbourhood`.
    - For over 99 per cent of stars the closest match had an angular distance <10 mas, and second closest match was >600 mas.
    - There is likely source confusion for <100 stars. For instance, for 57 of the 17000 stars with multiple matches in the `gaiaedr3.dr2_neighbourhood` table, the second closest match in angular distance has a smaller magnitude difference between Gaia DR2 and eDR3.


### `galah_dr3.vac_ages`
#### Ages, masses, distances and other parameters estimated using isochrones
To estimate stellar properties like age, mass, and distance we use the Bayesian Stellar Parameter Estimation code (BSTEP) from [Sharma et al. (2018)](http://doi.org/10.1093/mnras/stx2582). BSTEP provides a Bayesian estimate of intrinsic stellar parameters from observed parameters by making use of stellar isochrones.

For details of the adopted priors see Sharma et al. (2018). Briefly, a flat prior on age and metallicity was used and for density distribution of stars a combination of an exponential stellar disc and a diffuse stellar halo was used. For results presented in this paper, we use the PARSEC release v1.2S + COLIBRI stellar isochrone ([Marigo et al. 2017](https://doi.org/10.3847/1538-4357/835/1/77)). We use the following observables, T<sub>eff</sub> , log *g*, [Fe/H], [α/Fe] , 2MASS J and Ks photometry, and parallax from Gaia. The effective observed metallicity, log(Z/Z<sub>⊙</sub>), was estimated from [Fe/H] and [α/Fe] using the formula by [Salaris (2006)](https://books.google.de/books?id=A5DvAAAAMAAJ). This was compared with the surface metallicity reported by the isochrones, which takes the evolutionary changes in surface metallicity Z into account.

The code provides an estimate of age, actual mass, initial mass, initial metallicity, surface metallicity, radius, distance, extinction E(B-V), luminosity, surface gravity, temperature and the probability of being a red clump star. For each estimated parameter we report a mean value and the 16th, 50th, and 84th percentiles.

### `galah_dr3.vac_dynamics`
#### Galactic kinematic and dynamic information

{: .box-warning}
The distance to star reported in the `galah_dr3.vac_dynamics` table may differ from the distance used in the stellar parameter and abundance determination. This is because the GALAH DR3 analysis was done prior to the release of Gaia eDR3, and so used GALAH DR2-derived distances.

We provide a value-added-catalog with kinematic and dynamic information, that builds upon the 5D astrometric information by Gaia eDR3, and primarily radial velocities determined from GALAH spectra.

The radial velocity values were primarily (83 per cent of spectra) from values calculated by [Zwitter et al (2020)](https://arxiv.org/abs/2012.12201) from the GALAH DR3 spectra. Of the remainder, 13 per cent use the radial velocity calculated as part of the stellar parameter and abundance determination, 2 per cent use the Gaia DR2 value (which was not updated in Gaia eDR3), and 2 per cent have no radial velocity value. The method used for a given spectrum is provided by the `use_rv_flag` in the `galah_dr3.vac_dynamics` (or `galah_dr3.vac_rv`) catalogue.

For the vast majority of stars (96 per cent), we use `distance_bstep` from the [`vac_ages`](#galah_dr3vac_ages) catalogue, calculated by the Bayesian Stellar Parameter Estimation code (BSTEP) from [Sharma et al. (2018)](http://doi.org/10.1093/mnras/stx2582). For the other 4 per cent of the stars we mostly use the photogeometric distances from Bailer-Jones et al. (2020) (`r_med_photogeo` in the [`vac_gaiaedr3`](#galah_dr3vac_gaiaedr3) catalogue). The method used for a given spectrum is provided by the `use_dist_flag` in the `galah_dr3.vac_dynamics` table.

The `galah_dr3.vac_dynamics` catalogue provides columns calculated from the "best" input values:

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

For the calculation of orbit information we use version 1.6 of the python package galpy ([Bovy 2015](http://doi.org/10.1088/0067-0049/216/2/29)). To estimate actions, eccentricity, maximum orbit Galactocentric height, and apocenter/pericenter radii, we use the Staeckel fudge via the galpy module `actionAngleStaeckel` with a focus of 0.45. We use the following potentials and observed properties of the Galaxy:

* The best fitting axisymmetric potential by McMillan (2017);
* A solar radius of 8.21 kpc, consistent with the latest measurement by Gravity Collaboration et al. (2019) of 8.178 ± 0.013(stat.) ± 0.022(sys.) kpc;
* A circular velocity at this radius of 233.1 km/s;
* The total motion of the Sun in the V-direction of 248.27 km/s by evaluation the proper motion measurements from Reid & Brunthaler (2004) at our chosen Solar radius;
* The Sun placed 25 pc above the plane (Jurić et al. 2008);
* The peculiar solar velocities U = 11.1 km/s and W=7.25 km/s by Schönrich et al (2020) but V=15.17 km/s.

### `galah_dr3.vac_rv`
#### Collated radial velocity measurements

The `rv_galah` value in `galah_dr3.main_star`, `galah_dr3.main_spec` and `galah_dr3.vac_rv` catalogues reports our best value for the radial velocity of each spectrum. The radial velocity values were primarily (83 per cent of spectra) from values calculated by [Zwitter et al (2020)](https://arxiv.org/abs/2012.12201) from the GALAH DR3 spectra. Of the remainder, 13 per cent use the radial velocity calculated as part of the stellar parameter and abundance determination, 2 per cent use the Gaia DR2 value (which was not updated in Gaia eDR3), and 2 per cent have no radial velocity value. The method used for a given spectrum is provided by the `use_rv_flag` in the `galah_dr3.vac_dynamics` and `galah_dr3.vac_rv` catalogue.

The `galah_dr3.vac_rv` catalogue contains the possible radial velocities for the star, described here in descending order of preference:

* `rv_obst` and `rv_nogr_obst` (and their error columns)
    - [Zwitter et al (2020)](https://arxiv.org/abs/2012.12201) created essentially noiseless observed spectra for stars are created by creating median spectra for all GALAH DR3 stars belonging to the same bin with a width of 50 K in temperature, 0.2 dex in gravity, and 0.1 dex in metallicity. The observed spectra are then cross-correlated with these noiseless spectra to measure radial velocities with a typical accuracy of 0.1 km/s. The `rv_nogr_obst` reports the value without the gravitational redshift correction.
* `rv_sme_v2` (and its error columns)
    - The radial velocity calculated by SME as part of the stellar parameter and abundance determination.
    - There is also a `rv_sme_v1` column which was the value found in the original GALAH DR3 release which had an incorrect barycentric correction.
* `dr2_radial_velocity` (and its error columns)
    - Radial velocity from Gaia DR2
    - This value is also listed as `rv_gaia_dr2` in `galah_dr3.main_spec` and `galah_dr3.main_star`.

### FGK binary stars
Binary stellar systems represent a significant fraction of stars in our Galaxy. Therefore, their effect on observations, as well as their impact on the Galactic environment, have to be properly taken into account when studying Galactic structure and evolution. To this end, we present a sample of 12760 binary systems for which the properties of their stellar components were derived in a separate analysis from the main DR3 analysis.

The details of the analysis are described in Traven et al. (2020), and the catalogue of derived parameters is available at CDS.

### `galah_dr3.vac_galahfco`
#### List of all possible GALAH fields and field configurations

Each field is specified by its location (`ra`, `dec`) and has a unique identifier `field_id`. Each row describes a field configuration. There can be multiple rows with same `field_id` indicating different configurations that the field can be observed in, e.g., fields observed with different magnitude ranges specified by (`vmin` , `vmax`). Description of the available columns is given below.

* `field_id`: (int) Unique field identifier
* `ra`: (deg)
* `dec`: (deg)
* `radius`: (deg) Ranging from 0 to 1.0
* `selfunc`: (int) Selection function
* `vmin`: Minimum V(J,K) magnitude
* `vmax`: Maximum V(J,K) magnitude
* `vsplit`: V(J,K) mag used for complicated selection functions
* `vexp`: V(J,K) magnitude used to set exposure time.
* `progname`: (str) one of the following:
    - `bright`, `galah`, `galah_faint`, `galah_ufaint`, `k2`, `ocluster`, `repeat0`, `tess`
    -
* `fco_id`: field configuration identifier, row number in the table
* `priority`: (int) 0 or 1 (for internal use)
* `active`: (int) 0 or 1 (for internal use)
* `special`: (int) 0 or 1 (for internal use)
