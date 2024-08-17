import mysql.connector
import json

DB_CONFIG = {
    'user': 'sql12726531',
    'password': 'r5xy72c5Yk',
    'host': 'sql12.freemysqlhosting.net',
    'database': 'sql12726531',
}

def _connect():
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except mysql.connector.Error as err:
        raise RuntimeError(f"Database connection error: {err}")

def register(username: str, password: str, confirm_password: str):
    if password != confirm_password:
        raise ValueError("Passwords do not match")
    
    conn = _connect()
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT * FROM user WHERE UserName = %s", (username,))
        if cursor.fetchone():
            raise ValueError("Username already exists")
        
        cursor.execute("INSERT INTO user (UserName, Password, Variables) VALUES (%s, %s, %s)", 
                       (username, password, json.dumps({})))
        conn.commit()
    except mysql.connector.Error as err:
        raise RuntimeError(f"Database error during registration: {err}")
    finally:
        cursor.close()
        conn.close()

def login(username: str, password: str):
    conn = _connect()
    cursor = conn.cursor(dictionary=True)
    
    try:
        cursor.execute("SELECT * FROM user WHERE UserName = %s", (username,))
        user = cursor.fetchone()
        
        if user and user['Password'] == password:
            return Session(user['ID'])
        else:
            raise ValueError("Invalid username or password")
    except mysql.connector.Error as err:
        raise RuntimeError(f"Database error during login: {err}")
    finally:
        cursor.close()
        conn.close()

class Session:
    def __init__(self, user_id):
        self.user_id = user_id
        self._load_variables()
    
    def _load_variables(self):
        conn = _connect()
        cursor = conn.cursor(dictionary=True)
        
        try:
            cursor.execute("SELECT Variables FROM user WHERE ID = %s", (self.user_id,))
            result = cursor.fetchone()
            if result is None:
                raise ValueError("User ID does not exist")
            self._variables = json.loads(result['Variables'])
        except mysql.connector.Error as err:
            raise RuntimeError(f"Database error during variable load: {err}")
        except json.JSONDecodeError:
            raise RuntimeError("Error decoding JSON data")
        finally:
            cursor.close()
            conn.close()
    
    def get(self, variable_name: str):
        return self._variables.get(variable_name, "Variable not set")
    
    def create(self, variable_name: str, variable_value: str):
        if variable_name in self._variables:
            raise ValueError("Variable exists already. Use edit() to edit the value of the variable")
        
        self._variables[variable_name] = variable_value
        self._save()
    
    def delete(self, variable_name: str):
        if variable_name not in self._variables:
            raise ValueError("Variable not found. Use create() to set the variable first.")
        
        del self._variables[variable_name]
        self._save()
    
    def edit(self, variable_name: str, variable_value: str):
        if variable_name not in self._variables:
            raise ValueError("Variable not found. Use create() to set the variable first.")
        
        self._variables[variable_name] = variable_value
        self._save()
    
    def list(self):
        return self._variables
    
    def _save(self):
        conn = _connect()
        cursor = conn.cursor()
        
        try:
            cursor.execute("UPDATE user SET Variables = %s WHERE ID = %s", 
                           (json.dumps(self._variables), self.user_id))
            conn.commit()
        except mysql.connector.Error as err:
            raise RuntimeError(f"Database error during variable save: {err}")
        finally:
            cursor.close()
            conn.close()
