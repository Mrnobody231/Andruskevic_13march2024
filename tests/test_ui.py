import allure
from allure_commons.types import Severity

from pages_ui.MainPage import MainPage

@allure.severity(Severity.CRITICAL)
@allure.title("Find product")
@allure.description("Find product by name in the searchbox")
@allure.feature("Get")
def test_write_text_in_search_box():
    main = MainPage()
    main.write_text("//input[@class='searchpro__field-input js-searchpro__field-input']",
                    "Мумиё алтайское в капсулах, 60 капсул по 500 мг")
    main.click("(//div[@class='searchpro__field-button-container'])[1]")
    result = main.get_location_text(4,
                           "(//a[@class='link-blue'])[2]",
                           "Мумиё алтайское в капсулах, 60 капсул по 500 мг")
    assert result == "Мумиё алтайское в капсулах, 60 капсул по 500 мг"

@allure.severity(Severity.CRITICAL)
@allure.title("Add to cart")
@allure.description("Ckeck if the current product is added to the cart")
@allure.feature("Get")
def test_add_to_cart():
    main = MainPage()
    main.write_text("//input[@class='searchpro__field-input js-searchpro__field-input']",
                    "Мумиё алтайское в капсулах, 60 капсул по 500 мг")
    main.click("(//div[@class='searchpro__field-button-container'])[1]")
    main.click("(//div[@class='product__add_2_0'])[1]")
    result = main.get_location_text(4,
                           "(//div[@class='count-box'])[1]",
                           "1")
    assert result == "1"