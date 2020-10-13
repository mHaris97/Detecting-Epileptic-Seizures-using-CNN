import os
import re
import numpy as np
import matplotlib.pyplot as plt

file = 'MIT EEG Data\chb01-summary.txt'
f = open(file, 'r')
file_contents = f.read()

file_list = file_contents.split('\n')

subs = 'chb01_26'
subs = 'File Name: ' + subs + '.edf'
ind = file_list.index(subs)

##seizures = int(file_list[ind+3])
temp     = re.findall(r'\d+', file_list[ind+3]) 
seizures = list(map(int, temp))[0]
##print(seizures)

start = []
end   = []
for i in range(seizures):
    start.append(list(map(int, re.findall(r'\d+', file_list[ind+2*i+4])))[0])
    end.append(list(map(int, re.findall(r'\d+', file_list[ind+2*i+5])))[0])
    print(start, end)

if seizures == 0:
    labels = np.zeros((23, 921600))
else:
    labels = np.ones((23, 921600))
    labels[:, end[-1]*256:] *= 0
    for i in range(len(start)):
        labels[:, start[i]*256:end[i]*256] *= 2

##if seizures == 0:
##    labels = np.zeros((230, 3600))
##else:
##    labels = np.ones((230, 3600))
##    labels[:, end[-1]*1:] *= 0
##    for i in range(len(start)):
##        labels[:, start[i]*1:end[i]*1] *= 2

plt.imshow(labels)
plt.show()
    
    



    




