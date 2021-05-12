import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
from scipy.interpolate import interp2d
from skimage import exposure,data

plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

def dnde(mchi,branch,emid):
	
	datafile = '/home/wqkuo/Downloads/AtProductionNoEW_gammas.dat'
	header = open(datafile).readline().split()
	data = np.loadtxt(datafile,skiprows=1)
    
    ##x_pppc = log10(energy/mchi)
    ##x = energy/mchi
    ##energy  = mchi * (10 ** x_pppc), energy is the energy of each photon
    ## select line index range from 0 to 178
	x_pppc = data[0:180,1] 
    
    ## DM mass in GeV
    ## select the first value (index is 0), per 179 line, total number is 62, i.e., the first is 0 next is 179*1, then 179*2...
	mchi_pppc = data[180 * np.arange(0, 62), 0]
    
    
	if branch == 'mu' : branch='\\[Mu]'
	if branch == 'tau': branch='\\[Tau]'

    #obtain index of the inter 'branch'
	index = header.index(branch)
    #the len(mchi_pppc) is 62, obtain the dnde of each mass of DM
	dnde_pppc = np.array([data[i * 180 : (i + 1) * 180, index] for i in range(len(mchi_pppc))])
    #set the lower limit
	dnde_pppc[dnde_pppc < 1e-50] = 1e-50
    #print the dimension of the dede_pppc, x_pppc, mchi_pppc
	print (dnde_pppc.shape,x_pppc.shape,mchi_pppc.shape)
    
	dndx = interp2d(np.log(mchi_pppc), x_pppc, np.log(dnde_pppc).T)(np.log(mchi), np.log10(emid/mchi))
	try :
		dnde = np.exp(dndx[:,0]) / (emid * np.log(10))
	except IndexError :
		dnde=np.exp(dndx) / (emid * np.log(10))

	##dn/de=(dn/dx)*(dx/de)=(dn/dx)/(e*ln(10)) 
	return dnde

while 1:
    mchi = int(input('inter the mass of DM(GeV): '))
    
    if mchi != 0:
        branch = input('inter the branch of annihilation: ')
        xmin = int(np.log10(100))
        xmax = int(np.log10(mchi * 1e3))
        x = np.logspace(xmin, xmax, 50)/1e3
        y = dnde(mchi,branch,x)
        plt.loglog(x*1e3, y/1e3, label = str(mchi) + ' GeV', color = 'green')
        #plt.legend(loc = 'lower left')
        #plt.title(r'DM' + ' -> ' + branch)
        #plt.ylabel(r'$dN_{\gamma}/dE_{\gamma}$ $[MeV^{-1}]$')
        #plt.xlabel(r'Energy [Mev]')
        #plt.xlim(1e2, 1e6)
        #plt.ylim(1e-8, 1e-1)
    
    if mchi == 0:
        break


plt.title(r'DM -> $b$$\bar b$')
plt.xlabel('Energy [MeV]')
plt.ylabel('$dN_γ/dE_γ$ $[MeV^{-1}]$')

plt.ylim(1e-8, 1e-1)
plt.xlim(1e2, 1e6)
plt.legend(loc = 'lower left')
plt.xticks([1e2, 1e3, 1e4, 1e5, 1e6])
plt.tick_params(top = 'True', right = 'Ture', which = 'both')
#plt.savefig('/home/wqkuo/bbar')
plt.show()

'''
datafile = '/home/wqkuo/Downloads/AtProductionNoEW_gammas.dat'
header = open(datafile).readline().split()
data = np.loadtxt(datafile,skiprows=1)
    
    ##x_pppc = log10(energy/mchi)
    ##x = energy/mchi
    ##energy  = mchi * (10 ** x_pppc), energy is the energy of each photon
    ## select line index range from 0 to 178
x_pppc = data[0:181,0] 
print('EW =', x_pppc)

datafile1 = '/home/wqkuo/Downloads/AtProduction_gammas.dat'
header1 = open(datafile1).readline().split()
data1 = np.loadtxt(datafile1,skiprows=1)
x = data1[0:180,0]
print('noEW =',x)
'''








'''
import numpy as np
from scipy.interpolate import interp2d
import matplotlib.pyplot as plt

plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

def dnde(mchi,branch,emid):
	
	datafile = '/home/wqkuo/Downloads/AtProduction_gammas.dat'
	header = open(datafile).readline().split()
	data = np.loadtxt(datafile,skiprows=1)
    
    ##x_pppc = log10(energy/mchi)
    ##x = energy/mchi
    ##energy  = mchi * (10 ** x_pppc), energy is the energy of each photon
    ## select line index range from 0 to 178
	x_pppc = data[0:179,1] 
    
    ## DM mass in GeV
    ## select the first value (index is 0), per 179 line, total number is 62, i.e., the first is 0 next is 179*1, then 179*2...
	mchi_pppc = data[179 * np.arange(0, 62), 0]
    
    
	if branch == 'mu' : branch='\\[Mu]'
	if branch == 'tau': branch='\\[Tau]'

    #obtain index of the inter 'branch'
	index = header.index(branch)
    #the len(mchi_pppc) is 62, obtain the dnde of each mass of DM
	dnde_pppc = np.array([data[i * 179 : (i + 1) * 179, index] for i in range(len(mchi_pppc))])
    #set the lower limit
	dnde_pppc[dnde_pppc < 1e-50] = 1e-50
    #print the dimension of the dede_pppc, x_pppc, mchi_pppc
	print (dnde_pppc.shape,x_pppc.shape,mchi_pppc.shape)
    
	dndx = interp2d(np.log(mchi_pppc), x_pppc, np.log(dnde_pppc).T)(np.log(mchi), np.log10(emid/mchi))
	try :
		dnde = np.exp(dndx[:,0]) / (emid * np.log(10))
	except IndexError :
		dnde=np.exp(dndx) / (emid * np.log(10))

	##dn/de=(dn/dx)*(dx/de)=(dn/dx)/(e*ln(10)) 
	return dnde

while 1:
    mchi = int(input('inter the mass of DM(GeV): '))
    
    if mchi != 0:
        branch = input('inter the branch of annihilation: ')
        xmin = int(np.log10(100))
        xmax = int(np.log10(mchi * 1e3))
        x = np.logspace(xmin, xmax, 50)/1e3
        y = dnde(mchi,branch,x)
        plt.loglog(x*1e3, y/1e3, label = str(mchi) + ' GeV')
        plt.legend(loc = 'lower left')
        plt.title(r'DM' + ' -> ' + branch)
        plt.ylabel(r'$dN_{\gamma}/dE_{\gamma}$ $[MeV^{-1}]$')
        plt.xlabel(r'Energy [Mev]')
        plt.xlim(1e2, 1e6)
        plt.ylim(1e-8, 1e-1)
    
    if mchi == 0:
        break
plt.tick_params(top = 'True', right = 'True', which = 'both')
plt.show()
'''
