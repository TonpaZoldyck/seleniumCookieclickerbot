from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException


class ScrapingData:
    def __init__(self, driver):
        self.driver = driver
        self.product = 0
        self.xpath = f'//*[@id="productPrice{self.product}"]'

    @staticmethod
    def parse_price_string(price_text):
        # Define multipliers for each magnitude
        multipliers = {
            'thousand': 1e3,
            'million': 1e6,
            'billion': 1e9,
            'trillion': 1e12,
            'quadrillion': 1e15,
            'quintillion': 1e18,
            'sextillion': 1e21,
            'septillion': 1e24
        }
        if '.' in price_text:
            # If the price contains a decimal point, split it into parts
            parts = price_text.split('.')
            if len(parts) == 2:
                # Extract the numerical part before the decimal point
                numeric_part = parts[0]
                # Extract the multiplier (e.g., "million", "billion")
                multiplier = parts[1].strip().lower()
                # Check if the multiplier is valid
                if multiplier in multipliers:
                    # Multiply the numerical part by the corresponding multiplier
                    return int(float(numeric_part) * multipliers[multiplier])
        elif price_text == '':
            return None

        elif ' ' in price_text:
            # split text on the space delimiter
            parts = price_text.split(' ')
            # Extract the numerical part before the decimal point
            numeric_part = parts[0]
            # Extract the multiplier (e.g., "million", "billion")
            multiplier = parts[1].strip().lower()
            # Check if the multiplier is valid
            if multiplier in multipliers:
                # Multiply the numerical part by the corresponding multiplier
                return int(float(numeric_part) * multipliers[multiplier])
        else:
            try:
                return int(price_text)
            except ValueError:
                print('not a valid int value')
                pass

    def get_current_cookies(self):
        try:
            cookies_element = self.driver.find_element(By.ID, "cookies")
            cookies_text = cookies_element.text
            cookies_text = cookies_text.split(' cookies')[0]
            # print(f'Current Cookies Text:{cookies_text}')
            try:
                if ',' in cookies_text:
                    # Handle format like "1,000"
                    current_cookies = cookies_text.replace(",", "")
                    return int(current_cookies)

                elif '.' in cookies_text:
                    parts = cookies_text.split('.')
                    current_cookies_part = parts[0].strip()  # Extract numerical part before the decimal point

                    # Extract the multiplier (e.g., "million", "billion")
                    multiplier = parts[1].strip().lower()
                    if multiplier == 'million':
                        current_cookies = float(current_cookies_part) * 1e6
                    elif multiplier == 'billion':
                        current_cookies = float(current_cookies_part) * 1e9
                    elif multiplier == 'trillion':
                        current_cookies = float(current_cookies_part) * 1e12
                    else:
                        raise ValueError("Invalid multiplier")

                    return int(current_cookies)

                elif ' ' in cookies_text:
                    # Handle format like "10 cookies"
                    current_cookies = cookies_text.split()[0].replace(" ", "")
                    return int(current_cookies)

                elif ' ' not in cookies_text:
                    return int(cookies_text)
            except (IndexError, ValueError) as e:
                print(f"Error parsing cookies text: {e}")
                return None
        except TimeoutException:
            print("Timeout occurred while waiting for cookies element.")
            return None

    def get_current_price(self, xpath):
        try:
            price_element = self.driver.find_element(By.XPATH, xpath)
            price_text = price_element.text

            # handle comma in the text if there is one
            price_text = price_text.replace(",", "")

            # handle prices that are in "millions" e.g. 14.9 million
            price = self.parse_price_string(price_text)
            return price
        except NoSuchElementException:
            print(f"Element with xpath {xpath} not found.")
            return None
        except StaleElementReferenceException:
            print("Stale Element exception found")
            pass

    def check_current_prices(self):
        current_prices = []
        for product in range(19):
            self.product = product
            self.xpath = f'//*[@id="productPrice{product}"]'
            price = self.get_current_price(xpath=self.xpath)
            current_prices.append(price)
        return current_prices

    def get_cookies_per_sec(self):
        try:
            cookies_element = self.driver.find_element(By.ID, "cookies")
            cookies_per_sec = cookies_element.text
            cookies_per_sec = cookies_per_sec.split(' cookies')[1]
            return cookies_per_sec

        except:
            pass
