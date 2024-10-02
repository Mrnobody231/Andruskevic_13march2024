import allure
import requests


class ApiCollection:
    def __init__(self, url):
        self.url = url

    @allure.step("Add product to the cart where product_id: {product_id}, "
                 "quantity: {quantity} and check the status code")
    def add_to_cart(self, product_id: int, quantity: int):
        url_encoded = {
            "product_id": str(product_id),
            "S_wh": "1",
            "quantity": str(quantity),
            "S_cur_code": "usd"
        }
        cart_result = requests.post(self.url + "add_products_to_cart_from_preview.php", data=url_encoded)
        get_status = cart_result.status_code
        return [cart_result.json(), get_status]

    @allure.step("Delete product from the cart, where product_id: {product_id} and check the status code")
    def delete_from_cart(self, product_id: int):
        url_encoded = {
            "product_id": product_id,
            "S_wh": "1",
            "S_cur_code": "usd"
        }
        cart_result = requests.post(self.url + "delete_products_from_cart_preview.php", data=url_encoded)
        get_status = cart_result.status_code
        return [cart_result.json(), get_status]