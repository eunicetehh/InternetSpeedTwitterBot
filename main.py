import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PROMISED_DOWN = 30
PROMISED_UP = 40
CHROME_DRIVER_PATH = "C:\\Users\\User\\Downloads\\chromedriver.exe"
TWITTER_PASSWORD = "Zeu)K\"78"
TWITTER_ID = "internetbot123"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        s = Service(driver_path)
        self.browser = webdriver.Chrome(service=s)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        url = 'https://www.speedtest.net/'
        self.browser.get(url)
        self.browser.find_element(by=By.CLASS_NAME, value="start-button").click()
        time.sleep(50.0)

        self.up = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]'
                           '/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span'))).text
        self.down = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]'
                           '/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span'))).text

    def tweet_at_provider(self):
        url = 'https://twitter.com/login'
        self.browser.get(url)
        time.sleep(5)
        input_element = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.NAME, 'text')))
        input_element.send_keys(TWITTER_ID)
        self.browser.find_element(by=By.XPATH,
                                  value="//*[@id=\"layers\"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div["
                                        "2]/div[2]/div/div/div/div[6]/div").click()
        input_pswd = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.NAME, 'password')))
        input_pswd.send_keys(TWITTER_PASSWORD)
        self.browser.find_element(by=By.XPATH,
                                  value="//*[@id=\"layers\"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div["
                                        "2]/div[2]/div[2]/div/div[1]/div/div/div").click()
        time.sleep(10)
        input_tweet = self.browser.find_element(by=By.XPATH,
                                                value="//*[@id=\"react-root\"]/div/div/div["
                                                      "2]/main/div/div/div/div/div/div[ "
                                                      "2]/div/div[2]/div[1]/div/div/div/div[2]/div["
                                                      "1]/div/div/div/div/div/div/div/div/div/label/div["
                                                      "1]/div/div/div/div/div[ "
                                                      "2]/div/div/div/div")
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up? "
        time.sleep(10)
        input_tweet.send_keys(tweet)
        # WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.NAME, "//*[@id=\"react-root\"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span")))
        self.browser.find_element(by=By.XPATH,
                                  value="//*[@id=\"react-root\"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div").click()


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
