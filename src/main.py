import mysql.connector

# Database connection
try:
    con = mysql.connector.connect(
        user="root",
        password="mario123",
        host='localhost',
        database='Student_CRUD',
        auth_plugin='mysql_native_password'
    )
    cursor = con.cursor()
    print("Database connected successfully!")
except mysql.connector.Error as err:
    print(f"Error: {err}")
    exit()

# Function to create tables
def create_tables():
    try:
        student_table = '''
        CREATE TABLE IF NOT EXISTS student (
            stud_id VARCHAR(7) PRIMARY KEY,
            name VARCHAR(50),
            age INT,
            grade INT,
            mail_id VARCHAR(50)
        )
        '''
        staff_table = '''
        CREATE TABLE IF NOT EXISTS staff (
            staff_id VARCHAR(7) PRIMARY KEY,
            name VARCHAR(50),
            age INT,
            grade INT,
            mail_id VARCHAR(50)
        )
        '''
        cursor.execute(student_table)
        cursor.execute(staff_table)
        con.commit()
        print("Tables created successfully!")
    except mysql.connector.Error as err:
        print(f"Error creating tables: {err}")

# Function to add a record
def add_record(table_name, id, name, age, grade, mail):
    try:
        query = f"INSERT INTO {table_name} VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (id, name, age, grade, mail))
        con.commit()
        print("Record added successfully!")
    except mysql.connector.Error as err:
        print(f"Error adding record: {err}")

# Function to read records
def read_records(table_name):
    try:
        query = f"SELECT * FROM {table_name}"
        cursor.execute(query)
        records = cursor.fetchall()
        if records:
            for record in records:
                print(record)
        else:
            print("No records found!")
    except mysql.connector.Error as err:
        print(f"Error reading records: {err}")

# Function to update a record
def update_record(table_name, column, new_value, id_column, id_value):
    try:
        query = f"UPDATE {table_name} SET {column} = %s WHERE {id_column} = %s"
        cursor.execute(query, (new_value, id_value))
        con.commit()
        print("Record updated successfully!")
    except mysql.connector.Error as err:
        print(f"Error updating record: {err}")

# Function to delete a record
def delete_record(table_name, id_column, id_value):
    try:
        query = f"DELETE FROM {table_name} WHERE {id_column} = %s"
        cursor.execute(query, (id_value,))
        con.commit()
        print("Record deleted successfully!")
    except mysql.connector.Error as err:
        print(f"Error deleting record: {err}")

# Main menu
def main_menu():
    create_tables()
    while True:
        table_choice = input("\nSelect Table Name:\n1. student\n2. staff\nEnter your choice: ")
        table_name = 'student' if table_choice == '1' else 'staff'

        print("\nCRUD Operations:")
        print("1. Add to Table")
        print("2. Read from Table")
        print("3. Update Entry")
        print("4. Delete Entry")
        print("5. Exit")
        option = int(input("Enter your choice: "))

        if option == 1:
            id = input("ID: ")
            name = input("Name: ")
            age = int(input("Age: "))
            grade = int(input("Grade: "))
            mail = input("Mail ID: ")
            add_record(table_name, id, name, age, grade, mail)
        elif option == 2:
            read_records(table_name)
        elif option == 3:
            column = input("Enter column to update (name/age/grade/mail_id): ")
            new_value = input("Enter new value: ")
            id_value = input("Enter the ID of the record to update: ")
            id_column = 'stud_id' if table_name == 'student' else 'staff_id'
            update_record(table_name, column, new_value, id_column, id_value)
        elif option == 4:
            id_value = input("Enter the ID of the record to delete: ")
            id_column = 'stud_id' if table_name == 'student' else 'staff_id'
            delete_record(table_name, id_column, id_value)
        elif option == 5:
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again!")

# Run the program
main_menu()

# Close the connection
cursor.close()
con.close()
