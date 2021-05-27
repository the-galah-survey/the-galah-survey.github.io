---
layout: page
title: Technical Details
---

<!-- <h3> On this page</h3> -->
* This text gets replaced.
{:toc}
### The Anglo-Australian Telescope

The GALAH Survey primarily uses the [Anglo-Australian Telescope (AAT)](https://aat.anu.edu.au), a 4-metre equatorially-mounted telescope. It is located at Siding Spring Observatory in New South Wales, Australia, and is operated by the Australian National University on behalf of a consortium of 13 Australian Universities. Its function is to provide world-class observing facilities for Australian optical astronomers.

### 2dF and HERMES

{: style="text-align:center"}
![Light path of HERMES](/about/images/HERMES.png "Light path of HERMES")

GALAH observes using the HERMES spectrograph ([Sheinis et al. 2015](http://doi.org/10.1117/1.JATIS.1.3.035002)) at the Anglo-Australian Telescope. We were the primary science driver for the spectrograph. HERMES is a four-channel, multiobject, R~28,000 spectrograph fed by the 2dF fibre positioner ([Lewis et al. 2002](http://doi.org/10.1046/j.1365-8711.2002.05333.x)), which sits at prime focus. 2dF has two field plates, each of which has 392 science fibres and 8 guide bundles that can be allocated across a circular field with a two-degree diameter. One field plate can be set up by the fibre positioning robot while the other plate is being used for observation. Fibres subtend 2.1 arcseconds on the sky, with a positioning accuracy of 0.3 arcseconds, and have a minimum separation of about 30 arcseconds.

The fibres from the two 2dF plates are arranged in two pseudoslits that can move into place to inject light into the spectrograph. HERMES uses an off-axis collimator mirror, a series of dichroic elements, and volume phase holographic gratings to capture the following wavelength regions in four cameras with independent shutters:

| Band | λ<sub>min</sub> (nm) | λ<sub>max</sub> (nm) |
|:-------------:|:-------------:|:-------------:|
| Blue | 471.8 | 490.3 |
| Green | 564.9 | 587.3 |
| Red | 648.1 | 673.9 |
| IR | 759.0 | 789.0 |

The spectra are dispersed in the horizontal direction in the raw data, with one spectrum trace for each fibre.

The light path of HERMES:

{: style="text-align:center"}
![Light path of HERMES](/about/images/HERMES_light_path.png "Light path of HERMES")

HERMES spectra have a signal-to-noise ratio of 100 per resolution element in one hour of exposure time for stars with an apparent magnitude of 14 in the relevant Johnson/Cousins filter (B for the blue camera, V for the green camera, R for the red camera and I for the IR camera). The blue and green cameras use 16 micron, standard silicon detectors; the red camera has a 40 micron, deep depletion device with fringe suppression and an ER1 coating; and the IR camera has a 100-micron bulk silicon device with fringe suppression and a "Multi-9" coating. Further details on 2dF and HERMES can be found in the user manual.

#### 2018 Field Flattening Lens Replacement
In the first half of 2018, the original field flattening lenses of HERMES were replaced ([Edgar et al 2018](http://dx.doi.org/10.1117/12.2307305)). The original glass contained uranium that emitted α particles, which caused the saturated points and vertical readout streaks when they were captured by the HERMES CCDs. The point spread function in the HERMES cameras changed as a result of changing the field flattening lenses, and is now larger and less symmetric in the corners of the detectors. As part of HERMES recommissioning, the GALAH team fed light from a Fabry-Perot interferometer into HERMES to characterise the new PSF across each detector, and this information has been incorporated into the data reduction procedure.


### Target Selection

The target selection for the GALAH survey has had two phases.

#### Phase 1

The initial GALAH input catalog was made by combining the 2MASS (Skrutskie et al. 2006) catalog of infrared photometry with the UCAC4 (Zacharias et al. 2013) proper motion catalogue. We only included stars with reliable 2MASS data, as captured in their data quality flags (Q="A", B="1", C="0", X="0", A="0", prox>6"). We also rejected any star that had a nearby bright neighbour, with a rejection radius dependent on the bright star’s V magnitude, such that the potential target is rejected if the bright star is closer than (130 − [10 × V]) arcseconds.

The four main projects included in the GALAH DR3 catalogue are GALAH-main, GALAH-faint, K2-HERMES, and TESS- HERMES. The `survey_name` column of the main catalogue informs by which survey a given star was observed and its selection function:

* Main GALAH survey (`galah_main`): Potential targets are all stars with 12 < V < 14, δ < +10° and \|b\| > 10° in regions of the sky that have at least 400 targets in π² degrees (the 2dF field of view).
* GALAH-faint survey (`galah_faint`): Aimed at extending survey observations to regions with low target density. Given the lower density of stars the target selection was shifted to 12 < V < 14.3 as a way to maintain at least 400 stars per field.
* K2-HERMES (`k2_hermes`): Both "bright" (10 < V < 13) and "faint" (13 < V < 15, J − KS > 0.5) target cohorts, to complement the asteroseismic targets that are the focus of the K2 Galactic Archaeology Program (Stello et al. 2017)
* TESS-HERMES (`tess_hermes`) :Stars in the range 10.0 < V < 13.1 in the TESS Southern Continuous Viewing Zone ([Sharma et al 2018](doi.org/10.1093/mnras/stx2582))
* Other programs (`other`): Targeted observations in open clusters, the GALAH Pilot Survey (Martell et al. 2017), or targets from other HERMES observing that were not part of any of these surveys.


##### Signal-to-Noise
##### Spatial Coverage

#### Phase 2

##### A new focus for better ages

## K2-HERMES
## TESS-HERMES
## Open Clusters
## Other Programmes
