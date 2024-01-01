#Task: Find the Fourier transform of an arbitrary signal
import numpy as np
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt
 
sr=600 #Frekvencija uzorkovanja koja mora biti duplo veća od najveće frekvencije 
ts=1.0/sr 
tmax=240
t=np.arange(0,tmax,ts)
#read data from the MEG.txt file.The file contains data that shows the "magnetization" of the brain over time, measured at different locations, or with different electrodes.
#From Fourier analysis, we can see which frequencies were most represented, or which brain waves (alpha, beta, theta, etc.)
# su bili najviše zastupljeni.
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
#The scipy fft function is used to decompose the signal into its constituent frequencies
yf = fft(brojevi)
xf = fftfreq(N, 1 / sr)
plt.plot(xf, np.abs(yf))
plt.xlim(0,sr/2)
plt.title("Amplitudno-frekventna karakteristika")
plt.xlabel("Frekvencija(Hz)")
plt.ylabel("Amplituda")

