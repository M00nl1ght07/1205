# Импорт функции подулючения к БД из файла create_table
from create_table import connect_to_db
# Импорт библиотеки pandas
import pandas as pd


# Функция заполнения таблицы material_type_import
def filling_table_material_type_import(connection):
    # SQL - запрос заполнения таблицы
    query = 'insert into material_type_import values (%s, %s)'

    try:
        # Инициализация курсора
        cursor = connection.cursor()
        
        # Чтение excel - таблицы
        df = pd.read_excel('excel/Material_type_import.xlsx', engine='openpyxl')
        # Проход по строкам с содержимым
        for row in df.itertuples():
            # Список значений
            values = (row._1, str(round(row._2 * 100, 2)) + '%')

            # Выполнение SQL - запроса со списком данных
            cursor.execute(query, values)
        # Сохранение изменений
        connection.commit()
        # Закрытие курсора
        cursor.close()
        # Информационное сообщение о заполнении
        print("Таблица material_type_import заполнена даннными")
    
    # Обработка ошибок
    except Exception as err:
        print(f"Ошибка при заполнении таблицы material_type_import: {err}")


# Функция заполнения таблицы product_type_import
def filling_table_product_type_import(connection):
    # SQL - запрос заполнения таблицы
    query = 'insert into product_type_import values (%s, %s)'

    try:
        # Инициализация курсора
        cursor = connection.cursor()
        
        # Чтение excel - таблицы
        df = pd.read_excel('excel/Product_type_import.xlsx', engine='openpyxl')
        # Проход по строкам с содержимым
        for row in df.itertuples():
            # Список значений
            values = (row._1, row._2)

            # Выполнение SQL - запроса со списком данных
            cursor.execute(query, values)
        # Сохранение изменений
        connection.commit()
        # Закрытие курсора
        cursor.close()
        # Информационное сообщение о заполнении
        print("Таблица product_type_import заполнена даннными")
    
    # Обработка ошибок
    except Exception as err:
        print(f"Ошибка при заполнении таблицы product_type_import: {err}")


# Функция заполнения таблицы products_import
def filling_table_products_import(connection):
    # SQL - запрос заполнения таблицы
    query = 'insert into products_import values (%s, %s, %s, %s)'

    try:
        # Инициализация курсора
        cursor = connection.cursor()
        
        # Чтение excel - таблицы
        df = pd.read_excel('excel/Products_import.xlsx', engine='openpyxl')
        # Проход по строкам с содержимым
        for row in df.itertuples():
            # Список значений
            values = (row._1, row._2, row.Артикул, row._4)

            # Выполнение SQL - запроса со списком данных
            cursor.execute(query, values)
        # Сохранение изменений
        connection.commit()
        # Закрытие курсора
        cursor.close()
        # Информационное сообщение о заполнении
        print("Таблица products_import заполнена даннными")
    
    # Обработка ошибок
    except Exception as err:
        print(f"Ошибка при заполнении таблицы products_import: {err}")


# Функция заполнения таблицы partners_import
def filling_table_partners_import(connection):
    # SQL - запрос заполнения таблицы
    query = 'insert into partners_import values (%s, %s, %s, %s, %s, %s, %s, %s)'

    try:
        # Инициализация курсора
        cursor = connection.cursor()
        
        # Чтение excel - таблицы
        df = pd.read_excel('excel/Partners_import.xlsx', engine='openpyxl')
        # Проход по строкам с содержимым
        for row in df.itertuples():
            # Список значений
            values = (row._1, row._2, row.Директор, row._4, row._5, row._6, row.ИНН, row.Рейтинг)

            # Выполнение SQL - запроса со списком данных
            cursor.execute(query, values)
        # Сохранение изменений
        connection.commit()
        # Закрытие курсора
        cursor.close()
        # Информационное сообщение о заполнении
        print("Таблица products_import заполнена даннными")
    
    # Обработка ошибок
    except Exception as err:
        print(f"Ошибка при заполнении таблицы products_import: {err}")

# Функция заполнения таблицы partner_products_import
def filling_table_partner_products_import(connection):
    # SQL - запрос заполнения таблицы
    query = 'insert into partner_products_import values (%s, %s, %s, %s)'

    try:
        # Инициализация курсора
        cursor = connection.cursor()
        
        # Чтение excel - таблицы
        df = pd.read_excel('excel/Partner_products_import.xlsx', engine='openpyxl')
        # Проход по строкам с содержимым
        for row in df.itertuples():
            # Список значений
            values = (row.Продукция, row._2, row._3, row._4)

            # Выполнение SQL - запроса со списком данных
            cursor.execute(query, values)
        # Сохранение изменений
        connection.commit()
        # Закрытие курсора
        cursor.close()
        # Информационное сообщение о заполнении
        print("Таблица partner_products_import заполнена даннными")
    
    # Обработка ошибок
    except Exception as err:
        print(f"Ошибка при заполнении таблицы partner_products_import: {err}")



# Вызов функций заполнения таблиц
# filling_table_material_type_import(connect_to_db())
# filling_table_product_type_import(connect_to_db())
# filling_table_products_import(connect_to_db())
# filling_table_partners_import(connect_to_db())
# filling_table_partner_products_import(connect_to_db())