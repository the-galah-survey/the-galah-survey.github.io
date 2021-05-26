---
layout: page
title: Get the GALAH DR3 spectra
subtitle: Third Data Release
---

<h3> On this page</h3>
* This text gets replaced.
{:toc}

---

### Introduction to GALAH DR3 Spectral Library

GALAH DR3 provides reduced one-dimensional spectra for each star in the main catalogue. For each star there are (up to) four files, one for each HERMES camera. The entire GALAH DR3 spectral catalogue consists of 2,342,026 FITS files.

For a given star on a given camera, each file contains five extensions:

| Element | Name | Description |
| :------ |:--- | :--- |
| 0 | PRIMARY | Unnormalised spectrum with sky subtraction |
| 1 | input_sigma | Variance of the unnormalised spectrum with sky subtraction. This is expressed as the percentage of the unnormalised flux. |
| 2 | no_sky_subspectrum | Unnormalised spectrum with no sky subtraction |
| 3 | no_sky_sigma | Variance of the unnormalised spectrum with no sky subtraction |
| 4 | normalised spectra | Pseudo-continuum normalised spectrum with sky subtraction |

The naming convention of the spectra files is the `sobject_id` of a star followed by the camera number (i.e., 1=blue, 2=green, 3=red, 4=near-infrared). So, for example, for `sobject_id` 170418003701205, there are four files: 1704180037012051.fits, 1704180037012052.fits, 1704180037012053.fits, 1704180037012054.fits.

#### Missing spectral data

There are 12181 stars which are missing the spectra for some of their cameras. We provide a file at [GALAH_DR3_list_missing_reduced_spectra_v2.csv](https://cloud.datacentral.org.au/teamdata/GALAH/public/GALAH_DR3/spectra/GALAH_DR3_list_missing_reduced_spectra_v2.csv) that lists the sobject_id and the missing cameras. The missing spectra are concentrated into two data ranges:

* On the night of 27 August 2015 two fields (`field_id` 64 and 287) had data reduction problems that resulted in their spectra not being properly ingested into the Data Central system. This means that for `sobject_id` starting with 1508270040 or 1508270052, there are 243 and 111 stars respectively missing spectra for the blue and sometimes green camera.
* For the nights of 21--26 December 2018 (i.e., all `sobject_id` starting with 181221, 181222, 181223, 181224, 181225, 181226) there was a fault with the infrared camera of HERMES. This means that all stars observed on those nights lack a spectral file ending with 4.
    - For 227 stars of the stars observed on these nights, their spectrum files do not have the fifth extension described above – the normalized spectrum. We provide a file at [GALAH_DR3_list_missing_normalized_spectra_v2.csv](https://cloud.datacentral.org.au/teamdata/GALAH/public/GALAH_DR3/spectra/GALAH_DR3_list_missing_normalized_spectra_v2.csv) that lists the `sobject_id` of these files.

### Acquiring the spectral data

On this page we describe three methods for acquiring the spectra depending on your requirements:

1. [A few stars](#downloading-the-spectra-for-a-few-stars)
2. [A larger number of stars](#downloading-the-spectra-for-a-larger-number-of-stars)
3. The entire GALAH spectral catalogue.

#### Downloading the spectra for a few stars

The spectrum of an individual star can be accessed via the [Data Central Single Object Viewer](https://datacentral.org.au/services/sov/).

1. Search for the `sobject_id` of a given star, e.g., 170418003701205, and click on the entry that appears in the drop-down menu.

    <!-- ![Searching for a single star with the Data Central Single Object Viewer.](/dr3/images/sov_step1.png) -->

2. The results pages presents the normalized spectrum of the star. You can then either download all the available spectrum files for this `sobject_id` using the "Download all data products" button at the top-right of the page or download the spectrum from an individual camera.

    <!-- ![Searching for a single star with the Data Central Single Object Viewer.](/dr3/images/sov_step2.png) -->
    <!-- ![Searching for a single star with the Data Central Single Object Viewer.](/dr3/images/sov_step2b.png) -->
    <!-- ![Searching for a single star with the Data Central Single Object Viewer.](/dr3/images/sov_step2a.png) -->

#### Downloading the spectra for a larger number of stars

If you would like the spectra for a large number of stars, this can be achieved using the [Data Central Bulk Download](https://datacentral.org.au/services/download/). **A rule-of-thumb is that the query to create the packaged tar.gz file of spectra will take about 10 minutes per 10000 `sobject_id` requested**.

1. You will require the list of `sobject_id` you are interested in formatted as a comma-separated list. Copy the list of `sobject_id` in to *Source List* box, and select the following options:
* *GALAH Data Release 3* as the *Data Release*
* *GALAH DR3 HERMES 1D Spectrum* as the *Data products: Spectra*

2. Once the query is completed, you will be able to download tar.gz file of your requested spectra.

#### Downloading the entire GALAH spectral catalogue

{: .box-error}
**This is possible using the [bulk download option described above](#downloading-the-spectra-for-a-larger-number-of-stars), but the query takes about 20 hours to complete. Do not do this.**

{: .box-warning}
On decompression, you will require about 385 GB of free space. The decompressed files are located in a single directory, so please be aware of any file management limitations you might have dealing with 2 million files in a single directory.

The entire GALAH DR3 spectral library can be [dowloaded from here](https://cloud.datacentral.org.au/teamdata/GALAH/public/GALAH_DR3/spectra/). It is split over two files:

|  | Number of stars | Number of FITS files | Size |
| :------ |:--- | :--- |
| `GALAH_DR3_all_spectra_with_normalisation_v2.tar.gz`<br/><br/>GALAH DR3 spectral files that have been continuum normalised | 588,343 | 2,341,345 | 228 GB |
| `GALAH_DR3_all_spectra_missing_normalisation_v2.tar.gz`<br/><br/>GALAH DR3 spectral files that lack continuum normalisation. This is [discussed above](#missing-spectral-data) and their `sobject_id` are [listed here](https://cloud.datacentral.org.au/teamdata/GALAH/public/GALAH_DR3/spectra/GALAH_DR3_list_missing_normalized_spectra_v2.csv).| 227 | 681 | 49 MB |

As [discussed above](#missing-spectral-data), 12181 stars are missing spectra for one or two of their cameras due to reduction or instrumentation problems. A list of these missing spectra can be found in [GALAH_DR3_missing_reduced_spectra_v2.csv](https://cloud.datacentral.org.au/teamdata/GALAH/public/GALAH_DR3/spectra/GALAH_DR3_missing_reduced_spectra_v2.csv).

```bash
# Remove --spider to download
# Download the spectra for 588,343 stars that were successfully normalised.
wget --spider https://cloud.datacentral.org.au/teamdata/GALAH/public/GALAH_DR3/spectra/GALAH_DR3_all_spectra_with_normalisation_v2.tar.gz
# Download the spectra for 227 stars that were not normalised
wget --spider https://cloud.datacentral.org.au/teamdata/GALAH/public/GALAH_DR3/spectra/GALAH_DR3_all_spectra_missing_normalisation_v2.tar.gz
```

