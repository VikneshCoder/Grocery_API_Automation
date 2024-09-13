from faker import Faker


def AddToCart(ID):
    Body = {
        "productId": ID
    }
    return Body


def UserRegister(fake):
    Body = {
        "clientName": fake.name(),
        "clientEmail": fake.email()
    }
    return Body

def CreateOrder(Cart_ID):
    Body = {
            "cartId": Cart_ID,
            "customerName": "Viknesh"
        }
    return Body
