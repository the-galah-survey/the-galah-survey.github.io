---
layout: page
title: Flags in GALAH DR3
subtitle: Third Data Release
---

{: .main_blockquote}
This page gives details of the flags found in the GALAH DR3 catalogues. The main flags that will be of interest to most users of GALAH are: `flag_sp`, `flag_fe_h`, and the individual `flag_X_fe`.

{: .box-warning}
For science cases involving stellar parameters, it is highly recommended that you only consider stars where `flag_sp == 0` and `flag_fe_h == 0`. For science cases involving the abundance of element x, it is highly recommended that you only consider `X_fe` where `flag_X_fe == 0` and `snr_c3_iraf > 30`.

* This text gets replaced.
{:toc}

---
### `flag_sp`

This flag is found in the `GALAH_DR3_main_allstar_v2` (and `GALAH_DR3_main_allspec_v2`) catalogues and is the final bit-flag for the stellar parameter quality flag. Its value is found via the summation of the individual flags as tabulated below.

The first estimate of the surface gravity of each star was found from the Gaia DR2 parallax, so the first bit of `flag_sp` indicates stars with likely unreliable astrometry in Gaia DR2 (defined as `ruwe_dr2>1.4`). Note that a high RUWE in Gaia DR2 may not be indicative of a star having less reliable astrometry in Gaia eDR3 (and future releases).

The value of `flag_sp` are found via the summation of the individual flags as tabulated below:

| Value | Description |
| :------ |:--- |
| 0 | No identified problems with stellar parameter determination |
| 1 | Gaia DR2 `RUWE > 1.4` (unreliable astrometric solution, see Lindegren 2018) |
| 2 | Unreliable broadening |
| 4 | Low S/N (below 10 for CCD 2) |
| 8 | Reduction issues: (a) Wavelength solution (propagating of `red_flag`); (b) t-SNE projected reduction issues; (c) Negative/positive fluxes, spikes, etc. |
| 16 | t-SNE projected emission features |
| 32 | t-SNE projected binaries |
| 64 | Binary sequence/pre-main sequence flag |
| 128 | SNR-dependent high sme chi2 (bad fit) 512 |
| 256 | Problems with Fe lines, where line flux is not between 0.03 and 1.00, [Fe/H] not reliable, or blending suspected |
| 512 | SME did not finish: (a) No convergence == non-finite stellar parameters; (b) Gaussian RV fit failed |
| 1024 | MARCS grid limit reached or outside of reasonable parameter range |

---

### `flag_fe_h`
This flag is found in `GALAH_DR3_main_allstar_v2` and `GALAH_DR3_main_allstar_v2` and is the final bit-flag for the overall iron abundance `fe_h`. Its values are found via the summation of the individual flags as tabulated below.  

| Value | Meaning |
| :------ |:--- |
| 0 | No identified problems with abundance determination of element `fe_h` |
| 1 | Upper limit |
| 16 | No reliable measurement reported |

### `flag_X_fe`
These flag are found in `GALAH_DR3_main_allstar_v2` and are the final bit-flag for the elemental abundance quality flag for the elemental abundance `x_fe`. Their values are found via the summation of the individual flags as tabulated below.  

| Value | Meaning |
| :------ |:--- |
| 0 | No identified problems with abundance determination of element `X_fe` |
| 1 | Upper limit |
| 32 | No reliable measurement reported |

---

### `ind_flag_X1234`
These flags are found in the `GALAH_DR3_main_allspec_v2` and are the final bit-flag for the elemental abundance quality for the individual line `ind_X1234_fe` abundances. Their values are found via the summation of the individual flags as tabulated below.


| Value | Meaning |
| :------ |:--- |
| 0 | No identified problems with abundance determination of element `ind_X1234_fe` |
| 1 | Upper limit |
| 2 | Bad fit / large 𝜒<sup>2</sup> fit |
| 4 | Uncertain measurement / saturation |
| 8 | Bad wavelength solution / radial velocity for Li6708 |
| 16 | Bad stellar parameter flag (`flag_sp >= 128`) |
| 32 | No measurement available |

---

### Other flags
There are a number of other flags found in the GALAH catalogues. Most are only of interest for expert users.

#### `red_flag`
The spectrum reduction pipeline quality flag. It can be ignored except for expert use, as its value is folded into `flag_sp`.

#### `flag_guess`
The GUESS reduction pipeline finds a first estimate of the stellar parameters for a given spectrum. `flag_guess` is found in the `GALAH_DR3_main_allstar_v2` and `GALAH_DR3_main_allspec_v2` catalogues and is the GUESS quality flag. It can be ignored except for expert use. There are only about 2000 stars in GALAH DR3 for which `flag_guess>0` while `flag_sp==0`.

#### `flag_repeat`
This flag is set to `0` to indicate if a given `sobject_id` entry in the `GALAH_DR3_main_allspec_v2` is found in `GALAH_DR3_main_allstar_v2`.

#### `use_dist_flag`
This flag informs which distance value was used in the Galactic orbit calculations for the `GALAH_DR3_VAC_dynamics_v2` catalogue:
* 0: `distance_bstep`; 1: `r_med_photogeo`; 2: `r_med_geo`; 4: `parallax`; 8: No distance.

#### `use_rv_flag`
This flag informs which radial velocity value has been used for `rv_galah` for a given `sobject_id`:
* 0: `rv_obst`; 1: `rv_sme_v2`; 2: `dr2_radial_velocity`; 4: No radial velocity.

#### Flags from Gaia catalogues
`flag_edr3dist`, `proper_motion_propagation`, `astrometric_primary_flag` are flags propogated from the original Gaia catalogues.
