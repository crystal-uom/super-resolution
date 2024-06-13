# Super-resolution for OCT Medical Images

## Evaluation Metrics

- MSR (Mean-to-Standard Deviation Ratio)

$$
\text{MSR} = \left( \frac{\mu_f}{\mu_b} \right)
$$

- CNR (Contrast-to-Noise Ratio)

$$
\text{CNR} = \frac{|\mu_f - \mu_b|}{\sqrt{\frac{\sigma_f^2 + \sigma_b^2}{2}}}

$$

- $\mu_f$ is the mean intensity of the foreground.
- $\mu_b$ is the mean intensity of the background.
- $\sigma_f$ is the standard deviation of the foreground.
- $\sigma_b$ is the standard deviation of the background.

Source : [Reduction of speckle noise from optical coherence tomography images using multi-frame weighted nuclear norm minimization method](https://www.researchgate.net/publication/282486662_Reduction_of_speckle_noise_from_optical_coherence_tomography_images_using_multi-frame_weighted_nuclear_norm_minimization_method)