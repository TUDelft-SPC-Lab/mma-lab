#!/usr/bin/env python

from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt
import argparse
import feature_extraction as ft

# Initialize the parser object to process commandline arguments
parser = argparse.ArgumentParser(description="Tool to visualize the spectogram alongside the mfcc components of a given wavfile")
parser.add_argument("wav_path", help="Path to wavfile")
parser.add_argument("-n", help="Number of mfcc components that should be visualized", default=13)

args = parser.parse_args()


# Read the wavfile
fs,data = wavfile.read(args.wav_path)

print 'Processing wavfile: ' + args.wav_path + ' ... '

print 'Calculating MFCCs ... '
# extract mfcc coefficents 
ceps, mspec, spec = ft.extract_mfcc(data, fs)

print 'Generating spectogram ... '

# create pyplot figure with custom title 
fig = plt.figure()
title = 'Analysis of ' + args.wav_path
fig.canvas.set_window_title(title) 

# in upper subplot draw the spectogram
plt.subplot(2,1,1)
plt.specgram(data, Fs=fs)
plt.title('Spectogram of raw audio data')
plt.xlabel('time [s]')
plt.ylabel('Frequency [Hz]')

# plot the mfcc coefficients in the lower subplot
plt.subplot(2,1,2)
plt.plot(ceps[:,0:int(args.n)])
plt.title('Mel-cepstrum coefficients per mfcc frame')
plt.xlabel('MFCC frames')
plt.ylabel('Cepstrum amplitude')

# finally show the figure
plt.show()
