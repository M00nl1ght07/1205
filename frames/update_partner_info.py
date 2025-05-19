from PySide6.QtWidgets import *
from partner_static_name import PartnerStaticName
from frames import partner_frame
from send_message_box import *

class UpdatePartnerInfo(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.db = controller.db
        self.partner_name = PartnerStaticName.get_partner_name()
        self.partner_info = self.db.take_partner_info(self.partner_name)
        
        if not self.partner_info:
            send_C_message(f"Партнер {self.partner_name} не найден")
            self.controller.switch_frame(partner_frame.PartnerFrame)
            return
            
        self.setup_ui()

    def setup_ui(self):
        '''
        Создание интерфейса редактирования
        '''
        self.layout = QVBoxLayout(self)
        
        # Заголовок
        title = QLabel(f'Редактирование партнера {self.partner_name}')
        title.setObjectName("title_frame")
        self.layout.addWidget(title)

        # Поля ввода
        self.create_input_fields()
        
        # Кнопки
        self.create_buttons()

    def create_input_fields(self):
        """
        Создание полей ввода
        """
        # Тип партнера
        self.partner_type = QComboBox()
        self.partner_type.addItems(["ЗАО", "ООО", "ПАО", "ОАО"])
        self.partner_type.setCurrentText(self.partner_info['type_of_partner'].strip())
        self.add_field("Тип:", self.partner_type)
        
        # Остальные поля
        self.partner_name_edit = self.add_field("Наименование:", 
                                              QLineEdit(), 
                                              self.partner_info['name_of_partner'])
        
        self.partner_direktor = self.add_field("Директор:", 
                                             QLineEdit(), 
                                             self.partner_info['name_of_director'])
        
        self.partner_email = self.add_field("Email:", 
                                          QLineEdit(), 
                                          self.partner_info['email_of_partner'])
        
        self.partner_phone = self.add_field("Телефон:", 
                                          QLineEdit(), 
                                          "+7" + self.partner_info['phone_of_partner'])
        self.partner_phone.setInputMask('+7 000 000 00 00')
        
        self.partner_address = self.add_field("Адрес:", 
                                            QLineEdit(), 
                                            self.partner_info['addr_of_partner'])
        
        self.partner_inn = self.add_field("ИНН:", 
                                        QLineEdit(), 
                                        self.partner_info['inn'], 10)
        
        self.partner_rate = self.add_field("Рейтинг:", 
                                         QLineEdit(), 
                                         self.partner_info['rate'], 2)

    def create_buttons(self):
        """
        Создание кнопок
        """
        update_btn = QPushButton("Обновить")
        update_btn.clicked.connect(self.update_partner)
        self.layout.addWidget(update_btn)

        back_btn = QPushButton("Назад")
        back_btn.clicked.connect(lambda: self.controller.switch_frame(partner_frame.PartnerFrame))
        self.layout.addWidget(back_btn)

    def add_field(self, label_text, widget, text="", max_length=None):
        """
        Добавление поля ввода с меткой
        
        :param label_text: Текст метки
        :param widget: Поле ввода данных
        :param text: Текст по умолчанию
        :param max_length: Максимальная длина текста
        :return: Поле ввода данных
        """
        label = QLabel(label_text)
        label.setObjectName("text_hint")
        self.layout.addWidget(label)
        
        if isinstance(widget, QLineEdit):
            widget.setText(str(text))
            if max_length:
                widget.setMaxLength(max_length)
        
        self.layout.addWidget(widget)
        return widget

    def update_partner(self):
        """
        Обновление информации о партнере
        """
        partner_info = {
            "type_of_partner": self.partner_type.currentText(),
            "name_of_partner": self.partner_name_edit.text(),
            "name_of_director": self.partner_direktor.text(),
            "email_of_partner": self.partner_email.text(),
            "phone_of_partner": self.partner_phone.text()[3:],
            "addr_of_partner": self.partner_address.text(),
            "inn": self.partner_inn.text(),
            "rate": self.partner_rate.text()
        }
        
        if send_W_message("Проверьте введенные данные!") < 20000:
            if self.db.update_partner_info(self.partner_name, partner_info):
                send_I_message("Данные успешно обновлены!")
                self.controller.switch_frame(partner_frame.PartnerFrame)
        else:
            send_C_message("Данные не были обновлены!")
