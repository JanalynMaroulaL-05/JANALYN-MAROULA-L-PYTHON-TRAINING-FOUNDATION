from dao.IAdminService import IAdminService
from entity.Admin import Admin
from exception.DatabaseConnectionException import DatabaseConnectionException
from exception.InvalidInputException import InvalidInputException
import mysql.connector

class AdminServiceImpl(IAdminService):
    def __init__(self, conn):
        self.conn = conn

    def get_admin_by_id(self, admin_id):
        try:
            cursor = self.conn.cursor()
            sql = "SELECT * FROM admin WHERE AdminID = %s"
            cursor.execute(sql, (admin_id,))
            row = cursor.fetchone()
            if row:
                return Admin(*row)
            return None
        except mysql.connector.Error as e:
            raise DatabaseConnectionException(f"Error fetching admin by ID: {e}")

    def get_admin_by_username(self, username):
        try:
            cursor = self.conn.cursor()
            sql = "SELECT * FROM admin WHERE Username = %s"
            cursor.execute(sql, (username,))
            row = cursor.fetchone()
            if row:
                return Admin(*row)
            return None
        except mysql.connector.Error as e:
            raise DatabaseConnectionException(f"Error fetching admin by username: {e}")

    def register_admin(self, admin):
        try:
            cursor = self.conn.cursor()

            # Check for duplicate username
            check_sql = "SELECT * FROM admin WHERE Username = %s"
            cursor.execute(check_sql, (admin.get_username(),))
            if cursor.fetchone():
                raise InvalidInputException(" Admin username already exists. Please choose another.")

            sql = """INSERT INTO admin
                     (FirstName, LastName, Email, PhoneNumber, Username, Password, Role, JoinDate)
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
            values = (
                admin.get_first_name(),
                admin.get_last_name(),
                admin.get_email(),
                admin.get_phone_number(),
                admin.get_username(),
                admin.get_password(),
                admin.get_role(),
                admin.get_join_date()
            )
            cursor.execute(sql, values)
            self.conn.commit()
            return True
        except mysql.connector.Error as e:
            raise DatabaseConnectionException(f"Error registering admin: {e}")

    def update_admin(self, admin):
        try:
            cursor = self.conn.cursor()
            sql = """UPDATE admin SET FirstName=%s, LastName=%s, Email=%s, PhoneNumber=%s, Role=%s
                     WHERE AdminID = %s"""
            values = (
                admin.get_first_name(),
                admin.get_last_name(),
                admin.get_email(),
                admin.get_phone_number(),
                admin.get_role(),
                admin.get_admin_id()
            )
            cursor.execute(sql, values)
            self.conn.commit()
            return cursor.rowcount > 0
        except mysql.connector.Error as e:
            raise DatabaseConnectionException(f"Error updating admin: {e}")

    def delete_admin(self, admin_id):
        try:
            cursor = self.conn.cursor()
            sql = "DELETE FROM admin WHERE AdminID = %s"
            cursor.execute(sql, (admin_id,))
            self.conn.commit()
            return cursor.rowcount > 0
        except mysql.connector.Error as e:
            raise DatabaseConnectionException(f"Error deleting admin: {e}")
