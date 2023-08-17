from support.locators import Locators


class Succesfull_login:
    def __init__(self,driver):
        self.locator = Locators(driver)
    def verify_missmatch_password_error_message(self):
        self.locator.assertEqual("My Account","title")
