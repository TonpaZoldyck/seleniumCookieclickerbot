from Classes.Setup import Setup
from Classes.GameLogic import GameLogic
from Classes.scrapeData import ScrapingData
import time


# VARIABLES
DURATION_SECONDS: int = 300  # set timer for 5 minutes or however long you need
COUNTER: int = 0
CHECKING_THRESHOLD: int = 100  # check after this many loops - make it increase by a factor
INCREASE_FACTOR: float = 1.1

start_time = time.time()  # initialise timer

if __name__ == "__main__":
    chrome_driver_path = r"C:\Users\hamid\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"

    # use the setup class to set up the cookie clicker page
    setup = Setup(chrome_driver_path)
    setup.initialize_driver()
    setup.consent_to_cookies()
    setup.select_english_language()
    setup.click_got_it()

    # scrape some initial checking data from the webpage before starting the clicker loop
    scraping_data = ScrapingData(setup.driver)
    current_prices = scraping_data.check_current_prices()

    # initialise the gameLogic Class
    logic = GameLogic(setup.driver, scraping_data)
    logic.products_logic()


    while True:

        # Check if the elapsed time exceeds the duration
        if time.time() - start_time > DURATION_SECONDS:
            cookies_per_second = scraping_data.get_cookies_per_sec()
            print(f'The final Cookies per second is {cookies_per_second}')
            break  # Exit the loop if 5 minutes have elapsed

        logic.click_cookie()

        current_cookies = scraping_data.get_current_cookies()
        COUNTER += 1
        # print(checking_threshold)
        if COUNTER % CHECKING_THRESHOLD == 0:

            CHECKING_THRESHOLD = int(CHECKING_THRESHOLD * INCREASE_FACTOR)
            print(f'Checking threshold: {CHECKING_THRESHOLD}| Counter')
            print(
                f'Checking threshold: {CHECKING_THRESHOLD}| Current loop: {COUNTER}| Current Cookies: {current_cookies}'
            )

            # If we are in an even loop then prioritise buying products else buy the upgrades first
            if COUNTER % 2 == 0:
                logic.products_logic()
                logic.try_buy_upgrades()

            else:
                logic.try_buy_upgrades()
                logic.products_logic()
