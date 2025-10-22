# UI에서 입력되는 이벤트 처리나 UI 동작 제어와 관련된 내용 포함.
class Control:
    def __init__(self, view):
        self.view = view
        self.connectSignals()

    def calculate(self):
        pass

    def connectSignals(self):
        self.view.btn1.clicked.connect(self.view.activateMessage)
        self.view.btn2.clicked.connect(self.view.clearMessage)

    def sum(self, a, b):
        return a+b
