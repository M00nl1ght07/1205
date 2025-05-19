from PySide6.QtWidgets import *
from frames import partner_frame
from send_message_box import *

class AddPartnerInfo(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.db = controller.db
        self.setup_ui()

    def setup_ui(self):
        '''
        Создание интерфейса добавления партнера
        '''
        self.layout = QVBoxLayout(self)
        
        # Заголовок
        title = QLabel('Добавление партнера')
        title.setObjectName("title_frame")
        self.layout.addWidget(title)

        # Поля ввода
        self.create_input_fields()
        
        # Кнопки
        self.create_buttons()

    def create_input_fields(self):
        '''
        Создание полей ввода
        '''
        # Тип партнера
        self.partner_type = QComboBox()
        self.partner_type.addItems(["ЗАО", "ООО", "ПАО", "ОАО"])
        self.add_field("Тип:", self.partner_type)
        
        # Остальные поля
        self.partner_name = self.add_field("Наименование:", 
                                         QLineEdit(), "Строй - Построй")
        
        self.partner_direktor = self.add_field("Директор:", 
                                             QLineEdit(), "Иванов Иван Иванович")
        
        self.partner_email = self.add_field("Email:", 
                                          QLineEdit(), "stroy@postroy.com")
        
        self.partner_phone = self.add_field("Телефон:", 
                                          QLineEdit(), "+7 000 000 00 00")
        self.partner_phone.setInputMask('+7 000 000 00 00')
        
        self.partner_address = self.add_field("Адрес:", 
                                            QLineEdit(), 
                                            "123456, Россия, Москва, ул. Пушкина, д. 39")
        
        self.partner_rate = self.add_field("Рейтинг:", 
                                         QLineEdit(), "10", 2)
        
        self.partner_inn = self.add_field("ИНН:", 
                                        QLineEdit(), "3746388791", 10)

    def create_buttons(self):
        '''
        Создание кнопок
        '''
        add_btn = QPushButton("Добавить")
        add_btn.clicked.connect(self.add_partner)
        self.layout.addWidget(add_btn)

        back_btn = QPushButton("Назад")
        back_btn.clicked.connect(lambda: self.controller.switch_frame(partner_frame.PartnerFrame))
        self.layout.addWidget(back_btn)

    def add_field(self, label_text, widget, placeholder="", max_length=None):
        '''
        Добавление поля ввода с меткой
        '''
        label = QLabel(label_text)
        label.setObjectName("text_hint")
        self.layout.addWidget(label)
        
        if isinstance(widget, QLineEdit):
            widget.setPlaceholderText(placeholder)
            if max_length:
                widget.setMaxLength(max_length)
        
        self.layout.addWidget(widget)
        return widget

    def add_partner(self):
        '''
        Добавление партнера в БД
        '''
        partner_info = {
            "type_of_partner": self.partner_type.currentText(),
            "name_of_partner": self.partner_name.text(),
            "name_of_director": self.partner_direktor.text(),
            "email_of_partner": self.partner_email.text(),
            "phone_of_partner": self.partner_phone.text()[3:],
            "addr_of_partner": self.partner_address.text(),
            "inn": self.partner_inn.text(),
            "rate": self.partner_rate.text()
        }
        
        if send_W_message("Проверьте введенные данные!") < 20000:
            if self.db.add_partner_info(partner_info):
                send_I_message("Партнер успешно добавлен!")
                self.controller.switch_frame(partner_frame.PartnerFrame)
        else:
            send_C_message("Данные не были добавлены!")
