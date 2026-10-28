import torch

def eye(n: int) -> torch.Tensor:
    """n x n identity via comparisons (no torch.eye)."""
    t=torch.zeros((n,n),dtype=torch.float64)
    for i in range(n):
        for j in range(n):
            if i==j:
                t[i,j]=1
    return t
    pass
