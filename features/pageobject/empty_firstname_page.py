from support.locators import Locators


class Empty_firstname:
    def __init__(self,driver):
        self.locator = Locators(driver)
    def verify_firstname_error_message(self):
        self.locator.assertEqual("×\n" + "First Name must be between 1 and 32 characters!","passworderror_xpath")
