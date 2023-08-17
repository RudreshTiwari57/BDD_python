from support.locators import Locators


class Unavilable_loginname:
    def __init__(self,driver):
        self.locator = Locators(driver)
    def verify_unavilable_loginname_error_message(self):
        self.locator.assertEqual("×\n" + "This login name is not available. Try different login name!","passworderror_xpath")
