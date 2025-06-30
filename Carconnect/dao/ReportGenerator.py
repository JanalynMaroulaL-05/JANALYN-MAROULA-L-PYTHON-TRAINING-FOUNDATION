# dao/ReportGenerator.py

import mysql.connector
from exception.DatabaseConnectionException import DatabaseConnectionException

class ReportGenerator:
    def __init__(self, conn):
        self.conn = conn

    def generate_reservation_history(self):
        try:
            cursor = self.conn.cursor()
            sql = """
                SELECT r.ReservationID, c.FirstName, v.Model, r.StartDate, r.EndDate, r.TotalCost, r.Status
                FROM reservation r
                JOIN customer c ON r.CustomerID = c.CustomerID
                JOIN vehicle v ON r.VehicleID = v.VehicleID
                ORDER BY r.StartDate DESC
            """
            cursor.execute(sql)
            return cursor.fetchall()
        except mysql.connector.Error as e:
            raise DatabaseConnectionException(f"Error generating reservation history report: {e}")

    def generate_vehicle_utilization_report(self):
        try:
            cursor = self.conn.cursor()
            sql = """
                SELECT v.Model,
                       COUNT(r.ReservationID) AS TimesRented,
                       COALESCE(SUM(r.TotalCost), 0) AS TotalRevenue
                FROM vehicle v
                LEFT JOIN reservation r ON v.VehicleID = r.VehicleID
                GROUP BY v.Model
                ORDER BY TimesRented DESC
            """
            cursor.execute(sql)
            return cursor.fetchall()
        except mysql.connector.Error as e:
            raise DatabaseConnectionException(f"Error generating vehicle utilization report: {e}")
