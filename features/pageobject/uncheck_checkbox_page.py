from support.locators import Locators


class Unchecked_checkbox:
    def __init__(self,driver):
        self.locator = Locators(driver)
    def verify_uncheckeb_checkbox_error_message(self):
        self.locator.assertEqual("×\n" + "Error: You must agree to the Privacy Policy!","passworderror_xpath")
