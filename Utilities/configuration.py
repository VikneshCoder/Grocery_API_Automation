import configparser
import mysql.connector
from mysql.connector import Error

def GetConfig():
    config = configparser.ConfigParser()
    config.read('G:\\Selenium Project\\Grocery_API_Automation\\Utilities\\properties.ini')
    return config

Connection = {
    'host': GetConfig()['SQL']['host'],
    'user': GetConfig()['SQL']['user'],
    'password': GetConfig()['SQL']['password'],
    'database': GetConfig()['SQL']['database']
}

def GetConnectionDB():
    try:
        Connection_Success = mysql.connector.connect(**Connection)
        if Connection_Success.is_connected():
            print("DB Connected Successful")
        return Connection_Success

    except Error as e:
        print(e)


def GetRecord(Query):
    Connect = GetConnectionDB()
    cursor = Connect.cursor()

    try:
        cursor.execute(Query)
        Data = cursor.fetchone()  # Fetch a single row if expected
        # Ensure there are no unread results
        cursor.fetchall()  # Clear any remaining results
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        Data = None  # Ensure Data is set to None on error
    finally:
        cursor.close()
        Connect.close()

    return Data

