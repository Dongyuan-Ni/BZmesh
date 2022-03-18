import os
import numpy as np

##################################################################
# Calculate many lines in first BZ,characterize position of node 
# in each line by finding the minimal gap in each line
##################################################################

def grab(Ef):
	with open('EIGENVAL', 'r') as f:
		data = f.readlines()
	data = data[6:]
	for i in range(len(data)):
		data[i] = [float(j) for j in data[i].split()]
	for i in range(1, len(data)):
		if data[i] == []:
			nbands = i - 2
			break
	gapmin = 100
	kpts = [0.25, 0.25, 0.25, 0.25]
	for i in range(len(data)):
		if i%(nbands+2)==1:
			kpts = data[i]
		#if kpts[3] != 0.00000000:
		#	continue
		if i%(nbands+2)==(Ef+1):
			VBM = float(data[i][1])
		if i%(nbands+2)==(Ef+2):
                	CBM = float(data[i][1])
			gap = CBM - VBM
			if gap < gapmin:
				gapmin = gap
				kptsmin = kpts
	print('Node kpts: {}; Gap: {}'.format(kptsmin, gapmin))	
	return kptsmin, gapmin

if __name__ == '__main__':
	out = []
	fname = os.listdir('.')
	fname.remove('pre')
	with open('pre/POSCAR', 'r') as f:
		for i in range(6):
			f.readline()
		natoms = int(f.readline().split()[0])
	soc = int(input('input soc for 1 and non-soc for 0'))
	if soc == 0:
		noccupancy = natoms * 2
	if soc == 1:
		noccupancy = natoms * 4
	print('Number of occupancy: {}'.format(noccupancy))
	for i in fname:
		if os.path.isdir(i):
			print(i)
			os.chdir(i)
			kptsmin, gapmin = grab(noccupancy)
			out.append(kptsmin[:3]+[gapmin])
			os.chdir('..')
	out = np.array(out)
	np.savetxt('kout.dat', out, fmt='%.6f')
