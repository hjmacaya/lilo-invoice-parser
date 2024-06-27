""""
Modue to store the utils functions
"""
# GLOBAL IMPORTS
import os
import csv
import time
from random import randint

# SELENIUM IMPORTS
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def save_in_csv(data_dict, path):
    """Function to save data in a csv"""
    first_write = not os.path.exists(path)
    with open(path, 'a', newline='', encoding='utf-8') as file:
        if first_write:
            writer = csv.writer(file)
            writer.writerow(data_dict.keys())
        writer = csv.writer(file)
        writer.writerow([data_dict[key] for key in data_dict.keys()])

def set_up_chrome_options():
    """Function to set up the chrome options"""
    print('Setting up chrome options...')
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Runs Chrome in headless mode.
    chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
    chrome_options.add_argument("--disable-dev-shm-usage") # Overcome limited resource problems
    chrome_options.add_experimental_option(
        "prefs",
        {"profile.managed_default_content_settings.images": 2}
        )
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("--disable-javascript")
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')
    chrome_options.add_argument('--log-level=3') # Minimal logs in console (only fatal errors)
    return chrome_options

def set_up_driver():
    """Function to set up the driver"""

    # Set up options
    options = set_up_chrome_options()

    # Set up driver
    print("Setting up driver")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    print("Finish setting up driver")

    return driver

def webdriver_wait_page(driver, wait_time, by, element):
    """Function to wait for the page to load"""
    WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((by, element)))

def wait_random_time():
    """Funtion to wait a random time"""
    random_wait_time = randint(1, 2)
    print(f"Waiting {random_wait_time} seconds before scraping...")
    time.sleep(random_wait_time)

def my_find_element(driver, by, element):
    """Custom function to find element using selenium"""
    try:
        return WebDriverWait(
            driver, 10
        ).until(
            EC.presence_of_element_located((by, element))
        )
    except TimeoutException:
        print(f"Timeout while waiting for element {element}")
        return None
    except NoSuchElementException:
        print(f"No such element {element}")
        return None
