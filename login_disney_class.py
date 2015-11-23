from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


link = "http://watchdisneyjunior.go.com/activate"  # link to test site


class ActivateDisney(unittest.TestCase):
    def setUp(self):  # set up the webdriver for Firefox and link to test site
        self.driver = webdriver.Firefox()
        self.driver.get(link)

    def test_activ_code(self):  # start of test
        optimum_username = 'allservices300'  # for the future login to optimum
        optimum_password = '123456'  # for the future login to optimum
        driver = self.driver  # activate webdriver

        roku_select = driver.find_element_by_xpath(
            '//*[@id="avail_devices"]/option[@value="roku"]').click()  # selecting roku device
        driver.implicitly_wait(2)  # seconds

        optimum_select = driver.find_element_by_xpath(
            './/*[@id="avail_mvpds"]/option[@value="Cablevision"]').click()  # selecting optimum provider


if __name__ == '__main__':  # end of test
    unittest.main()
