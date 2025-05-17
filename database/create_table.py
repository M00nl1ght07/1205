# Импорт библиотеки для подключения к СУБД postgresql
import psycopg
# Импорт конфигурационного файла
from database.config import *

# Функция подключения к БД
def connect_to_db():
    # Создание подключения
    try:
        connection = psycopg.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            dbname=DBNAME,
            port=PORT
        )
        # Если есть подключение - возвращаем подключение
        if connection:
            print(f"Подключение к БД: {DBNAME} успешно")
            return connection
        else:
            # Возврат ничего в случае не успешного подключения
            print(f"Подключение к БД: {DBNAME} не успешно")
            return None
    # Обработка ошибок при подключении к БД
    except Exception as err:
        print(f"Ошибка подключения к базе данных: {err}")
        return None
    
# Функция создания таблиц в БД на основе представленных excel-файлов
def create_table_in_database(connection):
    # SQL-запрос для создания таблиц в БД
    query_create_table_in_database = '''
        -- Создание таблицы material_type_import
        CREATE TABLE material_type_import (
            type_of_material text primary key,
            percent_of_broke text not null
        );

        -- Создание таблицы product_type_import
        CREATE TABLE product_type_import (
            type_of_production text primary key,
            coef_type_of_production real not null
        );

        -- Создание таблицы products_import
        CREATE TABLE products_import (
            type_of_production_fk text not null,
            foreign key (type_of_production_fk) references product_type_import(type_of_production) on update cascade,
            name_of_production text primary key,
            acrticle_of_production text not null,
            min_cost_of_partner real not null
        );

        -- Создание таблицы partners_import
        CREATE TABLE partners_import(
            type_of_partner text not null,
            name_of_partner text primary key,
            name_of_director text not null,
            email_of_partner text not null,
            phone_of_partner text not null,
            addr_of_partner text not null,
            inn text not null,
            rate integer not null
        );

        -- Создание таблицы partner_products_import
        CREATE TABLE partner_products_import(
            name_of_production_fk text not null,
            foreign key (name_of_production_fk) references products_import(name_of_production) on update cascade,
            name_of_partner_fk text not null,
            foreign key (name_of_partner_fk) references partners_import(name_of_partner) on update cascade,
            quantity_of_production integer not null,
            date_of_sell date not null
        )
    '''
    try:
        # Инициализация курсора для подключения к БД
        cursor = connection.cursor()
        cursor.execute(query_create_table_in_database)
        connection.commit()
        cursor.close()
        print("В БД созданы таблицы")
    
    except Exception as err:
        print(f"Ошибка при создании таблиц {err}")

# Вызов функции для создания таблиц в БД
# create_table_in_database(connect_to_db())