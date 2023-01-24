import numpy as np
import csv
import matplotlib.pyplot as plt
import pandas as pd

def dft(x):
    X = [] 

    for n in range(len(x)):
        if (n%1000 == 0):
            print("{}回目".format(n))
        weight = np.exp(-1j*((2*np.pi*n)/len(x)))
        X_omega = 0
        for omega in range(len(x)):
            X_omega += x[omega] * (weight**omega)
        X.append(X_omega)
    return abs(np.array(X))
    
def sample_csv(frequency, seconds):
    sampling_freq = 44100
    amp, bias = 1.5 , 2.0
    t = np.arange(0, seconds, 1/sampling_freq)
    samp_wav = amp * np.sin(2 * np.pi * frequency * t) + bias

    with open(str(frequency)+'.csv', 'w', newline="") as sample_csv_fw:
        writer = csv.writer(sample_csv_fw)
        for r in range(int(sampling_freq * seconds)):
            writer.writerow([samp_wav[r]])
        
    return np.array(samp_wav)

def sample_csv2():
    sin1 = sample_csv(440*1, 0.2)
    sin2 = sample_csv(440*3, 0.2)
    sin3 = sample_csv(440*5, 0.2)
    combined = [a1 + a2 + a3 for (a1, a2, a3) in zip(sin1, sin2, sin3)]
    
    with open(str(440*(1+3+5))+'.csv', 'w', newline="") as sample_csv2_fw:
        sample_csv2_writer = csv.writer(sample_csv2_fw)
        for r2 in range(int(len(sin1))):
            sample_csv2_writer.writerow([combined[r2]])
    
    return np.array(combined)
    
def read_csv(file):
    readdata = []
    with open(file) as fr:
    
        reader = csv.reader(fr)
        
        for row in reader:
        
            readdata.append(float(row[0]))
        fr.close()
        
    return np.array(readdata)

def plot_csv(plotcsv_file):
    data = pd.read_csv(plotcsv_file)
    plt.xlabel('freqency[Hz]')
    plt.plot(data[data.keys()[0]], data[data.keys()[1]])
    plt.show()


if __name__ == '__main__':
    input_file = '440.csv'
    output_file = 'wanwan.csv'
    
    # 1つのみを使う。
    #kyodo = dft(sample_csv(440, 0.05)) #指定した時間、秒のサンプリングレート44100の正弦波をdft
    #kyodo = dft(sample_csv2()) # 440,1320,2200Hzの正弦波を合成した波形をdft
    kyodo = dft(read_csv(input_file)) # csvからファイルを読み込んでdft
    
    with open(output_file, 'w', newline="") as dft_fw:
        dft_writer = csv.writer(dft_fw)
        for r in range(int(len(kyodo)/2)):
            dft_writer.writerow([r * 44100 / len(kyodo), kyodo[r]])
            
    plot_csv('wanwan.csv')
