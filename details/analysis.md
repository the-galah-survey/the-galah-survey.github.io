---
layout: page
title: Analysis
subtitle: From reduced spectra to abundances
---

{: .main_blockquote}
The main data product of the GALAH survey are stellar parameters and elemental abundances for the stars we observe. Over time, the methods by which we do this have changed and evolved. In particular, we made use of The Cannon for Data Release 1 and Data Release 2, changed to Spectroscopy Made Easy for Data Release 3, and now we are using SME together with neural networks for [Data Release 4](/dr4/overview). For a given data release, it is important to consult the accompanying paper for the description of the methods.

On this page we give a overview of the method as used for [GALAH DR4](/dr4/overview). See [Buder *et al.* (2021)](https://doi.org/10.1093/mnras/stab1242) for all the details of the data analysis.

<!-- <h3> On this page</h3> -->
* This text gets replaced.
{:toc}

---

### Data Release 4 Analysis

#### Overview

We first estimate stellar parameters and then keep them fixed while only fitting one abundance at a time for the different lines/elements in the GALAH wavelength range. For the stellar parameter estimation, we perform a first normalisation and a first rough stellar parameter fit with one iteration, followed by a final normalisation and finer parameter fit with more iterations. For the abundance analysis, we only perform one normalisation and iteratively optimise the abundance based on those data points of the lines/elements that we estimate to be unblended enough after comparing a synthesis with all lines and another one with only the lines of the element in question.

#### Step-by-step

Below we describe this workflow in more detail, which mirror the challenges on technical and physical aspects of the analysis of very different spectra:

1. Initialise Spectroscopy Made Easy (`SME`; version 536) with choices of line data, atmosphere grid, non-LTE departure grids, observed spectrum (limited to the 46 segments used for the parameter estimation) including selection of continuum and line masks, initial parameters for χ2 optimisation.
1. Normalise all 46 segments individually with the chosen initial setup by fitting linear functions first to the observed spectrum and then to the difference of the observed and synthetic spectrum.
1. Optimise the stellar parameters T<sub>eff</sub> , [Fe/H], v<sub>broad</sub> (v *sin* i with v<sub>mac</sub> set to 05), and global radial velocity with 2 major `SME` update loops (calculating double-sided partial derivatives and exploring the local χ² surface with up to 5 different parameter choices). Consistently update log g and vmic from physical and empirical relations, respectively, with every change of T<sub>eff</sub> or [Fe/H]. In our test, this already led to updated parameters close to the χ² global minima.
1. Normalise all 46 segments again individually as in step 2, but with updated stellar parameters.
1. Optimise the stellar parameters T<sub>eff</sub>, [Fe/H], v<sub>broad</sub>, and v<sub>rad</sub> with up to 20 major `SME` update loops as in step 3 until fractional change of χ2 is below 0.001
1. Collect stellar parameters for validation. Save covariance uncertainties, based on the statistical χ² uncertainties given the uncertainties of the normalized flux, in addition to the uncertainties delivered by `SME` version 536.
1. Initialise `SME` (version 536) for the element abundance estimation with choices of line data, atmosphere grid, non-LTE departure grids, observed spectrum (limited to line segement(s) used for the element abundance estimation) including selection of continuum and line masks, final global atmosphere parameters for χ² optimisation.
1. Normalise all segments for the line (e.g. Li6708) or element (e.g. Ca) run individually with the chosen initial setup by fitting linear functions first to the observed spectrum. Improve this normalisation by fitting a linear function to the difference between the observed and synthetic spectrum to create a ’full’ synthetic spectrum.
1. Because the same line exhibits different degrees of blending in different stars, which are complex and difficult to predict ab initio, perform a blending test by creating a 'clean' synthetic spectrum only based on the lines of the element to be fitted. Then compare the 'full' and 'clean' spectra for the chosen line mask pixels and neglect those which deviate more than ∆χ2 > 0.005 for elements other than Fe.
1. Optimise the relevant element abundance entry in the abundance table (`SME`.abund) with up to 20 major `SME` update loops until fractional change of χ² is below 0.001. The atmosphere is updated with each change of chemical composition to stay consistent, but we note that for the sake of computation cost with `SME`, the abundances, that are not fitted, are kept at scaled-solar, with the exception of Li with A(Li) = 2.3, an enhancement of 0.4 fex for N, and the precomputed α-enhancement for α-process elements.
1. Collect stellar parameters and element abundances for validation and post-processing.
1. Calculate upper limits for each element/line for non-detections by estimating lowest abundance would lead to a line flux depression of 0.03 below normalised continuum.
1. Post-processing: apply flagging algorithms, calculate final uncertainties from accuracy and precision estimates, combine line-by-line measurements of element abundances weighted by their uncertainties.

#### Change in data analysis from Data Release 3

There are three main changes to the analysis methods for DR4 compared to DR3.

1. Using a neural network for rapid interpolation of synthetic spectra to various combinations of stellar parameters and abundances, trained on synthetic spectra produced with SME.
2. Simultaneous fitting of all stellar parameters and elemental abundances.
3. A three-phase process for the determination of stellar parameters and elemental abundances: first a pure spectroscopic analysis for individual observations of stars, then multiple observations are coadded and all spectra are reanalysed folding in photometric and astrometric information, then a post-analysis scan for signs of binarity, emission lines, and interstellar absorption.

Below is a comparison of GALAH DR3 (upper panels) and GALAH DR4 (lower panels, this release). The smooth light blue background indicates all measurements, whereas the colormap shows the number of unflagged measurements at each point. 

![Comparison of GALAH DR3 and GALAH DR4](/dr4/img/galah_dr4_comparison_dr3.png "Comparison of GALAH DR3 and GALAH DR4")
