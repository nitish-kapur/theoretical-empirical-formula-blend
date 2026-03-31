# Feedstock Blend Empirical Formula Predictor

A Python script that predicts the theoretical empirical formula of a multi-feedstock biomass blend by computing weighted elemental compositions and normalising molar ratios to carbon.

## Author

**Nitish Kapur**<br>
GitHub: [github.com/nitish-kapur](https://github.com/nitish-kapur)

## How It Works

The script computes a weighted average of the elemental compositions of the constituent feedstocks based on their mass fractions, converts the resulting mass percentages to molar ratios, and normalises all ratios to carbon = 1. This produces a theoretical empirical formula of the form C1.0 H x.xx O x.xx N x.xx S x.xx for each defined sample blend.

This is a theoretical prediction assuming ideal mixing — no chemical reactions or transformations during pyrolysis or co-processing are accounted for.

## Feedstocks

The elemental compositions (C, H, N, O, S as % mass) for each feedstock are hard-coded in the `material_compositions` dictionary at the top of the script. Update these values to match your own feedstocks and experimental data.

## Mixture Ratios

The sample mixtures and their mass fractions are defined in `mixture_ratios_list`. Each entry contains a sample name and the mass fractions of each feedstock. Update, add, or remove entries to match your experimental design.

## Requirements

No external libraries are required. The script uses only Python built-ins.

## Usage

Run the script directly:

    python feedstock-blend-empirical-formula.py

Results are printed to the console for each defined sample mixture.

## Output

For each sample, the console prints:

    Sample Name ->
    Scaled mole ratios: {C: x.xx, H: x.xx, N: x.xx, O: x.xx, S: x.xx}
    Trimmed ratios: {C: x.xx, H: x.xx, N: x.xx, O: x.xx, S: x.xx}
    Empirical Formula: C1.0 Hx.xx Ox.xx Nx.xx Sx.xx

## Notes

- This is a theoretical prediction based on ideal mixing — it does not account for any chemical transformations during pyrolysis or co-processing.
- Molar ratios are normalised to carbon = 1, which is the standard convention for expressing empirical formulas of biomass feedstocks.
- Elemental compositions and mixture ratios are both hard-coded in the script. Update them to match your own feedstocks and experimental samples.
- Commented-out entries in `mixture_ratios_list` can be uncommented to include additional samples.
