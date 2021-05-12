import numpy as np
from scipy import interpolate as itp
import sys

#mDM= 180
#channel="tautau"


try:
  mDM = sys.argv[1]
  channel = sys.argv[2]
except:
  print "Tell me about the mass  of dark matter"
  quit()

mDM=float(mDM)


if channel=="ee":
  column=4
elif channel=="mumu":
  column=7
elif channel=="tautau":
  column=10
elif channel=="qq":
  column=11
elif channel=="cc":
  column=12
elif channel=="bb":
  column=13
elif channel=="tt":
  column=14
elif channel=="ww":
  column=17
elif channel=="zz":
  column=20
elif channel=="hh":
  column=23

energies = np.loadtxt('AtProduction_gammas.dat',
                      usecols=(0,))[np.arange(11098, step=179)]
log10x = np.loadtxt('AtProduction_gammas.dat', usecols=(1,))[: 179]

'''muon channel'''
table = np.loadtxt('AtProduction_gammas.dat', usecols=(column,)).reshape((62, 179))

interp = itp.RectBivariateSpline(energies, log10x, table)


def spectrum(mDM_anni, E_gamma):
    """annihilation"""
    x = E_gamma / mDM_anni
    result = interp(mDM_anni, np.log10(x))
    result = result/(E_gamma * np.log(10))
    return result


'''DM paras'''

xlist =np.power(10, np.arange(-4, 0, 0.02))
Elist =mDM*xlist

spec=spectrum(mDM,Elist)

np.savetxt('flux_%s_%.2f.dat' %(channel, mDM), np.vstack((Elist/1e3, spec*1e3)).T)
a=open('flux_%s_%.2f.dat' %(channel, mDM),'a')
print >>a, mDM/1e3, 0.0
print >>a, mDM/1e3*1000, 0.0
