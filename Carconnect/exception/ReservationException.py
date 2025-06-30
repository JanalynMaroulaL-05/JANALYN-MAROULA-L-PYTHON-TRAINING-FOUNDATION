class ReservationException(Exception):
    def __init__(self, message="Reservation error occurred"):
        super().__init__(message)
