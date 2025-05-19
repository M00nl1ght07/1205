# Функции проверки данных в начале файла
def check_org_name(partner_name: str) -> bool:
    if not partner_name:
        print("Введите корректное имя партнера!")
        return False
    return True

def check_dir_name(director: str) -> bool:
    if len(director.split()) != 3:
        print("Введите ФИО директора по виду Фамилия Имя Отчество!")
        return False
    return True

def check_rate(rate: int) -> bool:
    if not 1 <= rate <= 10:
        print("Рейтинг партнера от 1 до 10!")
        return False
    return True

def check_phone(phone_number: str) -> bool:
    if len(phone_number) != 13:
        print("Введите корректный номер телефона!")
        return False
    return True

def check_mail(email: str) -> bool:
    if "@" not in email or "." not in email:
        print("Введите корректный адрес электронной почты!")
        return False
    return True

def check_inn(inn: str) -> bool:
    if not inn.isdigit() or len(inn) != 10:
        print("Введите корректный ИНН из 10 цифр!")
        return False
    return True

def check_ur_addr(ur_addr: str) -> bool:
    parts = ur_addr.split(",")
    if len(parts) <= 2 or len(parts[0]) != 6 or not parts[0].isdigit():
        print("Введите корректный юридический адрес (индекс, город, улица, дом)")
        return False
    return True

def start_check(partners_data: dict) -> bool:
    return all([
        check_inn(partners_data['inn']),
        check_mail(partners_data['email_of_partner']),
        check_rate(int(partners_data['rate'])),
        check_phone(partners_data['phone_of_partner']),
        check_org_name(partners_data['name_of_partner']),
        check_dir_name(partners_data['name_of_director']),
        check_ur_addr(partners_data['addr_of_partner'])
    ])