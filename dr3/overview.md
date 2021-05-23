---
layout: page
title: GALAH DR3
subtitle: Third Data Release
---

<div class="box-error">
<h3>Want to start working right now with GALAH data?</h3>
<p>We recommend the <code>galah_dr3.main_star</code> catalogue. This table can be directly downloaded <a href="https://cloud.datacentral.org.au/teamdata/GALAH/public/GALAH_DR3/">downloaded from here</a> under the filename <code>GALAH_DR3_main_allstar_v2.fits</code>.</p>
<p>Please make sure to read the Using GALAH Data page for our recommandations.</p>
</div>

The GALAH survey released our Third Data Release (DR3) on 6 November 2020. It provides reduced one-dimensional spectra, stellar atmospheric parameters and individual elemental abundances for almost 600,000 stars. The release is fully described in [Buder et al. (2021)](https://arxiv.org/abs/2011.02505).

### What's in GALAH+ DR3?

The Third Data Release of the Galactic Archaeology with HERMES (GALAH) survey provides stellar parameters and elemental abundances for 678,423 spectra of 588,571 mostly nearby stars, that have been observed with the HERMES spectrograph at the Anglo-Australian Telescope between November 2013 and February 2019. The release is fully described in Buder et al (2021).

#### Summary of GALAH DR3
* Our catalogue comprises 383,088 (65%) dwarfs and 200927 (34%) giants, with the remaining 4556 (1%) as unclassified stars.
* Based on stars with reliable chemical composition and age, we find 62.5% young low-alpha stars, 8.8% young high-alpha stars, 26.9% old stars, and 1.8% stars with [Fe/H] < -1. Based on kinematics, we find 4% halo stars.
* We provide the reduced one-dimensional spectra for the catalogued stars. Details on downloading the spectra can be found on the Spectra Data Access page.
* For ease of use, this release referred to as GALAH+ DR3 presents data from multiple programs as a single catalogue. It includes observations from GALAH Phase 1 (bright, main, and faint survey, 476,863 spectra), the K2-HERMES (112,943 spectra) and TESS-HERMES (34,263 spectra) surveys, as well as additional GALAH-related projects including the bulge and observations of more than 75 stellar clusters (54,354 spectra). See the Instrumentation, Target Selection and Observations page for more details.
* Compared to GALAH DR2, we improve our spectrum analysis with external astro- and photometric information from Gaia DR2 and 2MASS to estimate more accurate stellar surface gravities, thus breaking spectroscopic degeneracies. We also use Spectroscopy Made Easy (SME) to analyse the entire spectral data set. See the data reduction and analysis page for more details.

#### For all targets in DR3, we provide:

* Reduced one-dimensional spectra across the four wavelength regions of the HERMES spectrograph
* Barycentric radial velocities
* Stellar parameters (effective temperature, surface gravity, iron abundance, microturbulence, broadening)
* The overall alpha-element abundance, and up to 30 elemental abundances per star
    - light elements: Li, C, O
    - odd-Z elements: Na, Al, K
    - α-elements: Mg, Si, Ca, Ti (and TiII)
    - iron-peak elements: Sc, V, Cr, Mn, Co, Ni, Cu, Zn
    - light and heavy slow neutron capture elements: Y, Ba, La, Rb, Mo, Ru, Nd, Sm
    - rapid neutron capture element: Eu
* A number of value-added catalogues:
    - Age and mass estimates
    - Galactic orbital dynamics
    - Binarity probabilities

![Overview of distances and photometric information for the spectra](/assets/img/data_plots/plot_parallax_quality_and_cmds.png)

Above is an overview of distances and photometric information for the spectra (including repeats for some stars) observed as part of GALAH DR3. Panel a) shows the distances of stars in GALAH DR3. Due to the magnitude limited selection of stars, the majority of stars are not only dwarfs but also nearby; that is, within 1 kpc. Only 5.8% of stars are beyond 4 kpc. Panel b) shows a reddened color-absolute magnitude diagram in the optical Gaia DR2 passbands. Panel c) shows an analogous diagram made with the infrared 2MASS passbands.

#### Sky Coverage

![Sky coverage of GALAH DR3](/assets/img/data_plots/lb_overview_colored.png)

Overview of the distribution of stars included in this data release in Galactic coordinates with the centre of the Galaxy at the origin. Shown are the GALAH main (blue) and faint (orange) targets, which avoid the Galactic plane. The targets of the *K2*-HERMES follow-up (green) fall within with the *K2* campaigns along the ecliptic and show the characteristic tile-pattern of the *Kepler* telescope. The *TESS*-HERMES observations (red) are focused on the *TESS* Southern Continuous Viewing Zone. Other HERMES targets (purple) are distributed across the sky and were observed during independent programs.

### The GALAH DR3 Data Products
The two main data products of GALAH DR3 are the catalogue of stellar parameters & abundances, and the spectral library. We also provide several value-added catalogues.

#### Catalogues

{: .box-warning}
For science cases involving stellar parameters, it is highly recommended that you use the `galah_dr3.main_star` table, and that you only consider stars where `flag_sp == 0` and `flag_fe_h == 0`. For science cases involving the abundance of element `X`, it is highly recommended that you only consider `x_fe` where `flag_x_fe == 0` and `snr_c3_iraf > 30`. See the Using GALAH Data page for short guide to the tables and our recommendations.

The GALAH DR3 catalogues can be accessed either by:
* [Direct download from Data Central](https://cloud.datacentral.org.au/teamdata/GALAH/public/GALAH_DR3/) of the catalogues as FITS files
* The query services on the Data Central webpage (note that these are currently out of date).

We provide two versions of the GALAH DR3 catalogue (`galah_dr3.main_xx`), and several value-added catalogues (`galah_dr3.vac_xx`). Full instructions on how to retrieve GALAH DR3 catalogues can be found on the Catalogue data access documentation page. Full details on the value-added catalogues can be found here.

| Table name | File name | Description |
| :------ |:--- | :--- |
| galah_dr3.main_star | GALAH_DR3_main_allstar_v2.fits<br/>(833 MB) | **Strongly recommend the use of this table**. One entry per star observed. Radial velocity, stellar parameters and abundance data. Important data from Gaia, 2MASS, and WISE. |
| galah_dr3.main_spec | GALAH_DR3_main_allspec_v2.fits<br/>(2.1 GB) | One entry per observation. Radial velocity, stellar parameters for each observation. Also contains abundances derived for each individual line. Important data from Gaia, 2MASS, and WISE. |
| galah_dr3.vac_gaiaedr3 | GALAH_DR3_VAC_GaiaEDR3_v2.fits<br/>(338 MB) | Gaia eDR3 data for all stars in GALAH DR3 |
| galah_dr3.vac_ages | GALAH_DR3_VAC_ages_v2.fits<br/>(362 MB | Stellar ages, masses, distances and other parameters estimated using isochrones |
| galah_dr3.vac_dynamics | GALAH_DR3_VAC_dynamics_v2.fits<br/>(554 MB) | Galactic kinematic and dynamic parameters |
| galah_dr3.vac_rv | GALAH_DR3_VAC_rv_v2.fits<br/>(67 MB) | Collated radial velocity measurements |
| galahfco | target/galahfco_3_public.txt<br/>(957kB) | List of fields and field configurations. Each field has a unique ra, dec coordinates and field_id. Multiple configurtations can have same field_id.|
| FGK binary stars |  | Identification of likely for double-lined spectroscopic binaries. This VAC is served on the Centre de Données astronomiques de Strasbourg rather than Data Central. |

#### Spectra

GALAH DR3 provides the reduced one-dimensional spectrum for each star in the main catalogue. These files can be accessed via the Single Object Viewer or as a Bulk Download. Instructions on how to retrieve GALAH DR3 spectra can be found on the Spectra data access documentation page.

For each star there are four files, one for each of the four HERMES cameras, with each spectrum file containing:
* The reduced spectrum
* The variance of the reduced spectrum
* The pseudo-continuum normalized spectrum
* The variance of the pseudo-continuum normalized spectrum
* The sky spectrum used for sky subtraction

### Changes from the Second Data Release of GALAH

#### Data Reduction

There have been two major improvements to the data reduction:
1. The main improvement is the wavelength solution, which is now more stable at the edges of green and red CCDs, where we lack arc lines. This has been achieved by monitoring the solution and fixing the polynomial describing the pixel-to-wavelength transformation, if deviations from a typical or average solution are detected.
2. Cross-talk is now parametrized differently. It can only be measured in larger gaps between every 10th spectrum.
Analysis

There are two main changes to the analysis methods for DR3 compared to DR2:
1. We are using astrometric information from Gaia DR2 to break spectroscopic degeneracies. This requirement has resulted in about 5000 stars that were in GALAH DR2 not being in GALAH DR3. See the data reduction and analysis documentation for more details.
2. GALAH DR3 uses Spectroscopy Made Easy for all the stellar parameter and elemental abundance determination. For the second data release of the GALAH survey we made use of data-driven approaches to improve both speed and precision of the spectroscopic analysis. Although the data-driven approaches were successful for the majority of GALAH DR2 stars, we know that these approaches can suffer from signal aliasing, they can learn unphysical correlations between the input data and the output stellar labels, and the results are not necessarily valid outside the parameter space of the training set. We found in DR2 that the data-driven approaches meant that stars at the periphery in stellar label space, e.g. high temperature or low metallicity did not receive optimal labels from the data driven process.

Below is a comparison of GALAH DR2 (upper panels) and GALAH DR3 (lower panels, this release). The smooth light blue background indicates all measurements, whereas the colormap shows the number of unflagged measurements at each point. The stellar parameters and abundances from GALAH DR2 appear more tightly constrained, but we note that this is an artefact of the data-driven approach, which tends to find solutions closer to the mean parameter/abundance patterns.

![Sky coverage of GALAH DR3](/assets/img/data_plots/galah_dr3_comparison_dr2.png)

### Need help?
Questions about GALAH DR3 that are not answered in the documentation? Contact us:

* Email galah.helpdesk@gmail.com
* Twitter: @galahsurvey

<!-- ### Quick start

Do you want the GALAH DR3 catalogue of stellar parameters and abundances for your research?

We recommend the `galah_dr3.main_star` catalogue. This table can be downloaded from here (it has the file name `GALAH_DR3_main_allstar_v2.fits`), or by using `wget` (removing the ``--spider` flag) at the command line:

```
# Remove the --spider flag
wget --spider https://cloud.datacentral.org.au/teamdata/GALAH/public/GALAH_DR3/GALAH_DR3_main_allstar_v2.fits
```

For science cases involving stellar parameters, it is **highly recommended** that you only consider stars where `flag_sp == 0` and `flag_fe_h == 0`. For science cases involving the abundance of element X, it is highly recommended that you only consider X_fe where ``flag_X_fe == 0`` and ``snr_c3_iraf > 30``. See the Using GALAH Data page for short guide to the tables and our recommendations. -->
