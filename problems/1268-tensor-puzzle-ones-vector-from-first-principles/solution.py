import numpy as np

def ones(n: int) -> np.ndarray:
    """Return a length-n float vector of ones without calling np.ones."""
    arr=np.arange(n,dtype=np.float64)
    x=[]
    for i in range(-1,len(arr)-1):
        x.append(float(i))
    x=np.array(x)
    return arr-x
    pass
