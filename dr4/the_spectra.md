---
layout: page
title: GALAH DR4 spectra
subtitle: Fourth Data Release
---

{: .main_blockquote}
This page describes the spectral library of GALAH DR4 and how to get it.

* This text gets replaced.
{:toc}

---

### Introduction to GALAH DR4 Spectral Library

GALAH DR4 provides reduced one-dimensional spectra for each star in the main catalogue. For each star there are (up to) four files, one for each HERMES camera. The entire GALAH DR4 spectral catalogue consists of *find this number* FITS files.

For a given star on a given camera, each file contains eight extensions:

1. `Primary`: Reduced spectrum, sky subtracted, not normalised
2. `normalized`: Normalised spectrum
3. `relative_error`: Relative error of spectrum. Multiply by normalised or non-normalised spectrum to get error values. 
4. `sky`: Sky spectrum used for sky subtraction
5. `teluric`: Telluric correction
6. `scattered`: Scattered light
7. `cross_talk`: Crosstalk
8. `resolution_profile`: Resolution profile, given as the FWHM of the LSF

The naming convention of the spectra files is the `sobject_id` of a star followed by the camera number (i.e., 1=blue, 2=green, 3=red, 4=near-infrared). So, for example, for `sobject_id` 170418003701205, there are four files: 1704180037012051.fits, 1704180037012052.fits, 1704180037012053.fits, 1704180037012054.fits.

#### Missing spectral data

A fraction of stars are missing the spectra from one or more cameras. Here are the specific nights and fields affected:

1. For the nights of 20--26 December 2018 (i.e., all `sobject_id` starting with 181220, 181221, 181222, 181223, 181224, 181225, 181226) there was a fault with the infrared camera of HERMES, and all stars observed on those nights lack CCD4 data (i.e., a spectral file with a filename ending in 4).
3. On 8 February 2023, stars in `field_id` 7471 (`sobject_id` starting with 2302080028) and `field_id` 8123 (`sobject_id` starting with 2302080022) are missing CCD4 data. Stars in `field_id` 9726 (`sobject_id` starting with 2302080016) are missing CCD3 and CCD4 data.
4. On 2, 3, 10 March 2023 (`sobject_id` starting with 230302, 230303, and 230310) there was a fault with the infrared camera of HERMES and all stars observed on those nights lack CCD4 data.

---

### Acquiring the spectral data

The GALAH DR4 spectral library is served by [Data Central](https://datacentral.org.au). There are four methods for acquiring the spectra depending on your requirements:

1. [Simple Spectral Access Service](#simple-spectral-access-service)
1. [A few stars](#downloading-the-spectra-for-a-few-stars)
2. [A larger number of stars](#downloading-the-spectra-for-a-larger-number-of-stars)
3. [The entire GALAH spectral catalogue.](#downloading-the-entire-galah-spectral-catalogue)

#### Simple Spectral Access Service

The Simple Spectral Access (SSA) service provides a Virtual Observatory (VO) compliant standard interface to query and [access spectroscopic data hosted at Data Central](https://docs.datacentral.org.au/reference/services/simple-spectral-access-ssa-service/). Queries may be submitted through an HTTP GET request to the service. Results of the query are returned in VOTABLE format that includes spectra metadata and links to spectra. A default limit of 1000 results is in place to ensure results are returned in a timely manner. Data Central provides an example written in Python of a [GALAH DR3 Interactive Spectra Explorer enhanced by the Data Central API](https://docs.datacentral.org.au/help-center/virtual-observatory-examples/ssa-galah-dr3-interactive-spectra-explorer-enhanced-data-central-api/).

Effectively, you need to construct a URL of the form:
```bash
https://datacentral.org.au/vo/slink/links?ID=sobject_id&DR=galah_dr3&IDX=0&FILT=x&RESPONSEFORMAT=fits
```
changing the `sobject_id` to a valid value from the GALAH catalogue, and the `x` in `FILT=x` to `B`, `G`, `R`, `I` (respectively Blue/CCD1, Green/CCD2, Red/CCD3, Infrared/CCD4) for the particular camera of interest.

<!---
#### Downloading the spectra for a few stars

The spectrum of an individual star can be accessed via the [Data Central Single Object Viewer](https://datacentral.org.au/services/sov/).
1. Search for the `sobject_id` of a given star, e.g., 170418003701205, and click on the entry that appears in the drop-down menu.
2. The results pages presents the normalized spectrum of the star. You can then either download all the available spectrum files for this `sobject_id` using the "Download all data products" button at the top-right of the page or download the spectrum from an individual camera.
--->

#### Viewing the spectra for a small number of stars

Coming soon: access to the spectrum of an individual star via the [Data Central Spectrum Viewer](https://apps.datacentral.org.au/galah/spectra). You can choose to look at the normalised or non-normalised spectrum, from individual sobject_ids or combined, and you can overplot the best-fitting model and the locations of the spectral lines used for abundance determination. The current version of the page shows one star, 140116004301057, and Data Central are adding a search box so you can view any star from GALAH DR4.

#### Downloading the spectra for a larger number of stars

As well as the [Simple Spectral Access Service](#simple-spectral-access-service), if you would like the spectra for a large number of stars, this can be achieved using the [Data Central Bulk Download](https://datacentral.org.au/services/download/). **A rule-of-thumb is that the query to create the packaged tar.gz file of spectra will take about 10 minutes per 10000 `sobject_id` requested**.

1. You will require the list of `sobject_id` you are interested in formatted as a comma-separated list. Copy the list of `sobject_id` in to *Source List* box, and select the following options:
* *GALAH Data Release 3* as the *Data Release*
* *GALAH DR3 HERMES 1D Spectrum* as the *Data products: Spectra*

2. Once the query is completed, you will be able to download tar.gz file of your requested spectra.

#### Downloading the entire GALAH spectral catalogue

{: .box-error}
It is possible to get the entire spectral catalogue with the [bulk download option described above](#downloading-the-spectra-for-a-larger-number-of-stars), but the query takes about 20 hours to complete. 

{: .box-warning}
On decompression, you will require about 385 GB of free space. The decompressed files are located in a single directory, so please be aware of any file management limitations you might have dealing with millions of files in a single directory.

Please contact us ([galahsurvey@gmail.com](mailto:galahsurvey@gmail.com)) about your data needs instead of doing this.
