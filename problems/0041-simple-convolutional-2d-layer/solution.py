import numpy as np

def simple_conv2d(input_matrix: np.ndarray, kernel: np.ndarray, padding: int, stride: int):
	k_height,k_len=kernel.shape
	inp_height,inp_len=input_matrix.shape
	lout=((inp_len+2*padding-k_len)//stride)+1
	nout=((inp_height+2*padding-k_height)//stride)+1
	input_matrix=np.pad(input_matrix,padding,mode='constant')
	nl=[]
	for i in range(nout):
		l=[]
		for j in range(lout):
			f=input_matrix[stride*i:k_height+i*stride,stride*j:stride*j+k_len,]
			#print(f)
			hadamard=np.sum(f*kernel)
			l.append(hadamard)
		nl.append(l)
	output_matrix=np.array(nl)
	return output_matrix 

	

