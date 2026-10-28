import torch

def flatten_then_reshape(x: torch.Tensor, new_shape) -> torch.Tensor:
    # TODO: flatten x to 1-D, then rearrange into new_shape
    x.reshape((1,-1))
    return x.reshape (new_shape)
    pass

def transpose_last_two(x: torch.Tensor) -> torch.Tensor:
    # TODO: swap the last two dimensions of x
    return x.transpose(1,2) if len(x.shape)>2 else x.transpose(0,1)
    pass
    
