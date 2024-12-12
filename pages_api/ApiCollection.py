import allure
import requests


class ApiCollection:
    def __init__(self, url):
        self.url = url

    @allure.step("Add product to the cart where product_id: {product_id}, "
                 "quantity: {quantity} and check the status code")
    def add_to_cart(self, product_id: int, quantity: int):
        body_request = {
            "operations": [
                {
                    "operation": "OrderAddGoodToBasket",
                    "arguments": {
                        "goodId": product_id,
                        "quantity": quantity
                    }
                }
            ]
        }
        cart_result = requests.post(self.url + "batch/order", json=body_request)
        get_status = cart_result.status_code
        return [cart_result.json(), get_status]

    @allure.step("Change product's quantity in the cart, where order_id: {product_id} and check the status code")
    def change_product_quantity(self, quantity: int, order_id:int, client_id: int):
        body_request = {
            "quantity": quantity
        }
        params = {
            "clientId": client_id
        }
        cart_result = requests.patch(self.url + f"order/{order_id}/basket/1", json=body_request, params=params)
        get_status = cart_result.status_code
        return [cart_result.json(), get_status]