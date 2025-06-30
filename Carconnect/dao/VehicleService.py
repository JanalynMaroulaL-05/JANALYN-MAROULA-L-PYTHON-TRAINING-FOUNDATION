from dao.IVehicleService import IVehicleService
from entity.Vehicle import Vehicle
from util.DBConnUtil import get_connection

class VehicleService(IVehicleService):

    def get_vehicle_by_id(self, vehicle_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Vehicle WHERE VehicleID = %s", (vehicle_id,))
            result = cursor.fetchone()
            if result:
                return Vehicle(*result)
            else:
                return None
        finally:
            cursor.close()
            conn.close()

def get_available_vehicles(self):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Vehicle WHERE Availability = TRUE")
        vehicles = cursor.fetchall()

        if not vehicles:
            print("No vehicles available at the moment.")
            return

        print("\nAvailable Vehicles:")
        for v in vehicles:
            vehicle = Vehicle(*v)
            print(f"ID: {vehicle.vehicle_id}, Model: {vehicle.model}, Make: {vehicle.make}, Year: {vehicle.year}, "
                  f"Color: {vehicle.color}, Reg#: {vehicle.registration_number}, Rate: ₹{vehicle.daily_rate}/day")

    finally:
        cursor.close()
        conn.close()


    def add_vehicle(self, vehicle_data):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = '''
            INSERT INTO Vehicle (Model, Make, Year, Color, RegistrationNumber, Availability, DailyRate)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            '''
            cursor.execute(query, (
                vehicle_data.model,
                vehicle_data.make,
                vehicle_data.year,
                vehicle_data.color,
                vehicle_data.registration_number,
                vehicle_data.availability,
                vehicle_data.daily_rate
            ))
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    def update_vehicle(self, vehicle_data):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = '''
            UPDATE Vehicle
            SET Model = %s, Make = %s, Year = %s, Color = %s, RegistrationNumber = %s, Availability = %s, DailyRate = %s
            WHERE VehicleID = %s
            '''
            cursor.execute(query, (
                vehicle_data.model,
                vehicle_data.make,
                vehicle_data.year,
                vehicle_data.color,
                vehicle_data.registration_number,
                vehicle_data.availability,
                vehicle_data.daily_rate,
                vehicle_data.vehicle_id
            ))
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    def remove_vehicle(self, vehicle_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Vehicle WHERE VehicleID = %s", (vehicle_id,))
            conn.commit()
        finally:
            cursor.close()
            conn.close()
