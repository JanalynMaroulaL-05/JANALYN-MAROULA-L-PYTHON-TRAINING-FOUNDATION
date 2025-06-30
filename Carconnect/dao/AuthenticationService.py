from dao.CustomerServiceImpl import CustomerServiceImpl
from dao.AdminServiceImpl import AdminServiceImpl
from exception.AuthenticationException import AuthenticationException

class AuthenticationService:
    def __init__(self, conn):
        self.conn = conn
        self.customer_service = CustomerServiceImpl(conn)
        self.admin_service = AdminServiceImpl(conn)

    def authenticate_customer(self, username, password):
        customer = self.customer_service.get_customer_by_username(username)
        if customer and customer.get_password() == password:
            return customer
        else:
            raise AuthenticationException("Invalid customer username or password.")

    def authenticate_admin(self, username, password):
        admin = self.admin_service.get_admin_by_username(username)
        if admin and admin.get_password() == password:
            return admin
        else:
            raise AuthenticationException("Invalid admin username or password.")
