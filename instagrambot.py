from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

import wget


driver = webdriver.Chrome()

driver.get('http://instagram.com')

time.sleep(5)

# print('Sleeping is Over')


class InstagramBot:
    def __init__(self, user_name, password, hashtag):
        self.user_name = user_name
        self.password = password
        self.hashtag = hashtag

        driver.find_element_by_name('username').send_keys(self.user_name)
        time.sleep(4)

        driver.find_element_by_name('password').send_keys(self.password)
        time.sleep(4)

        self.btn_login = driver.find_element_by_xpath(
            '//button[@type="submit"]').click()
        time.sleep(5)

        driver.find_element_by_xpath(
            '/html/body/div[4]/div/div/div[3]/button[2]').click()

        time.sleep(10)

        search_input_field = driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        time.sleep(2)

        search_input_field.send_keys(self.hashtag)
        search_input_field.send_keys(Keys.ENTER)
        time.sleep(10)

        driver.find_element_by_class_name('z556c').click()
        time.sleep(12)

        uploaded_image = driver.find_element_by_class_name('FFVAD')
        # print(uploaded_image)

        image_count = 0
        for i in driver.find_elements_by_class_name('FFVAD'):
            if(image_count < 3):
                # insta_img = driver.find_elements_by_class_name('FFVAD')

                src = i.get_attribute('src')
                wget.download(src)
                # print(src)

                image_count += 1


# KL4Bh KL4Bh

# username or email | password | instagram username
client1 = InstagramBot("", "", '')
# https://stackoverflow.com/questions/27006698/selenium-iterating-through-groups-of-elements
# download image - https://stackoverflow.com/questions/17361742/download-image-with-selenium-python
