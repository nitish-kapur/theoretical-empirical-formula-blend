"""
Feedstock Blend Empirical Formula Predictor
Copyright (C) 2026 Nitish Kapur
GitHub: github.com/nitish-kapur
Licensed under GNU GPLv3

    This script was made as a part of a biofuel research project.

    1.  Defines the atomic masses of C, H, N, O, and S in the
        atomic_masses dictionary. These are standard values and do
        not need to be modified.

    2.  Defines the elemental compositions (C, H, N, O, S as % mass)
        for each feedstock in the material_compositions dictionary.
        Update these values to match your own feedstocks and
        experimental data.

    3.  Defines a list of sample mixtures in mixture_ratios_list, where
        each entry contains a sample name and the mass fractions of each
        feedstock. Update, add, or remove entries to match your
        experimental design.

    4.  For each sample mixture, computes the theoretical empirical
        formula through the following steps:

            a.  Weighted average of elemental % mass:
                    element% = sum(mass_fraction_i × element%_i)

            b.  Conversion of mass percentages to moles:
                    moles = element% / atomic_mass

            c.  Normalisation of all mole values to carbon = 1:
                    ratio = moles_element / moles_C

            d.  Rounding to 5 decimal places and formatting as an
                empirical formula string:
                    C1.0 Hx.xx Ox.xx Nx.xx Sx.xx

    5.  Prints the following to the console for each sample:

            Sample Name ->
            Scaled mole ratios: {C: x.xx, H: x.xx, ...}
            Trimmed ratios: {C: x.xx, H: x.xx, ...}
            Empirical Formula: C1.0 Hx.xx Ox.xx Nx.xx Sx.xx
"""

# Define atomic masses for each element
atomic_masses = {'C': 12.01, 'H': 1.008, 'N': 14.01, 'O': 16.00, 'S': 32.07}

# Define the molecular compositions of the materials (coconut, rice, walnut, LDPE)
# These compositions are hypothetical and need to be defined for each material.
material_compositions = {
    'coconut': {'C': 45.0, 'H': 6.0, 'N': 0.1, 'O': 48.0, 'S': 0.1},
    'rice': {'C': 43.0, 'H': 6.9, 'N': 1.0, 'O': 49.0, 'S': 0.1},
    'walnut': {'C': 58.0, 'H': 8.0, 'N': 1.5, 'O': 31.5, 'S': 0.1},
    'LDPE': {'C': 85.0, 'H': 14.0, 'N': 0.0, 'O': 0.0, 'S': 0.0}
}

# Sample data
mixture_ratios_list = [
    {'name': 'Sample: 1/24/38', 'ratios': {'coconut': 0.333, 'rice': 0.0, 'walnut': 0.333, 'LDPE': 0.333}},
    {'name': 'Sample: 2/39/54', 'ratios': {'coconut': 0, 'rice': 0.333, 'walnut': 0.333, 'LDPE': 0.333}},
    {'name': 'Sample: 3/40/55', 'ratios': {'coconut': 0.333, 'rice': 0.333, 'walnut': 0, 'LDPE': 0.333}},
    {'name': 'Sample: 4/41', 'ratios': {'coconut': 0.333, 'rice': 0.333, 'walnut': 0.333, 'LDPE': 0}},
    {'name': 'Sample: 5/51', 'ratios': {'coconut': 0.166, 'rice': 0.50, 'walnut': 0.166, 'LDPE': 0.166}},
    {'name': 'Sample: 6/52', 'ratios': {'coconut': 0.50, 'rice': 0.166, 'walnut': 0.166, 'LDPE': 0.166}},
    {'name': 'Sample: 7/53', 'ratios': {'coconut': 0.166, 'rice': 0.166, 'walnut': 0.50, 'LDPE': 0.166}},
    {'name': 'Sample: 8/45/57', 'ratios': {'coconut': 0.166, 'rice': 0.166, 'walnut': 0.166, 'LDPE': 0.50}},
    {'name': 'Sample: 9/46', 'ratios': {'coconut': 0.833, 'rice': 0.75, 'walnut': 0.8333, 'LDPE': 0.8333}},
    {'name': 'Sample: 10/47', 'ratios': {'coconut': 0.75, 'rice': 0.8333, 'walnut': 0.8333, 'LDPE': 0.8333}},
    {'name': 'Sample: 11/48', 'ratios': {'coconut': 0.8333, 'rice': 0.8333, 'walnut': 0.75, 'LDPE': 0.8333}},
    {'name': 'Sample: 12/49', 'ratios': {'coconut': 0.8333, 'rice': 0.8333, 'walnut': 0.8333, 'LDPE': 0.75}},
    {'name': 'Sample: 13/25/44', 'ratios': {'coconut': 0, 'rice': 1.0, 'walnut': 0, 'LDPE': 0}},
    {'name': 'Sample: 14/30', 'ratios': {'coconut': 1.0, 'rice': 0, 'walnut': 0, 'LDPE': 0}},
    {'name': 'Sample: 15/34', 'ratios': {'coconut': 0, 'rice': 0, 'walnut': 1.0, 'LDPE': 0}},
    {'name': 'Sample: 16/29/42', 'ratios': {'coconut': 0, 'rice': 0, 'walnut': 0, 'LDPE': 1.0}},
    {'name': 'Sample: 17/50/58', 'ratios': {'coconut': 0.25, 'rice': 0.25, 'walnut': 0.25, 'LDPE': 0.25}},
    {'name': 'Sample: 18/26/69', 'ratios': {'coconut': 0, 'rice': 0.25, 'walnut': 0, 'LDPE': 0.75}},
    {'name': 'Sample: 19/27/70', 'ratios': {'coconut': 0, 'rice': 0.50, 'walnut': 0, 'LDPE': 0.50}},
    {'name': 'Sample: 20/28/43', 'ratios': {'coconut': 0, 'rice': 0.75, 'walnut': 0, 'LDPE': 0.25}},
    {'name': 'Sample: 31', 'ratios': {'coconut': 0.75, 'rice': 0.25, 'walnut': 0, 'LDPE': 0}},
    {'name': 'Sample: 32', 'ratios': {'coconut': 0.50, 'rice': 0.50, 'walnut': 0, 'LDPE': 0}},
    {'name': 'Sample: 33', 'ratios': {'coconut': 0.25, 'rice': 0.75, 'walnut': 0, 'LDPE': 0}},
    {'name': 'Sample: 35', 'ratios': {'coconut': 0, 'rice': 0.25, 'walnut': 0.75, 'LDPE': 0}},
    {'name': 'Sample: 36', 'ratios': {'coconut': 0, 'rice': 0.50, 'walnut': 0.50, 'LDPE': 0}},
    {'name': 'Sample: 37', 'ratios': {'coconut': 0, 'rice': 0.75, 'walnut': 0.25, 'LDPE': 0}},
    {'name': 'Sample: 59', 'ratios': {'coconut': 0, 'rice': 0.40, 'walnut': 0.40, 'LDPE': 0.20}},
    {'name': 'Sample: 60', 'ratios': {'coconut': 0, 'rice': 0.25, 'walnut': 0.50, 'LDPE': 0.25}},
    {'name': 'Sample: 61', 'ratios': {'coconut': 0, 'rice': 0.50, 'walnut': 0.25, 'LDPE': 0.25}},
    {'name': 'Sample: 62', 'ratios': {'coconut': 0.50, 'rice': 0.25, 'walnut': 0, 'LDPE': 0.25}},
    {'name': 'Sample: 63', 'ratios': {'coconut': 0.40, 'rice': 0.40, 'walnut': 0, 'LDPE': 0.20}},
    {'name': 'Sample: 64', 'ratios': {'coconut': 0.25, 'rice': 0.50, 'walnut': 0, 'LDPE': 0.25}},
    {'name': 'Sample: 65', 'ratios': {'coconut': 0.20, 'rice': 0.60, 'walnut': 0, 'LDPE': 0.20}},
    {'name': 'Sample: 66', 'ratios': {'coconut': 0, 'rice': 0.60, 'walnut': 0.25, 'LDPE': 0.20}},
]


# Function to calculate empirical formula
def calculate_empirical_formula(sample):
    # Step 1: Calculate the weighted averages of element ratios for each material in the mixture
    weighted_composition = {element: 0 for element in atomic_masses}  # Initialize the composition dictionary
    for material, ratio in sample['ratios'].items():
        if material in material_compositions:
            for element in atomic_masses:
                weighted_composition[element] += material_compositions[material][element] * ratio

    # Step 2: Convert mass percentages to moles for each element in the mixture
    moles = {element: weighted_composition[element] / atomic_masses[element] for element in weighted_composition}

    # Step 3: Normalize the ratios by dividing by the smallest mole value (which is that of Carbon)
    carbon_moles = moles['C']
    ratios = {element: moles[element] / carbon_moles for element in moles}

    # Step 4: Trim the ratios to three decimal places
    trimmed_ratios = {element: round(ratios[element], 5) for element in ratios}

    # Step 5: Format the empirical formula with the trimmed mole ratios
    empirical_formula = ""
    for element, ratio in trimmed_ratios.items():
        empirical_formula += f"{element}{ratio} "

    return {
        'scaled_ratios': ratios,
        'trimmed_ratios': trimmed_ratios,
        'empirical_formula': empirical_formula.strip()
    }


# Process each sample in the mixture_ratios_list
for sample in mixture_ratios_list:
    result = calculate_empirical_formula(sample)

    # Printing output in the specified format
    print(f"{sample['name']} ->")
    print("Scaled mole ratios:", result['scaled_ratios'])
    print("Trimmed ratios:", result['trimmed_ratios'])
    print("Empirical Formula:", result['empirical_formula'])
    print()  # Add a blank line for separation
