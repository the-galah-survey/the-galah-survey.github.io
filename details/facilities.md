---
layout: page
title: Facilities
subtitle: The telescope and the spectrograph
---

{: .main_blockquote}
The GALAH survey uses the Two-Degree Field (2dF) fibre positioner with the HERMES spectrograph at the Anglo-Australian Telescope. Explore below to learn more about the Anglo-Australian Telescope and the HERMES spectrograph.

<!-- <h3> On this page</h3> -->
* This text gets replaced.
{:toc}

---

### The Anglo-Australian Telescope

{: style="text-align:center"}
![The HERMES Spectrograph installed at the AAT](/details/img/aat_hermes.png)
*The Two-Degree Field fibre positioner installed at the top-end of the Anglo-Australian Telescope.*

The GALAH Survey primarily uses the [Anglo-Australian Telescope](https://aat.anu.edu.au), a 4-metre equatorially-mounted telescope. It is located at Siding Spring Observatory in New South Wales, Australia, and is operated by the Australian National University on behalf of a consortium of 13 Australian Universities. Its function is to provide world-class observing facilities for Australian optical astronomers.

{% include youtube.html id="qOtkI4HYzTk" %}

---

### 2dF and HERMES

{: style="text-align:center"}
![The HERMES Spectrograph installed at the AAT](/details/img/HERMES_photo.png "The HERMES Spectrograph installed at the AAT")
*The HERMES Spectrograph installed at the AAT.*

GALAH observes using the HERMES spectrograph ([Sheinis et al. 2015](http://doi.org/10.1117/1.JATIS.1.3.035002)) at the Anglo-Australian Telescope. GALAH was the primary science driver for the HERMES, a high resolution (R~28,000 or 50,000) fibre-fed multi-object spectrometer. It has four non-contiguous spectral bands, covering a total of approximately 100 nm between about 470 nm and 790 nm. These bands were selected to permit the measurement of the abundances of as many elements as possible from the major nucleosynthetic processes.

HERMES utilizes the 2-degree field (2dF) positioner ([Lewis et al. 2002](http://doi.org/10.1046/j.1365-8711.2002.05333.x)). 2dF has two field plates, each of which has 392 science fibres and 8 guide bundles that can be allocated across a circular field with a two-degree diameter. One field plate can be set up by the fibre positioning robot while the other plate is being used for observation. Fibres subtend 2.1 arcseconds on the sky, with a positioning accuracy of 0.3 arcseconds, and have a minimum separation of about 30 arcseconds.

The fibres from the two 2dF plates are arranged in two pseudoslits that can move into place to inject light into the spectrograph. HERMES uses an off-axis collimator mirror, a series of dichroic elements, and volume phase holographic gratings to capture the following wavelength regions in four cameras with independent shutters:

| Band | λ<sub>min</sub> (nm) | λ<sub>max</sub> (nm) |
|:-------------:|:-------------:|:-------------:|
| Blue | 471.8 | 490.3 |
| Green | 564.9 | 587.3 |
| Red | 648.1 | 673.9 |
| IR | 759.0 | 789.0 |

The spectra are dispersed in the horizontal direction in the raw data, with one spectrum trace for each fibre.

![Light path of HERMES](/details/img/HERMES_light_path.png "Light path of HERMES")
*The light path of HERMES.*{: .mx-auto.d-block :}

HERMES spectra have a signal-to-noise ratio of 100 per resolution element in one hour of exposure time for stars with an apparent magnitude of 14 in the relevant Johnson/Cousins filter (B for the blue camera, V for the green camera, R for the red camera and I for the IR camera). The blue and green cameras use 16 micron, standard silicon detectors; the red camera has a 40 micron, deep depletion device with fringe suppression and an ER1 coating; and the IR camera has a 100-micron bulk silicon device with fringe suppression and a "Multi-9" coating. Further details on 2dF and HERMES can be found at the [Anglo-Australian Telescope website](https://aat.anu.edu.au/science/instruments/current/HERMES).

#### 2018 Field Flattening Lens Replacement
In the first half of 2018, the original field flattening lenses of HERMES were replaced ([Edgar et al 2018](http://dx.doi.org/10.1117/12.2307305)). The original glass contained uranium that emitted α particles, which caused the saturated points and vertical readout streaks when they were captured by the HERMES CCDs. The point spread function in the HERMES cameras changed as a result of changing the field flattening lenses, and is now larger and less symmetric in the corners of the detectors. As part of HERMES recommissioning, the GALAH team fed light from a Fabry-Perot interferometer into HERMES to characterise the new PSF across each detector, and this information has been incorporated into the data reduction procedure.

#### Technical papers describing HERMES
These technical papers describe various aspects of the design, construction, and first light performance of HERMES.

##### 2018
{:.no_toc}

* [**Radioactive emission from high-index,optical glasses and atypical effects on CCDs**](https://ui.adsabs.harvard.edu/abs/2018SPIE10706E..33E)<br/>Edgar *et al.* (2018) SPIE **10706** 1070633 <small>([doi:10.1117/12.2307305](https://doi.org/10.1117/12.2307305))</small>

##### 2016
{:.no_toc}

* [**First light results from the HERMES spectrograph at the AAT**](https://ui.adsabs.harvard.edu/abs/2016SPIE.9908E..1CS)<br/>Sheinis (2016) SPIE **9908** 99081C <small>([doi:10.1117/12.2234334](https://doi.org/10.1117/12.2234334), [arXiv:1509.00129](https://arxiv.org/abs/arXiv:1509.00129))</small>

##### 2015
{:.no_toc}

* [**First light results from the High Efficiency and Resolution Multi-Element Spectrograph at the Anglo-Australian Telescope**](https://ui.adsabs.harvard.edu/abs/2015JATIS...1c5002S)<br/>Sheinis *et al.* (2015) JATIS **1** 035002 <small>([doi:10.1117/1.JATIS.1.3.035002](https://doi.org/10.1117/1.JATIS.1.3.035002))</small>

##### 2014
{:.no_toc}

* [**First light results from the Hermes spectrograph at the AAT**](https://ui.adsabs.harvard.edu/abs/2014SPIE.9147E..0YS)<br/>Sheinis *et al.* (2014) SPIE **9147** 91470Y <small>([doi:10.1117/12.2055595](https://doi.org/10.1117/12.2055595))</small>
* [**The deterministic optical alignment of the HERMES spectrograph**](https://ui.adsabs.harvard.edu/abs/2014SPIE.9151E..13G)<br/>Gers and Staszak (2014) SPIE **9151** 915113 <small>([doi:10.1117/12.2055574](https://doi.org/10.1117/12.2055574))</small>
* [**The software for the AAT's HERMES instrument**](https://ui.adsabs.harvard.edu/abs/2014SPIE.9152E..23F)<br/>Farrell *et al.* (2014) SPIE **9152** 915223 <small>([doi:10.1117/12.2054805](https://doi.org/10.1117/12.2054805))</small>
* [**HERMES travels by CAN bus**](https://ui.adsabs.harvard.edu/abs/2014SPIE.9152E..2AW)<br/>Waller *et al.* (2014) SPIE **9152** 91522A <small>([doi:10.1117/12.2055022](https://doi.org/10.1117/12.2055022))</small>

##### 2013
{:.no_toc}

* [**Metrology measurements for large-aperture VPH gratings**](https://ui.adsabs.harvard.edu/abs/2013SPIE.8838E..0GZ)<br/>Zheng *et al.* (2013) SPIE **8838** 88380G <small>([doi:10.1117/12.2024493](https://doi.org/10.1117/12.2024493))</small>

##### 2012
{:.no_toc}

* [**Integrating the HERMES spectrograph for the AAT**](https://ui.adsabs.harvard.edu/abs/2012SPIE.8446E..0WH)<br/>Heijmans *et al.* (2012) SPIE **8446** 84460W <small>([doi:10.1117/12.925806](https://doi.org/10.1117/12.925806))</small>
* [**The AAO fiber instrument data simulator**](https://ui.adsabs.harvard.edu/abs/2012SPIE.8446E..2DG)<br/>Goodwin *et al.* (2012) SPIE **8446** 84462D <small>([doi:10.1117/12.924990](https://doi.org/10.1117/12.924990))</small>
* [**Hermes: the engineering challenges**](https://ui.adsabs.harvard.edu/abs/2012SPIE.8446E..4NB)<br/>Brzeski *et al.* (2012) SPIE **8446** 84464N <small>([doi:10.1117/12.924635](https://doi.org/10.1117/12.924635))</small>

##### 2011
{:.no_toc}

* [**Design and development of the high-resolution spectrograph HERMES and the unique volume phase holographic gratings**](https://ui.adsabs.harvard.edu/abs/2011SPIE.8167E..1AH)<br/>Heijmans *et al.* (2011) SPIE **8167** 81671A <small>([doi:10.1117/12.897273](https://doi.org/10.1117/12.897273))</small>
* [**Design and development of the fibre cable and fore optics of the HERMES Spectrograph for the Anglo-Australian Telescope (AAT)**](https://ui.adsabs.harvard.edu/abs/2011SPIE.8125E..04B)<br/>Brzeski *et al.* (2011) SPIE **8125** 812504 <small>([doi:10.1117/12.896389](https://doi.org/10.1117/12.896389))</small>

##### 2010
{:.no_toc}

* [**HERMES: revisions in the design for a high-resolution multi-element spectrograph for the AAT**](https://ui.adsabs.harvard.edu/abs/2010SPIE.7735E..09B)<br/>Barden *et al.* (2010) SPIE **7735** 773509 <small>([doi:10.1117/12.856103](https://doi.org/10.1117/12.856103))</small>
* [**Data simulator for the HERMES instrument**](https://ui.adsabs.harvard.edu/abs/2010SPIE.7735E..7UG)<br/>Goodwin *et al.* (2010) SPIE **7735** 77357U <small>([doi:10.1117/12.856773](https://doi.org/10.1117/12.856773))</small>
