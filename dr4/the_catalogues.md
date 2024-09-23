---
layout: page
title: GALAH DR4 catalogues
subtitle: Fourth Data Release
---

{: .main_blockquote}
This page describes the catalogues of GALAH DR4 and how to get them.

* This text gets replaced.
{:toc}

---

### GALAH DR4 Main Catalogues

We provide two versions of the GALAH DR4 catalogue (`GALAH_DR4_main_xx.fits`)

#### Recommended catalogue of stellar parameters and abundances
##### [Download `GALAH_DR4_main_allstar.fits`](https://cloud.datacentral.org.au/teamdata/GALAH/public/GALAH_DR4/catalogs/) (723 MB)
 {:.no_toc}

{: .box-warning}
Strongly recommend the use of this table for most science cases interested in stellar parameters and abundances.

The `GALAH_DR4_main_allstar` is our main results catalogue. It contains results for 917,588 stars observed as part of the GALAH, K2-HERMES, TESS-HERMES, and other related surveys that used the HERMES spectrograph on the Anglo-Australian Telescope between December 2013 and August 2023. For all targets we provide stellar parameters, radial velocities, and elemental abundances.

We recommend this catalogue for most science cases as it contains only one entry **per star** (about 50000 stars were observed multiple times; if you are interested in the per observation results, see the [`GALAH_DR4_main_allspec_v2` catalogue](#extended-catalogue-of-stellar-parameters-and-abundances)). The full list of columns is on the [Table Schema documentation](/dr4/table_schema). For each star we provide:
* Star identifers:
    - the GALAH observation ID (`sobject_id`)
    - 2MASS identifier (`tmass_id`)
    - Gaia DR3 `source_id` (`gaiadr3_source_id`)
* Stellar parameters (and their errors):
    - Effective temperature (`teff`), surface gravity (`logg`), iron abundance (`fe_h`)
    - Microturbulence (`vmic`) and broadening velocities (`vsini`)
* Fundamental stellar properties estimated from Bayesian isochrone fitting:
    - Mass (`mass`), age (`age`) and bolometric luminosity (`lbol`)
* Barycentric radial velocity of the star (`rv_comp_1`) and a binary companion if it is detected (`rv_comp_2`)
* Elemental abundances (and their errors) for:
    - These all take the form `X_fe`, where `X` is the element's chemical symbol
    - light elements: Li, C, N, O
    - odd-Z elements: Na, Al, K
    - α-elements: Mg, Si, Ca, Ti 
    - iron-peak elements: Sc, V, Cr, Mn, Co, Ni, Cu, Zn
    - light and heavy slow neutron capture elements: Rb, Sr, Y, Zr, Mo, Ba, La, Ce, Nd
    - rapid neutron capture elements: Ru, Sm, Eu
* Flagging information:
    - Please read our [GALAH DR4 Best Practices page](/dr4/using_the_data) for recommendations on flags.
    - Overall spectroscopic quality flag `flag_sp`
    - A data reduction pipeline quality flag (`flag_red`)
* Other useful information:
    - The internal survey name (`survey_name`), observation field identifer (`field_id`), MJD of the observation (`mjd`)
    - Signal-to-noise per pixel for the spectrum from each camera (`snr_px_ccd1`, `snr_px_ccd2`, `snr_px_ccd3`, `snr_px_ccd3`)
* Photometry:
    - Gaia (`phot_g_mean_mag`, `bp_rp`)
    - 2MASS (`j_m`, `h_m`, `ks_m`)
    - WISE (`W2mag`)
* Gaia DR3 astrometric and spectroscopic information:
    - `ra`, `dec`, `parallax`, `ruwe`, `rv_gaia_dr3`

#### Extended catalogue of stellar parameters and abundances
##### [Download `GALAH_DR4_main_allspec.fits`](https://cloud.datacentral.org.au/teamdata/GALAH/public/GALAH_DR4/catalogs/) (833 MB)
 {:.no_toc}

{: .box-warning}
`GALAH_DR4_main_allspec` is not recommended for most science cases. It is an extended version of the [`GALAH_DR4_main_allstar`](#recommended-catalogue-of-stellar-parameters-and-abundances). It contains results **per spectrum** (rather than per star) and includes extra columns for individual spectral lines.

The `GALAH_DR4_main_allspec` catalogue has results for 1,085,520 spectra acquired as part of the GALAH, K2-HERMES, TESS-HERMES, and other related surveys that used the HERMES spectrograph on the Anglo-Australian Telescope between December 2013 and August 2023. As with the `GALAH_DR4_main_allstar`, for all spectra we provide stellar parameters, radial velocities, and elemental abundances. For the full list of columns, see the [Table Schema page](/dr4/table_schema).

As well as the information included in `GALAH_DR4_main_allstar`, the `GALAH_DR4_main_allspec` catalogue has:
* Additional detail on candidate binaries
    - Prominence of both components in the cross-correlation function (`rv_comp_1_p` and `rv_comp2_p`) and height of the secondary component in the CCF (`rv_comp_2_h`)

---

### GALAH DR4 Value-Added Catalogues

---

#### Crossmatch to Gaia DR3, 2MASS, and WISE
##### [Download `GALAH_DR4_VAC_crossmatch.fits`](https://cloud.datacentral.org.au/teamdata/GALAH/public/GALAH_DR4/catalogs/) (743 MB)
{:.no_toc}

We provide a value-added catalog with information from the Gaia DR3 `gaia_source` catalogue, 2MASS photometry and quality flags, and WISE photometry and quality flags for each star in GALAH DR4. The full list of columns is on the [Table Schema documentation](/dr4/table_schema). This catalogue provides:

* Unique identifiers for all four catalogues (`sobject_id`, `source_id`, `tmass_id`, `wise_id`)
* Photometry and associated errors:
    - Gaia DR3 G (`phot_g_mean_mag`), BP (`phot_bp_mean_mag`), RP (`phot_rp_mean_mag`), BP-RP (`bp_rp`), BP-G (`bp_g`), G-RP (`g_rp`), E(B-V) (`ebv`), G-band extinction (`ag_gspphot`), BP-RP reddening (`ebpminrp_gspphot`) and photometric variability flag (`phot_variable_flag`)
    - 2MASS J (`j_m`), H (`h_m`), Ks (`ks_m`)
    - WISE W1 (`W1mag`), W2 (`W2mag`), W3 (`W3mag`), W4 (`W4mag`)
* Gaia DR3 astrometry:
    - Parallax (`parallax`), proper motion (`pmra`, `pmdec`), and renormalised unit weight error (`ruwe`)
* Distances:
    - Bayesian geometric (`r_med_geo`, `r_lo_geo`, `r_hi_geo`) and photogeometric (`r_med_photogeo`, `r_lo_photogeo`, `r_hi_photogeo`) distances derived for Gaia DR3 in [Bailer-Jones *et al.* (2021)](https://ui.adsabs.harvard.edu/abs/2021AJ....161..147B/abstract)
* Gaia spectroscopic information:
    - Stellar parameter estimates Teff (`teff_gspphot`), logg (`logg_gspphot`), [Fe/H] (`mh_gspphot`) and distance (`distance_gspphot`) from BP/RP spectra
    - Radial velocity (`radial_velocity`) and line broadening (`vbroad`) from RVS spectra

---

#### Galactic kinematic and dynamic information
##### [Download `GALAH_DR4_VAC_dynamics.fits`](https://cloud.datacentral.org.au/teamdata/GALAH/public/GALAH_DR4/catalogs/) (155 MB)
{:.no_toc}

We provide a value-added catalog with kinematic and dynamical information that builds upon the 5D astrometric information from Gaia DR3 and radial velocities determined from GALAH spectra. The full list of columns is on the [Table Schema documentation](/dr4/table_schema). This catalogue provides:

* Heliocentric cartesian coordinates (`X_XYZ`, `Y_XYZ`, `Z_XYZ`) and velocities (`U_UVW`, `V_UVW`, `W_UVW`)
* Galactocentric cylindrical coordinates (`R_Rzphi`, `z_Rzphi`, `phi_Rzphi`) and velocities (`vR_Rzphi`, `vz_Rzphi`, `vT_Rzphi`)
* Orbital angles (`angle_R`, `angle_phi`, `angle_z`) and frequencies (`omega_R`, `omega_phi`, `omega_z`)
* Actions (`J_R`, `L_Z`, `J_Z`)
* Eccentricity (`ecc`)
* Maximum Galactocentric orbit height (`zmax`), pericenter and apocenter distances (`R_peri`, `R_ap`)
* Orbital energy (`Energy`)

For the calculation of orbit information we use the Python package `galpy` ([Bovy 2015](http://doi.org/10.1088/0067-0049/216/2/29)). To estimate actions, eccentricity, maximum orbit Galactocentric height, and apocenter/pericenter radii, we use the Staeckel fudge via the galpy module `actionAngleStaeckel` with a focal length of 0.45. We use the following potentials and observed properties of the Galaxy:
* The best fitting axisymmetric potential by McMillan (2017);
* A solar radius of 8.21 kpc, consistent with the latest measurement by Gravity Collaboration *et al.* (2019) of 8.178 ± 0.013(stat.) ± 0.022(sys.) kpc;
* A circular velocity at this radius of 233.1 km/s;
* The total motion of the Sun in the V-direction of 248.27 km/s by evaluation the proper motion measurements from Reid & Brunthaler (2004) at our chosen Solar radius;
* The Sun placed 25 pc above the plane (Jurić *et al.* 2008);
* The peculiar solar velocities U = 11.1 km/s and W=7.25 km/s by Schönrich *et al.* (2020) but V=15.17 km/s.

The input values for each star were:
* Sky positions (`ra`, `dec`) and proper motions (`pmra`, `pmdec`) from Gaia DR3 
* Radial velocities from GALAH DR4 (`rv_comp_1`)
* Distances from [Bailer-Jones *et al.* 2021](https://ui.adsabs.harvard.edu/abs/2021AJ....161..147B/abstract) (`r_med`)

----

#### 3D NLTE Li abundances
##### [Download `GALAH_DR4_VAC_li_allstar.fits`](https://cloud.datacentral.org.au/teamdata/GALAH/public/GALAH_DR4/catalogs/) (174 MB)
{:.no_toc}

We provide a value-added catalogue of 3D NLTE Li abundances, calculated with the same process as described in [Wang *et al.* (2024)](https://ui.adsabs.harvard.edu/abs/2024MNRAS.528.5394W/abstract). The full list of columns is on the [Table Schema documentation](/dr4/table_schema). This catalogue provides:

* Li 6708 line equivalent width (`EW`) and its uncertainties (`e_EW_low`, `e_EW_upp`) and the FWHM (`fwhm_li`)
* A(Li) abundance (`ALi`) and its uncertainties (`e_ALi_low`, `e_ALi_upp`)
* Li abundance quality flag (`flag_ALi`)

We recommend choosing only stars with `flag_ALi < 2` when using Li abundances and `flag_ALi < 4` when using Li equivalent widths (see [using the data](/dr4/using_the_data/) for more information). 

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
We recommend the `GALAH_DR4_main_allstar.fits` catalogue if you want our best effort stellar parameters and elemental abundances. This catalogue can be [directly downloaded from Data Central](https://cloud.datacentral.org.au/teamdata/GALAH/public/GALAH_DR4/catalogs/).<br/><br/>
Please read our [best practices for using GALAH DR4](/dr4/using_the_data).

Our primary repository of GALAH DR4 is provided by [Data Central](https://datacentral.org.au). From them you can [directly download](#downloading-the-fits-files) the catalogues as FITS files, or query via [TAP](#tap-query) or [ADQL](#adql-query).

Most of our catalogues are also found on [VizieR service](#vizier) of the Centre de Données astronomiques de Strasbourg (CDS).

#### Downloading the FITS files

The catalogues can be [downloaded from Data Central](https://cloud.datacentral.org.au/teamdata/GALAH/public/GALAH_DR3/) as FITS files, or using the following command (removing the `--spider` flag and replacing with the appropriate file name as listed below):

```bash
# Download the galah_dr4.main_star catalogue
wget --spider https://cloud.datacentral.org.au/teamdata/GALAH/public/GALAH_DR4/catalogs/GALAH_DR4_main_allstar.fits
```
#### TAP query

#### ADQL query

The catalogues can be accessed using the [query services provided by Data Central](https://datacentral.org.au/services/query/). The [Data Central schema browser](https://datacentral.org.au/services/schema/) contains the table and column names. The latest GALAH release is **Data Release 4**.

As an example, here the ADQL query for Data Central that would retrieve the first 100 likely members of globular cluster ω&nbsp;Centauri found in GALAH DR4:

```sql
SELECT
   TOP 100
   galah_main.sobject_id, galah_main.rv_galah,
   galah_main.fe_h, gaia_vac.dr3_source_id
   FROM galah_dr3p2.main_star as galah_main
   INNER JOIN galah_dr3p2.vac_gaia_edr3 as gaia_vac on galah_main.dr3_source_id = gaia_vac.dr3_source_id
   WHERE galah_main.flag_sp = 0 AND galah_main.flag_fe_h = 0
   AND sqrt(power(gaia_vac.pmra-(-3.2),2)+power(gaia_vac.pmdec-(-6.9),2)) < 1.5
   AND galah_main.rv_galah > 170
   AND 1=CONTAINS(POINT('ICRS', gaia_vac.ra, gaia_vac.dec),
                  CIRCLE('ICRS', 201.6836, -47.5068, 1.0 ))
```

{: .box-warning}
Data Central's ADQL engine does not like column name clashes. So if you are merging tables, it is necessary to explicitly list the columns of interest.

---
