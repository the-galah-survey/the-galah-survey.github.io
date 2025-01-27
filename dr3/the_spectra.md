---
layout: page
title: GALAH DR3 spectra
subtitle: Third Data Release
---

{: .main_blockquote}
This page describes the spectral library of GALAH DR3 and how to get it.

* This text gets replaced.
{:toc}

---

### Introduction to GALAH DR3 Spectral Library

GALAH DR3 provides reduced one-dimensional spectra for each star in the main catalogue. For each star there are (up to) four files, one for each HERMES camera. The entire GALAH DR3 spectral catalogue consists of 2,342,026 FITS files.

For a given star on a given camera, each file contains five extensions:

1. `PRIMARY`: Unnormalised spectrum with sky subtraction
2. `input_sigma`: Relative error of spectrum with sky subtraction. To calculate absolute error multiply with first extension for unnormalised error (fits[0] * fits[1]), and with the fifth extension for pseudo-continuum normalised error (fits[4] * fits[1]).
3. `no_sky_subspectrum`: Unnormalised spectrum with no sky subtraction
4. `no_sky_sigma`: Variance of the unnormalised spectrum with no sky subtraction
5. `normalised spectra`: Pseudo-continuum normalised spectrum with sky subtraction

The naming convention of the spectra files is the `sobject_id` of a star followed by the camera number (i.e., 1=blue, 2=green, 3=red, 4=near-infrared). So, for example, for `sobject_id` 170418003701205, there are four files: 1704180037012051.fits, 1704180037012052.fits, 1704180037012053.fits, 1704180037012054.fits.

#### Missing spectral data

There are 12181 stars which are missing the spectra for some of their cameras. We provide a [list of the `sobject_id` and the missing cameras](https://cloud.datacentral.org.au/teamdata/GALAH/public/GALAH_DR3/spectra/GALAH_DR3_list_missing_reduced_spectra_v2.csv). The missing spectra are concentrated into two data ranges:

1. On the night of 27 August 2015 two fields (`field_id` 64 and 287) had data reduction problems that resulted in their spectra not being properly ingested into the Data Central system. This means that for `sobject_id` starting with 1508270040 or 1508270052, there are 243 and 111 stars respectively missing spectra for the blue and sometimes green camera.
2. For the nights of 21--26 December 2018 (i.e., all `sobject_id` starting with 181221, 181222, 181223, 181224, 181225, 181226) there was a fault with the infrared camera of HERMES. This means that all stars observed on those nights lack a spectral file ending with 4.
    - For 227 stars of the stars observed on these nights, their spectrum files do not have the fifth extension described above – the normalized spectrum. We provide [list of these by `sobject_id`](https://cloud.datacentral.org.au/teamdata/GALAH/public/GALAH_DR3/spectra/GALAH_DR3_list_missing_normalized_spectra_v2.csv).

---

### Acquiring the spectral data

The GALAH DR3 spectral library is served by [Data Central](https://datacentral.org.au). There are four methods for acquiring the spectra depending on your requirements:

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

#### Downloading the spectra for a few stars

The spectrum of an individual star can be accessed via the [Data Central Single Object Viewer](https://datacentral.org.au/services/sov/).
1. Search for the `sobject_id` of a given star, e.g., 170418003701205, and click on the entry that appears in the drop-down menu.
2. The results pages presents the normalized spectrum of the star. You can then either download all the available spectrum files for this `sobject_id` using the "Download all data products" button at the top-right of the page or download the spectrum from an individual camera.

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
On decompression, you will require about 385 GB of free space. The decompressed files are located in a single directory, so please be aware of any file management limitations you might have dealing with 2 million files in a single directory.

The entire GALAH DR3 spectral library is found in two files:

* `GALAH_DR3_all_spectra_with_normalisation_v2.tar.gz` (compressed 228 GB file)
    - The collection of spectra for 588,343 stars that have a continuum normalised spectrum.
    - Contains 2,341,345 individual files.

* `GALAH_DR3_all_spectra_missing_normalisation_v2.tar.gz` (compressed 49 MB file)
    - The collection of spectra for 227 stars that [lack continuum normalisation](#missing-spectral-data).
    - Contains 681 individual files.
    - There is a [list of their `sobject_id`](https://cloud.datacentral.org.au/teamdata/GALAH/public/GALAH_DR3/spectra/GALAH_DR3_list_missing_normalized_spectra_v2.csv).

These two files can be [dowloaded from Data Central](https://cloud.datacentral.org.au/teamdata/GALAH/public/GALAH_DR3/spectra/). Due to the size of the compressed files, we would recommend using something like a `wget` command to download these spectra (removing the `--spider` flag):

```bash
# Remove --spider to download
# Download the spectra for 588,343 stars that were successfully normalised.
wget --spider https://cloud.datacentral.org.au/teamdata/GALAH/public/GALAH_DR3/spectra/GALAH_DR3_all_spectra_with_normalisation_v2.tar.gz
# Download the spectra for 227 stars that were not normalised
wget --spider https://cloud.datacentral.org.au/teamdata/GALAH/public/GALAH_DR3/spectra/GALAH_DR3_all_spectra_missing_normalisation_v2.tar.gz
```
