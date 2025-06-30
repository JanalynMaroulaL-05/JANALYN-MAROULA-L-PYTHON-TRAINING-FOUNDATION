from dao.ICustomerService import ICustomerService
from entity.Customer import Customer
from exception.DatabaseConnectionException import DatabaseConnectionException
from exception.InvalidInputException import InvalidInputException
import mysql.connector

class CustomerServiceImpl(ICustomerService):
    def __init__(self, conn):
        self.conn = conn

    def get_customer_by_id(self, customer_id):
        try:
            cursor = self.conn.cursor()
            sql = "SELECT * FROM customer WHERE CustomerID = %s"
            cursor.execute(sql, (customer_id,))
            row = cursor.fetchone()
            if row:
                return Customer(*row)
            return None
        except mysql.connector.Error as e:
            raise DatabaseConnectionException(f"Error fetching customer by ID: {e}")

    def get_customer_by_username(self, username):
        try:
            cursor = self.conn.cursor()
            sql = "SELECT * FROM customer WHERE Username = %s"
            cursor.execute(sql, (username,))
            row = cursor.fetchone()
            if row:
                return Customer(*row)
            return None
        except mysql.connector.Error as e:
            raise DatabaseConnectionException(f"Error fetching customer by username: {e}")

    def register_customer(self, customer):
        try:
            cursor = self.conn.cursor()

            # Check for duplicate username
            check_sql = "SELECT * FROM customer WHERE Username = %s"
            cursor.execute(check_sql, (customer.get_username(),))
            if cursor.fetchone():
                raise InvalidInputException(" Username already exists. Please choose another.")

            sql = """INSERT INTO customer
                     (FirstName, LastName, Email, PhoneNumber, Address, Username, Password, RegistrationDate)
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
            values = (
                customer.get_first_name(),
                customer.get_last_name(),
                customer.get_email(),
                customer.get_phone_number(),
                customer.get_address(),
                customer.get_username(),
                customer.get_password(),
                customer.get_registration_date()
            )
            cursor.execute(sql, values)
            self.conn.commit()
            return True
        except mysql.connector.Error as e:
            raise DatabaseConnectionException(f"Error registering customer: {e}")

    def update_customer(self, customer):
        try:
            cursor = self.conn.cursor()
            sql = """UPDATE customer SET FirstName=%s, LastName=%s, Email=%s, PhoneNumber=%s, Address=%s
                     WHERE CustomerID = %s"""
            values = (
                customer.get_first_name(),
                customer.get_last_name(),
                customer.get_email(),
                customer.get_phone_number(),
                customer.get_address(),
                customer.get_customer_id()
            )
            cursor.execute(sql, values)
            self.conn.commit()
            return cursor.rowcount > 0
        except mysql.connector.Error as e:
            raise DatabaseConnectionException(f"Error updating customer: {e}")

    def delete_customer(self, customer_id):
        try:
            cursor = self.conn.cursor()
            sql = "DELETE FROM customer WHERE CustomerID = %s"
            cursor.execute(sql, (customer_id,))
            self.conn.commit()
            return cursor.rowcount > 0
        except mysql.connector.Error as e:
            raise DatabaseConnectionException(f"Error deleting customer: {e}")
