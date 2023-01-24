import numpy as np
import csv
import matplotlib.pyplot as plt

sump_freq = 44100.0
sec = 0.2 #second
dt = 1.0/sump_freq # 標本化間隔[s]

amp = 1.5 #最大振幅
freq = 440 # 400Hzの正弦波
bias = 2.0
out = []

t = np.arange(0, sec, dt)
out = amp * np.sin(2 * np.pi * freq * t) + bias




#for i in range(int(sump_freq * sec)):
#    rad = (2 * np.pi * freq * float(i*dt) /(sump_freq * sec))
#    out.append(float(amp * np.sin(rad) + bias))

File_write = str(freq) + '.csv'

with open(File_write, 'w', newline="") as fw:
    writer = csv.writer(fw)
    for r in range(int(sump_freq * sec)):
        writer.writerow([out[r]])
        
#plt.plot(t,y)
#plt.show()