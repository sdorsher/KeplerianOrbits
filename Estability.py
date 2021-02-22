import numpy as np
import math
def Estability(npstar1x,npstar2x,masses):
    npstar1pos=npstar1x[:,0:3]
    npstar1v=npstar1x[:,3:]
    npstar2pos=npstar2x[:,0:3]
    npstar2v=npstar2x[:,3:]
    nprstars12=np.sqrt(np.sum((npstar1pos-npstar2pos)**2,axis=1))
    npcm=(masses[0]*npstar1pos+masses[1]*npstar2pos)/np.sum(masses)
    npvcm =( masses[0]*npstar1v+masses[1]*npstar2v)/np.sum(masses)


    Egrav=-masses[0]*masses[1]/nprstars12
    Ekinetic=masses[0]*0.5*np.sum((npstar1v-npvcm)**2,axis=1)+masses[1]*0.5*np.sum((npstar2v-npvcm)**2,axis=1)
    Etot=Ekinetic+Egrav
    deltaE=np.abs(np.std(Etot)/np.mean(Etot))
    return deltaE, np.mean(Etot),Etot,Ekinetic,Egrav
