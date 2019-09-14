import threading
import time
import subprocess
from tkinter import *
from pygame import mixer
from mutagen.mp3 import MP3
import pyaudio
import wave
import os
from result_controller import ResultController
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from result_view import ResultView

mixer.init()
paused = False
playing = False
recording = True
saveFinished = False

class MainController(QObject):
    progressChanged = QtCore.pyqtSignal(int)

    def __init__(self, Voice, MainView, parent=None):
        super(QObject, self).__init__(parent)
        self.__view = MainView
        self.__model = Voice
        self.__view.loadFileBtn.clicked.connect(self.loadFile)
        self.threadpool = QtCore.QThreadPool()
        self.__view.playBtn.clicked.connect(self.playVoice)
        self.progressChanged.connect(self.__view.soundPgBar.setValue)
        self.__view.stopBtn.clicked.connect(self.stopVoice)
        self.__view.recordBtn.clicked.connect(self.recordVoice)
        self.__view.emotionAnalyzeBtn.clicked.connect(self.analyzeEmotion)
        self.__view.volumeSlider.valueChanged.connect(self.changeVolume)

    def __extractMp3(self, parentDir, fileName):
        subprocess.call(['ffmpeg', '-y', '-i',
                         os.path.join(parentDir, fileName),
                         os.path.join(parentDir, fileName + ".mp3")
                         ])

    def loadFile(self):
        parentDir, fileName = self.__view.loadFile()
        if fileName == "":
            return

        length = len(fileName)
        dir = ""
        if fileName[length-1] == "4":
            self.__extractMp3(parentDir, fileName)
            dir = parentDir + "/" + fileName + ".mp3"
        else:
            dir = parentDir + "/" + fileName

        self.__model.setFileName(dir)
        mixer.music.load(dir)

    def playVoice(self):
        global paused
        fileName = self.__model.getFileName()
        if fileName == "":
            self.__view.showMessage("파일을 선택해주세요")
            return
        if playing:
            return

        file_data = os.path.splitext(fileName)
        if file_data[1] == ".mp3":
            total_length = MP3(fileName).info.length
        else:
            total_length = mixer.Sound(fileName).get_length()

        self.worker = Worker(self.__startCount, total_length, parent=self)

        if paused:
            mixer.music.unpause()
            paused = False
            self.threadpool.start(self.worker)
        else:
            mixer.music.stop()
            mixer.music.play()
            self.threadpool.start(self.worker)

    def __startCount(self, t):
        global paused
        global playing
        # mixer.music.get_busy(): - Returns FALSE when we press the stop button (music stop playing)
        # Continue - Ignores all of the statements below it. We check if music is paused or not.
        current_time = 0
        playing = True
        while current_time <= t and mixer.music.get_busy():
            if paused:
                break
            else:
                self.progressChanged.emit((mixer.music.get_pos() / 1000) / t * 100)
                time.sleep(1)
                current_time += 1
        if paused == False:
            self.progressChanged.emit(100)
        playing = False

    def stopVoice(self):
        global paused
        global playing

        if playing == False:
            return

        paused = True
        mixer.music.pause()

    def recordVoice(self):
        text = self.__view.recordBtn.text()
        global recording
        global saveFinished

        if text == "음성 녹음":
            self.__view.updateRecordBtnText("녹음 정지")
            recording = True
            t1 = threading.Thread(target=self.__startRecord)
            t1.start()
            t2 = threading.Thread(target=self.__countRecord)
            t2.start()
        else:
            recording = False
            mixer.music.load("0.mp3")
            self.__view.updateRecordBtnText("음성 녹음")
            while saveFinished == False:
                pass

            dir = "D://pyproject/file.wav"
            self.__model.setFileName(dir)
            mixer.music.load(dir)
            saveFinished = False

    def __countRecord(self):
        global recording
        current_time = 0

        while recording:
            mins, secs = divmod(current_time, 60)
            mins = round(mins)
            secs = round(secs)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            self.__view.updateRecordTimeLabelText("Current Time" + ' - ' + timeformat)
            time.sleep(1)
            current_time += 1

    def __startRecord(self):
        global recording
        global saveFinished

        po = pyaudio.PyAudio()
        # 1 마이크
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100
        CHUNK = 1024
        RECORD_SECONDS = 10
        WAVE_OUTPUT_FILENAME = "file.wav"
        stream = po.open(format=pyaudio.paInt16,
                         channels=CHANNELS,
                         rate=RATE,
                         input=True,
                         input_device_index=1,
                         frames_per_buffer=CHUNK)

        frames = []
        while True:
            if recording:
                data = stream.read(CHUNK)
                frames.append(data)
            else:
                stream.stop_stream()
                stream.close()
                po.terminate()

                waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
                waveFile.setnchannels(CHANNELS)
                waveFile.setsampwidth(po.get_sample_size(FORMAT))
                waveFile.setframerate(RATE)
                waveFile.writeframes(b''.join(frames))
                waveFile.close()
                saveFinished = True
                break

    def changeVolume(self):
        volume = float(self.__view.volumeSlider.value())
        volume = volume / 100
        mixer.music.set_volume(volume)


    def analyzeEmotion(self):
        if self.__model.getFileName() == "":
            self.__view.showMessage("파일을 선택해주세요")
            return

        Dialog = QtWidgets.QDialog()
        resultView = ResultView(Dialog)
        resultView.setupUi(resultView.dialog)
        resultController = ResultController(self.__model, resultView)
        resultController.analyzeEmotion()

class Worker(QRunnable):

    def __init__(self, fn, totalLength, parent=None):
        super(Worker, self).__init__()
        self.fn = fn
        self.totalLength = totalLength

    @pyqtSlot()
    def run(self):
        self.fn(self.totalLength)