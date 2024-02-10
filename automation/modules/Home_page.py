import time

from selenium.webdriver.common.by import By
from automation.locators.locators_home_page import HomePageLocators
from automation.test_data.data import TestData


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def cantact_form(self):
        """
                Perform actions to fill the cantact form.
        """
        driver = self.driver
        driver.find_element(By.XPATH, HomePageLocators.CANTACT_NAME_BTN).send_keys(TestData.name)
        time.sleep(20)

    def another_page(self):
        driver = self.driver

        driver.find_element(By.XPATH, HomePageLocators.CANTACT_EMAIL_BTN).send_keys(TestData.email)
        time.sleep(10)
        driver.find_element(By.XPATH, HomePageLocators.CANTACT_PHONE_BTN).send_keys(TestData.phone)
        time.sleep(10)
        print("hellooo")
        driver.find_element(By.XPATH, HomePageLocators.CANTACT_MESSAGE_BTN).send_keys(TestData.message)
