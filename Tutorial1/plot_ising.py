########## Machine Learning for Quantum Matter and Technology  ######################
### Juan Carrasquilla, Estelle Inack, Giacomo Torlai, Roger Melko
### with code from Lauren Hayward Sierens/PSI
### Tutorial 1: Monte Carlo for the Ising model
#####################################################################################

from matplotlib import pyplot
import numpy as np

### Input parameters (these should be the same as in ising_mc.py): ###
T_list = np.linspace(5.0,0.5,20) #temperature list
L_array = [4, 6, 8, 10]                         #linear size of the lattice
J = 1                            #coupling parameter
### Critical temperature: ###
Tc = 2.0/np.log(1.0 + np.sqrt(2))*J
fig = pyplot.figure()
ax = fig.add_subplot(221)
ax1 = fig.add_subplot(222)
ax2 = fig.add_subplot(223)
ax3 = fig.add_subplot(224)


for L in L_array:
### Observables to plot as a function of temperature: ###
  N_spins = L**2                   #total number of spins
  energy   = np.zeros(len(T_list))
  mag      = np.zeros(len(T_list))
  specHeat = np.zeros(len(T_list))
  susc     = np.zeros(len(T_list))

  ### Loop to read in data for each temperature: ###
  for (iT,T) in enumerate(T_list):
    file = open('Data/ising2d_L%d_T%.4f.txt' %(L,T), 'r')
    data = np.loadtxt( file )

    E   = data[:,1]
    M   = abs(data[:,2])

    energy[iT] = np.mean(E)
    mag[iT]    = np.mean(M)
    
    # *********************************************************************** #
    # *********** 2b) FILL IN CODE TO CALCULATE THE SPECIFIC HEAT *********** #
    # ***********               AND SUSCEPTIBILITY                *********** #
    # *********************************************************************** #
    specHeat[iT] = (np.mean(E**2) - np.mean(E)**2) / (T ** 2)
    susc[iT]     = (np.mean(M ** 2) - np.mean(np.abs(M))**2) / (T)
  #end loop over T

  ax.axvline(x=Tc, color='k', linestyle='--')
  ax.plot(T_list, energy/(1.0*N_spins), 'o-', label = r"$L = %i$"%L)
  ax.set_xlabel(r'$T$')
  ax.set_ylabel(r'$<E>/N$')

  ax1.axvline(x=Tc, color='k', linestyle='--')
  ax1.plot(T_list, mag/(1.0*N_spins), 'o-', label = r"$L = %i$"%L)
  ax1.set_xlabel(r'$T$')
  ax1.set_ylabel(r'$<|M|>/N$')

  ax2.axvline(x=Tc, color='k', linestyle='--')
  ax2.plot(T_list, specHeat/(1.0*N_spins), 'o-', label = r"$L = %i$"%L)
  ax2.set_xlabel(r'$T$')
  ax2.set_ylabel(r'$C_V/N$')

  ax3.axvline(x=Tc, color='k', linestyle='--')
  ax3.plot(T_list, susc/(1.0*N_spins), 'o-', label = r"$L = %i$"%L)
  ax3.set_xlabel(r'$T$')
  ax3.set_ylabel(r'$\chi/N$')

axes = [ax, ax1, ax2, ax3]
for a in axes:
  a.legend(loc="best")
  a.grid()

pyplot.show()
