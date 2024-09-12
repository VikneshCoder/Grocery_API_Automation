import requests
from faker import Faker

# Get Status
response = requests.get("https://simple-grocery-store-api.glitch.me")
Response = response.json()
assert response.status_code == 200
assert 'Simple Grocery Store API.' in Response["message"]
print(Response)

# Get Products
response_product = requests.get("https://simple-grocery-store-api.glitch.me/products")
Product_Response = response_product.json()
assert response_product.status_code == 200
Product_ID = Product_Response[3]["id"]
print(f"Product ID for Third: {Product_ID}")
for Products in Product_Response:
    if Products["category"] == "coffee":
        ID = Products["id"]
        print(f"Product ID for Coffee: {ID}")
        break


# Create a new cart
response_Create_Cart = requests.post("https://simple-grocery-store-api.glitch.me/carts")
Cart_Response = response_Create_Cart.json()
assert response_Create_Cart.status_code == 201
Cart_ID = Cart_Response["cartId"]
print(f"Cart Created Successfully: {Cart_Response}")
print(f"Cart Created ID is: {Cart_ID}")


# Add a Product to the cart
response_Add_Item_to_Cart = requests.post(f"https://simple-grocery-store-api.glitch.me/carts/{Cart_ID}/items", json={"productId": Product_ID})
print(f"Status Code: {response_Add_Item_to_Cart.status_code}")
print(f"Response Content: {response_Add_Item_to_Cart.text}")
Add_Item_to_Cart = response_Add_Item_to_Cart.json()
assert Add_Item_to_Cart["created"] is True
Item_id = Add_Item_to_Cart["itemId"]
print(f"Item added to Cart and the ID is: {Item_id}")


# Get Items from the Cart
response_Get_Item_From_Cart = requests.get(f"https://simple-grocery-store-api.glitch.me/carts/{Cart_ID}/items")
Get_Item_Response = response_Get_Item_From_Cart.json()
assert response_Get_Item_From_Cart.status_code == 200
for item in Get_Item_Response:
    if item["productId"] == Product_ID:
        print(f"Item ID: {item['id']}, Product ID: {item['productId']}")


# User Register
fake = Faker()
response_User_Login = requests.post("https://simple-grocery-store-api.glitch.me/api-clients", json={
    "clientName": fake.name(),
    "clientEmail": fake.email()
})
User_Login_Response = response_User_Login.json()
print(f"Status Code For New User Register :{response_User_Login.status_code}")
assert response_User_Login.status_code == 201
User_Token = User_Login_Response["accessToken"]
print(f"User Token: {User_Token}")

# Create a New Order
response_Create_Order = requests.post(f"https://simple-grocery-store-api.glitch.me/orders", json={
    "cartId": Cart_ID,
    "customerName": "Viknesh"
},  headers={
        "Authorization": User_Token
    })
Order_Response = response_Create_Order.json()
print(f"Status Code For New Order : {response_Create_Order.status_code}")
assert response_Create_Order.status_code == 201
Order_ID = Order_Response["orderId"]
print(f"Order Created Successfully: {Order_Response}")
print(f"Order Created ID is: {Order_ID}")

# Get Order Details
response_Get_Order_Details = requests.get(f"https://simple-grocery-store-api.glitch.me/orders", headers={
        "Authorization": User_Token
    })
Get_Order_Details_Response = response_Get_Order_Details.json()
print(f"Status Code For Order Details : {response_Get_Order_Details.status_code}")
assert response_Get_Order_Details.status_code == 200


# Delete a Product
response_Delete_Product = requests.delete(f"https://simple-grocery-store-api.glitch.me/orders/{Order_ID}", headers={
        "Authorization": User_Token
    })
print(f"Status Code For Deleting Product : {response_Delete_Product.status_code}")
assert response_Delete_Product.status_code == 204
















