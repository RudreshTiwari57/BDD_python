from support.Base import Browser
from support.locators import Locators

class Already_registerd_mail(Browser):

    def get(self,browser):
        self.driver = self.browser(browser)
        return self.driver

    def nagavite(self):
        self.locator = Locators(self.driver)
        self.locator.move_to_element("homebutton_xpath")
        self.locator.move_to_element("accountbutton_xpath")
        self.locator.move_to_element_clcik("login_xpath")


    def verify_loginpage(self):
        self.locator.assertEqual("Account Login","title")

    def click_radiobutton(self):
        self.locator.click("register_account_id")

    def click_continue(self):
        self.locator.click("accountcontinuebuttton_xpath")

    def verify_registration(self):
        self.locator.assertEqual("Create Account","title")

    def enter_firstname(self, value):
        self.locator.send_keys("firstname_id", value)

    def enter_lastname(self,value):
        self.locator.send_keys("lastname_id",value)

    def enter_email(self, value):
        self.locator.send_keys("email_id", value)

    def enter_telephone(self, value):
        self.locator.send_keys("telephone_id", value)

    def enter_fax(self, value):
        self.locator.send_keys("fax_id", value)

    def enter_comapnyname(self, value):
        self.locator.send_keys("company_id", value)

    def enter_address_1(self, value):
        self.locator.send_keys("address_1_id", value)

    def enter_address_2(self, value):
        self.locator.send_keys("address_2_id", value)

    def enter_city(self, value):
        self.locator.send_keys("city_id", value)

    def enter_zip_code(self, value):
        self.locator.send_keys("postcode_id", value)

    def enter_loginname(self, value):
        self.locator.send_keys("Loginname_id", value)

    def enter_password(self, value):
        self.locator.send_keys("loginpassword_id", value)

    def enter_confirmpassword(self, value):
        self.locator.send_keys("confirmpassword_id", value)

    def click_policyagrement(self):
        self.locator.check_checkbox("registrationcheckbox_id")

    def verify_checkbox(self):
        self.locator.assert_isselected("registrationcheckbox_id")

    def click_registration_continue(self):
        self.locator.click("registercontinue_xpath")

    def verify_registration_error(self):
        self.locator.assertEqual("×\n" + "Error: E-Mail Address is already registered!","passworderror_xpath")


    def select_country(self,country):
        self.locator.select_by_visible_text("country_id",country)

    def select_state(self,state):
        self.driver.implicitly_wait(3)
        self.locator.select_by_visible_text("state_id",state)







