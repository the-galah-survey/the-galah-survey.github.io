---
layout: page
title: Known caveats for GALAH DR3
subtitle: Third Data Release
---

{: .main_blockquote}
This page relays a list of known issues in the GALAH DR3. Please also see the GALAH Survey Third Data Release paper ([Buder et al 2021](https://doi.org/10.1093/mnras/stab1242)).

{: .box-error}
We caution that it is not possible to inspect all of the more than 30 million measurements that make up GALAH DR3. So, there are likely to be some unexpected correlations and problems with the data.

* This text gets replaced.
{:toc}

---

### Gaia data included with GALAH DR3 catalogues

{: .box-warning}
Note that our tables contain a mixture of Gaia DR2 and Gaia eDR3 values. The former are indicated by having column names including `dr2`.

The results from the Gaia mission are integral to GALAH DR3. Our analysis makes use of Gaia DR2 results, in particular using a parallax-derived distance estimate for each star to provide a first estimate of its surface gravity. The release of Gaia eDR3 occurred after the main analysis for GALAH DR3 was finished, and we have not re-run the analysis pipeline using the new parallaxes from Gaia eDR3. As a consequence:
* The overall `flag_sp` in `GALAH_DR3_main_allstar_v2` and `GALAH_DR3_main_allspec_v2` (see our [Flag documenation](/dr3/flags)) includes a bitmask for unreliable astrometry in Gaia DR2 based upon their RUWE. A high RUWE in Gaia DR2 may not be indicative of a star having less reliable astrometry in Gaia eDR3 and beyond.
* The distance to star reported in the `GALAH_DR3_VAC_dynamics_v2` catalogue may differ from the distance used in the stellar parameter and abundance determination.

Some further notes and caveats about the cross-match between GALAH DR3 and Gaia eDR3:
* This cross-match used the previously identified Gaia DR2 `source_id` for each GALAH DR3 star, and the [`gaiaedr3.dr2_neighbourhood`](https://gea.esac.esa.int/archive/documentation/GEDR3/Gaia_archive/chap_datamodel/sec_dm_auxiliary_tables/ssec_dm_dr2_neighbourhood.html) table created by the Gaia team. The Gaia DR2 `source_id` had been found using the [`gaiadr2.tmass_best_neighbour`](https://gea.esac.esa.int/archive/documentation/GDR2/Gaia_archive/chap_datamodel/sec_dm_crossmatches/ssec_dm_tmass_best_neighbour.html) and the 2MASS ID of each GALAH star. In the future, we suggest to perform this crossmatch via GALAH's 2MASS ID and the yet-to-come match of Gaia EDR3 and 2MASS identifiers.
* All `GALAH_DR3_VAC_GaiaEDR3_v2` entries have an angular distance between their Gaia DR2 and eDR3 sources smaller than 160 mas, and 99.9 per cent are within 20 mas.
* There is a Gaia eDR3 source for every entry in the `GALAH_DR3_main_allstar_v2` table.
    - There are 111 entries in the `GALAH_DR3_main_allspec_v2` table that lack a Gaia `source_id` as we have not attempted to find them in Gaia eDR3 and they never had a Gaia DR2 `source_id`. Of these 38 are bright stars and do have a parallax from Hipparcos.
* 17654 stars had more than one Gaia eDR3 match (98 per cent two matches and the remainder with 3 or 4 matches). For simplicity we have chosen the match with the smallest angular distances between the Gaia DR2 and Gaia eDR3 position as reported by the `gaiaedr3.dr2_neighbourhood`.
    - For over 99 per cent of stars the closest match had an angular distance <10 mas, and second closest match was >600 mas.
    - There is likely source confusion for <100 stars. For instance, for 57 of the 17000 stars with multiple matches in the `gaiaedr3.dr2_neighbourhood` table, the second closest match in angular distance has a smaller magnitude difference between Gaia DR2 and eDR3.

---

### Flags

{: .box-warning}
We highly recommend only using stars with `flag_sp == 0`, `flag_fe_h == 0`, `flag_X_fe == 0`, and `snr_c3_iraf > 30`.

There are three types of flags for the data.
* `flag_sp` – reliability of the stellar parameters
* `flag_fe_h` – reliability of the iron abundance
* `flag_x_fe` – reliability of the abundance of [x/Fe]
We leave it up to the user which flags they apply but stress that ignoring the given flags is strongly discouraged and only advisable if necessary for the science case.

For more information, see the [Best Practices for using GALAH DR3](/dr3/using_the_data) and the [Flags in GALAH DR3](/dr3/flags) pages.

---

### Uncertainties

For this data release, we include more accuracy and precision estimates than for GALAH DR2. However, for several stellar parameters and abundances, the means of accuracy estimation are limited, because there are no benchmark values available. We therefore want to caution the user that the accuracy uncertainties might be underestimated and also not complete in terms of their parameter dependence.

For hot stars we have identified a systematic trend causing increasingly underestimated T<sub>eff</sub> for hotter stars above 6000 K. The comparison with the GBS shows agreement of our and the literature values within the uncertainties, but our absolute accuracy value for Teff is likely underestimating the uncertainty for the hottest stars.

We have not been able to find enough benchmark values to test the accuracy of [Fe/H] as a function of stellar parameters and therefore only employ an absolute value for the [Fe/H] accuracy. More benchmark measurements, especially with similar conditions to the survey setup (instead of nearby bright stars as validators for distant faint stars), for all stellar parameters would be useful.

For GALAH+ DR3, our precision estimates are based on the repeat uncertainties and internal fitting uncertainties from SME, which for some parameters have been rescaled to match in overall shape. As we continue to develop our pipeline, and obtain more repeat observations in the future, we will be able to also expand the precision estimation not only as a function of an average S/N, but S/N in particular line regions as well as T<sub>eff</sub>, log *g*, and [Fe/H], similar to the APOGEE survey Jönsson et al. (2020).

---

### Upper limits

{: .box-warning}
Upper limits are reported in some cases. We advise caution in their use.

While we report upper limits for advanced users, we strongly recommend everyone to be careful with these measurements. For all elements, but especially for neutron-capture elements, these estimates are pushing the limits of what we can be extracted from the data and are by definition only an upper limit, not a measurement. We therefore strongly recommend to check upper limit estimates against the data and inspect spectra when possible.

---
### Caveats for certain groups of stars

#### Red clump stars

An ongoing disagreement concerns the stellar parameters of metal-rich giants, and especially metal-rich red clump stars. Already in GALAH DR2 our analysis has yielded unreasonable stellar parameters (in the case of DR2 the estimated logg were deviating significantly by up to 0.7 dex from those expected from astro-/photometry, while Teff and [Fe/H] agreed with other literature estimates/expectations).

For DR3, the use of astrometry and photometry allows us to get more accurate logg. For the metal-rich ([Fe/H] > 0) giants and RC stars, however, we notice that the estimated iron abundances show a significant trend of underestimated [Fe/H] with increasing metallicity. This is an indicator that our synthetic spectra are inaccurate for this specific type of stars or spectra. As discussed above, Jofre et al. (2017) showed that for giant stars, an over-/underestimated vmic can change the measured abundances of some lines significantly, by up to 1.5 dex. The reasons for underestimated [Fe/H] are however more diverse and also include missing/unreliable molecular line data, the underestimation of blending and incorrect continuum normalisation. We believe that we can exclude incorrect estimates of logg estimates, e.g. as a result of poor mass-estimates from missing isochrone models in the super-Solar [Fe/H] regime, because photometric and spectroscopic positions in the CMD and Kiel diagrams agree well.

We find systematically higher abundances of Na, Al, Sc, TiII, Ni, and Ba among metal-rich RC stars when compared to RGB stars. These can be identified as unexpected extensions of high [X/Fe] elevated above the majority of stars in [Fe/H] vs. [X/Fe] plots, especially when selecting only high-S/N spectra of giants. The disagreement among those increases from 0 at Solar [Fe/H] to ∆[X/Fe] > 0.4 dex above [Fe/H] > 0.2 dex for these elements. However, another neutron capture element Y is not as affected. When using the K2 sample with asteroseismic classifications of evolutionary stages within this DR (Stello, priv. communication), we find a significant difference of around 0.3 dex between RC and RGB stars. The reasons for this might be manifold and could for example suggest non-scaled-Solar abundance patterns for C and N among the RC stars, as shown by Tautvaišienė et al. (2013).

The follow-up of these spectroscopic shortcomings are beyond the scope of this paper, but should also assess line saturation and discuss the implications of different formation depths of atomic lines (see e.g. Gurtovenko 2015), which could possibly explain the different effect for different lines within the GALAH range as well.

#### Abundance patterns of Am/Fm stars

Above we show stars with Teff > 6500 K. We identified a group of stars with high [Ba/Fe] among these stars, coinciding with those identified by Fossati et al. (2007, 2008) for a handful of stars (shown in red). Similar to Xiang et al. (2020) who identified tens of thousands of these Am/Fm stars we measure typically higher [Ba/Fe] than for the Sun, but lower alpha- enhancement than in the Sun for these typically young stars, when assuming ionisation equilibrium. We note these stars as they are in fact a real astrophysical result.

#### Young star parameters

We stress that our stellar parameters for the youngest stars (below 0.5 Gyr) are likely unreliable. This is caused by our analysis setup with an isochrone grid selection favouring older stars, tying microturblence velocity to an empirical relation and estimating stellar parameters mainly from iron lines (Baratella et al. 2020), but also neglecting stellar rotation, possible stellar activity and magnetic fields (Spina et al. 2020) which can alter the shape of stellar lines quite drastically.

#### Unexpected over-/underdensities

While using the recent versions of SME, we have identified several overdensities in the parameter space, coinciding with grid points of the chosen atmosphere grids. We especially warn the user of these overdensities at 3500 K as well as 4750..(250)..8000 K. We further have found an under-density around of stars with temperatures below 4750 K, which coincide with regions a different atmosphere grid spacing. Comparisons with the IRFM temperatures show however that the temperatures of these stars are not drastically different and we have therefore decided to not flag them. We have further identified an overdensity at 4650 K and log g of 4.7 dex, which we can ascribe to an issue in the isochrone interpolation due to sparsely available isochrone points.

---
### Possible systematic trends
#### High abundances of V, Co, Rb, Sr, Zr, Mo, Ru, La, Nd, and Sm

In this data release, we try to push the boundary of what can be extracted from the observed spectra with the aim to deliver as many abundance measurements as possible. This does, however, not only push the limits of deciding what measurement is reliable, that is, significantly different from a continuum measurement, but leads to complicated cases where lines are blended, leading to possible wrong systematics. We therefore especially caution the use of elevated abundance measurements (especially above [X/Fe] of 0.3 dex) for V, Co, Rb, Sr, Zr, Mo, Ru, La, Nd, and Sm, as we suspect that these are most likely affected by blending issues close to the detection limit. Only visual inspection could however confirm this, which is not possible for the vast number of measurements at hand and we therefore advise the user to inspect the published spectra before using these measurements blindly.

* For V, we caution the use of measurements with `nr_v_fe` equal to 2 or 3, that is, using VI 4832.
* For Co, we caution the use of measurements with `nr_co_fe` equal to 2 or 8, that is, measurements purely based on lines CoI 6490 and 7713. While we have not been able to narrow down the exact cause, we assume that measurements only based on these lines are caused by imperfect telluric corrections in CCD 3 for CoI 6490 and spikes or imperfect telluric corrections in CCD4 for CoI 7713.

#### 1D-LTE/1D-NLTE and microturbulence

Our spectrum synthesis is performed by assuming 1D-LTE and 1D-NLTE. However, modelling stellar atmospheres with a 1-dimensional description is neglecting 3-dimensional, time-dependent effects, which can only partially be mitigated by fudge factors, like vmic. While allowing this factor to be fitted as part of the analysis, our tests have shown that the abundance precision decreases. We have therefore implemented an empirical relation, estimated by Gao et al. (2020) for GALAH, over the whole parameter space, as shown in panel a) of the figure below.

During the validation of element abundances, we have discovered several temperature-dependent trends. These occur in regions where our analysis approach is prone to systematic trends anyway, that is, the coolest/most line-rich (<4500 K) and hottest/most line-poor (>6500 K) regions. We cannot exclude that the found systematic trends can also be partially caused by over- or underestimated vmic (in addition to a systematically incorrect normalisation for the most line-righ spectra). Comparisons with other vmic-relations, see e.g. the relations by Dutra-Ferreira et al. (2016) based on 3D atmosphere calculations (see panel b) suggest large deviations for certain stars, leading to a difference of up to 2 km/s (see panel c). The tests by Jofre et al. (2017) also showed that different stellar types are affected differently by inaccurate vmic, with strongest implications for (more metal-rich) giant stars among the analysed sample of GBS.

While our long-term goal is to implement 3D-NLTE calculations, we believe that it is worth testing the implementation of v_mic as a free parameter or the relations estimated by Dutra-Ferreira et al. (2016) for certain parts of the parameter space, if the advantages outweigh the loss in abundance precision. Using vmic as a free parameter showed for example significant improvements of trends with Teff for the APOGEE survey Holtzman et al. (2018})

----
### Consistency of atmosphere composition for spectrum synthesis

For computational reasons, we estimate the abundances of all elements independently, and assume scaled-Solar patterns for most other elements during that optimisation. However, our approach might introduce systematic trend for elements which are often correlated (e.g. C and O), surrounded by lines that are deviating from the scaled-Solar pattern, or when the abundance pattern in general differs from the scaled-Solar pattern, thus leading to differences in the continuum and molecular lines strengths. If computationally possible, it would therefore be preferable to fit all elements partially Brewer et al. (2016) or fully self-consistent Ting et al. (2019), which could also allow to estimate abundances not only via atomic lines, but also molecular features, which follow molecular equilibria Ting et al. (2018).

### Metallicity/abundance trends

For numerous open and globular clusters we have found trends of [Fe/H] with temperature and/or evolutionary stage at the coolest and hottest ends of the Teff range or in general for young clusters.

Stellar clusters are not the main focus of our survey, and many of the observations that were performed for them are outside of the typical GALAH magnitude, distance, and age range. Most of the open and globular clusters targeted by our observations are much more distant, which leads to less reliable distance estimates, with implications for our distance-dependent logg estimates of their stars. Many of stars in the open clusters stars are typically younger than the GALAH targets, with astrophysical implications on additional features in their spectra.

Baratella et al. (2020) found that vmic is overestimated and thus [Fe/H] is underestimated when using Fe lines in clusters, a trend that we also observe in some of our cluster observations. We therefore cannot a priori exclude wrong vmic values as the influence of cluster abundance trends (see comments on vmic above).

We note, however, that for open clusters, differences in [Fe/H] as well as other abundances have been found to be of astrophysical nature, e.g. atomic diffusion (e.g. Souto et al. 2018, Gao et al. 2018, Bertelli-Motta et al. 2018, Souto et al. 2019, Liu et al. 2019, Semenova et al. 2020) or stellar activity (e.g. Spina et al. 2020). Furthermore, astrophysical abundance trends, like anti-correlations of light elements (see Bastian et al. 2018 and references therein), have also been found in globular clusters and are partially hard to disentangle from other abundance trends, e.g. those introduced by our analysis pipeline. We will follow this up for globular clusters with a dedicated study (D. M. Nataf et al., in prep.).

### Binarity

A central assumption of our observations is that each fibre observes only one star. We try to ensure this by only selecting point sources from 2MASS with a sufficient separation from other bright neighbours. Our selection does however not exclude stars that are not extended within 2MASS, for example spectroscopic binaries.

Our means to identify (spectroscopic) binaries are, however, limited, because as part of GALAH we usually only take three spectra within typically 1 hour per star, and can only resolve spectroscopic binaries if the lines of both components are resolved with the given broadening induced by our instrument and stellar rotation. Although we try to identify and flag stars as part of our validation, we expect that we are not able to identify a significant fraction of stars as binaries. Price-Whelan et al. (2020) find 19,635 high confidence close-binaries among 232,495 APOGEE sources (8%), and El-Badry et al. (2018b) find that for 2645 of 20,142 analysed main sequence targets (13%), more than one star contributes significantly to the spectrum. Based on the results of Price-Whelan et al. (2020) we would expect at least 10% of the stars above >6000 K (23% of GALAH+ DR3) and more than 40% of stars with >7000 K (3% of GALAH+ DR3) to be binaries.

The implications of not identifying a star as a binary can be manifold. Firstly the binarity changes the astrometric solution, which is not always identified via Gaia warnings or quality values like the RUWE value. This can falsify the estimated distance of objects. Secondly, the photometry of a binary system can deviate significantly from that of the primary component, depending on the flux contribution of the secondary. Thirdly, the flux contribution within the spectrum lead to inaccurate fits when assuming a single star as quantified by El-Badry et al. (2018a, b), which leads to inaccurate stellar parameters as well as element abundances. For binaries, the measured vrad also only reflects (at best) the value at the time of observation and is thus not indicative of its Galactic orbit. We note that we have not made use of the assessment of vrad changes among our 51,539 spectra with dedicated repeat observations (typically on different nights).

### Stars with uncertain/unreliable astrometry

As part of our spectroscopic analysis we rely on the quality of astrometric measurements, to infer reliable absolute photometry and then logg. While we flag stars with high RUWE values above 1.4 (Lindegren et al. 2018, 2018b), we caution the user to not blindly use all measurements, especially those of stars with uncertain astrometry.

We have used more elaborate distance estimates from Bailer-Jones et al. (2018) which infer more trustworthy distances based on a Galactic prior for stars with parallax uncertainties beyond 20%. Especially for very distant stars, like some of our observations of LMC stars, this Galactic prior leads to an underestimated distance and thus likely overestimated logg.

In general, we note that for stars with more constrained distance estimates, like open clusters Cantat-Gaudin et al. (2020), globular clusters Baumgardt et al. (2019) and stars of the LMC (de Grijs et al. 2014), a reanalysis would be leading to more reliable stellar parameters and abundances, when using these distances instead of the ones solely estimated from Gaia parallaxes.

### Influences of isochrone choice

For computational reasons we have limited the isochrones used for the on-the-fly mass estimation to a grid of 0.5..(0.5)..13.5 Gyr. We note that for the youngest stars this might not be a good choice, as we see some noding in the on-the-fly mass and age estimates, especially for hot stars and secondary RC stars. In the future we would like to make use of a better set of isochrones in terms of sampling (more ages on a logarithmic scale), which will hopefully also include different alpha-enhancements and will take into account atomic diffusion as well as stellar rotation. For a better quantification of the uncertainties, for example when using (Markov Chain) Monte Carlo sampling, it would also be useful to be able to sample ages above the age of the universe.

### High extinction

86% of the stars of this data release have estimated E(B-V) < 0.2 mag from Schlegel et al. (1998) and 95% below 0.2 mag. Similarly, 90% and 98% of the stars have estimated A_Ks < 0.1 mag and 0.2 mag, respectively. If a star has a high and uncertain extinction, this can influence the bolometric luminosity that we estimate and thus introduce biases in the surface gravity and thus all subsequent analyses. Our pipeline especially is only optimised for E(B-V) < 0.48 mag. We therefore caution that trends found among stars with high extinction, and where A_Ks estimated via the RJCE method and E(B-V) differ significantly should be treated with caution..

Potassium is estimated from the KI 7699 resonance line. This line is also a good tracer of interstellar potassium which leads to contamination of the stellar line in highly extinct regions. In the future we aim to estimate the extinction for example via diffuse interstellar bands and possibly use correlation of extinction and line strength of interstellar potassium (Munari et al. 1997) to correct the spectra and measurements of stellar [K/Fe]. For this DR, we however caution the user to check the extinction of stars when using [K/Fe], as we measure this abundance without any corrections causing a rather hard to predict systematics (depending on the velocities of star and ISM) of [K/Fe].

### Scattering in Potassium

Potassium is estimated from the KI 7699 resonance line. This line is also a good tracer of interstellar potassium which leads to contamination of the stellar line in highly extinct regions.
