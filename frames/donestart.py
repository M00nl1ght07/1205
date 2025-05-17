from PySide6.QtWidgets import * 
from PySide6.QtGui import *

class PartnerFrame(QWidget):
    def __init__(self, controller):
        super().__init__()
        
        self.controller = controller
        self.db = controller.db

        self.setup_ui()
    
    def setup_ui(self):
        self.layout = QVBoxLayout(self)

        title = QLabel("Мастер Пол")
        title.setObjectName("title_main")
        self.layout.addWidget(title)
        
        icon = QLabel()
        icon.setPixmap(QPixmap("res/icon.png"))
        icon.setFixedSize(100, 100)
        icon.setScaledContents(True)

        icon_layout = QHBoxLayout()
        icon_layout.addStretch()
        icon_layout.addWidget(icon)
        icon_layout.addStretch()

        self.layout.addLayout(icon_layout)
        
        self.create_partners()
    
    def create_partners(self):
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        cards = QWidget()
        cards_layout = QVBoxLayout(cards)

        for partner in self.db.take_all_partner_info():
            card = QWidget()
            card.setObjectName("card")
            card_layout = QVBoxLayout(card)

            header = QHBoxLayout()
            title_type_and_name = QLabel(f'{partner["type_of_partner"]} | {partner["name_of_partner"]}')
            title_type_and_name.setObjectName("title_header")

            title_discount = QLabel(f'{self.discount_calculate(partner['name_of_partner'])}%')
            title_discount.setObjectName("title_right")

            header.addWidget(title_type_and_name)
            header.addWidget(title_discount)

            card_layout.addLayout(header)

            title_director = QLabel(f'Директор: {partner["name_of_director"]}')
            title_director.setObjectName("subtitle")

            title_phone_number = QLabel(f'+7 {partner["phone_of_partner"]}')
            title_phone_number.setObjectName("subtitle")

            title_rate = QLabel(f'Рейтинг: {partner["rate"]}')
            title_rate.setObjectName("subtitle")

            card_layout.addWidget(title_director)
            card_layout.addWidget(title_phone_number)
            card_layout.addWidget(title_rate)
            
            cards_layout.addWidget(card)

        scroll.setWidget(cards)
        self.layout.addWidget(scroll)
    

    def discount_calculate(self, partner):
        sum_quantity = self.db.take_quantity_partner(partner)
        # Возврат из функции % скидки
        if sum_quantity > 300000:
            return 15
        
        elif sum_quantity > 50000:
            return 10
        
        elif sum_quantity > 10000:
            return 5
        
        else:
            return 0