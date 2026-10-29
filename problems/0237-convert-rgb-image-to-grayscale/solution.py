import numpy as np
import math

def rgb_to_grayscale(image):
	def nearest(i):
		frac=i-math.floor(i)
		if frac>0.5:
			i=math.floor(i)+1
		elif frac<=0.5:
			i=math.floor(i)
		return i
	if type(image)==list:
		image=np.array(image)
	s=tuple(image.shape)
	if 0 in s or s[len(s)-1]!=3:
		return - 1
	else:
		coeff=np.array([0.299,0.587,0.114])
		gs=[]
		for m in image:
			l=[]
			for pix in m:
				for each in pix:
					if each<0 or each>255:
						return -1	
				pix=np.array(pix)
				gray=np.dot(coeff,pix).item()
				gr=nearest(gray)
				l.append(gr)
			gs.append(l)	
		return gs
	pass
	