# BZmesh
Scan the Brillouin zone to characterize the shape of nodal line, nodal net, etc.

Process:

1. scf calculation
2. make a folder BZmesh, containing pre folder
3. pre folder contains kpts.dat, INCAR, POSCAR, POTCAR, submit.sh, CHGCAR, WAVECAR
4. run makekpoints.py
5. submit jobs
6. run grabnode.py to deal with results
