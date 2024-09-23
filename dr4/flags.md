---
layout: page
title: Flags in GALAH DR4
subtitle: Fourth Data Release
---

{: .main_blockquote}
This page gives details of the flags found in the GALAH DR4 catalogues. The main flags that will be of interest to most users of GALAH are the overall quality flag `flag_sp` and the individual abundance flag `flag_X_fe`.

{: .box-warning}
For science cases involving stellar parameters, it is highly recommended that you only consider stars where `flag_sp == 0`. For science cases involving the abundance of element X, it is highly recommended that you only consider `X_fe` where `flag_X_fe == 0` and `snr_px_ccd3 > 30`.

* This text gets replaced.
{:toc}

---
### `flag_sp`

This flag is found in the `GALAH_DR4_main_allstar` (and `GALAH_DR4_main_allspec`) catalogues and is the final bit-flag for the stellar parameter quality flag. Its value is found via the summation of the individual flags as tabulated below.

| Value | Description |
| :------ |:--- |
| 0 | No identified problems with stellar parameter determination |
| 1 | Emission lines |
| 2 | Data from at least one CCD is missing |
| 4 | Single-line spectroscopic binary |
| 8 | Double-line spectroscopic binary |
| 16 | Chi squared for the model spectrum is larger than 3 sigma |
| 32 | Warning on v sin i value |
| 64 | Warning on v<sub>mic</sub> value |
| 128 | Triple star warning |
| 256 | Warning on T<sub>eff</sub> value |
| 512 | Warning on log *g* value |
| 1024 | Warning on [Fe/H] value |
| 2048 | Low S/N | 
| 4096 | Fit did not converge |
| 8192 | Extrapolated model; stellar parameters outside the MARCS grid | 
| 16384 | No analysis results |


---

### `flag_X_fe`
These flags are found in `GALAH_DR4_main_allstar` and are the final bit-flag for the elemental abundance quality for the elemental abundance `X_fe`. Their values are found via the summation of the individual flags as tabulated below.  

| Value | Meaning |
| :------ |:--- |
| 0 | No identified problems with abundance determination of element `X_fe` |
| 1 | Value is an upper limit |
| 2 | Line is not detectable |
| 4 | Fit did not converge | 
| 8 | Value above the analysis limit | 
| 16 | Value below the analysis limit | 
| 32 | Measurement issue with C, N, or O |
| 64 | Measurement issue with Li, Ca, or Ba |

---

### Other flags
There are a number of other flags found in the GALAH catalogues. Most are only of interest for expert users.

#### `flag_red`
The spectrum reduction pipeline quality flag. 

#### `flag_sp_fit`
A diagnostic flag from the analysis pipeline.

#### `flag_fe_h`
A diagnostic flag from the analysis pipeline. Its value is found via the summation of the individual flags as tabulated below. However, there is an error in the upper limit bit, and this flag should not be used in its current state.

| Value | Meaning |
| :------ |:--- |
| 0 | No identified problems with determination of `fe_h` |
| 1 | Value is an upper limit |
| 2 | No measurement available |
| 4 | Fit did not converge | 
| 8 | Value above the analysis limit | 
| 16 | Value below the analysis limit | 
