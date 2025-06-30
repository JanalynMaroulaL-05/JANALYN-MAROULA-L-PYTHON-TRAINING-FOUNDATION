from dao.IReservationService import IReservationService
from entity.Reservation import Reservation
from util.DBConnUtil import get_connection

class ReservationService(IReservationService):

    def get_reservation_by_id(self, reservation_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Reservation WHERE ReservationID = %s", (reservation_id,))
            result = cursor.fetchone()
            return Reservation(*result) if result else None
        finally:
            cursor.close()
            conn.close()

    def get_reservations_by_customer_id(self, customer_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Reservation WHERE CustomerID = %s", (customer_id,))
            results = cursor.fetchall()
            return [Reservation(*row) for row in results]
        finally:
            cursor.close()
            conn.close()
def create_reservation(self, customer_id, vehicle_id, start_date, end_date):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = '''
        INSERT INTO Reservation (CustomerID, VehicleID, StartDate, EndDate, Status)
        VALUES (%s, %s, %s, %s, 'Confirmed')
        '''
        cursor.execute(query, (customer_id, vehicle_id, start_date, end_date))
        conn.commit()
        print("Reservation created successfully.")
    finally:
        cursor.close()
        conn.close()


    def update_reservation(self, reservation_data):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = '''
            UPDATE Reservation
            SET CustomerID = %s, VehicleID = %s, StartDate = %s, EndDate = %s, TotalCost = %s, Status = %s
            WHERE ReservationID = %s
            '''
            cursor.execute(query, (
                reservation_data.customer_id,
                reservation_data.vehicle_id,
                reservation_data.start_date,
                reservation_data.end_date,
                reservation_data.total_cost,
                reservation_data.status,
                reservation_data.reservation_id
            ))
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    def cancel_reservation(self, reservation_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE Reservation SET Status = 'cancelled' WHERE ReservationID = %s", (reservation_id,))
            conn.commit()
        finally:
            cursor.close()
            conn.close()
