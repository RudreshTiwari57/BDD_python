from support.locators import Locators


class Empty_address:

    def __init__(self,driver):
        self.locator = Locators(driver)



    def verify_address_error_message(self):
        self.locator.assertEqual("×\n" + "Address 1 must be between 3 and 128 characters!","passworderror_xpath")


