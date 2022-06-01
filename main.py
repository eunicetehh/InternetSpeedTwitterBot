from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

PROMISED_DOWN = 30
PROMISED_UP = 40
CHROME_DRIVER_PATH = "C:\\Users\\User\\Downloads\\chromedriver.exe"
TWITTER_EMAIL = "hasdfgjd@gmail.com"
TWITTER_PASSWORD = "Zeu)K\"78"
id = "internetBot29"


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

    def tweet_at_provider(self):
        pass


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
