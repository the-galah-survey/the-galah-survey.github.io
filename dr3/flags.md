---
layout: page
title: Flags in GALAH DR3
subtitle: Third Data Release
---

<h3> On this page</h3>
* This text gets replaced.
{:toc}

### `flag_sp` bitmask values

{: .box-warning}
For science cases involving stellar parameters, it is highly recommended that you only consider stars where `flag_sp == 0`.

This flag is found in the `main_star` (and `main_spec`) catalogues and is the final bit-flag for the stellar parameter quality flag. Its value is found via the summation of the individual flags as tabulated below.

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

### `flag_X_fe` and `ind_flag_X1234` bitmask values

{: .box-warning}
For science cases involving stellar parameters, it is highly recommended that you only consider stars where `flag_sp == 0` and `flag_fe_h == 0`. For science cases involving the abundance of element x, it is highly recommended that you only consider `X_fe` where `flag_X_fe == 0` and `snr_c3_iraf > 30`.

These flags are found in the `main_star` (and `main_spec`) catalogues and are the final bit-flag for the elemental abundance quality flag, either the final `X_fe` abundance or the individual line `ind_X1234_fe` abundance. Their values are found via the summation of the individual flags as tabulated below.


| Value | Meaning |
| :------ |:--- |
| 0 | No identified problems with abundance determination of element x |
| 1 | Upper limit |
| 2 | Bad chi2 fit |
| 4 | Saturation |
| 8 | Bad wavelength solution / rv for Li6708 |
| 16 | Bad stellar parameter flag (`flag_sp >= 128`) |
| 32 | No measurement available |
