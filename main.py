from algo import countEquelsWords
import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QTextEdit, QPushButton
from datetime import datetime

app = QApplication([])
window = QWidget()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 640
INPUT_HEIGHT = 450
TOP_PADDING = 20
TOP_PADDING_INPUT = 50
TOP_PADDING_BTN = TOP_PADDING + TOP_PADDING_INPUT + INPUT_HEIGHT + 30
SCREEN_SIZE = window.screen().size()

textEditInput = QTextEdit(parent=window)
textEditOutput = QTextEdit(parent=window)
btnCalc = QPushButton('Поиск', parent=window)
helloMsg = QLabel('<h1>Слова</h1>', parent=window)

window.setWindowTitle('Repeat Word')
window.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)

helloMsg.move(int((WINDOW_WIDTH - helloMsg.fontMetrics().boundingRect(helloMsg.text()).width()) / 2), TOP_PADDING)
textEditInput.setFixedSize(int(WINDOW_WIDTH / 2), INPUT_HEIGHT)
textEditOutput.setFixedSize(int(WINDOW_WIDTH / 2), INPUT_HEIGHT)
textEditOutput.setReadOnly(True)
textEditInput.move(0, TOP_PADDING + TOP_PADDING_INPUT)
textEditOutput.move(int(WINDOW_WIDTH / 2), TOP_PADDING + TOP_PADDING_INPUT)
btnCalc.move(int((WINDOW_WIDTH - btnCalc.width()) / 2), TOP_PADDING_BTN)

def onClick():
  start_time = datetime.now()
  inputText = textEditInput.toPlainText()
  outputText = countEquelsWords(inputText)
  textEditOutput.setText(outputText)
  print('Время работы: ', datetime.now() - start_time)

btnCalc.clicked.connect(onClick)

window.show()
sys.exit(app.exec())