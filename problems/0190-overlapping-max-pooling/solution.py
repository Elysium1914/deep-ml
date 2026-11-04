import numpy as np

def overlapping_max_pool2d(x: np.ndarray, kernel_size: int = 3, stride: int = 2) -> np.ndarray:
    out=[]
    for batch in x:
        batchout=[]
        for channel in batch:
            chan_height,chan_len=channel.shape
            nout=(chan_height-kernel_size)//stride + 1
            lout=(chan_len-kernel_size)//stride + 1
            chanout=[]
            for i in range(nout):
                row=[]
                for j in range(lout):
                    pool=channel[i*stride:i*stride+kernel_size,j*stride:j*stride+kernel_size]
                    elements=[]
                    for element in np.nditer(pool):
                        elements.append(element.item())
                    poolmax=max(elements)
                    row.append(poolmax)
                chanout.append(row)
            batchout.append(chanout)
        out.append(batchout)
    outarr=np.array(out)
    return outarr
    """
    Applies overlapping max pooling to a 4D tensor (N, C, H, W).
    Uses ceil mode for output dimensions (allows partial windows at boundaries).

    Args:
        x: Input array of shape (N, C, H, W)
        kernel_size: Size of pooling window (int)
        stride: Stride between pooling windows (int), must be < kernel_size

    Returns:
        A 4D tensor after overlapping pooling with ceil mode.
    """
    # Your code here
    pass