import allure
from allure_commons.types import Severity

from constants import API_URl
from pages_api.ApiCollection import ApiCollection

@allure.severity(Severity.CRITICAL)
@allure.title("Add product to the cart")
@allure.description("Click button 'В корзину' to add the product to the cart")
@allure.feature("Add")
def test_add_to_cart():
    api = ApiCollection(API_URl)
    result = api.add_to_cart(4593, 1)
    with allure.step("Check if the getting list is not empty"):
        assert result is not None
    with allure.step("Check if added quantity is equal 1"):
        assert result[0]['new_quantity'] == 1
    with allure.step("Check if the status is equal 200"):
        assert result[1] == 200

@allure.severity(Severity.CRITICAL)
@allure.title("Delete product from the cart")
@allure.description("Click icon X to delete the product from the cart")
@allure.feature("Delete")
def test_delete_from_cart():
    api = ApiCollection(API_URl)
    result = api.delete_from_cart(4593)
    with allure.step("Check if deleted quantity is equal 1"):
        assert result[0]['quantity_to_delete'] == '1'
    with allure.step("Check if the status is equal 200"):
        assert result[1] == 200