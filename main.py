import mysql.connector

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password",
            database="pharmacy_db"
        )
        self.cursor = self.conn.cursor()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()

class Medicine:
    def __init__(self, name, qty, manufacture_date, expiry_date, price):
        self.name = name
        self.qty = qty
        self.manufacture_date = manufacture_date
        self.expiry_date = expiry_date
        self.price = price

class PharmacyManager:
    def __init__(self, db):
        self.db = db

    def add_medicine(self, medicine):
        query = "INSERT INTO medicines (name, qty, manufacture_date, expiry_date, price) VALUES (%s, %s, %s, %s, %s)"
        values = (medicine.name, medicine.qty, medicine.manufacture_date, medicine.expiry_date, medicine.price)
        self.db.cursor.execute(query, values)
        self.db.conn.commit()
        print("Medicine Added Successfully")

    def view_medicine(self):
        query = "SELECT * FROM medicines"
        self.db.cursor.execute(query)
        medicines = self.db.cursor.fetchall()
        for medicine in medicines:
            print(medicine)

class Admin:
    def __init__(self, db):
        self.db = db

    def view_manager(self):
        query = "SELECT * FROM managers"
        self.db.cursor.execute(query)
        managers = self.db.cursor.fetchall()
        for manager in managers:
            print(manager)

def main():
    db = Database()
    pharmacy_manager = PharmacyManager(db)
    admin = Admin(db)

    while True:
        print("Select an option:")
        print("1. Pharmacy Manager")
        print("2. Admin")
        print("3. Exit")

        choice = input("Enter The Number 1 to 3: ")

        if choice == '1':
            pass
        elif choice == '2':
            pass
        elif choice == '3':
            db.close_connection()
            print("Exiting The System")
            break
        else:
            print("Enter The Number Between 1 to 3")

if __name__ == "__main__":
    main()
