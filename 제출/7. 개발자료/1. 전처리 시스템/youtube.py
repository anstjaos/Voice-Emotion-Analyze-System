import os
import subprocess
import copy
import cv2
import sys
import librosa
import requests
import json
import pymysql
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import uic
from tkinter import filedialog
from tkinter import *
import pytube
from video_window import Ui_Dialog

form_class = uic.loadUiType("main.ui")[0]
subscription_key = 'b1d8936629204f49ac42c433869fd90d'
assert subscription_key

class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super(__class__, self).__init__()
        self.setupUi(self)
        self.file_name = "0"
        self.parent_dir = "D:/asdf/DATASET"

    def insert_db(self):
        self.extract_mp3()
        #self.video_capture()
        if self.file_name == "":
            return

        mfcc = self.extract_feature()
        #print(self.file_name)
        #emotion = self.get_emotion()
        emotion = self.file_name[0]
        self.insert_sound_features(emotion, mfcc)

    def extract_mp3(self):
        print(self.parent_dir)
        print(self.file_name)
        subprocess.call(['ffmpeg', '-y', '-i',
                         os.path.join(self.parent_dir, self.file_name),
                         os.path.join(self.parent_dir, self.file_name + ".mp3")
                         ])

    def openFile(self):
        root = Tk()
        root.filename = filedialog.askopenfilename(initialdir="D:\\asdf\\DATASET", title="choose your file",
                                                   filetypes=[("mp4 files", "*.mp4"), ("all files", "*.*")])

        fn = root.filename.split('/')
        fn.reverse()

        dir = ""
        for i in range(len(fn)-1, 0, -1):
            dir += fn[i]
            if i != 1:
                dir += "/"

        self.parent_dir = copy.deepcopy(dir)
        self.file_name = copy.deepcopy(fn[0])
        self.insert_db()
        root.destroy()

    def clicked(self):
        link = self.urlTxt.toPlainText()
        yt = pytube.YouTube(link)

        vids = yt.streams.all()

        vnum = int(0)

        vids[vnum].download(self.parent_dir)

        default_filename = vids[vnum].default_filename
        self.file_name = default_filename
        self.insert_db()

    def video_capture(self):
        flag = False
        while flag == False:
            cap = cv2.VideoCapture(self.file_name)
            while (True):
                if cap.isOpened() == False:
                    flag = True
                    break

                ret, frame = cap.read()
                cv2.imshow('frame', frame)

                if cv2.waitKey(25) & 0xFF == ord('q'):
                    cv2.imwrite("0.jpg", frame)
                    flag = True
                    break

            if flag == True:
                cap.release()
                cv2.destroyAllWindows()
                break

    def extract_feature(self):
        y, sr = librosa.load(self.parent_dir + '/' + self.file_name)
        S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128, fmax = 8000)
        mfcc = librosa.feature.mfcc(y=y, sr=sr, S=librosa.power_to_db(S), n_mfcc=13)
        print(mfcc)
        res_arr = []

        for i in range(0,13):
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
        print(res_arr)
        return res_arr

    def get_emotion(self):
        face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'

        headers = {'Content-Type': 'application/octet-stream', 'Ocp-Apim-Subscription-Key': subscription_key}

        data = open('D:\\asdf\\0.jpg', 'rb')

        params = {
            'returnFaceId': 'true',
            'returnFaceLandmarks': 'false',
            'returnFaceAttributes': 'emotion',
        }

        response = requests.post(face_api_url, params=params, headers=headers, data=data)
        json_data = json.dumps(response.json())
        json_data = json.loads(json_data)
        print(json_data)
        emotion_data = json_data[0]["faceAttributes"]["emotion"]
        print(emotion_data)

        result = 0.0
        emotion = 0
        if result < float(emotion_data["anger"]):
            emotion = 1
            result = float(emotion_data["anger"])

        if result < float(emotion_data["sadness"]):
            emotion = 2
            result = float(emotion_data["sadness"])

        if result < float(emotion_data["happiness"]):
            emotion = 3
            result = float(emotion_data["happiness"])

        if result < float(emotion_data["surprise"]):
            emotion = 4
            result = float(emotion_data["surprise"])

        if result < float(emotion_data["neutral"]):
            emotion = 5
            result = float(emotion_data["neutral"])

        print(emotion)
        return emotion

    # MySQL
    def db_query(self, sql, params):
        # Connect to MySQL
        pymysql.converters.encoders[np.float64] = pymysql.converters.escape_float
        pymysql.converters.conversions = pymysql.converters.encoders.copy()
        pymysql.converters.conversions.update(pymysql.converters.decoders)

        conn = pymysql.connect(
            host='3.16.43.38',
            user='root',
            password='1234',
            charset='utf8',
            db='emotion'
        )
        id = 0
        try:
            # create Dictionary Cursor
            with conn.cursor() as cursor:
                sql_query = sql
                # excute SQL
                cursor.execute(sql_query, params)
            # commit data
            conn.commit()
            id = cursor.lastrowid
        finally:
            conn.close()

        return id

    def insert_sound_features(self, emotion, mfcc):
        sql = 'INSERT INTO sounddata (emotionValue, value1, value2, value3, value4, value5, value6,' \
              'value7, value8, value9, value10, value11, value12, value13) ' \
              'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

        params = (emotion, mfcc[0], mfcc[1], mfcc[2], mfcc[3], mfcc[4], mfcc[5], mfcc[6], mfcc[7], mfcc[8], mfcc[9], mfcc[10], mfcc[11], mfcc[12])
        self.db_query(sql=sql, params=params)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoForm()
    demoWindow.show()
    app.exec_()
