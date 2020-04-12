from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('http://twitter.com/login')


class TwitterBot:
    def __init__(self, username, password, tweet_text):
        self.username = username
        self.password = password
        self.tweet_text = tweet_text

        time.sleep(20)

        # Get the username input field and enter a username, email or phonenumber
        driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input').send_keys(self.username)

        # Get the password input field and enter a password
        driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input').send_keys(self.password)

        # Get the login button and click it
        driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[3]/div/div').click()
        # Pause as the login process happends
        time.sleep(10)

        # After login, click the Tweet button/icon in order to pop up a tweet field
        driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div/div[3]/a/div').click()
        # Pause while it happens
        time.sleep(5)

        # Find the tweet input field and enter the tweet text
        driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div').send_keys(self.tweet_text)
        time.sleep(3)

        # Tweet by clicking the tweet button
        driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]').click()


# Enter username, email or phonenumber | password | Tweet text
twitter_user = TwitterBot('', '', '')
