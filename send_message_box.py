from PySide6.QtWidgets import QMessageBox


# Информационное сообщение
def send_I_message(message_text: str):
    message = QMessageBox()
    message.setText(message_text)
    message.setIcon(QMessageBox.Icon.Information)
    message.setStandardButtons(QMessageBox.StandardButton.Yes)
    return message.exec()


# Предупреждающее сообщение
def send_W_message(message_text: str):
    message = QMessageBox()
    message.setText(message_text)
    message.setIcon(QMessageBox.Icon.Warning)
    message.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
    return message.exec()


# Запрещающее сообщение
def send_C_message(message_text: str):
    message = QMessageBox()
    message.setText(message_text)
    message.setIcon(QMessageBox.Icon.Critical)
    message.setStandardButtons(QMessageBox.StandardButton.Yes)
    return message.exec()