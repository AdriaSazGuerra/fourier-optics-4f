# Experimental design and quantitative checks

## 4f architecture

The optical train is

`object plane P0 -> lens L1 -> Fourier plane P1 -> lens L2 -> image plane P2`.

With coherent, approximately collimated illumination, the field in the back focal plane of the first lens is proportional to the spatial Fourier transform of the object transmission function.

## Parameters

The proposed laboratory source is a He–Ne laser with

- wavelength: `lambda = 632.8 nm`
- first focal length: selected according to the available optical bench
- second focal length: selected according to the desired image magnification

## Quantitative predictions

### 1. Transverse magnification

For the 4f system,

`M = -f2 / f1`

so the reconstructed image is inverted and scaled by `|f2/f1|`. The symmetric case `f1=f2` gives unit magnification with inversion.

### 2. Diffraction orders and spatial frequency

For a periodic object with period `d`, the m-th spatial harmonic has

`nu_x = m / d`.

At the Fourier plane of lens L1 its position is approximately

`x_m = lambda * f1 * m / d`.

This relation provides a direct experimental map between position in the Fourier plane and spatial frequency.

### 3. Low-pass cut-off

A centred iris of radius `R` in the Fourier plane transmits spatial frequencies up to approximately

`nu_c = R / (lambda * f1)`.

Reducing the iris radius therefore removes high spatial frequencies first, producing progressive loss of fine detail and edge smoothing in the reconstructed image.

## Filtering experiments

The design includes:

- **low-pass** filtering with four iris radii and predicted cut-off frequencies
- **high-pass** filtering to suppress the zero/low-frequency background and emphasise edges
- **band-pass** filtering to isolate structures at intermediate spatial scales
- **directional filtering** to select Fourier components associated with specific orientations
- **notch filtering** to remove a localised periodic contamination without suppressing the full spectrum
- **harmonic reconstruction** of a rectangular grating, progressively adding the odd Fourier orders

## Validation strategy

The practical is designed around quantitative checks rather than a purely qualitative demonstration:

1. measure image magnification and compare it with `|f2/f1|`
2. measure diffraction-order positions and compare them with `lambda*f1*m/d`
3. calculate the spatial-frequency cut-off for each iris radius and compare it with the observed transmitted orders
4. connect the reconstructed image to the specific Fourier components that remain after each mask

Because this project is an **experimental design**, not a completed measurement campaign, the repository reports theoretical predictions and validation procedures rather than inventing an experimental accuracy figure.
