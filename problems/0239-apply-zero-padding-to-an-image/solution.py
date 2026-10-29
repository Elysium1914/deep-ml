import torch

def zero_pad_image(img, pad_width):
    img=torch.tensor(img)
    z=torch.tensor([0])
    dz=torch.tensor([0,0])
    l,l2,out=[],[],[]
    if len(img.shape)!=2:
        return -1
    elif pad_width<0:
        return -1
    elif len(list(img))==0:
        return -1
    else:
        for inner in img:
            for _ in range(pad_width):
                inner=torch.cat((z,inner),dim=0)
                inner=torch.cat((inner,z),dim=0)
            l.append(list(inner))
        imgo1=torch.tensor(l)
        for _ in range(pad_width):
            zl=torch.full_like(imgo1[:1],0)
            imgo1=torch.cat((zl,imgo1),dim=0)
            imgo1=torch.cat((imgo1,zl),dim=0)
        return imgo1.tolist()        

    """
    Add zero padding around a grayscale image.
    
    Args:
        img: 2D list or torch.Tensor of pixel values
        pad_width: integer number of pixels to pad on each side
    
    Returns:
        Padded image as 2D list with integer values,
        or -1 if input is invalid
    """
    # Write your code here
    pass