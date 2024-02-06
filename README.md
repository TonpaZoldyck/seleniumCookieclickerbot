# Cookie Clicker Bot

This is a Python web automation script using Selenium to automate the Cookie Clicker game.

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/TonpaZoldyck/seleniumCookieclickerbot.git
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the main script:
   ```bash
   python main.py
   ```

## Project Overview

The project consists of the following components:

- `main.py`: This is the main script that controls the automation process.
- `Classes/Setup.py`: Contains the Setup class responsible for initializing the WebDriver and setting up the Cookie Clicker page.
- `Classes/GameLogic.py`: Contains the GameLogic class responsible for implementing the game logic and automating clicks.
- `Classes/scrapeData.py`: Contains the ScrapingData class responsible for scraping data from the webpage.

## Use
- This is an object oriented Selenium bot which attempts to gain a high score on the cookie clicker game with in 5 minutes.
- Feel free to mess around with the variables and see if the performance of the bot can be optimised based on stratigies for this game.
- Or if you wanna use some of the code for other scraping activities, go for it.

## Additional Information

- The script is designed to run for a specified duration (default is 300 seconds which is 5 minutes) and automatically click on the cookie to increase the cookie count.
- In 5 minutes it is able to gain a cookies per second multiplyer of around ~93.4. 
- It also automatically buys products and upgrades based on predefined logic.
- Make sure to adjust the Chrome driver path in `main.py` according to your system configuration.

## Dependencies

- Python 3.x
- Selenium

## Author

[Tonpa Zoldyck]([https://github.com/YourUsername](https://github.com/TonpaZoldyck))
