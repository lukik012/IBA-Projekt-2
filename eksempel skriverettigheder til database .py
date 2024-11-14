
import sqlite3

def validate_login(username, password):
    conn = sqlite3.connect("indsæt din database")
    cursor = conn.cursor()
    cursor.execute("SELECT role FROM users WHERE username = ? AND password = ?", (username, password))
    result = cursor.fetchone()  
    conn.close()
    
    if result:
        return result[0] 
    else:
        return None 
    
def modify_data(username, data):
    role = validate_login(username, '12345')  
    if role == "admin":
        conn = sqlite3.connect("indsæt din database")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO (#indsæt det i din tabel her) (data) VALUES (?)", (data,))
        conn.commit()
        conn.close()
        print(f"Data '{data}' written to the database by admin user '{username}'.")
    else:
        print("User does not have admin rights to modify the database.")




