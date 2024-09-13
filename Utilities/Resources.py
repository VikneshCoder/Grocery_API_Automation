
class Resources:
    def __init__(self, Cart_ID):
        self.Cart_ID = Cart_ID


    GetProduct = '/products'
    AddCart = '/carts'

    def get_add_product_to_cart(self):
        return f'/carts/{self.Cart_ID}/items'

    def get_cart_items(self):
        return f"/carts/{self.Cart_ID}/items"

    UserRegister = "/api-clients"
    NewOrder = "/orders"
