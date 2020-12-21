# Detecting Epileptic Seizures From EEG Data using CNN

In this project we work on an open source dataset, from MIT, which contained Electroencephalographic (EEG) readings of epileptic patients labelled with time stamps for seizures. We worked on a very simple, Computer Vision inspired, Convolutional Neural Network (CNN) to get a satisfactory level of accuracy for classification of the three phases of a seizure: pre-ictal (one hour before a seizure), ictal (during) and interictal (between two seizures). The following architecture was used (which yielded the best results):

![alt text](https://github.com/mHaris97/Detecting-Epileptic-Seizures-using-CNN/blob/main/images/orgArch.PNG)

## Results
The following are the results for frequency domain and over individual patients, and time domain.

![alt text](https://github.com/mHaris97/Detecting-Epileptic-Seizures-using-CNN/blob/main/images/freq_acc.png)
![alt text](https://github.com/mHaris97/Detecting-Epileptic-Seizures-using-CNN/blob/main/images/acc24.png)
![alt text](https://github.com/mHaris97/Detecting-Epileptic-Seizures-using-CNN/blob/main/images/time_acc.png)


## Getting Started

The .ipynb works on Google Colab. Make sure you have tensorflow 1.x installed. Set the runtime to TPU for maximum Disk storage as well as RAM. 
