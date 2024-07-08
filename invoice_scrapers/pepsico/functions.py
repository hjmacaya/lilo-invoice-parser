"""
Module to store all the functions
"""
import pandas as pd
from datetime import datetime

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

        orders_urls = [a_tag.get_attribute('href') for a_tag in a_tags] if a_tags else []
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
    return subtotal.strip()

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
    return address.strip()

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
    return total_tax.strip()

def extract_total(soup):
    """Function to extract the total of the order"""
    total_div = soup.find('div', class_='item-group total')
    span_value = total_div.find('span', class_='item-value')
    total = span_value.text if span_value else ""
    return total.strip()

def reformat_date(date_str):
    # Extract the date part
    date_part = date_str.split()[1]

    # Parse the date part into a datetime object
    date_obj = datetime.strptime(date_part, "%m/%d/%Y")

    # Reformat the date to MM/DD/YYYY
    formatted_date = date_obj.strftime("%m/%d/%Y")

    return formatted_date

def extract_order_date(soup):
    """Function to extract the date of the order"""
    # Extract the date
    date_span = soup.find('span', id='orderdetails_placeddate')
    date = date_span.text if date_span else ""

    # Process the date
    if date != "":
        date = reformat_date(date)

    return date.strip()

def extract_order_items(soup):
    """Function to extract the items of an order"""
    orders_table = soup.find('table', class_='detailOrderHistory')
    tbody = orders_table.find('tbody') if orders_table else None
    item_trs = tbody.find_all('tr', class_='responsive-table-item') if tbody else []
    return item_trs

def extract_product_title(item_tr):
    """Function to extract the title of a product"""
    title_span = item_tr.find('span', class_='item-name')
    title = title_span.text if title_span else ""
    return title.strip()

def extract_product_case_pack_size(item_tr):
    """Function to extract the case and pack size of a product"""
    sizes_div = item_tr.find_all('div', class_='item-unit-package')
    for div in sizes_div:
        if 'Case' in div.text:
            case_pack_size_div = div
        else:
            pack_size_div = div

    # Set case size
    case_pack_size_span = case_pack_size_div.find('span')
    case_pack_size = case_pack_size_span.text if case_pack_size_span else ""

    # Set the pack size
    pack_size_span = pack_size_div.find('span')
    pack_size = pack_size_span.text if pack_size_span else ""

    return case_pack_size.strip(), pack_size.strip()

def extract_product_sku_and_upc(item_tr):
    """Function to extract the SKU and UPC of a product"""
    skus_divs = item_tr.find_all('div', class_='item-sku')
    for div in skus_divs:
        if 'SKU' in div.text:
            sku_div = div
        else:
            upc_div = div

    # Set the SKU
    sku_span = sku_div.find('span')
    sku = sku_span.text if sku_span else ""

    # Set the UPC
    upc_span = upc_div.find('span')
    upc = upc_span.text if upc_span else ""

    return sku.strip(), upc.strip()

def extract_product_quantity(item_tr):
    """Function to extract the ordered qty of a product"""
    qty_div = item_tr.find('div', class_='item-quantity')
    qty_span = qty_div.find('span', class_='qtyValue')
    qty = qty_span.text if qty_span else ""
    return qty.strip()

def extract_unit_price(item_tr):
    """Function to extract the unit price of a product"""
    unit_price_span = item_tr.find('span', class_='item-unit-price')
    unit_price = unit_price_span.text if unit_price_span else ""
    return unit_price.strip()

def extract_product_price(item_tr):
    """Function to extract the product price"""
    price_div = item_tr.find('div', class_='item-total')
    price = price_div.text if price_div else ""
    return price.strip()

def extract_items_data(order_items, order_id):
    """Function to extract the data of the items of an order"""
    items_data = []
    for item in order_items:
        item_data = {}

        # Set the order id and description
        item_data['OrderId'] = order_id
        item_data['ProductDescription'] = extract_product_title(item)

        # Extract sizes
        case_size, pack_size = extract_product_case_pack_size(item)
        item_data['CaseSize'] = case_size
        item_data['PackSize'] = pack_size

        # Extract SKU and UPC
        item_data['SKU'], item_data['UPC'] = extract_product_sku_and_upc(item)

        # Extract quantity and prices
        item_data['OrderedQuantity'] = extract_product_quantity(item)
        item_data['UnitPrice'] = extract_unit_price(item)
        item_data['Price'] = extract_product_price(item)

        items_data.append(item_data)
    return items_data

def extract_order_data(soup):
    """Function to extract the data of an order"""
    order_data = {}
    items = []

    # Extact general data
    order_data['VendorName'] = 'Pepsico'
    order_data['OrderId'] = extract_order_id(soup)
    order_data['Subtotal'] = extract_subtotal(soup)
    order_data['ShippingAddress'] = extract_shipping_address(soup)
    order_data['TotalTax'] = extract_total_tax(soup)
    order_data['Total'] = extract_total(soup)
    order_data['OrderDate'] = extract_order_date(soup)

    # Extract the items of the order
    order_items = extract_order_items(soup)
    items = extract_items_data(order_items, order_data['OrderId'])

    # Save the data
    fields_df = pd.DataFrame([order_data])
    items_df = pd.DataFrame(items)
    ut.write_in_excel_file(p.OUTPUT_PATH, fields_df, items_df)

def get_order_data(driver, order_url):
    """Function to get the data of an order of Pepsico"""
    try:
        driver.get(order_url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'detailOrderHistory'))
        )

        # Get soup
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Extract and save the data
        extract_order_data(soup)

    except (TimeoutException, NoSuchElementException) as e:
        print(f"Error while extracting the data: {e}")

        # TODO: Add logic to handle the error and/or saving the order url with the error
