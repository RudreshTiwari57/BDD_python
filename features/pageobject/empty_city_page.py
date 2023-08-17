from support.locators import Locators



class Empty_city:

    def __init__(self,driver):
        self.locator = Locators(driver)


    def verify_empty_city_error_message(self):
        self.locator.assertEqual("×\n" + "City must be between 3 and 128 characters!","passworderror_xpath")
