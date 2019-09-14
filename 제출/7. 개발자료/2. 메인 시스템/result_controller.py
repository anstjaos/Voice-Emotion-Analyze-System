class ResultController():
    def __init__(self, Voice, ResultView):
        self.__model = Voice
        self.__view = ResultView
        self.__view.saveBtn.clicked.connect(self.saveResult)

    def analyzeEmotion(self):
        result = self.__model.analysisVoice()
        self.__view.updateResultView(result)
        self.__view.displayResultView()

    def saveResult(self):
        self.__view.saveFile(self.__model.getFileName(), self.__model.getResult())