from PySide6.QtWidgets import *
from PySide6.QtGui import QPixmap

class PartnerFrame(QWidget):
    def __init__(self, controller):
        super().__init__()

        self.controller = controller
        self.db = controller.db
        self.layout = QVBoxLayout(self)
        self.setup_ui()
        
    
    def setup_ui(self):

        title = QLabel("Партнеры")
        self.layout.addWidget(title)

        icon = QLabel()
        icon.setPixmap(QPixmap("res/icon.png"))
        icon.setScaledContents(True)
        icon.setFixedSize(100, 100)

        icon_layout = QHBoxLayout()
        icon_layout.addStretch()
        icon_layout.addWidget(icon)
        icon_layout.addStretch()

        self.layout.addLayout(icon_layout)

        self.partner()

    
    def partner(self):
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        cards = QWidget()
        cards_layout = QVBoxLayout(cards)

        for partner in self.db.take_all_partner_info():
            card = QWidget()
            card_layout = QVBoxLayout(card)

            header = QHBoxLayout()
            title1 = QLabel(f'{partner["type_of_partner"]} | {partner["name_of_partner"]}')
            title_discount = QLabel(f'{self.discount_calculate(partner["name_of_partner"])}%')

            header.addWidget(title1)
            header.addWidget(title_discount)

            card_layout.addLayout(header)

            title2 = QLabel(f'{partner["name_of_director"]}')
            title3 = QLabel(f'+7 {partner["phone_of_partner"]}')
            title4 = QLabel(f'Рейтинг: {partner["rate"]}')

            card_layout.addWidget(title2)
            card_layout.addWidget(title3)
            card_layout.addWidget(title4)

            cards_layout.addWidget(card)
        scroll.setWidget(cards)
        self.layout.addWidget(scroll)
    
    def discount_calculate(self, partner):
        quantity = self.db.take_quantity_partner(partner)
        if quantity > 300000:
            return 15
        elif quantity > 50000:
            return 10
        elif quantity > 10000:
            return 5
        else:
            return 0