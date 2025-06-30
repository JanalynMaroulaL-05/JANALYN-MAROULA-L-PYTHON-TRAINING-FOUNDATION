import unittest
import time
from dao.CustomerServiceImpl import CustomerServiceImpl
from dao.VehicleServiceImpl import VehicleServiceImpl
from dao.ReservationServiceImpl import ReservationServiceImpl
from entity.Customer import Customer
from entity.Vehicle import Vehicle
from entity.Reservation import Reservation
from util.DBConnUtil import get_connection

class TestReservationService(unittest.TestCase):
    def setUp(self):
        self.conn = get_connection()
        self.customer_service = CustomerServiceImpl(self.conn)
        self.vehicle_service = VehicleServiceImpl(self.conn)
        self.reservation_service = ReservationServiceImpl(self.conn)

        ts = int(time.time() * 1000)
        self.username = f"res_user_{ts}"
        self.reg_no = f"RES_REG_{ts}"

        self.customer = Customer(
            0, "Res", "User", "res@example.com", "9999999999",
            "Test Address", self.username, "pass123", "2025-06-26"
        )
        self.customer_service.register_customer(self.customer)
        self.customer = self.customer_service.get_customer_by_username(self.username)

        self.vehicle = Vehicle(
            0, "ResModel", "ResMake", 2023, "Black", self.reg_no, True, 500.0
        )
        self.vehicle_service.add_vehicle(self.vehicle)
        vehicles = self.vehicle_service.get_available_vehicles()
        self.vehicle = next((v for v in vehicles if v.get_registration_number() == self.reg_no), None)

    def tearDown(self):
        cursor = self.conn.cursor()
        cursor.execute(
            "DELETE FROM reservation WHERE CustomerID IN (SELECT CustomerID FROM customer WHERE Username LIKE %s)",
            (f"{self.username}%",)
        )
        cursor.execute("DELETE FROM customer WHERE Username LIKE %s", (f"{self.username}%",))
        cursor.execute("DELETE FROM vehicle WHERE RegistrationNumber LIKE %s", (f"{self.reg_no}%",))
        self.conn.commit()
        self.conn.close()

    def test_create_reservation(self):
        reservation = Reservation(
            0,
            self.customer.get_customer_id(),
            self.vehicle.get_vehicle_id(),
            "2025-07-01",
            "2025-07-03",
            1000.0,
            "confirmed"
        )
        result = self.reservation_service.create_reservation(reservation)
        self.assertTrue(result)

    def test_update_reservation(self):
        # Create one
        reservation = Reservation(
            0,
            self.customer.get_customer_id(),
            self.vehicle.get_vehicle_id(),
            "2025-07-10",
            "2025-07-12",
            2000.0,
            "pending"
        )
        self.reservation_service.create_reservation(reservation)

        reservations = self.reservation_service.get_reservations_by_customer_id(self.customer.get_customer_id())
        self.assertGreater(len(reservations), 0)

        reservation = reservations[0]
        reservation.set_status("completed")
        result = self.reservation_service.update_reservation(reservation)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
