class Admin:
    def __init__(self, admin_id=None, first_name=None, last_name=None, email=None, phone_number=None,
                 username=None, password=None, role=None, join_date=None):
        self.admin_id = admin_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.username = username
        self.password = password
        self.role = role
        self.join_date = join_date

    # Getters
    def get_admin_id(self):
        return self.admin_id

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_email(self):
        return self.email

    def get_phone_number(self):
        return self.phone_number

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_role(self):
        return self.role

    def get_join_date(self):
        return self.join_date

    # Setters
    def set_admin_id(self, admin_id):
        self.admin_id = admin_id

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_email(self, email):
        self.email = email

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

    def set_role(self, role):
        self.role = role

    def set_join_date(self, join_date):
        self.join_date = join_date

    def __str__(self):
        return (
            f"\n===== Admin Details =====\n"
            f"Admin ID   : {self.admin_id}\n"
            f"Name       : {self.first_name} {self.last_name}\n"
            f"Email      : {self.email}\n"
            f"Phone      : {self.phone_number}\n"
            f"Username   : {self.username}\n"
            f"Role       : {self.role}\n"
            f"Join Date  : {self.join_date}"
        )
