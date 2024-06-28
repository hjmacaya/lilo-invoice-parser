""""
Modue to store the utils functions
"""
# GLOBAL IMPORTS
import os
import csv
import time
from random import randint
from requests import Session
import pandas as pd

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

def get_cookies(driver):
    """Function to get the cookies"""
    selenium_cookies = driver.get_cookies()
    cookies = {}
    for cookie in selenium_cookies:
        cookies[cookie['name']] = cookie['value']
    return cookies

def get_headers():
    """Function to get the headers"""
    headers = {
            'accept': '*/*',
            'accept-language': 'es-419,es;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'priority': 'u=1, i',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
    }
    return headers

def get_params():
    """Function to get the params"""
    params = {
        'expand': 'orderLines,shipments',
    }
    return params

def set_up_session(driver):
    """
    Function to set up the request session
    1. Get the cookies
    2. Set the headers
    3. Set the params
    """
    cookies = get_cookies(driver)
    headers = get_headers()
    params = get_params()
    session = Session()
    session.headers.update(headers)
    session.cookies.update(cookies)
    session.params.update(params)
    return session

def append_to_excel(writer, df, sheet_name, output_path):
    """Function to append a DataFrame to an excel file"""
    try:
        old_df = pd.read_excel(output_path, sheet_name=sheet_name)
        print("Found old df")
        new_df = pd.concat([old_df, df], ignore_index=True)
    except FileNotFoundError:
        new_df = df
    except ValueError:
        new_df = df
    new_df.to_excel(writer, sheet_name=sheet_name, index=False)

def write_in_excel_file(output_path, fields_df, products_df):
    """Function to write in the excel file"""
    try:
        with pd.ExcelWriter(output_path, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
            append_to_excel(writer, fields_df, 'InvoiceData', output_path)
            append_to_excel(writer, products_df, 'ProductsData', output_path)
    except FileNotFoundError:
        with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
            append_to_excel(writer, fields_df, 'InvoiceData', output_path)
            append_to_excel(writer, products_df, 'ProductsData', output_path)
