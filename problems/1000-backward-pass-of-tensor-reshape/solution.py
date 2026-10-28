import numpy as np

def reshape_backward(grad_output: np.ndarray, original_shape: tuple) -> np.ndarray:
    try:
        out= grad_output.reshape(original_shape)
    except ValueError:
        raise
    return out
    """
    Backward pass for a reshape/view operation.

    Args:
        grad_output: numpy array, gradient w.r.t. the reshape output.
        original_shape: tuple of ints, shape of the input to the forward reshape.

    Returns:
        numpy array of shape `original_shape` containing the gradient
        w.r.t. the input tensor.
    """
    pass
