---
layout: page
title: GALAH DR4
subtitle: Fourth Data Release
---
{: .main_blockquote}
The Fourth Data Release of the Galactic Archaeology with HERMES (GALAH) survey provides one-dimensional spectra, stellar atmospheric parameters and individual elemental abundances for 1,085,520 spectra of 917,588 stars in the Milky Way. They were observed with the HERMES spectrograph at the Anglo-Australian Telescope between December 2013 and August 2023. The release will be fully described in the forthcoming Buder *et al.* (2024)

{: .box-error}
**Want to start working right now with GALAH DR4?**{: style="font-size: 1.5rem;  font-weight: 800; line-height: 1.1;"}<br/><br/>
We recommend the `galah_dr4_allstar_240705.fits` catalogue if you want our best effort stellar parameters and elemental abundances. This catalogue can be [directly downloaded](https://cloud.datacentral.org.au/teamdata/GALAH/public/GALAH_DR4/catalogs/).<br/><br/>

Please read our [best practices for using GALAH DR4](/dr4/using_the_data).

<h3> On this page</h3>
* This text gets replaced.
{:toc}

---


#### Summary of GALAH DR4
![Overview of distances and photometric information for the stars](/dr4/img/plot_parallax_quality_and_cmds.png "Overview of distances and photometric information for the stars")

<!-- Above is an overview of distances and photometric information for the stars observed as part of GALAH DR4. The left panel shows the distances to stars in GALAH DR4 from the [Bailer-Jones *et al.* 2021](https://ui.adsabs.harvard.edu/abs/2021AJ....161..147B/abstract) catalogue. Due to the magnitude limited selection of stars, the majority of stars are not only dwarfs but also nearby; that is, within 1 kpc. Only 3.5% of stars are beyond 4 kpc. The center panel shows a reddened color-absolute magnitude diagram in the optical Gaia DR3 passbands. The right panel shows an analogous diagram made with the infrared 2MASS passbands. -->

* Our main catalogue contains data for 917,588 stars. It is fully described on our [Catalogue documentation](/dr4/the_catalogues).
 * We provide the reduced one-dimensional spectra for the catalogued stars. These are is fully described in our [Spectra documentation](/dr4/the_spectra).
* For ease of use, this release referred to as GALAH DR4 presents data from [multiple programs](/dr4/details/observing) as a single catalogue. It includes observations from:
  - GALAH Phase 1 (bright, main, and faint survey, 518,689 stars)
  - GALAH Phase 2 (focus on stars with reliable age determinations, 125,058 stars)
  - K2-HERMES (117,708 stars)
  - TESS-HERMES (37,228 stars) 
  - additional GALAH-related projects including the bulge and observations of more than 300 stellar clusters (5,675 stars).
* Compared to GALAH DR3, we improve our spectrum analysis with a neural network approach to spectrum synthesis that interpolates quickly from a base grid of synthetic spectra to simultaneously solve for stellar parameters and abundances. We also introduce a new module for identifying binary stars and fitting two superposed spectra. 

#### Data provided in GALAH DR4

For each star, we provide:
* [Reduced one-dimensional spectra](/dr4/the_spectra) across the four wavelength regions of the HERMES spectrograph
* Barycentric radial velocity
* In the case of a binary, barycentric radial velocity for the secondary star
* Stellar parameters (effective temperature, surface gravity, iron abundance, microturbulence, broadening)
* Up to 30 elemental abundances per star
    - light elements: Li, C, N, O
    - odd-Z elements: Na, Al, K
    - α-elements: Mg, Si, Ca, Ti 
    - iron-peak elements: Sc, V, Cr, Mn, Co, Ni, Cu, Zn
    - light and heavy slow neutron capture elements: Rb, Sr, Y, Zr, Mo, Ba, La, Ce, Nd
    - rapid neutron capture elements: Ru, Sm, Eu
* [Three value-added catalogues](/dr4/the_catalogues):
    - Galactic orbital properties
    - Crossmatches to Gaia DR3, 2MASS, and WISE with the contents of those catalogues
    - 3D NLTE lithium abundances

    #### Sky Coverage

![Sky coverage of GALAH DR4](/dr4/img/lb_overview_colored.png "Sky coverage of GALAH DR3")

The figure above displays the GALAH DR4 sky coverage in Galactic coordinates with the centre of the Galaxy at the origin. Shown are the GALAH Phase 1 targets (blue), which avoid the Galactic plane, and the GALAH Phase 2 targets (orange), which lie at low latitudes. The targets of the *K2*-HERMES follow-up (green) fall within with the *K2* campaigns along the ecliptic and show the characteristic tile-pattern of the *Kepler* telescope. The *TESS*-HERMES observations (red) are focused on the *TESS* Southern Continuous Viewing Zone. Additional GALAH-related projects (purple) are distributed across the sky.

---

### The GALAH DR4 Data Products
The two main data products of GALAH DR4 are the catalogue of stellar parameters & abundances, and the spectral library. We also provide three value-added catalogues.

#### GALAH DR4 Catalogues

{: .box-warning}
For science cases involving stellar parameters, it is highly recommended that you use the `galah_dr4_allstar_240705.fits` table, and that you only consider stars where `flag_sp == 0` and `flag_sp_fit == 0` (indicating reliable spectroscopic analysis), `flag_red == 0` (indicating successful data reduction), and `flag_fe_h == 0` (indicating a reliable metallicity). For science cases involving the abundance of element `X`, it is highly recommended that you only consider `x_fe` where `flag_x_fe == 0` and `snr_px_ccd3 > 30`. Our [Best Practices](/dr4/using_the_data) is a short guide of our recommendations for using GALAH DR4.

We provide two versions of the main GALAH DR4 catalogue:
* `galah_dr4_allstar_240705.fits` (723 MB). **Strongly recommend the use of this table for stellar parameters and abundances**. It contains one entry **per star**, and has radial velocity, stellar parameters and abundance data along with fundamental data from Gaia, 2MASS, and WISE.
* `galah_dr4_allspec_240705.fits` (833 MB). **This table is for expert use only**. It is the extended catalogue of stellar parameters and abundances, with one entry **per observation** and the same information as in the `allstar` file. 

There are also three value-added catalogues:
* Galactic orbital properties
* Crossmatches to Gaia DR3, 2MASS, and WISE with the contents of those catalogues
* 3D NLTE lithium abundances

The [Catalogue documentation](/dr4/the_catalogues) provides details on the catalogues and how to acquire them.

#### GALAH DR4 Spectra

GALAH DR4 provides the reduced one-dimensional spectrum for each star in the main catalogue. These can be downloaded either individually or in bulk. Instructions on how to retrieve GALAH DR4 spectra can be found on the Spectra data access documentation page.

For each star there are four files, one for each of the four HERMES cameras, with each spectrum file containing the:
* reduced spectrum
* normalised spectrum
* relative error of spectrum 
* sky spectrum used for sky subtraction
* telluric correction
* scattered light
* crosstalk
* resolution profile/FWHM

The [Spectra documentation](/dr4/the_spectra) provides details on the spectra and how to acquire them.


### Changes from the Third Data Release of GALAH

#### Data Reduction

There have been two major improvements to the data reduction:
1. Improved wavelength calibration for the long-wavelength end of the red camera, recovering spectra for around 15% of stars that were excluded from DR3.
2. Better identification and exclusion of bad or mislabeled data.

There are three main changes to the analysis methods for DR4 compared to DR3:
1. Using a neural network for rapid interpolation of synthetic spectra to various combinations of stellar parameters and abundances, trained on synthetic spectra produced with SME.
2. Simultaneous fitting of all stellar parameters and elemental abundances.
3. A three-phase process for the determination of stellar parameters and elemental abundances: first a pure spectroscopic analysis for individual observations of stars, then multiple observations are coadded and all spectra are reanalysed folding in photometric and astrometric information, then a post-analysis scan for signs of binarity, emission lines, and interstellar absorption.

Below is a comparison of results from GALAH DR3 (upper panels) and GALAH DR4 (lower panels, this release). The smooth light blue background indicates all measurements, whereas the colormap shows the number of unflagged measurements at each point. 

![Comparison of GALAH DR3 and GALAH DR4](dr4/img/galah_dr4_comparison_dr3.png "Comparison of GALAH DR3 and GALAH DR4")


---


### Need help?
Questions about GALAH DR4 that are not answered in the documentation? Contact us:

* Email galahsurvey@gmail.com


