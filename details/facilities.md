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
![Light path of HERMES](/science/images/HERMES.png "Light path of HERMES")

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
![Light path of HERMES](/science/images/HERMES_light_path.png "Light path of HERMES")

HERMES spectra have a signal-to-noise ratio of 100 per resolution element in one hour of exposure time for stars with an apparent magnitude of 14 in the relevant Johnson/Cousins filter (B for the blue camera, V for the green camera, R for the red camera and I for the IR camera). The blue and green cameras use 16 micron, standard silicon detectors; the red camera has a 40 micron, deep depletion device with fringe suppression and an ER1 coating; and the IR camera has a 100-micron bulk silicon device with fringe suppression and a "Multi-9" coating. Further details on 2dF and HERMES can be found in the user manual.

#### 2018 Field Flattening Lens Replacement
In the first half of 2018, the original field flattening lenses of HERMES were replaced ([Edgar et al 2018](http://dx.doi.org/10.1117/12.2307305)). The original glass contained uranium that emitted α particles, which caused the saturated points and vertical readout streaks when they were captured by the HERMES CCDs. The point spread function in the HERMES cameras changed as a result of changing the field flattening lenses, and is now larger and less symmetric in the corners of the detectors. As part of HERMES recommissioning, the GALAH team fed light from a Fabry-Perot interferometer into HERMES to characterise the new PSF across each detector, and this information has been incorporated into the data reduction procedure.
