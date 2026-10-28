def pad_vocab_size(vocab_size: int, alignment: int) -> int:
    if vocab_size>0 and alignment>0:
        r=vocab_size % alignment
        diff= alignment-r
        if vocab_size> alignment and vocab_size% alignment!=0:
            out=diff+vocab_size
        elif vocab_size% alignment==0:
            out=vocab_size
        else:
            out= alignment
        return out
    else:
        raise ValueError
   
        
    """
    Round vocab_size up to the smallest multiple of alignment.

    Args:
        vocab_size: original number of tokens in the vocabulary (must be > 0).
        alignment: tensor-core friendly alignment (must be > 0), e.g. 64 or 128.

    Returns:
        The padded vocabulary size as a Python int.
    """
    pass
