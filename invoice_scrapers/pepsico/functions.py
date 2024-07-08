"""
Module to store all the functions
"""
import pandas as pd

# Selenium imports
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException

# Internal imports
import parameters as p
import utils as ut
###################################### SCRAPING FUNCTIONS ######################################
def login_to_pepsico(driver, url, username, password):
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class*="loginDD"]')))

        print('Signing in...')
        print('Clicking on login overlay...')
        log_in_div = driver.find_element(By.CSS_SELECTOR, 'div[class*="loginDD"]')
        nav_section_span = log_in_div.find_element(By.CSS_SELECTOR, 'span[class*="navSection"]')
        nav_section_span.click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[class*="login_overlay"]')))
        log_in_overlay = driver.find_element(By.CSS_SELECTOR, 'div[class*="login_overlay"]')

        print('Submitting credentials...')
        username_input = driver.find_element(By.CSS_SELECTOR, 'input[id="j_username"]')
        password_input = driver.find_element(By.CSS_SELECTOR, 'input[id="j_password"]')

        username_input.send_keys(username)
        password_input.send_keys(password)

        remember_me_checkbox = driver.find_element(By.CSS_SELECTOR, 'input[class*="login_remember"]')
        remember_me_checkbox.click()

        print('Accepting terms...')
        terms_checkbox = driver.find_element(By.CSS_SELECTOR, 'input[class*="login_terms"]')
        terms_checkbox.click()

        print('Clicking submit button...')
        submit_button = log_in_overlay.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        submit_button.click()

        # Check if login was a succes or not
        nav_menu = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'nav[class="navigation"]'))
        )
        if nav_menu:
            print('Login was a success!')
            return True
        print('Login failed :(')
        return False

    except (TimeoutException, NoSuchElementException) as e:
        print(f"Error: {e}")
        return False

def go_to_order_history_page(driver):
    """Function to navigate to the order history page"""
    try:
        # Get url and go to it
        print('Navigating to order history page...')
        order_history_atag = driver.find_element(By.CSS_SELECTOR, 'a[data-title="Order History"]')
        order_history_link = order_history_atag.get_attribute('href')
        driver.get(order_history_link)

        # Check if we are in the order history page
        in_login_page = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'accountOrderHistoryDataTable_wrapper'))
        )
        if in_login_page:
            print('In order history page')
            return True
        print('Not in order history page')
        return False

    except (TimeoutException, NoSuchElementException) as e:
        print(f"Error: {e}")
        return False

def get_the_urls(driver):
    """Function to get the urls of the orders"""
    try:
        # Get the links
        print('Getting the order urls...')
        a_tags = driver.find_elements(By.CLASS_NAME, 'responsive-table-link')

        orders_urls = [a_tag['href'] for a_tag in a_tags] if a_tags else []
        return orders_urls

    except (TimeoutException, NoSuchElementException) as e:
        print(f"Error: {e}")
        return []

def extract_order_id(soup):
    """Function to extract the order id"""
    order_id = soup.find('input', id='siebelOrderid')
    order_id = order_id['value'] if order_id else ""
    return order_id

def extract_subtotal(soup):
    """Function to extract the subtotal of an order"""
    all_items_groups = soup.find_all('div', class_='item-group')

    # Find the subtotal div
    for group in all_items_groups:
        if 'Sub Total' in group.text:
            subtotal_group = group
            break

    # Extract the subtotal
    span_value = subtotal_group.find('span', class_='item-value')
    subtotal = span_value.text if span_value else ""
    return subtotal

def extract_shipping_address(soup):
    """Function to extract the shipping address of an order"""
    address_divs = soup.find_all('div', class_='deliveryAddress')

    # The address div is the one withoud hide class
    for div in address_divs:
        if 'hide' not in div['class']:
            address_div = div
            break

    # Extract the address
    div_value = address_div.find('div', class_='col-value')
    address = div_value.text if div_value else ""
    return address

def extract_total_tax(soup):
    """Funtion to extract the total tax of an order"""
    all_items_groups = soup.find_all('div', class_='item-group')

    # Find the total tax div
    for group in all_items_groups:
        if 'Tax' in group.text:
            total_tax_group = group
            break

    # Extract the total tax
    span_value = total_tax_group.find('span', class_='item-value')
    total_tax = span_value.text if span_value else ""
    return total_tax

def extract_total(soup):
    """Function to extract the total of the order"""
    total_div = soup.find('div', class_='item-group total')
    span_value = total_div.find('span', class_='item-value')
    total = span_value.text if span_value else ""
    return total


def extract_order_data(soup):
    """Function to extract the data of an order"""
    order_data = {}

    # Extact data
    order_data['OrderId'] = extract_order_id(soup)
    order_data['Subtotal'] = extract_subtotal(soup)
    order_data['ShippingAddress'] = extract_shipping_address(soup)

def get_order_data(driver, order_url):
    """Function to get the data of an order of Pepsico"""
    try:
        driver.get(order_url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'detailOrderHistory'))
        )

        # Get soup
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        order_data = extract_order_data(soup)
        return order_data
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Error: {e}")
        return None
