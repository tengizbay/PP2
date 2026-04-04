import csv
from connect import get_connection

def create_table():
    conn = get_connection()
    if conn is None:
        return
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) UNIQUE,
            phone VARCHAR(20)
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

def insert_from_csv(filename='contacts.csv'):
    conn = get_connection()
    if conn is None:
        return
    cur = conn.cursor()
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        data = [(row['name'], row['phone']) for row in reader]
    cur.executemany(
        "INSERT INTO contacts (name, phone) VALUES (%s, %s) ON CONFLICT (name) DO NOTHING",
        data
    )
    conn.commit()
    cur.close()
    conn.close()
    print(f"{len(data)} contacts inserted from CSV.")

def insert_from_console():
    conn = get_connection()
    if conn is None:
        return
    cur = conn.cursor()
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    cur.execute(
        "INSERT INTO contacts (name, phone) VALUES (%s, %s) ON CONFLICT (name) DO NOTHING",
        (name, phone)
    )
    conn.commit()
    cur.close()
    conn.close()
    print("Contact added.")

def update_contact():
    conn = get_connection()
    if conn is None:
        return
    cur = conn.cursor()
    name = input("Enter name to update: ")
    new_phone = input("Enter new phone number: ")
    cur.execute(
        "UPDATE contacts SET phone=%s WHERE name=%s",
        (new_phone, name)
    )
    conn.commit()
    cur.close()
    conn.close()
    print("Contact updated.")

def delete_contact():
    conn = get_connection()
    if conn is None:
        return
    cur = conn.cursor()
    value = input("Enter name or phone to delete: ")
    cur.execute(
        "DELETE FROM contacts WHERE name=%s OR phone=%s",
        (value, value)
    )
    conn.commit()
    cur.close()
    conn.close()
    print("Contact deleted.")

def query_contacts():
    conn = get_connection()
    if conn is None:
        return
    cur = conn.cursor()
    choice = input("Search by name or phone prefix? (name/phone): ").lower()
    if choice == 'name':
        name_filter = input("Enter name or part of name: ")
        cur.execute("SELECT * FROM contacts WHERE name ILIKE %s", (f"%{name_filter}%",))
    elif choice == 'phone':
        phone_filter = input("Enter phone prefix: ")
        cur.execute("SELECT * FROM contacts WHERE phone LIKE %s", (f"{phone_filter}%",))
    else:
        print("Invalid choice")
        cur.close()
        conn.close()
        return
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

# Menu
def main():
    create_table()
    while True:
        print("\n1. Insert from CSV")
        print("2. Insert from console")
        print("3. Update contact")
        print("4. Delete contact")
        print("5. Query contacts")
        print("6. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            insert_from_csv()
        elif choice == '2':
            insert_from_console()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            query_contacts()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()