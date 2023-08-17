from support.locators import Locators


class Empty_missmatch_password:
    def __init__(self,driver):
        self.locator = Locators(driver)
    def verify_missmatch_password_error_message(self):
        self.locator.assertEqual("×\n" + "Password confirmation does not match password!","passworderror_xpath")
