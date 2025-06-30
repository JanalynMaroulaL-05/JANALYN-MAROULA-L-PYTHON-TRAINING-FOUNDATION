from dao.IAdminService import IAdminService
from entity.Admin import Admin
from util.DBConnUtil import get_connection

class AdminService(IAdminService):

    def get_admin_by_id(self, admin_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Admin WHERE AdminID = %s", (admin_id,))
            result = cursor.fetchone()
            return Admin(*result) if result else None
        finally:
            cursor.close()
            conn.close()

    def get_admin_by_username(self, username):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Admin WHERE Username = %s", (username,))
            result = cursor.fetchone()
            return Admin(*result) if result else None
        finally:
            cursor.close()
            conn.close()

    def register_admin(self, admin_data):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = '''
            INSERT INTO Admin (FirstName, LastName, Email, PhoneNumber, Username, Password, Role, JoinDate)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            '''
            cursor.execute(query, (
                admin_data.first_name,
                admin_data.last_name,
                admin_data.email,
                admin_data.phone_number,
                admin_data.username,
                admin_data.password,
                admin_data.role,
                admin_data.join_date
            ))
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    def update_admin(self, admin_data):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = '''
            UPDATE Admin
            SET FirstName = %s, LastName = %s, Email = %s, PhoneNumber = %s,
                Username = %s, Password = %s, Role = %s, JoinDate = %s
            WHERE AdminID = %s
            '''
            cursor.execute(query, (
                admin_data.first_name,
                admin_data.last_name,
                admin_data.email,
                admin_data.phone_number,
                admin_data.username,
                admin_data.password,
                admin_data.role,
                admin_data.join_date,
                admin_data.admin_id
            ))
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    def delete_admin(self, admin_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Admin WHERE AdminID = %s", (admin_id,))
            conn.commit()
        finally:
            cursor.close()
            conn.close()
