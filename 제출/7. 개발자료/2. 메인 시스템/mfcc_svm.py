import numpy as np
import pandas as pd
import os
import librosa
from tqdm import tqdm
import pandas.io.sql as psql
import MySQLdb
from mlxtend.plotting import plot_decision_regions
import matplotlib.pyplot as plt

tqdm.pandas()

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC

class Voice():
    def __init__(self):
        self.__name = ""
        self.__result = 0
        self.clf = None
        self.X_train = None
        self.y_train = None

    def setFileName(self, fileName):
        self.__name = fileName

    def getFileName(self):
        return self.__name

    def getResult(self):
        return self.__result

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
        train_data, feature_names, y = self.__loadData()
        if self.clf is None:
            self.clf, self.X_train, self.y_train = self.__createClassifier(train_data, y)

        #self.__drawGraph()
        voiceFeatures = self.__extractVoiceFeatures()
        voiceFeatures = np.reshape(voiceFeatures, (-1, 13))
        voiceFeatures = pd.DataFrame(data=voiceFeatures, columns=feature_names)

        self.__result = str((self.clf.predict(voiceFeatures) + 1)[0])
        print(self.__result)
        # print("####")
        # ####### gridsearchCV
        # C_grid = [0.0001, 0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]
        # gamma_grid = [0.0001, 0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]
        # param_grid = {'C': C_grid, 'gamma': gamma_grid}
        #
        # X_train, X_val, y_train, y_val = train_test_split(train_data, y, test_size=0.2, random_state=42, shuffle=True)
        #
        # grid = GridSearchCV(SVC(kernel='rbf', C=10.0, gamma=0.001, decision_function_shape='ovo'), param_grid, cv=3, scoring="accuracy")
        # grid.fit(X_train, y_train)
        # print(grid.predict(voiceFeatures))
        # print(accuracy_score(grid.predict(X_val), y_val))
        # # Find the best model
        # print(grid.best_score_)
        # print(grid.best_params_)
        # print(grid.best_estimator_)
        # print("####")
        # ##########
        # clf = SVC(kernel='rbf', C=10, gamma=0.001, decision_function_shape='ovo', probability=True)
        # clf.fit(X_train, y_train)
        # print(accuracy_score(clf.predict(X_val), y_val))
        # print(clf.predict(voiceFeatures))
        # print("####")
        # ##########
        return self.__result

    def __loadData(self):
        HOST = '3.16.43.38'
        USER = 'root'
        PW = '1234'
        DBNAME = 'emotion'

        db = MySQLdb.connect(host = HOST, user = USER, passwd= PW, db=DBNAME)
        query = 'SELECT * FROM sounddata'
        train_data = psql.read_sql(query, con=db)
        db.close()
        X = train_data.drop(['soundNum', 'emotionValue'], axis=1)
        feature_names = list(X.columns)
        X = X.values

        labels = np.sort(np.unique(train_data.emotionValue.values))
        c2i = {}
        for i, c in enumerate(labels):
            c2i[c] = i
        y = np.array([c2i[x] for x in train_data.emotionValue.values])
        return X, feature_names, y

    def saveResult(self):
        print("save")

    def __createClassifier(self, train_data, y):
        X_train, X_val, y_train, y_val = train_test_split(train_data, y, test_size=0.2, random_state=42, shuffle=True)
        clf = SVC(kernel='rbf', C=10.0, gamma=0.001, decision_function_shape='ovo', probability=True)
        clf.fit(X_train, y_train)


        print(accuracy_score(clf.predict(X_val), y_val))
        return clf, X_train, y_train

    def __drawGraph(self):
        value = 1.5
        width = 0.75
        ax = plot_decision_regions(X=self.X_train,
                                   y=self.y_train,
                                   clf=self.clf,
                                   filler_feature_values={2: value, 3: value, 4: value, 5: value, 6: value, 7: value,
                                                          8: value, 9: value, 10: value, 11: value, 12: value},
                                   filler_feature_ranges={2: width, 3: width, 4: width, 5: width, 6: width, 7: width,
                                                          8: width, 9: width, 10: width, 11: width, 12: width},
                                   legend=0)

        # Update plot object with X/Y axis labels and Figure Title
        plt.xlabel('Train Data', size=14)
        plt.ylabel('Emotion Value', size=14)
        plt.title('SVM Decision Region Boundary', size=16)

        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles,
                  ['anger', 'sadness', 'happiness', 'surprise', 'neutral'],
                  framealpha=0.3, scatterpoints=1)

        plt.show()


