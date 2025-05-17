from database.create_table import connect_to_db

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

