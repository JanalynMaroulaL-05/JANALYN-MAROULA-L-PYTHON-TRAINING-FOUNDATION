from dao.IVehicleService import IVehicleService
from entity.Vehicle import Vehicle
from exception.VehicleNotFoundException import VehicleNotFoundException
from exception.DatabaseConnectionException import DatabaseConnectionException

class VehicleServiceImpl(IVehicleService):
    def __init__(self, conn):
        self.conn = conn

    def get_vehicle_by_id(self, vehicle_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Vehicle WHERE VehicleID = %s", (vehicle_id,))
            row = cursor.fetchone()
            if row:
                return Vehicle(*row)
            raise VehicleNotFoundException("Vehicle not found.")
        except Exception as e:
            raise DatabaseConnectionException(f"Error fetching vehicle by ID: {e}")

    def get_available_vehicles(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Vehicle WHERE Availability = TRUE")
            rows = cursor.fetchall()
            return [Vehicle(*row) for row in rows]
        except Exception as e:
            raise DatabaseConnectionException(f"Error fetching available vehicles: {e}")

    def add_vehicle(self, vehicle):
        try:
            cursor = self.conn.cursor()
            sql = """
                INSERT INTO Vehicle
                (Model, Make, Year, Color, RegistrationNumber, Availability, DailyRate)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            values = (
                vehicle.get_model(),
                vehicle.get_make(),
                vehicle.get_year(),
                vehicle.get_color(),
                vehicle.get_registration_number(),
                vehicle.get_availability(),
                vehicle.get_daily_rate()
            )
            cursor.execute(sql, values)
            self.conn.commit()
            return cursor.rowcount
        except Exception as e:
            raise DatabaseConnectionException(f"Error adding vehicle: {e}")

    def update_vehicle(self, vehicle):
        try:
            cursor = self.conn.cursor()
            sql = """
                UPDATE Vehicle
                SET Model=%s, Make=%s, Year=%s, Color=%s,
                    RegistrationNumber=%s, Availability=%s, DailyRate=%s
                WHERE VehicleID=%s
            """
            values = (
                vehicle.get_model(),
                vehicle.get_make(),
                vehicle.get_year(),
                vehicle.get_color(),
                vehicle.get_registration_number(),
                vehicle.get_availability(),
                vehicle.get_daily_rate(),
                vehicle.get_vehicle_id()
            )
            cursor.execute(sql, values)
            self.conn.commit()
            return cursor.rowcount
        except Exception as e:
            raise DatabaseConnectionException(f"Error updating vehicle: {e}")

    def remove_vehicle(self, vehicle_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM Vehicle WHERE VehicleID = %s", (vehicle_id,))
            self.conn.commit()
            return cursor.rowcount
        except Exception as e:
            raise DatabaseConnectionException(f"Error removing vehicle: {e}")
