---
layout: page
title: Observing
---

<!-- <h3> On this page</h3> -->
* This text gets replaced.
{:toc}



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
