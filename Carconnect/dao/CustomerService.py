from dao.ICustomerService import ICustomerService
from entity.Customer import Customer
from util.DBConnUtil import get_connection

class CustomerService(ICustomerService):

    def get_customer_by_id(self, customer_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Customer WHERE CustomerID = %s", (customer_id,))
            result = cursor.fetchone()
            if result:
                return Customer(*result)
            else:
                return None
        finally:
            cursor.close()
            conn.close()

    def get_customer_by_username(self, username):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Customer WHERE Username = %s", (username,))
            result = cursor.fetchone()
            if result:
                return Customer(*result)
            else:
                return None
        finally:
            cursor.close()
            conn.close()

    def register_customer(self, customer_data):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = '''
            INSERT INTO Customer (FirstName, LastName, Email, PhoneNumber, Address, Username, Password, RegistrationDate)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            '''
            cursor.execute(query, (
                customer_data.first_name,
                customer_data.last_name,
                customer_data.email,
                customer_data.phone,
                customer_data.address,
                customer_data.username,
                customer_data.password,
                customer_data.registration_date
            ))
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    def update_customer(self, customer_data):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = '''
            UPDATE Customer
            SET FirstName = %s, LastName = %s, Email = %s, PhoneNumber = %s, Address = %s, Username = %s, Password = %s
            WHERE CustomerID = %s
            '''
            cursor.execute(query, (
                customer_data.first_name,
                customer_data.last_name,
                customer_data.email,
                customer_data.phone,
                customer_data.address,
                customer_data.username,
                customer_data.password,
                customer_data.customer_id
            ))
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    def delete_customer(self, customer_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Customer WHERE CustomerID = %s", (customer_id,))
            conn.commit()
        finally:
            cursor.close()
            conn.close()
