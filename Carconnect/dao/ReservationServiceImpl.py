from dao.IReservationService import IReservationService
from entity.Reservation import Reservation
from exception.ReservationException import ReservationException
from exception.DatabaseConnectionException import DatabaseConnectionException

class ReservationServiceImpl(IReservationService):
    def __init__(self, conn):
        self.conn = conn

    def get_reservation_by_id(self, reservation_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Reservation WHERE ReservationID = %s", (reservation_id,))
            row = cursor.fetchone()
            if row:
                return Reservation(*row)
            raise ReservationException("Reservation not found.")
        except Exception as e:
            raise DatabaseConnectionException(f"Error fetching reservation: {e}")

    def get_reservations_by_customer_id(self, customer_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Reservation WHERE CustomerID = %s", (customer_id,))
            rows = cursor.fetchall()
            return [Reservation(*row) for row in rows]
        except Exception as e:
            raise DatabaseConnectionException(f"Error fetching reservations: {e}")

    def create_reservation(self, reservation):
        try:
            cursor = self.conn.cursor()
            # Conflict Check
            cursor.execute("""
                SELECT * FROM Reservation
                WHERE VehicleID = %s AND (
                    (StartDate <= %s AND EndDate >= %s) OR
                    (StartDate <= %s AND EndDate >= %s)
                )
            """, (reservation.get_vehicle_id(),
                  reservation.get_start_date(), reservation.get_start_date(),
                  reservation.get_end_date(), reservation.get_end_date()))
            conflict = cursor.fetchone()
            if conflict:
                raise ReservationException("Vehicle already reserved in selected time frame.")

            sql = """
                INSERT INTO Reservation
                (CustomerID, VehicleID, StartDate, EndDate, TotalCost, Status)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            values = (
                reservation.get_customer_id(),
                reservation.get_vehicle_id(),
                reservation.get_start_date(),
                reservation.get_end_date(),
                reservation.get_total_cost(),
                reservation.get_status()
            )
            cursor.execute(sql, values)
            self.conn.commit()
            return cursor.rowcount
        except ReservationException as re:
            raise re
        except Exception as e:
            raise DatabaseConnectionException(f"Error creating reservation: {e}")

    def update_reservation(self, reservation):
        try:
            cursor = self.conn.cursor()
            sql = """
                UPDATE Reservation
                SET StartDate=%s, EndDate=%s, TotalCost=%s, Status=%s
                WHERE ReservationID=%s
            """
            values = (
                reservation.get_start_date(),
                reservation.get_end_date(),
                reservation.get_total_cost(),
                reservation.get_status(),
                reservation.get_reservation_id()
            )
            cursor.execute(sql, values)
            self.conn.commit()
            return cursor.rowcount
        except Exception as e:
            raise DatabaseConnectionException(f"Error updating reservation: {e}")

    def cancel_reservation(self, reservation_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("UPDATE Reservation SET Status = 'cancelled' WHERE ReservationID = %s", (reservation_id,))
            self.conn.commit()
            return cursor.rowcount
        except Exception as e:
            raise DatabaseConnectionException(f"Error cancelling reservation: {e}")
