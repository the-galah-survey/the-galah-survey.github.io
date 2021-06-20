---
layout: page
title: Reduction
subtitle: From raw image to spectra
---

{: .main_blockquote}
This page gives a very brief description of the GALAH Survey data reduction pipeline. If you are interested in all the details of the reduction used for Data Release 3, see [Kos *et al.* (2017)](https://doi.org/10.1093/mnras/stw2064). Essentially we use a [bespoke `iraf` pipeline](https://github.com/sheliak/galah_reduction) to collate and reduce all the HERMES spectra, and provide first estimates of the radial velocity and stellar parameters.


<!-- <h3> On this page</h3> -->
* This text gets replaced.
{:toc}

### Reduction used in Data Release 3

This follows the usual steps for reducing multi-object spectrograph data:

1. Raw images are corrected for bias level and flat field, and cosmic rays are removed with a modified LaCosmic algorithm ([van Dokkum 2001](http://doi.org/10.1086/323894)). Scattered light and fibre-cross talk signals are removed.
2. The wavelength solution for the extracted spectra is found via fitting of ThXe arc lamp observations.
3. Sky spectra are modelled from the 25 sky fibres included in each field and subtracted, and synthetic telluric lines are computed using `molecfit` ([Kausch *et al.* 2015](http://doi.org/10.1051/0004-6361/201423909); [Smette *et al.* 2015](http://dx.doi.org/10.1051/0004-6361/201423932%7D)) and removed from observed spectra.
4. The reduction pipeline runs a cross-correlation with AMBRE spectra ([De Laverny *et al.* 2012](https://dx.doi.org/10.1051/0004-6361/201219330)) to provide a first estimate of stellar parameters T<sub>eff</sub>, log*g*, [Fe/H], and radial velocity, (these values are labelled as `x_guess` in the main_spec catalogue; see the [Table Schema](/dr3/table_schema) documentation) and to normalise the spectra.

#### Changes in data reduction from GALAH Data Release 2

We are always working to improve our reduction. Between GALAH DR2 and GALAH DR3 there were two major improvements to the data reduction:

1. The main improvement is the wavelength solution, which is now more stable at the edges of green and red CCDs, where we lack arc lines. This has been achieved by monitoring the solution and fixing the polynomial describing the pixel-to-wavelength transformation, if deviations from a typical or average solution are detected.
2. Cross-talk is now parametrized differently. It can only be measured in larger gaps between every 10th spectrum.

<!-- ### Future improvements -->