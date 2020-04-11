# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# browser = webdriver.Chrome()

# browser.get('https://www.selenium.dev/')

# elem = browser.find_element_by_link_text('Downloads')
# elem.click()

# search_input = browser.find_element_by_id('gsc-i-id1')
# search_input.send_keys('the code artisan')
# search_input.send_keys(Keys.ENTER)

import wget

img_url = "https://instagram.febb1-1.fna.fbcdn.net/v/t51.2885-15/sh0.08/e35/s640x640/91832507_150747899645424_5714958336507882933_n.jpg?_nc_ht=instagram.febb1-1.fna.fbcdn.net&_nc_cat=100&_nc_ohc=Tf3xaNc3fPwAX8ajSFD&oh=0f378ec7791c0e4d75c03bae2f3da488&oe=5EBD7AE1"
wget.download(img_url)
