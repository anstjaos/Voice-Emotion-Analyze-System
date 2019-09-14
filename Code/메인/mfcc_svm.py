import numpy as np
import pandas as pd
import os
import librosa
import scipy
from scipy.stats import skew
#from tqdm import tqdm, tqdm_pandas

#tqdm.pandas()

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

from sklearn.svm import SVC

class Voice():
    def __init__(self):
        self.__name = ""
        self.__result = 0

    def setFileName(self, fileName):
        self.__name = fileName

    def getFileName(self):
        return self.__name

    def __extractVoiceFeatures(self):
        y, sr = librosa.load(self.__name)
        s = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128, fmax=8000)
        mfcc = librosa.feature.mfcc(y=y, sr=sr, S=librosa.power_to_db(s), n_mfcc=13)

        res_arr = []
        for i in range(0, 13):
            mean = np.mean(mfcc[i])
            std = np.std(mfcc[i])
            sum = 0.0
            cnt = 0.0
            for j in range(len(mfcc[i])):
                val = mfcc[i][j]
                if (val >= (mean - 2*std)) and (val <= (mean + 2*std)):
                    sum += val
                    cnt += 1.0
            res_arr.append(sum / cnt)
        return res_arr

    def analysisVoice(self):
        result = str(0)
        voiceFeatures = self.__extractVoiceFeatures()
        #
        #
        #
        return result

    def __loadData(self):
        print("check")

    def saveResult(self):
        print("save")

    def __createClassifier(self):
        print("asdf")


