from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException, \
    NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GameLogic:
    def __init__(self, driver, scraping_data):
        self.driver = driver
        self.scraping_data = scraping_data

    def click_cookie(self):
        cookie = self.driver.find_element(By.CSS_SELECTOR, "button#bigCookie")
        cookie.click()


    @staticmethod
    def locate_element(driver, by, xpath):
        try:
            return WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((by, xpath))
            )
        except (TimeoutException, StaleElementReferenceException):
            return None

    def buy_products(self, xpath):
        try:
            product_to_buy = self.locate_element(self.driver, By.XPATH, xpath)
            if product_to_buy is not None:
                product_to_buy.click()
        except ElementClickInterceptedException:
            # Handle ElementClickInterceptedException
            print("Element click intercepted. Skipping click.")
        except ElementNotInteractableException:
            # Handle ElementNotInteractableException
            print("Element not interactable. Skipping click.")
        except NoSuchElementException:
            # Handle NoSuchElementException
            print("Element not found. Skipping click.")

    def products_logic(self):

        # scrape the list of current prices using the scrape date module
        # the key for the list is the name in the div and the element is the current price
        current_prices = self.scraping_data.check_current_prices()


        # get the current cookie count
        current_cookies = self.scraping_data.get_current_cookies()

        # print(f'Current Prices{current_prices}; Current Cookies:{current_cookies}')

        # loop through each of these ## LOOP THROUGH LIST BACKWARDS TO LOOK AT MORE EXPENSIVENESS ITEMS FIRST
        for key, element in reversed(list(enumerate(current_prices))):
            if element is not None and current_cookies > 2 * element:
                # assert isinstance(element, object)
                xpath = f'//*[@id="product{key}"]'  # this is the path to click - the other path is the path for the
                # price text
                # print(xpath)
                # print(element)

                self.buy_products(xpath=xpath)

    def try_buy_upgrades(self):
        upgrade_elements = self.driver.find_elements(By.CSS_SELECTOR, "div.upgrade.enabled")

        for upgrade_element in upgrade_elements:
            try:
                upgrade_element.click()
                print(f'Upgrade Bought {upgrade_element.text}')
                # # Optional: You may want to wait for the upgrade to be processed before continuing
                # WebDriverWait(self.driver, 5).until(
                #     EC.staleness_of(upgrade_element)
                # )
            except (NoSuchElementException, StaleElementReferenceException, TimeoutException):
                # Handle exceptions if upgrade cannot be clicked or processed
                pass
