from support.locators import Locators


class Empty_lastname:
    def __init__(self,driver):
        self.locator = Locators(driver)
    def verify_last_error_message(self):
        self.locator.assertEqual("×\n" + "Last Name must be between 1 and 32 characters!","passworderror_xpath")
