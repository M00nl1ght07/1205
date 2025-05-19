from database.create_table import connect_to_db
from database.check_input_data import start_check

class Database():
    def __init__(self):
        self.connection = connect_to_db()
    
    def take_all_partner_info(self):
        query = 'select * from partners_import'
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)

            partners_data = []

            for row in cursor.fetchall():
                partners_data.append({
                    "type_of_partner":row[0],
                    "name_of_partner":row[1],
                    "name_of_director":row[2],
                    "email_of_partner":row[3],
                    "phone_of_partner":row[4],
                    "addr_of_partner":row[5],
                    "inn":row[6],
                    "rate":row[7]
                })
                cursor.close()
            return partners_data
        
        except Exception as err:
            print(err)
            return []
    
    def take_quantity_partner(self, partner):
        query = f'''
            select sum(quantity_of_production)
            from partner_products_import
            where name_of_partner_fk = '{partner}'
        '''
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            quantity_of_prod = cursor.fetchone()[0] or 0
            return quantity_of_prod
        except Exception as err:
            print(err)
            return 0


    def take_partner_info(self, partner_name: str):
        try:
            cursor = self.connection.cursor()
            cursor.execute(f'''
                SELECT * FROM partners_import
                WHERE name_of_partner = '{partner_name}'
            ''')
            data = cursor.fetchone()
            if data:
                return {
                    'type_of_partner': data[0],
                    'name_of_partner': data[1],
                    'name_of_director': data[2],
                    'email_of_partner': data[3],
                    'phone_of_partner': data[4],
                    'addr_of_partner': data[5],
                    'inn': data[6],
                    'rate': data[7]
                }
            return {}
        except Exception as error:
            print(f'Ошибка: {error}')
            return {}

    def update_partner_info(self, partner_name: str, partner_info: dict):
        try:
            if not start_check(partner_info):
                return False
                
            cursor = self.connection.cursor()
            cursor.execute(f'''
                UPDATE partners_import SET
                name_of_partner = '{partner_info["name_of_partner"]}',
                name_of_director = '{partner_info["name_of_director"]}',
                email_of_partner = '{partner_info["email_of_partner"]}',
                phone_of_partner = '{partner_info["phone_of_partner"]}',
                addr_of_partner = '{partner_info["addr_of_partner"]}',
                inn = '{partner_info["inn"]}',
                rate = '{partner_info["rate"]}'
                WHERE name_of_partner = '{partner_name}'
            ''')
            self.connection.commit()
            cursor.close()
            return True
        except Exception as error:
            print(f'Ошибка: {error}')
            return False

    def add_partner_info(self, partner_info: dict):
        try:
            if not start_check(partner_info):
                return False
                
            cursor = self.connection.cursor()
            cursor.execute('''
                INSERT INTO partners_import (
                    type_of_partner, name_of_partner, name_of_director,
                    email_of_partner, phone_of_partner, addr_of_partner,
                    inn, rate
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ''', (
                partner_info["type_of_partner"],
                partner_info["name_of_partner"],
                partner_info["name_of_director"],
                partner_info["email_of_partner"],
                partner_info["phone_of_partner"],
                partner_info["addr_of_partner"],
                partner_info["inn"],
                partner_info["rate"]
            ))
            self.connection.commit()
            cursor.close()
            return True
        except Exception as error:
            print(f'Ошибка: {error}')
            return False