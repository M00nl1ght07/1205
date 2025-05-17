from PySide6.QtWidgets import *
from PySide6.QtGui import QPixmap
from frames import donestart
from database import db
import sys

class MainApplication(QWidget):
    def __init__(self):
        super().__init__()

        self.db = db.Database()

        self.resize(1280, 720)
        self.setWindowTitle("Мастер Пол")
        self.setWindowIcon(QPixmap("res/icon.png"))

        frames_container = QStackedWidget()
        frame_start = donestart.PartnerFrame(self)
        frames_container.addWidget(frame_start)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(frames_container)

style = '''
    #title_main {
        font-size: 24px;
        font-weight: 500;
        qproperty-alignment: AlignCenter;
    }

    #card {
        border: 1px solid black;
        background: #F4E8D3;
    }

    #title_header {
        font-size: 20px;
        font-weight: 500;
        margin-left: 20px;
    }

    #title_right {
        font-size: 20px;
        font-weight: 500;
        margin-right: 20px;
        qproperty-alignment: AlignRight;
    }

    #subtitle {
        font-size: 18px;
        margin-left: 20px;
    }
'''

app = QApplication(sys.argv)
main_class = MainApplication()
app.setFont("Segou UI")
app.setStyleSheet(style)
main_class.show()
app.exec()