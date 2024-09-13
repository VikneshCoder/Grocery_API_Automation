import configparser

def GetConfig():
    config = configparser.ConfigParser()
    config.read('G:\\Selenium Project\\Grocery_API_Automation\\Utilities\\properties.ini')
    return config