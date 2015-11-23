from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import unittest
import login_disney_class as login

jun = "http://watchdisneyjunior.go.com/activate"
xd = "http://watchdisneyxd.go.com/activate"
chan = "http://watchdisneychannel.go.com/activate"


class ActivateDisneyXD(login.ActivateDisney):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(xd)


class ActivateDisneyJun(login.ActivateDisney):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(jun)


class ActivateDisneyChan(login.ActivateDisney):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(chan)


if __name__ == '__main__':
    unittest.main()
