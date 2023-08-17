from support.locators import Locators


class Empty_zipcode:
    def __init__(self,driver):
        self.locator = Locators(driver)
    def verify_zipcode_error_message(self):
        self.locator.assertEqual("×\n" + "Zip/postal code must be between 3 and 10 characters!","passworderror_xpath")
