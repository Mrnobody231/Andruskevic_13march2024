import allure
from allure_commons.types import Severity

from constants import API_URl
from pages_api.ApiCollection import ApiCollection


@allure.severity(Severity.CRITICAL)
@allure.title("Add product to the cart")
@allure.description("Click button 'купить' to add the product to the cart")
@allure.feature("Add")
def test_add_to_cart():
    api = ApiCollection(API_URl)
    result = api.add_to_cart( 188021, 1)
    with allure.step("Check if the getting list is not empty"):
        assert result is not None
    with allure.step("Check if added quantity is equal 1"):
        assert result[0]['payload']['order']['basket']['items'][0]['amount'] == 1
    with allure.step("Check if the status is equal 200"):
        assert result[1] == 200

@allure.severity(Severity.CRITICAL)
@allure.title("Change product's quantity in the cart")
@allure.description("Click icon + to change product's quantity in the cart")
@allure.feature("Change")
def test_change_quantity():
    api = ApiCollection(API_URl)
    result = api.change_product_quantity(2,33969502, 8877727)
    with allure.step("Check if changed quantity is equal 2"):
        assert result[0]['payload']['order']['basket']['items'][0]['amount'] == 2
    with allure.step("Check if the status is equal 200"):
        assert result[1] == 200