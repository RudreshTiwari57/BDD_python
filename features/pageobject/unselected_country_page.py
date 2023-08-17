from support.locators import Locators


class Unselected_country:
    def __init__(self,driver):
        self.locator = Locators(driver)
    def verify_unselected_country_error_message(self):
        self.locator.assertEqual("×\n" + "Please select a region / state!","passworderror_xpath")
