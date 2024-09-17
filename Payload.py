from faker import Faker
from Utilities.configuration import GetRecord

def AddToCart(ID):
    Body = {
        "productId": ID
    }
    return Body


def Register(Query):
    OneData = {}
    Tuple = GetRecord(Query)

    if Tuple:  # Check if Tuple is not None
        OneData['clientName'] = Tuple[0] if len(Tuple) > 0 else None
        OneData['clientEmail'] = Tuple[1] if len(Tuple) > 1 else None
    else:
        print("No data returned from the database.")
        OneData['clientName'] = None
        OneData['clientEmail'] = None

    return OneData


def CreateOrder(Cart_ID):
    Body = {
        "cartId": Cart_ID,
        "customerName": "Viknesh"
    }
    return Body
