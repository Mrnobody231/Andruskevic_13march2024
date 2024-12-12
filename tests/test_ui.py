import allure
from allure_commons.types import Severity

from pages_ui.MainPage import MainPage


@allure.severity(Severity.CRITICAL)
@allure.title("Find product")
@allure.description("Find product by name in the searchbox")
@allure.feature("Get")
def test_write_text_in_search_box():
    main = MainPage()
    main.write_text("//input[@placeholder='Найти']",
                    "Смартфон Samsung Galaxy A14 64GB Черный")
    main.click_with_keyboard("//input[@placeholder='Найти']")
    result = main.get_url()
    with allure.step("Check if url contains selected product"):
        assert result == ("https://moscow.shop.megafon.ru/search?qry=%D0%A1%D0%BC%D0%B0%D1%80%D1%82%D1%84%D0%BE%D0%BD+"
                      "Samsung+Galaxy+A14+64GB+%D0%A7%D0%B5%D1%80%D0%BD%D1%8B%D0%B9")

@allure.severity(Severity.CRITICAL)
@allure.title("Add to cart")
@allure.description("Ckeck if the current product is added to the cart")
@allure.feature("Get")
def test_add_to_cart():
    main = MainPage()
    main.write_text("//input[@placeholder='Найти']",
                    "Смартфон Samsung Galaxy A14 64GB Черный")
    main.click_with_keyboard("//input[@placeholder='Найти']")
    main.click(10,"//div[@class='b-good__buy buyBut']")
    result = main.get_location_text(4,
                                    "(//div[@class='Title-module__title--lh3ei Title-module__h3--serax"
                                    " Title-module__default--aVCoc Title-module__wide--sz3iM'])[1]",
                                    "Товар добавлен в корзину")
    with allure.step("Check if the cart icon has changed"):
        assert result == "Товар добавлен в корзину"