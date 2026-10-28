import numpy as np

def vector_sum(a: np.ndarray):
    """Sum elements of 1-D array a without np.sum / loops."""
    return np.dot(a,np.full_like(a,1))
    pass
