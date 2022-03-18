import os
import numpy as np

kpts = np.loadtxt('pre/kpts.dat')
for i in range(len(kpts)):
	os.system('mkdir '+str(i+1))
	os.chdir(str(i+1))
	os.system('cp ../pre/{INCAR,POSCAR,POTCAR,submit.sh,CHGCAR,WAVECAR} .')
	with open('KPOINTS', 'w') as f:
        	f.write('ORCC\n')
       		f.write('100\n')
        	f.write('Line-mode\n')
        	f.write('reciprocal\n')
        	f.write('  '+str(kpts[i][0])+' '+'-0.5'+' '+str(kpts[i][1])+'\n')
        	f.write('  '+str(kpts[i][0])+' '+'0.5'+' '+str(kpts[i][1]))
	os.chdir('..')
