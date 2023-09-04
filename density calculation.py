filein = open('changing_density1.xvg', 'w')
filein1 = open('changing_density1.txt', 'w')

len = 130 # number of gmx density files from trajectories

# read minimum water densities from xvg files
for i in range(len):
	f = open(f'density{i}.xvg', 'r').readlines()[24:] 
	f = [float(x[20:]) for x in f]
	filein.write(str(i)+'	'+str(min(f))+'\n') # save as xvg
	filein1.write(str(i)+';'+str(min(f))+'\n') # save as txt

filein.close()
filein1.close()
