import numpy as np
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt

sr=600
ts=1.0/sr 
tmax=240
t=np.arange(0,tmax,ts)
#Unos podataka iz datoteke MEG.txt. U datoteci se nalaze podaci koji 
#prikazuju "magnetizaciju" mozga od vremena, mjerenu na raznim lokacijama odnosno s raznim elektrodama. 
#Iz Fourierove anlalize možemo uočiti koje su frekvencije bile najviše zastupljene, odnosno koji moždani talasi (alfa,beta,theta ...)
# su bili najvise zastupljeni.
f1 = open("MEG.txt", "r")
brojevi = []
linija = f1.readline()
for broj in linija.split():
    brojevi.append(float(broj))

linije = f1.readlines()
for i in linije:
    for broj in i.split():
        brojevi.append(float(broj))
f1.close()
plt.plot(t, brojevi)
plt.xlabel("t")
plt.ylabel("MEG Signal")
plt.title("MEG signal u zavisnosti od vremena")
plt.show()
N=len(brojevi)
yf = fft(brojevi)
xf = fftfreq(N, 1 / sr)
plt.plot(xf, np.abs(yf))
plt.xlim(0,sr/2)
plt.title("Amplitudno-frekventna karakteristika")
plt.xlabel("Frekvencija(Hz)")
plt.ylabel("Amplituda")

