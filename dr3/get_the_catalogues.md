---
layout: page
title: Get the GALAH DR3 catalogues
subtitle: Third Data Release
---

### On this page:

* [Introduction to GALAH DR3 Spectral Library](#introduction-to-the-galah-dr3-catalogues)
* [How to get the GALAH DR3 catalogues](#getting-the-catalogues)
    - [Downloading the FITS files](#downloading-the-fits-files)
    - [Using ADQL](#adql-query)

### Introduction to the GALAH DR3 Catalogues

We provide two versions of the GALAH DR3 catalogue (`galah_dr3.main_xx`):

* `galah_dr3.main_star`
    - GALAH_DR3_main_allstar_v2.fits (833 MB)
    - **Strongly recommend the use of this table**. One entry per star observed. Radial velocity, stellar parameters and abundance data. Important data from Gaia, 2MASS, and WISE.
* `galah_dr3.main_spec`
    - GALAH_DR3_main_allspec_v2.fits (2.1 GB)
    - **This table is for expert use only**. One entry per observation. Radial velocity, stellar parameters for each observation. Also contains abundances derived for each individual line. Important data from Gaia, 2MASS, and WISE.

There are also [several value-added catalogues](/dr3/value_added_catalogues/) (`galah_dr3.vac_xx`):

* `galah_dr3.vac_gaiaedr3`
    - GALAH_DR3_VAC_GaiaEDR3_v2.fits (338 MB)
    - *Gaia* eDR3 data for all stars in GALAH DR3
* `galah_dr3.vac_ages`
    - GALAH_DR3_VAC_ages_v2.fits (362 MB)
    - Stellar ages, masses, distances and other parameters estimated using isochrones
* `galah_dr3.vac_dynamics`
    - GALAH_DR3_VAC_dynamics_v2.fits (554 MB)
    - Galactic kinematic and dynamic parameters
* `galah_dr3.vac_rv`
    - GALAH_DR3_VAC_rv_v2.fits (67 MB)
    - Collated radial velocity measurements
* `galah_dr3.vac_galahfco`
    - target/galahfco_3_public.txt (957kB)
    - List of fields and field configurations. Each field has a unique ra, dec coordinates and field_id. Multiple configurtations can have same field_id.
* FGK binary stars
    - Identification of likely for double-lined spectroscopic binaries.
    - This VAC is served on the Centre de Données astronomiques de Strasbourg rather than Data Central.


### Getting the catalogues

{: .box-warning}
We recommend you use the `galah_dr3.main_star` catalogue if you want our best effort stellar parameters and elemental abundances. This catalogue can be directly downloaded from here (it has the file name `GALAH_DR3_main_allstar_v2.fits`)

{: .box-warning}
For science cases involving stellar parameters, it is highly recommended that you only consider stars where `flag_sp == 0` and `flag_fe_h == 0`. For science cases involving the abundance of element x, it is highly recommended that you only consider `X_fe` where `flag_X_fe == 0` and `snr_c3_iraf > 30`.

There are two methods for accessing these catalogues depending on your requirements

#### Downloading the FITS files

The catalogues can be [downloaded from here](https://cloud.datacentral.org.au/teamdata/GALAH/public/GALAH_DR3/) as FITS files, or using the following command (removing the `--spider` flag and replacing with the appropriate file name from the table above):

```bash
  # Download the galah_dr3.main_star catalogue
  wget --spider https://cloud.datacentral.org.au/teamdata/GALAH/public/GALAH_DR3/GALAH_DR3_main_allstar_v2.fits
```

#### ADQL query

{: .box-error}
The versions served by Data Central are currently our initial DR3 release and contain some minor errors.

The catalogues can be accessed using the [query services provided by Data Central](https://datacentral.org.au/services/). For example, if you are interested in all of the entries for stars likely to be members of the globular cluster omega Centauri, these could be found using a query like:

```sql
SELECT
   TOP 100
   *
   FROM galah_dr3.main_star
   WHERE
      1=CONTAINS(POINT('ICRS', ra, dec),
                 CIRCLE('ICRS', 201.6836, -47.5068, 1.0 ))
   AND sqrt(power(pmra-(-3.2),2)+power(pmdec-(-6.9),2)) < 1.5
   AND rv_galah > 170
```

**The catalogues of GALAH DR3 must be joined or cross-matched using the `sobject_id`**. Do not use Gaia source_id or the star_id for joining catalogues. These value-added catalogues are based upon the extended catalogue which contains measurements per observed spectrum. About 50000 stars were observed multiple times, and therefore have multiple observed spectra. The `sobject_id` column is our internal ID for each observation and using this column for joining will ensure that you are matching information derived from the same spectrum. For instance, to join the `galah_dr3.main_star` to the value-added catalogue of ages (`galah_dr3.vac_ages`), the following ADQL query could be used:

```sql
SELECT
   TOP 100
   g_ms.source_id, g_ages.sobject_id, g_ages.age_bstep, g_ages.e_age_bstep
   FROM galah_dr3.main_star AS g_ms
   JOIN galah_dr3.vac_ages AS g_ages
   	ON g_ms.sobject_id = g_ages.sobject_id
```
