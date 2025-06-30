class Reservation:
    def __init__(self, reservation_id=None, customer_id=None, vehicle_id=None,
                 start_date=None, end_date=None, total_cost=0.0, status="Pending"):
        self.reservation_id = reservation_id
        self.customer_id = customer_id
        self.vehicle_id = vehicle_id
        self.start_date = start_date
        self.end_date = end_date
        self.total_cost = total_cost
        self.status = status

    # Getters
    def get_reservation_id(self):
        return self.reservation_id

    def get_customer_id(self):
        return self.customer_id

    def get_vehicle_id(self):
        return self.vehicle_id

    def get_start_date(self):
        return self.start_date

    def get_end_date(self):
        return self.end_date

    def get_total_cost(self):
        return self.total_cost

    def get_status(self):
        return self.status

    # Setters
    def set_reservation_id(self, reservation_id):
        self.reservation_id = reservation_id

    def set_customer_id(self, customer_id):
        self.customer_id = customer_id

    def set_vehicle_id(self, vehicle_id):
        self.vehicle_id = vehicle_id

    def set_start_date(self, start_date):
        self.start_date = start_date

    def set_end_date(self, end_date):
        self.end_date = end_date

    def set_total_cost(self, total_cost):
        self.total_cost = total_cost

    def set_status(self, status):
        self.status = status

    # Helper method
    def calculate_total_cost(self, days, daily_rate):
        self.total_cost = days * daily_rate

    def __str__(self):
        return (
            f"\n===== Reservation Details =====\n"
            f"Reservation ID : {self.reservation_id}\n"
            f"Customer ID    : {self.customer_id}\n"
            f"Vehicle ID     : {self.vehicle_id}\n"
            f"Start Date     : {self.start_date}\n"
            f"End Date       : {self.end_date}\n"
            f"Total Cost     : ₹{self.total_cost:.2f}\n"
            f"Status         : {self.status}"
        )
