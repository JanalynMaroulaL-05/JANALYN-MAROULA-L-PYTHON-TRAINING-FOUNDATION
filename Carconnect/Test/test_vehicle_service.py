import unittest
import time
from dao.VehicleServiceImpl import VehicleServiceImpl
from entity.Vehicle import Vehicle
from util.DBConnUtil import get_connection

class TestVehicleService(unittest.TestCase):
    def setUp(self):
        self.conn = get_connection()
        self.service = VehicleServiceImpl(self.conn)
        ts = int(time.time() * 1000)
        self.reg_no = f"TEST_REG_{ts}"
        self.vehicle = Vehicle(
            0, "TestModel", "TestMake", 2024, "Blue", self.reg_no, True, 1000.0
        )
        self.service.add_vehicle(self.vehicle)
        vehicles = self.service.get_available_vehicles()
        self.vehicle = next((v for v in vehicles if v.get_registration_number() == self.reg_no), None)

    def tearDown(self):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM vehicle WHERE RegistrationNumber LIKE %s", (f"{self.reg_no}%",))
        self.conn.commit()
        self.conn.close()

    def test_add_vehicle(self):
        self.assertIsNotNone(self.vehicle)

    def test_update_vehicle(self):
        self.vehicle.set_color("Red")
        result = self.service.update_vehicle(self.vehicle)
        self.assertTrue(result)

    def test_get_available_vehicles(self):
        vehicles = self.service.get_available_vehicles()
        self.assertGreater(len(vehicles), 0)

if __name__ == '__main__':
    unittest.main()
