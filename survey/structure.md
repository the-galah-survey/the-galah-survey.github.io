---
layout: page
title: Survey Management
---

The GALAH Survey is an Australian-led project of [over 50 scientists at dozens of institutions](/survey/people). The scientific achievements of the GALAH have been enabled by the technical and financial contributions, and the collective scientific expertise, of this vibrant collaboration.

The GALAH Survey is led by a Survey Managment Group (SMG) and an Executive group. Below this is a Working Group structure.

### Executive group

##### **Joss Bland-Hawthorn (University of Sydney), Ken Freeman (Australian National University), Sarah Martell (UNSW)**

The executive group decides on membership and external collaborators, advises the survey management, and is responsible for conflict solution. Joss Bland-Hawthorn also acts as the project lead for GALAH within [ASTRO 3D](https://astro3d.org.au/galah-project/).

### Working Groups
#### WG1: Survey Design
##### **Lead: Sanjib Sharma (University of Sydney)**

This working group is responsible for the target selection and maintains `obsmanager`, the tool to select targets/plates/fields.

#### WG2: Observations
##### **Lead: Sarah Martell (University of New South Wales)**

This working group coordinates the observations of the survey. WG2 is in charge of acquiring and verifying raw data. It is aware of the HERMES instrument status, carries out observations and trains new observers, checks raw data for errors, and sends the raw data to the WG3 reduction teams.

#### WG3: Reduction
##### **Lead: Janez Kos (University of Ljubljana)**

This working group reduces the raw data of the observations, including velocity corrections, normalisation, and a preliminary estimate of T<sub>eff</sub>, log*g*, and [Fe/H] via the GUESS template matching code. Much of their work can be found described in [Kos *et al.* (2018)](https://doi.org/10.1093/mnras/stw2064).

#### WG4: Analysis
##### **Lead: Sven Buder (Australian National University)**

This working group uses the reduced data (both normalised and un-normalised) to estimate final stellar parameters and element abundances. For DR1 and DR2, we used a combination of the spectrum synthesis code Spectroscopy Made Easy (SME) and the data-driven tool The Cannon. For DR3, we only use (SME). For DR4, we use a neural network to interpolate a basis set of SME spectra to solve for all stellar parameters and abundances simultaneously.

#### WG5: Communication
##### **Lead: Michael Hayden (University of Oklahoma)**

This working group coordinates the internal communications (e.g., weekly telecons) as well as the external communication (e.g., press releases, science meetings, Twitter).

#### Additional Survey Management Group members
* Gaia: Tomaz Zwitter (University of Ljubljana) is the contact person to the Gaia DPAC
* Support for WG2 and WG5: Dan Zucker (Macquarie University)
* Science strategy: Clare Worley (University of Canterbury) and Melissa Ness (ANU)
