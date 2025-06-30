class Vehicle:
    def __init__(self, vehicle_id=None, model=None, make=None, year=None, color=None,
                 registration_number=None, availability=True, daily_rate=0.0):
        self.vehicle_id = vehicle_id
        self.model = model
        self.make = make
        self.year = year
        self.color = color
        self.registration_number = registration_number
        self.availability = availability
        self.daily_rate = daily_rate

    
    def get_vehicle_id(self):
        return self.vehicle_id

    def get_model(self):
        return self.model

    def get_make(self):
        return self.make

    def get_year(self):
        return self.year

    def get_color(self):
        return self.color

    def get_registration_number(self):
        return self.registration_number

    def get_availability(self):  
        return self.availability

    def get_daily_rate(self):
        return self.daily_rate

  
    def set_vehicle_id(self, vehicle_id):
        self.vehicle_id = vehicle_id

    def set_model(self, model):
        self.model = model

    def set_make(self, make):
        self.make = make

    def set_year(self, year):
        self.year = year

    def set_color(self, color):
        self.color = color

    def set_registration_number(self, registration_number):
        self.registration_number = registration_number

    def set_availability(self, availability):  
        self.availability = availability

    def set_daily_rate(self, daily_rate):
        self.daily_rate = daily_rate


    def __str__(self):
        return (
            f"\n===== Vehicle Details =====\n"
            f"Vehicle ID         : {self.vehicle_id}\n"
            f"Model              : {self.model}\n"
            f"Make               : {self.make}\n"
            f"Year               : {self.year}\n"
            f"Color              : {self.color}\n"
            f"Registration No    : {self.registration_number}\n"
            f"Available          : {'Yes' if self.availability else 'No'}\n"
            f"Daily Rate         : ₹{self.daily_rate}"
        )
