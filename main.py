from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

chrome_driver_path = ("C:\Developement\chromedriver.exe")
SIMILAR_ACCOUNT = your instagram account you want become
EMAIL = your email
PASSWORD = your password

class InstaFollowers:
    def __init__(self,path):
        self.driver = webdriver.Chrome(executable_path = path)


    def login(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(5)
        email = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        email.click()
        password = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.click()
        email.send_keys(EMAIL)
        password.send_keys(PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)
    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        time.sleep(3)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        time.sleep(3)
        modal = self.driver.find_element_by_css_selector('.isgrP')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight",modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector('li button')
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollowers(chrome_driver_path)
bot . login()
bot . find_followers()
bot . follow()
