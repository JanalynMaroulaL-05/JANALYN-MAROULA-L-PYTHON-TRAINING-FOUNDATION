class Customer:
    def __init__(self, customer_id=None, first_name=None, last_name=None, email=None, phone_number=None,
                 address=None, username=None, password=None, registration_date=None):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.username = username
        self.password = password
        self.registration_date = registration_date

    # Getters
    def get_customer_id(self):
        return self.customer_id

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_email(self):
        return self.email

    def get_phone_number(self):
        return self.phone_number

    def get_address(self):
        return self.address

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_registration_date(self):
        return self.registration_date

    # Setters
    def set_customer_id(self, customer_id):
        self.customer_id = customer_id

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_email(self, email):
        self.email = email

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def set_address(self, address):
        self.address = address

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

    def set_registration_date(self, registration_date):
        self.registration_date = registration_date

    # String representation
    def __str__(self):
        return (
            f"\n===== Customer Details =====\n"
            f"Customer ID       : {self.customer_id}\n"
            f"Name              : {self.first_name} {self.last_name}\n"
            f"Email             : {self.email}\n"
            f"Phone Number      : {self.phone_number}\n"
            f"Address           : {self.address}\n"
            f"Username          : {self.username}\n"
            f"Registration Date : {self.registration_date}"
        )
