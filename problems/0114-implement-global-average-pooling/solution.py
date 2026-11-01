import numpy as np

def global_avg_pool(x: np.ndarray) -> np.ndarray:
	out=[]
	l=[]
	for kernel in x.T:
		c=0
		for i in np.nditer(kernel):
			c+=1
		avg=(sum(sum(kernel))/c).item()
		out.append(avg)
	return out