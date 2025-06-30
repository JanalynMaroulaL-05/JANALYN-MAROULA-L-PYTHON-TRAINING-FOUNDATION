from dao.CustomerServiceImpl import CustomerServiceImpl
from dao.AdminServiceImpl import AdminServiceImpl
from dao.VehicleServiceImpl import VehicleServiceImpl
from dao.ReservationServiceImpl import ReservationServiceImpl
from dao.ReportGenerator import ReportGenerator
from util.DBConnUtil import get_connection
from entity.Customer import Customer
from entity.Admin import Admin
from entity.Vehicle import Vehicle
from entity.Reservation import Reservation
from datetime import datetime
from exception.InvalidInputException import InvalidInputException
from exception.DatabaseConnectionException import DatabaseConnectionException


def customer_menu(service):
    while True:
        print("\n====== Customer Menu ======")
        print("1. Register Customer")
        print("2. Get Customer by ID")
        print("3. Get Customer by Username")
        print("4. Update Customer")
        print("5. Delete Customer")
        print("6. Exit to Main Menu")
        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                print("\n-- Register New Customer --")
                first = input("First Name: ")
                last = input("Last Name: ")
                email = input("Email: ")
                phone = input("Phone Number: ")
                address = input("Address: ")
                username = input("Username: ")
                password = input("Password: ")
                date = datetime.now().strftime('%Y-%m-%d')

                customer = Customer(0, first, last, email, phone, address, username, password, date)
                result = service.register_customer(customer)
                print("Registration successful!" if result else "Registration failed!")

            elif choice == '2':
                cid = int(input("Enter Customer ID: "))
                customer = service.get_customer_by_id(cid)
                print(customer if customer else "Customer not found.")

            elif choice == '3':
                uname = input("Enter Username: ")
                customer = service.get_customer_by_username(uname)
                print(customer if customer else "Customer not found.")

            elif choice == '4':
                cid = int(input("Enter Customer ID to Update: "))
                customer = service.get_customer_by_id(cid)
                if not customer:
                    print("Customer not found.")
                    continue
                customer.set_first_name(input("New First Name: "))
                customer.set_last_name(input("New Last Name: "))
                customer.set_email(input("New Email: "))
                customer.set_phone_number(input("New Phone: "))
                customer.set_address(input("New Address: "))
                print("Updated successfully!" if service.update_customer(customer) else "Update failed.")

            elif choice == '5':
                cid = int(input("Enter Customer ID to delete: "))
                print("Deleted!" if service.delete_customer(cid) else "Delete failed.")

            elif choice == '6':
                break
            else:
                print("Invalid option.")

        except (InvalidInputException, DatabaseConnectionException) as e:
            print(f"Error: {e}")


def admin_menu(service):
    while True:
        print("\n====== Admin Menu ======")
        print("1. Register Admin")
        print("2. Get Admin by ID")
        print("3. Get Admin by Username")
        print("4. Update Admin")
        print("5. Delete Admin")
        print("6. Exit to Main Menu")
        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                first = input("First Name: ")
                last = input("Last Name: ")
                email = input("Email: ")
                phone = input("Phone Number: ")
                username = input("Username: ")
                password = input("Password: ")
                role = input("Role: ")
                join_date = datetime.now().strftime('%Y-%m-%d')

                admin = Admin(0, first, last, email, phone, username, password, role, join_date)
                print("Registered!" if service.register_admin(admin) else " Failed.")

            elif choice == '2':
                aid = int(input("Admin ID: "))
                admin = service.get_admin_by_id(aid)
                print(admin if admin else "Not found.")

            elif choice == '3':
                uname = input("Username: ")
                admin = service.get_admin_by_username(uname)
                print(admin if admin else " Not found.")

            elif choice == '4':
                aid = int(input("Admin ID to update: "))
                admin = service.get_admin_by_id(aid)
                if not admin:
                    print(" Admin not found.")
                    continue
                admin.set_first_name(input("New First Name: "))
                admin.set_last_name(input("New Last Name: "))
                admin.set_email(input("New Email: "))
                admin.set_phone_number(input("New Phone: "))
                admin.set_role(input("New Role: "))
                print(" Updated!" if service.update_admin(admin) else " Update failed.")

            elif choice == '5':
                aid = int(input("Admin ID to delete: "))
                print(" Deleted!" if service.delete_admin(aid) else " Delete failed.")

            elif choice == '6':
                break
            else:
                print("Invalid choice.")

        except Exception as e:
            print(f" Error: {e}")


def vehicle_menu(service):
    while True:
        print("\n====== Vehicle Menu ======")
        print("1. Add Vehicle")
        print("2. View Vehicle by ID")
        print("3. View Available Vehicles")
        print("4. Update Vehicle")
        print("5. Remove Vehicle")
        print("6. Exit to Main Menu")
        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                model = input("Model: ")
                make = input("Make: ")
                year = int(input("Year: "))
                color = input("Color: ")
                reg_no = input("Registration Number: ")
                available = input("Available (1/0): ") == '1'
                rate = float(input("Daily Rate: "))

                vehicle = Vehicle(0, model, make, year, color, reg_no, available, rate)
                print(" Added!" if service.add_vehicle(vehicle) else " Failed.")

            elif choice == '2':
                vid = int(input("Vehicle ID: "))
                vehicle = service.get_vehicle_by_id(vid)
                print(vehicle if vehicle else " Not found.")

            elif choice == '3':
                vehicles = service.get_available_vehicles()
                for v in vehicles:
                    print(v)

            elif choice == '4':
                vid = int(input("Vehicle ID: "))
                vehicle = service.get_vehicle_by_id(vid)
                if not vehicle:
                    print(" Not found.")
                    continue
                vehicle.set_model(input("New Model: "))
                vehicle.set_make(input("New Make: "))
                vehicle.set_year(int(input("New Year: ")))
                vehicle.set_color(input("New Color: "))
                vehicle.set_registration_number(input("New Reg No: "))
                vehicle.set_availability(input("Available (1/0): ") == '1')
                vehicle.set_daily_rate(float(input("New Rate: ")))
                print(" Updated!" if service.update_vehicle(vehicle) else " Failed.")

            elif choice == '5':
                vid = int(input("Vehicle ID: "))
                print(" Removed!" if service.remove_vehicle(vid) else " Failed.")

            elif choice == '6':
                break
            else:
                print("Invalid.")

        except Exception as e:
            print(f" Error: {e}")


def reservation_menu(service):
    while True:
        print("\n====== Reservation Menu ======")
        print("1. Create Reservation")
        print("2. View Reservation by ID")
        print("3. View Reservations by Customer ID")
        print("4. Update Reservation")
        print("5. Cancel Reservation")
        print("6. Exit to Main Menu")
        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                cid = int(input("Customer ID: "))
                vid = int(input("Vehicle ID: "))
                start = input("Start Date (YYYY-MM-DD): ")
                end = input("End Date (YYYY-MM-DD): ")
                total = float(input("Total Cost: "))
                status = input("Status: ")

                res = Reservation(0, cid, vid, start, end, total, status)
                print(" Created!" if service.create_reservation(res) else " Failed.")

            elif choice == '2':
                rid = int(input("Reservation ID: "))
                res = service.get_reservation_by_id(rid)
                print(res if res else " Not found.")

            elif choice == '3':
                cid = int(input("Customer ID: "))
                reservations = service.get_reservations_by_customer_id(cid)
                for r in reservations:
                    print(r)

            elif choice == '4':
                rid = int(input("Reservation ID: "))
                res = service.get_reservation_by_id(rid)
                if not res:
                    print(" Not found.")
                    continue
                res.set_start_date(input("New Start Date (YYYY-MM-DD): "))
                res.set_end_date(input("New End Date (YYYY-MM-DD): "))
                res.set_total_cost(float(input("New Cost: ")))
                res.set_status(input("New Status: "))
                print(" Updated!" if service.update_reservation(res) else " Failed.")

            elif choice == '5':
                rid = int(input("Reservation ID: "))
                print(" Cancelled!" if service.cancel_reservation(rid) else " Failed.")

            elif choice == '6':
                break
            else:
                print("Invalid option.")

        except Exception as e:
            print(f" Error: {e}")


def report_menu(report_gen):
    while True:
        print("\n====== Report Menu ======")
        print("1. Reservation History")
        print("2. Vehicle Utilization")
        print("3. Exit to Main Menu")
        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                rows = report_gen.generate_reservation_history()
                print("\n===== Reservation History Report =====")
                if not rows:
                    print("No reservation data found.")
                else:
                    for row in rows:
                        print(
                            f"Reservation ID : {row[0]}\n"
                            f"Customer Name  : {row[1]}\n"
                            f"Vehicle         : {row[2]}\n"
                            f"Start Date      : {row[3]}\n"
                            f"End Date        : {row[4]}\n"
                            f"Total Cost      : ₹{row[5]}\n"
                            f"Status          : {row[6]}\n"
                            f"{'-'*40}"
                        )

            elif choice == '2':
                rows = report_gen.generate_vehicle_utilization_report()
                print("\n===== Vehicle Utilization Report =====")
                if not rows:
                    print("No vehicle data found.")
                else:
                    for row in rows:
                        print(
                            f"Vehicle Model       : {row[0]}\n"
                            f"Total Reservations  : {row[1]}\n"
                            f"Total Revenue       : ₹{row[2]}\n"
                            f"{'-'*40}"
                        )

            elif choice == '3':
                break
            else:
                print("Invalid choice.")
        except Exception as e:
            print(f" Error: {e}")


def main():
    conn = get_connection()
    customer_service = CustomerServiceImpl(conn)
    admin_service = AdminServiceImpl(conn)
    vehicle_service = VehicleServiceImpl(conn)
    reservation_service = ReservationServiceImpl(conn)
    report_generator = ReportGenerator(conn)

    while True:
        print("\nWelcome to CarConnect Rental System")
        print("====== Main Menu ======")
        print("1. Customer Menu")
        print("2. Admin Menu")
        print("3. Vehicle Menu")
        print("4. Reservation Menu")
        print("5. Reports Menu")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            customer_menu(customer_service)
        elif choice == '2':
            admin_menu(admin_service)
        elif choice == '3':
            vehicle_menu(vehicle_service)
        elif choice == '4':
            reservation_menu(reservation_service)
        elif choice == '5':
            report_menu(report_generator)
        elif choice == '6':
            print("Exiting... Thank you for using CarConnect")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
