import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import BASE_URL


class MainPage:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(BASE_URL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    @allure.step("Click on whatever button: {locator}")
    def click(self, locator: str):
        self.driver.find_element(By.XPATH, locator).click()

    @allure.step("Get text from the element: {text}")
    def get_location_text(self, time_out: int, locator: str, text: str) -> str:
        WebDriverWait(self.driver, time_out).until(EC.text_to_be_present_in_element(
            (By.XPATH, locator), text))
        text = self.driver.find_element(By.XPATH, locator).text
        return text

    @allure.step("Insert {text} in the searchbox")
    def write_text(self, locator: str, text: str):
        self.driver.find_element(By.XPATH, locator).send_keys(text)