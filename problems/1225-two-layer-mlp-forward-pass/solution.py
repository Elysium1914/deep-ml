import torch
import torch.nn as nn


def two_layer_mlp_forward(x, w1, b1, w2, b2):
    l1=nn.Linear(2,2)
	l2=nn.Linear(2,1)
	MLP=nn.Sequential(l1,nn.ReLU(),l2)
	with torch.no_grad():
		w1.reshape((2,2))
		b1.reshape((2,))
		w2.reshape((1,2))
		b2.reshape((1,))
		l1.weight.copy_(w1)
		l1.bias.copy_(b1)
		l2.weight.copy_(w2)
		l2.bias.copy_(b2)
		out=MLP(x)
	return out.item()
    """Build a 2-layer MLP, set fixed weights, return scalar output.

    Args:
        x (torch.Tensor): Input of shape (1, 2).
        w1 (torch.Tensor): First Linear weight, shape (2, 2).
        b1 (torch.Tensor): First Linear bias, shape (2,).
        w2 (torch.Tensor): Second Linear weight, shape (1, 2).
        b2 (torch.Tensor): Second Linear bias, shape (1,).

    Returns:
        float: Scalar network output.
    """
    # TODO
    pass
