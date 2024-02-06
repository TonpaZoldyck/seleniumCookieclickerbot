from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By


class Setup:
    def __init__(self, driver_path=r"C:\Users\hamid\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.chrome_driver_path = driver_path
        self.driver = None

    def initialize_driver(self):
        self.driver = webdriver.Chrome(options=self.chrome_options, executable_path=self.chrome_driver_path)
        self.driver.maximize_window()
        self.driver.get("https://orteil.dashnet.org/cookieclicker/")

    def consent_to_cookies(self):
        consent_button = self.driver.find_element_by_class_name("fc-button-label")
        consent_button.click()

    def select_english_language(self):
        wait = WebDriverWait(self.driver, 5)  # Adjust timeout as needed
        try:
            english_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#langSelect-EN")))
            english_button.click()
        except TimeoutException:
            print("Timeout occurred while waiting for the English button.")

    def click_got_it(self):
        wait = WebDriverWait(self.driver, 5)  # Adjust timeout as needed
        try:
            got_it_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/a[1]")))
            got_it_button.click()
        except StaleElementReferenceException:
            # Element reference is stale, retry finding the element
            print("StaleElementReferenceException occurred. Retrying...")
            self.click_got_it()  # Recursively call click_got_it to retry
        except TimeoutException:
            print("Timeout occurred while waiting for the English button.")
