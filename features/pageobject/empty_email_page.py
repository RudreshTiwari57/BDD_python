from support.locators import Locators


class Empty_email:
    def __init__(self,driver):
        self.locator = Locators(driver)


    def verify_email_error_message(self):

        self.locator.assertEqual("×\n" + "Email Address does not appear to be valid!","passworderror_xpath")
