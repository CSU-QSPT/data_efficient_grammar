from tkinter import ALL
from rdkit import DataStructs, Chem
from rdkit.Chem import AllChem
import numpy as np

QSAR_MAPPING = {'logP': _logP,
                'another_qsar': _another_qsar}

SUPPORTED_QSAR_TYPES = list(QSAR_MAPPING.keys())

def qsar(generated_samples, qsar_type):
    if qsar_type not in SUPPORTED_QSAR_TYPES:
        qtypes = ', '.join(f"'{q}'" for q in SUPPORTED_QSAR_TYPES)
        raise ValueError(f"Error': qsar_type '{qsar_type}' is not supported. Must be one of {qtypes}")
    score = QSAR_MAPPING[qsar_type](generated_samples)
    return score

def _logP(generated_samples):
    score = np.random.rand()
    return score

def _another_qsar(generated_samples):
    score = np.random.rand()
    return score
