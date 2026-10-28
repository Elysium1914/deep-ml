import numpy as np

def diag(A: np.ndarray) -> np.ndarray:
    """Return the main diagonal of square matrix A."""
    out=[]
    for i,j in zip((r for r in range(A.shape[0])),(c for c in range(A.shape[1]))):
        if i==j:
            out.append(float(A[i,j]))
    return out
    pass
