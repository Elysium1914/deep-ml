import numpy as np

def outer(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Outer product of 1-D arrays a and b via broadcasting."""
    nl,l=[],[]
    for i in (list(a)):
        for j in list(b):
            l.append(i*j)
        nl.append(l)
        l=[]
    return np.array(nl)


    pass
