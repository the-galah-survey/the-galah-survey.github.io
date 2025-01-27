---
layout: page
title: Observing and target selection
subtitle: Choosing which stars to look at
---

* This text gets replaced.
{:toc}

---

### Instrumentation requirements

The GALAH survey uses the [Two-Degree Field (2dF) fibre positioner with the HERMES spectrograph at the Anglo-Australian Telescope](/details/facilities). This instrumentation introduces requirements on our observing strategy and target selection:
* With 2dF we can observe about 350 stars per field (with another 25 fibres for the sky);
* We need to expose for about an hour per field as this is how long it takes the 2dF robot to reconfigure a field;
* There is a faint limit imposed by the size of the telescope and a reasonable rate of observing stars.

---

### Target Selection

The GALAH survey target selection and observing strategy consists of two generations, with a shift in focus driven by data from Gaia:
* [Phase 1](#phase-1-up-to-2020): Primarily a magnitude-limited survey
* [Phase 2](#phase-2-2020-onwards): Primarily focused on main sequence turn-off stars for age estimation.

#### Phase 1 (up to late 2020)

**A simple selection function**

The initial GALAH input catalog was made by combining the 2MASS catalog of infrared photometry with the UCAC4 proper motion catalogue. We only included stars with reliable 2MASS data, as captured in their data quality flags (`Q="A"`,` B="1"`, `C="0"`, `X="0"`, `A="0"`, `prox>6"`). We also rejected any star that had a nearby bright neighbour, with a rejection radius dependent on the bright star’s V magnitude, such that the potential target is rejected if the bright star is closer than (`130 − [10 × V]`) arcseconds.

The five main projects included in the GALAH DR4 catalogue are GALAH-main, GALAH-faint, GALAH Phase 2, K2-HERMES, and TESS-HERMES. The `survey_name` column of the [main catalogue](/dr4/the_catalogues) (`GALAH_DR4_main_allstar`) informs by which survey a given star was observed and its selection function:

* Main GALAH survey (`galah_main`): Potential targets are all stars with 12 < V < 14, δ < +10° and \|b\| > 10° in regions of the sky that had at least 400 targets in π² degrees (the 2dF field of view).
* GALAH-faint survey (`galah_faint`): Aimed at extending survey observations to regions with low target density. Given the lower density of stars the target selection was shifted to 12 < V < 14.3 as a way to maintain at least 400 stars per field.
* GALAH Phase 2 (`galah_phase2`): Selections in colour and absolute magnitude were added to give top priority to stars near the main sequence turnoff. When there were fewer than 400 of these in a field of view, the remaining fibres were filled with the main GALAH survey selection function.
* K2-HERMES (`k2_hermes`): Both "bright" (10 < V < 13) and "faint" (13 < V < 15, J − KS > 0.5) target cohorts, to complement the asteroseismic targets that are the focus of the K2 Galactic Archaeology Program ([Stello *et al.* 2017](https://doi.org/10.3847/1538-4357/835/1/83))
* TESS-HERMES (`tess_hermes`): Stars in the range 10.0 < V < 13.1 in the TESS Southern Continuous Viewing Zone ([Sharma *et al.* 2018](https://doi.org/10.1093/mnras/stx2582))
* Other programs (`other`): Targeted observations in open and globular clusters, the GALAH Pilot Survey, or targets from other HERMES observing that were not part of any of these surveys.

![Magnitude histograms for major subsurveys](/survey/img/mag_dist_function.svg){:width="100%"}

The imprints of these various magnitude limits from each sub-survey can be seen above in the overall apparent magnitude distribution function for stars observed by the GALAH survey (except for the `other` programs) as of August 2023.

---

#### Phase 2 (late 2020 onwards)

**A new focus for better ages**

In Phase 1, we primarily observed a magnitude-limited survey with an easily reproducible selection function and a broad scientific applicability. But the parallax information from Gaia allows us to estimate ages for evolved dwarfs like main sequence turnoff stars and subgiants (MSTO hereafter) with a precision of about 10%. Ages are an exciting complement to our stellar parameters, abundances and radial velocities, and add an important new dimension to several of our main science goals. In Phase 2, we are focusing our observations on stars for which precise ages can be estimated. There are three important changes to our target selection and observing strategy in GALAH Phase 2:

1. **Absolute magnitude limits**: We still select stars in the apparent magnitude range 12<V<14, but to focus on MSTO stars for which we can estimate ages reliably, we now prioritize stars with 2<M<sub>G</sub><4, which make up 37% of all stars in the range 12<V<14. For statistical completeness and to support other science projects that do not require ages, we allocate 10% of fibres to stars outside the range 2<M<sub>G</sub><4. For fields where we have fewer than 350 stars in this absolute magnitude range, we fill the remaining fibres following the apparent magnitude-based selection from Phase 1. We note that this modified selection function, being based directly on observables, is still easily reproducible for the purpose of Galactic modelling.

2. **Galactic latitude limits**: In the absence of Gaia DR2, in Phase 1, we selected stars with Galactic latitude \|b\| > 10 degrees, to avoid crowded lines of sight with high and uncertain extinction. The high-latitude selection returned a data set with a significant fraction of old stars, covering a wide region of the Galaxy. This selection limits our ability to study chemodynamical evolution and present-day radial and vertical trends near the Galactic plane. In Phase 2, with the availability of Gaia DR2, observations at 0°<\|b\|<10° fill in this gap in the data set and observations at 10°<\|b\|<30° increase our radial coverage out of the midplane. This expands our scientific capabilities, allowing us to explore the radial structure of the thin disc and its interface with the thick disc. There are about 2.35 million MSTO stars with 12<V<14, δ < 10° and \|b\|<30°, and GALAH can observe 264,000 of those in 2020-2022.

3. **Exposure time**: In Phase 1, we observed stars in range 12<V<14 with an exposure time of 1 hour. In Phase 2 we will observe stars in 12<V<13 for 1 hour and stars in 13<V<14 for 2 hours. This will increase the average exposure time from 1 hour to a modest 1.5 hours, but will significantly increase the overall precision of our stellar parameters and abundances. A SNR of 72 is required to achieve σ[α/Fe] of 0.04 (desirable for separating the thin and thick disc). Currently only 42% of our stars have SNR > 72. With this increase in exposure time 65% of stars will have SNR > 72 and 75% will have σ[α/Fe] better than 0.048, which is the global uncertainty of [α/Fe] in APOGEE.

---

### Tiling strategy

![Number of publications using GALAH](/survey/img/all_fields_on_sky.png)
<!-- {:width="100%"} -->

The GALAH survey tiles the sky into nearly 8000 possible field configurations covering about 7200 possible field centres. These are shown above in equatorial and galactic coordinates, GALAH fields in pink, K2-HERMES fields in gold, TESS-HERMES fields in silver, and open cluster fields in bronze. The [observing progress page](/survey/progress) shows which of these field centres have been observed.

The [list of all possible fields is available](https://cloud.datacentral.org.au/teamdata/GALAH/public/GALAH_DR3/target/galahfco_3_public.txt), and discussed in the [DR3 Catalogue documentation](/dr3/the_catalogues). For a given field centre (i.e., a given `ra`, `dec`) there is an associated unique identifier (`field_id`). For a given `field_id`, there can be one or more possible observable fields --- for instance if the target density is high enough, or there are bright and faint fields. Each possible configuration has a unique identifier of `fco_id`.

---

### Observing procedure

The observer at the telescope selects a field to observe from a list of possible fields identified by GALAH's `obsmanager` software. This identifies fields that will be about 45 minutes from transiting the meridian at the planned start of observing that field, i.e., they will highest in the sky. The coordinates and proper motions for the targets in each configuration are input into the [AAT's `configure`](https://aat.anu.edu.au/science/software/configure) software, along with a set of 20 candidate fiducial stars for guiding, and 50 possible "sky" positions. The fiducial stars are taken from the GALAH target catalogue in the same field of view, with magnitudes in the range 11<V<12. `configure` finds an optimal arrangement for the science targets, sky positions, and fiducial stars using a simulated annealing algorithm and outputs a file that is passed to the fibre positioning robot to set up the field. Further details on `configure` can be found in [Miszalski *et al.* 2006](https://doi.org/10.1111/j.1365-2966.2006.10777.x).

The standard observing procedure for regular GALAH survey fields is to take three equal-length exposures (3×1200s in GALAH Phase 1; up to 3×1800s in GALAH Phase 2), which is extended to four science exposures if the seeing is between 2 and 2.5 arcseconds, and to six exposures if the seeing is between 2.5 and 3 arcseconds. Flat-field and arc exposures are taken directly before or after each science configuration, since moving between the two pseudoslits of HERMES moves the position of the spectrum traces on the detector slightly. Bright-star fields are observed in evening and morning twilight, and in case of seeing too poor for the regular survey fields.

---

#### Achieved Signal-to-noise

![SNR histogram for each camera](/survey/img/snr_per_camera.svg){:width="100%"}
Distribution of signal-to-noise ratio in each camera. For each camera, the filled histogram represents stars with `flag_sp` < 512, which are likely to have reliable stellar parameters and abundances, and the black histogram represents stars with higher `flag_sp`, which may need to be excluded from some analyses.

![SNR versus apparent magnitude](/survey/img/survey_progress_signal_to_noise_per_mag.svg){:width="100%"}
Distribution of average achieved S/N per pixel for the green camera (CCD 2) as a function of apparent Gaia G magnitude. The dashed white line is our S/N=50 aim, and the red curve is the median S/N achieved as a function of magnitude.
