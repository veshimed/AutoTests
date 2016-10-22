from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest
from selenium.webdriver.support.select import Select
import time


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://facebook.com")

    def test_Login(self):
        driver = self.driver
        facebookUsername = 'veshimed@gmail.com'
        facebookPassword = 'ger-kon'
        emailFieldID     = 'email'
        passFieldID      = 'pass'
        fbNewsXpath      = '//div[span="Лента новостей"]/span'
        logoutBlokID     = 'userNavigationLabel'
        logoutXPath      = '//input[@value="Выйти"]'

        blockDown = driver.find_element_by_id('month')
        Select(blockDown).select_by_visible_text("May")
        time.sleep(8)

        """emailFieldElement = driver.find_element_by_id(emailFieldID)
        passFieldElement = driver.find_element_by_id(passFieldID)

        emailFieldElement.clear()
        emailFieldElement.send_keys(facebookUsername)
        passFieldElement.clear()
        passFieldElement.send_keys(facebookPassword + Keys.RETURN)

        driver.find_element_by_xpath(fbNewsXpath).click()


        driver.find_element_by_id(logoutBlokID).click()
        driver.find_element_by_xpath(logoutXPath).click()"""


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()




