from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from utilities.configer import configread
from selenium.webdriver.support.select import Select


# d = Chrome()
# d.
class Locators:
    def __init__(self,driver):
        self.driver = driver
        self.file = configread()


    def move_to_element(self,path):
        action = ActionChains(self.driver)
        if str(path).endswith("_id"):
            action.move_to_element(self.driver.find_element(By.ID,self.file.configreader("Locators",path))).perform()
        elif str(path).endswith("_name"):
            action.move_to_element(self.driver.find_element(By.NAME,self.file.configreader("Locators",path))).perform()
        elif str(path).endswith("_class_name"):
            action.move_to_element(self.driver.find_element(By.CLASS_NAME,self.file.configreader("Locators",path))).perform()
        elif str(path).endswith("_tag_name"):
            action.move_to_element(self.driver.find_element(By.TAG_NAME, self.file.configreader("Locators", path))).perform()
        elif str(path).endswith("_xpath"):
            action.move_to_element(self.driver.find_element(By.XPATH, self.file.configreader("Locators", path))).perform()
        elif str(path).endswith("_css_selector"):
            action.move_to_element(self.driver.find_element(By.CSS_SELECTOR, self.file.configreader("Locators", path))).perform()
        elif str(path).endswith("_link-text"):
            action.move_to_element(self.driver.find_element(By.LINK_TEXT, self.file.configreader("Locators", path))).perform()
        elif str(path).endswith("_partia;_link_text"):
            action.move_to_element(self.driver.find_element(By.PARTIAL_LINK_TEXT, self.file.configreader("Locators", path))).perform()
        else:
            print("----------------------------invalide selector---------------------------------")


    def assertEqual(self,actualtext,path):

        if str(path).endswith("_id"):
            assert actualtext == self.driver.find_element(By.ID, self.file.configreader("Locators", path)).text,"both are not same"
        elif str(path).endswith("_name"):
            assert actualtext == self.driver.find_element(By.NAME, self.file.configreader("Locators", path)).text,"both are not same"
        elif str(path).endswith("_class_name"):
            assert actualtext == self.driver.find_element(By.CLASS_NAME, self.file.configreader("Locators", path)).text,"both are not same"
        elif str(path).endswith("_tag_name"):
            assert actualtext == self.driver.find_element(By.TAG_NAME, self.file.configreader("Locators", path)).text,"both are not same"

        elif str(path).endswith("_xpath"):
            assert actualtext == self.driver.find_element(By.XPATH, self.file.configreader("Locators", path)).text,"both are not same"

        elif str(path).endswith("_css_selector"):
            assert actualtext == self.driver.find_element(By.CSS_SELECTOR, self.file.configreader("Locators", path)).text,"both are not same"

        elif str(path).endswith("_link-text"):
            assert actualtext == self.driver.find_element(By.LINK_TEXT, self.file.configreader("Locators", path)).text,"both are not same"

        elif str(path).endswith("_partia;_link_text"):
            assert actualtext == self.driver.find_element(By.PARTIAL_LINK_TEXT, self.file.configreader("Locators", path)).text,"both are not same"
        elif path == "title":
            assert actualtext == self.driver.title,"both are not same"
        else:
            print("----------------------------invalide selector---------------------------------")

    def click(self,path):
        if str(path).endswith("_id"):
            self.driver.find_element(By.ID, self.file.configreader("Locators", path)).click()
        elif str(path).endswith("_name"):
            self.driver.find_element(By.NAME, self.file.configreader("Locators", path)).click()
        elif str(path).endswith("_class_name"):
            self.driver.find_element(By.CLASS_NAME, self.file.configreader("Locators", path)).click()
        elif str(path).endswith("_tag_name"):
            self.driver.find_element(By.TAG_NAME, self.file.configreader("Locators", path)).click()
        elif str(path).endswith("_xpath"):
            self.driver.find_element(By.XPATH, self.file.configreader("Locators", path)).click()
        elif str(path).endswith("_css_selector"):
            self.driver.find_element(By.CSS_SELECTOR, self.file.configreader("Locators", path)).click()
        elif str(path).endswith("_link-text"):
            self.driver.find_element(By.LINK_TEXT, self.file.configreader("Locators", path)).click()
        elif str(path).endswith("_partia;_link_text"):
            self.driver.find_element(By.PARTIAL_LINK_TEXT, self.file.configreader("Locators", path)).click()
        else:
            print("----------------------------invalide selector---------------------------------")


    def send_keys(self,path,values):

        if str(path).endswith("_id"):
            self.driver.find_element(By.ID, self.file.configreader("Locators", path)).send_keys(values)
        elif str(path).endswith("_name"):
            self.driver.find_element(By.NAME, self.file.configreader("Locators", path)).send_keys(values)
        elif str(path).endswith("_class_name"):
            self.driver.find_element(By.CLASS_NAME, self.file.configreader("Locators", path)).send_keys(values)
        elif str(path).endswith("_tag_name"):
            self.driver.find_element(By.TAG_NAME, self.file.configreader("Locators", path)).send_keys(values)
        elif str(path).endswith("_xpath"):
            self.driver.find_element(By.XPATH, self.file.configreader("Locators", path)).send_keys(values)
        elif str(path).endswith("_css_selector"):
            self.driver.find_element(By.CSS_SELECTOR, self.file.configreader("Locators", path)).send_keys(values)
        elif str(path).endswith("_link-text"):
            self.driver.find_element(By.LINK_TEXT, self.file.configreader("Locators", path)).send_keys(values)
        elif str(path).endswith("_partia;_link_text"):
            self.driver.find_element(By.PARTIAL_LINK_TEXT, self.file.configreader("Locators", path)).send_keys(values)
        else:
            print("----------------------------invalide selector---------------------------------")



    def check_checkbox(self,path):
        if str(path).endswith("_id"):
            elements = self.driver.find_elements(By.ID, self.file.configreader("Locators", path))
        elif str(path).endswith("_name"):
            elements = self.driver.find_elements(By.NAME, self.file.configreader("Locators", path))
        elif str(path).endswith("_class_name"):
            elements = self.driver.find_elements(By.CLASS_NAME, self.file.configreader("Locators", path))
        elif str(path).endswith("_tag_name"):
            elements = self.driver.find_elements(By.TAG_NAME, self.file.configreader("Locators", path))
        elif str(path).endswith("_xpath"):
            elements = self.driver.find_elements(By.XPATH, self.file.configreader("Locators", path))
        elif str(path).endswith("_css_selector"):
            elements = self.driver.find_elements(By.CSS_SELECTOR, self.file.configreader("Locators", path))
        elif str(path).endswith("_link-text"):
            elements = self.driver.find_elements(By.LINK_TEXT, self.file.configreader("Locators", path))
        elif str(path).endswith("_partia;_link_text"):
            elements = self.driver.find_elements(By.PARTIAL_LINK_TEXT, self.file.configreader("Locators", path))
        else:
            print("----------------------------invalide selector---------------------------------")

        for i in elements:
           if  i.is_selected():
               i.click()

        for i in elements:
            i.click()


    def assert_isselected(self,path):

        if str(path).endswith("_id"):
            assert True == self.driver.find_element(By.ID, self.file.configreader("Locators", path)).is_selected(), "both are not same"
        elif str(path).endswith("_name"):
            assert True == self.driver.find_element(By.NAME, self.file.configreader("Locators",path)).is_selected(), "both are not same"
        elif str(path).endswith("_class_name"):
            assert True == self.driver.find_element(By.CLASS_NAME, self.file.configreader("Locators",path)).is_selected(), "both are not same"
        elif str(path).endswith("_tag_name"):
            assert True == self.driver.find_element(By.TAG_NAME, self.file.configreader("Locators",path)).is_selected(), "both are not same"

        elif str(path).endswith("_xpath"):
            assert True == self.driver.find_element(By.XPATH, self.file.configreader("Locators",path)).is_selected(), "both are not same"

        elif str(path).endswith("_css_selector"):
            assert True == self.driver.find_element(By.CSS_SELECTOR, self.file.configreader("Locators",path)).is_selected(), "both are not same"

        elif str(path).endswith("_link-text"):
            assert True == self.driver.find_element(By.LINK_TEXT, self.file.configreader("Locators",path)).is_selected(), "both are not same"

        elif str(path).endswith("_partia;_link_text"):
            assert True == self.driver.find_element(By.PARTIAL_LINK_TEXT, self.file.configreader("Locators",path)).is_selected(), "both are not same"
        elif path == "title":
            assert True == self.driver.title, "both are not same"
        else:
            print("----------------------------invalide selector---------------------------------")

    def move_to_element_clcik(self, path):
        action = ActionChains(self.driver)
        if str(path).endswith("_id"):
            action.move_to_element(self.driver.find_element(By.ID, self.file.configreader("Locators", path))).click().perform()
        elif str(path).endswith("_name"):
            action.move_to_element(
                self.driver.find_element(By.NAME, self.file.configreader("Locators", path))).click().perform()
        elif str(path).endswith("_class_name"):
            action.move_to_element(
                self.driver.find_element(By.CLASS_NAME, self.file.configreader("Locators", path))).click().perform()
        elif str(path).endswith("_tag_name"):
            action.move_to_element(
                self.driver.find_element(By.TAG_NAME, self.file.configreader("Locators", path))).click().perform()
        elif str(path).endswith("_xpath"):
            action.move_to_element(
                self.driver.find_element(By.XPATH, self.file.configreader("Locators", path))).click().perform()
        elif str(path).endswith("_css_selector"):
            action.move_to_element(
                self.driver.find_element(By.CSS_SELECTOR, self.file.configreader("Locators", path))).click().perform()
        elif str(path).endswith("_link-text"):
            action.move_to_element(
                self.driver.find_element(By.LINK_TEXT, self.file.configreader("Locators", path))).click().perform()
        elif str(path).endswith("_partia;_link_text"):
            action.move_to_element(
                self.driver.find_element(By.PARTIAL_LINK_TEXT, self.file.configreader("Locators", path))).click().perform()
        else:
            print("----------------------------invalide selector---------------------------------")


    def select_by_index(self, path,value):

        if str(path).endswith("_id"):
            select = Select(self.driver.find_element(By.ID, self.file.configreader("Locators", path)))
        elif str(path).endswith("_name"):
            select = Select(self.driver.find_element(By.NAME, self.file.configreader("Locators", path)))
        elif str(path).endswith("_class_name"):
            select = Select(self.driver.find_element(By.CLASS_NAME, self.file.configreader("Locators", path)))
        elif str(path).endswith("_tag_name"):
            select = Select(self.driver.find_element(By.TAG_NAME, self.file.configreader("Locators", path)))
        elif str(path).endswith("_xpath"):
            select = Select(self.driver.find_element(By.XPATH, self.file.configreader("Locators", path)))
        elif str(path).endswith("_css_selector"):
            select = Select(self.driver.find_element(By.CSS_SELECTOR, self.file.configreader("Locators", path)))
        elif str(path).endswith("_link-text"):
            select = Select(self.driver.find_element(By.LINK_TEXT, self.file.configreader("Locators", path)))
        elif str(path).endswith("_partia;_link_text"):
            select = Select(self.driver.find_element(By.PARTIAL_LINK_TEXT, self.file.configreader("Locators", path)))
        else:
            print("----------------------------invalide selector---------------------------------")
        select.select_by_index(value)


    def select_by_visible_text(self, path,value):

        if str(path).endswith("_id"):
            select = Select(self.driver.find_element(By.ID, self.file.configreader("Locators", path)))
        elif str(path).endswith("_name"):
            select = Select(self.driver.find_element(By.NAME, self.file.configreader("Locators", path)))
        elif str(path).endswith("_class_name"):
            select = Select(self.driver.find_element(By.CLASS_NAME, self.file.configreader("Locators", path)))
        elif str(path).endswith("_tag_name"):
            select = Select(self.driver.find_element(By.TAG_NAME, self.file.configreader("Locators", path)))
        elif str(path).endswith("_xpath"):
            select = Select(self.driver.find_element(By.XPATH, self.file.configreader("Locators", path)))
        elif str(path).endswith("_css_selector"):
            select = Select(self.driver.find_element(By.CSS_SELECTOR, self.file.configreader("Locators", path)))
        elif str(path).endswith("_link-text"):
            select = Select(self.driver.find_element(By.LINK_TEXT, self.file.configreader("Locators", path)))
        elif str(path).endswith("_partia_link_text"):
            select = Select(self.driver.find_element(By.PARTIAL_LINK_TEXT, self.file.configreader("Locators", path)))
        else:
            print("----------------------------invalide selector---------------------------------")
        select.select_by_visible_text(value)



    def select_by_value(self, path,value):

        if str(path).endswith("_id"):
            select = Select(self.driver.find_element(By.ID, self.file.configreader("Locators", path)))
        elif str(path).endswith("_name"):
            select = Select(self.driver.find_element(By.NAME, self.file.configreader("Locators", path)))
        elif str(path).endswith("_class_name"):
            select = Select(self.driver.find_element(By.CLASS_NAME, self.file.configreader("Locators", path)))
        elif str(path).endswith("_tag_name"):
            select = Select(self.driver.find_element(By.TAG_NAME, self.file.configreader("Locators", path)))
        elif str(path).endswith("_xpath"):
            select = Select(self.driver.find_element(By.XPATH, self.file.configreader("Locators", path)))
        elif str(path).endswith("_css_selector"):
            select = Select(self.driver.find_element(By.CSS_SELECTOR, self.file.configreader("Locators", path)))
        elif str(path).endswith("_link-text"):
            select = Select(self.driver.find_element(By.LINK_TEXT, self.file.configreader("Locators", path)))
        elif str(path).endswith("_partia;_link_text"):
            select = Select(self.driver.find_element(By.PARTIAL_LINK_TEXT, self.file.configreader("Locators", path)))
        else:
            print("----------------------------invalide selector---------------------------------")
        select.select_by_value(value)















