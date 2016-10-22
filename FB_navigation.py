# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class FbNavigation(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://ru-ru.facebook.com")

    def test_login_logout(self):
        driver = self.driver
        facebookUsername = 'veshimed@gmail.com'
        facebookPassword = 'Master-Faceb00k'
        emailFieldID     = 'email'
        passFieldID      = 'pass'
        fbNewsXpath      = '//div[span="Лента новостей"]/span'
        logoutBlokID     = 'userNavigationLabel'
        logoutXPath      = '//input[@value="Выйти"]'

        emailFieldElement = driver.find_element_by_id(emailFieldID)
        passFieldElement = driver.find_element_by_id(passFieldID)
        print(emailFieldElement.get_attribute("name"))

        emailFieldElement.clear()
        emailFieldElement.send_keys(facebookUsername)
        passFieldElement.clear()
        passFieldElement.send_keys(facebookPassword + Keys.RETURN)

        driver.find_element_by_xpath(fbNewsXpath).click()

        driver.find_element_by_id(logoutBlokID).click()
        driver.find_element_by_xpath(logoutXPath).click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()