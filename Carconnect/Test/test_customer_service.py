import unittest
import time
from dao.CustomerServiceImpl import CustomerServiceImpl
from entity.Customer import Customer
from util.DBConnUtil import get_connection

class TestCustomerService(unittest.TestCase):
    def setUp(self):
        self.conn = get_connection()
        self.service = CustomerServiceImpl(self.conn)
        ts = int(time.time() * 1000)
        self.username = f"test_user_{ts}"
        self.customer = Customer(
            0, "Test", "User", "test@example.com", "1234567890",
            "Test Address", self.username, "password", "2025-06-26"
        )
        self.service.register_customer(self.customer)
        self.customer = self.service.get_customer_by_username(self.username)

    def tearDown(self):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM customer WHERE Username LIKE %s", (f"{self.username}%",))
        self.conn.commit()
        self.conn.close()

    def test_get_customer_by_username(self):
        customer = self.service.get_customer_by_username(self.username)
        self.assertIsNotNone(customer)
        self.assertEqual(customer.get_username(), self.username)

    def test_update_customer(self):
        self.customer.set_first_name("UpdatedName")
        result = self.service.update_customer(self.customer)
        self.assertTrue(result)

    def test_delete_customer(self):
        result = self.service.delete_customer(self.customer.get_customer_id())
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
