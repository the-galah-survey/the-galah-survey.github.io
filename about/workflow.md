---
layout: page
title: Workflow: From Stellar Light to Abundances
---

How do we estimate stellar elemental abundances from stellar light? Let's explore our workflow with images:

Flowchart of night sky -> AAT + 2dF + HERMES -> Raw CCD Image + Arc + Flat -> 1 Spectrum -> Observed Spectrum + Synthesis (e.g. H_alpha, Li line) -> where this A(Li) measurement ends up in the A(Li) vs. [Fe/H] diagram.

| Workflow|
|:-------------:|
| **Target Selection** |
| For more information click [here](../blob/galah_production/about/technical_details.md) |
| ![This picture shows spatial coverage of stars observed with HERMES](assets/lb_overview_colored.png "AAT with 2dF topend") |
| **Observations** |
| For more information read our [observational overview paper](https://ui.adsabs.harvard.edu/abs/2017MNRAS.465.3203M/) |
| ![This picture shows the Anglo-Australian Telescope (with a yellow horseshoe mount and its topend with the 2dF Positioner](../blob/galah_production/assets/aat_hermes.png "AAT with 2dF topend") |
| ![This picture shows the HERMES spectrograph (a black box with all the optics well covered).](../blob/galah_production/assets/hermes.png "HERMES spectrograph") |
| **Reduction** |
| For more information read our [reduction pipeline paper](http://adsabs.harvard.edu/abs/2017MNRAS.464.1259K) |
| ![This picture shows a part of the CCD Camera image of the 3rd HERMES detector. Spectra per star go horizontally with a greyscale indicating the number of photons/electrons counted. Absorption lines, like the strong Halpha line in the left third of each spectrum are dark black lines and are wiggling from star to star due to their motion away from us or towards us.](../assets/ccd3.png "Part of a raw image of CCD3 with spectra going horizontally") |
| **Analysis** |
| GALAH DR1: see our [release paper for GALAH DR1 (Martell et al., 2017)](https://ui.adsabs.harvard.edu/abs/2017MNRAS.465.3203M/). |
| GALAH DR2: see our [release paper for GALAH DR2 (Buder et al., 2018)](http://adsabs.harvard.edu/abs/2018MNRAS.478.4513B). |
| GALAH+ DR3: see our [release paper for GALAH+ DR3 (Buder et al., 2021)](https://ui.adsabs.harvard.edu/abs/2021MNRAS.tmp.1259B). |
| **Catalogs** |
| We put our catalogs and documentation on [Datacentral](https://docs.datacentral.org.au/galah/). |
| You can download the whole [FITS files here](https://cloud.datacentral.org.au/teamdata/GALAH/public/). |
| **Sciencific Exploration** |
| See our [list of publications](../blob/galah_production/publications.md). |
