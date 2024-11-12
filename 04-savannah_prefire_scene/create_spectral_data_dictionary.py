import xarray as xr

#
# The default scene spectral parameters for savannah_prefire are monochromatic
# values at the wavelengths of the 14 abstract satellite bands of the RAMI-V benchmark.
# The current script loads more realistic datasets of grass, bark, ground and leaves reflectance,
# extracted from the original M.I. Disney et al. (2011) reference.
#


reflectance_dataset = xr.load_dataset("./data/savannah_pre_fire_reflectance_spectra.nc")

bark_spectrum =  {
    "wavelengths": reflectance_dataset.bark_reflectance.w,
    "values": reflectance_dataset.bark_reflectance.values,
    "type": "interpolated"
}

spectral_data = {
    "ground": {
        "reflectance": {
            "wavelengths": reflectance_dataset.bright_soil_reflectance.w,
            "values": reflectance_dataset.bright_soil_reflectance.values,
            "type": "interpolated"
        }
    }
} | {
    f"grass{idx}": {
        "measured_stem": {
            "reflectance": {
                "wavelengths": reflectance_dataset.dry_grass_reflectance.w,
                "values": reflectance_dataset.dry_grass_reflectance.values,
                "type": "interpolated"
            }
        },
    }
    for idx in range(0, 10)
} | {
    f"combretum_leafoff{idx}": {
        "measured_trunk": {
            "reflectance": bark_spectrum
        },
        "measured_branch": {
            "reflectance": bark_spectrum
        },
        "Bough": {
            "reflectance": bark_spectrum
        },
    }
    for idx in range(1, 6)
} | {
    f"combretum_leafoff{idx}_flat": {
        "measured_trunk": {
            "reflectance": bark_spectrum,
        },
        "measured_branch": {
            "reflectance": bark_spectrum,
        },
        "Bough": {
            "reflectance": bark_spectrum,
        },
    }
    for idx in range(1, 6)
} | {
    f"combretum_leafon{idx}": {
        "Leaf1": {
            "reflectance": {
                "wavelengths": reflectance_dataset.leaves_reflectance.w,
                "values": reflectance_dataset.leaves_reflectance.values,
                "type": "interpolated",
            }
        },
        "measured_trunk": {
            "reflectance": bark_spectrum,
        },
        "measured_branch": {
            "reflectance": bark_spectrum,
        },
        "Bough": {
            "reflectance": bark_spectrum,
        },
    }
    for idx in range(1, 3)
} | {
    f"combretum_leafon{idx}_flat": {
        "Leaf1": {
            "reflectance": {
                "wavelengths": reflectance_dataset.leaves_reflectance.w,
                "values": reflectance_dataset.leaves_reflectance.values,
                "type": "interpolated",
            }
        },
        "measured_trunk": {
            "reflectance": bark_spectrum,
        },
        "measured_branch": {
            "reflectance": bark_spectrum,
        },
        "Bough": {
            "reflectance": bark_spectrum,
        },
    }
    for idx in range(1, 3)
} | {
    f"merula{idx}": {
        "Leaf1": {
            "reflectance": {
                "wavelengths": reflectance_dataset.leaves_reflectance.w,
                "values": reflectance_dataset.leaves_reflectance.values,
                "type": "interpolated",
            }
        },
        "measured_trunk": {
            "reflectance": bark_spectrum,
        },
        "measured_branch": {
            "reflectance": bark_spectrum,
        },
        "Bough": {
            "reflectance": bark_spectrum,
        },
    }
    for idx in range(1, 5)
}