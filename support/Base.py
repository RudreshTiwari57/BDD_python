from selenium import webdriver
from  selenium.webdriver import *
from utilities.configer import configread

class Browser:
    def browser(self,browser):
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        if browser == 'CHROME':
            options = ChromeOptions()
            options.add_argument("--start-maximized")
            self.driver = Chrome(options=options)
        elif browser == 'IE':
            options = IeOptions()
            options.add_argument("--start-maximized")
            self.driver = Ie(options=options)
        elif browser == 'EDGE':
            options = EdgeOptions()
            options.add_argument("--start-maximized")
            self.driver = Edge(options=options)
        elif browser == 'FIREFOX':
            options = FirefoxOptions()
            options.add_argument("--start-maximized")
            self.driver = Firefox(options=options)

        elif browser == 'SAFARI':
            options = webdriver.safari.options.Options()
            options.add_argument("--start-maximized")
            driver = Safari(options=options)

        a = configread()
        self.driver.get(a.configreader("URL","url"))
        return self.driver

