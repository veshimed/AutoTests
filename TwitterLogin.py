import unittest
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TweetterLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://twitter.com")

    def test_search(self):
        driver = self.driver

        tweetter_username = 'S_test_user_'
        tweetter_password = 'test-user'
        text_in_tweet = 'Hi! It is a test from ' + str(datetime.datetime.today())

        email_field_element = driver.find_element_by_id('signin-email')
        email_field_element.clear()
        email_field_element.send_keys(tweetter_username)
        pass_field_element = driver.find_element_by_id('signin-password')
        pass_field_element.clear()
        pass_field_element.send_keys(tweetter_password + Keys.RETURN)

        tweet_button_elem = driver.find_element_by_id('global-new-tweet-button').click()
        tweet_box_elem = driver.find_element_by_id('tweet-box-global')
        tweet_box_elem.clear()
        tweet_box_elem.send_keys(text_in_tweet)
        tweet_submit_button = driver.find_element_by_xpath(
            ".//*[@id='global-tweet-dialog-dialog']/div[2]/div[4]/form/div[2]/div[2]/button").click()

        follow_button = driver.find_element_by_xpath(
            ".//*[@id='page-container']/div[1]/div[2]/div/div[2]/div[2]/div[2]/div/button").click()


if __name__ == '__main__':
    unittest.main()
