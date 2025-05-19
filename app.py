from PySide6.QtWidgets import *
from PySide6.QtGui import QPixmap
from frames import partner_frame
from partner_static_name import PartnerStaticName
from database import db
import sys

class MainApplication(QWidget):
    def __init__(self):
        super().__init__()

        self.db = db.Database()

        self.resize(1280, 720)
        self.setWindowTitle("Мастер Пол")
        self.setWindowIcon(QPixmap("res/icon.png"))

        self.frames_container = QStackedWidget()
        frame_start = partner_frame.PartnerFrame(self)
        self.frames_container.addWidget(frame_start)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.frames_container)

    def switch_frame(self, frame_new, partner_name = None):
        if partner_name != None:
            PartnerStaticName.set_partner_name(partner_name)

        new_frame = frame_new(controller = self)
        self.frames_container.addWidget(new_frame)
        self.frames_container.setCurrentWidget(new_frame)

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
    
    QPushButton{
        background: #67BA80;
    }
'''

app = QApplication(sys.argv)
main_class = MainApplication()
app.setFont("Segou UI")
app.setStyleSheet(style)
main_class.show()
app.exec()