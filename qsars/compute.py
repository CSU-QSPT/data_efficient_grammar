#------------------------------------------------------------------------------
# Import all of the QSARs of interest
#------------------------------------------------------------------------------
from qsars.logp import logp
from qsars.another_qsar import another_qsar

# Update these as modules are added
QSAR_MAPPING = {'logp': logp,
                'another_qsar': another_qsar}

#------------------------------------------------------------------------------

SUPPORTED_QSAR_TYPES = list(QSAR_MAPPING.keys())

#------------------------------------------------------------------------------

# The main function to dispatch to the separate functions
def qsar(generated_samples, qsar_type):
    if qsar_type not in SUPPORTED_QSAR_TYPES:
        qtypes = ', '.join(f"'{q}'" for q in SUPPORTED_QSAR_TYPES)
        raise ValueError(f"Error': qsar_type '{qsar_type}' is not supported. Must be one of {qtypes}")
    score = QSAR_MAPPING[qsar_type](generated_samples)
    return score
