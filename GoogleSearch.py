import unittest
import datetime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class GoogleSearchChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C://chromedriver")
        self.screen_name = (
            'Screenshots/Chrome.GoogleSearch.' + str(datetime.datetime.today()) + '.jpg'
        ).replace(':', '.')

    def test_search(self):
        driver = self.driver
        driver.get("https://www.google.com")

        self.assertIn("Google", driver.title)
        search_field = driver.find_element_by_id("lst-ib")
        search_field.clear()
        search_field.send_keys("Love is..." + Keys.RETURN)

        driver.implicitly_wait(10)  # seconds
        img = driver.find_element_by_xpath('//*[@id="hdtb-msb"]/div[2]/a').click()
        driver.implicitly_wait(10)  # seconds
        driver.find_element_by_xpath('//*[@id="rg_s"]/div[15]/a/img')
        if ("No result found" in driver.page_source):
            driver.save_screenshot(self.screen_name)
            print(self.screen_name)
            self.fail()

    def tearDown(self):
        self.driver.quit()


class GoogleSearchFF(GoogleSearchChrome):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.screen_name = ('Screenshots/FF.GoogleSearch.' + str(datetime.datetime.today()) + '.jpg').replace(':', '.')


if __name__ == "__main__":
    unittest.main()
