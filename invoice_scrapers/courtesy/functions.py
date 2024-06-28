"""
Module to store the functions
"""
import pandas as pd

# Selenium imports
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException

# Internal imports
import parameters as p
import utils as ut

# Scraping functions
def login_to_courtesy(driver, url, username, password):
    """Function to login to Courtesy"""
    try:
        # Get the website url
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-test-selector*="header_signIn"]')))

        # Get the link to the login page
        login_url = driver.find_element(By.CSS_SELECTOR, 'a[data-test-selector*="header_signIn"]')
        driver.get(login_url.get_attribute('href'))
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'form')))

        # Get the form
        form_element = driver.find_element(By.CSS_SELECTOR, 'form')
        user_input = form_element.find_element(By.CSS_SELECTOR, 'input[data-test-selector="signIn_userName"]')
        password_input = form_element.find_element(By.CSS_SELECTOR, 'input[data-test-selector="signIn_password"]')

        # Fill the form
        user_input.send_keys(username)
        password_input.send_keys(password)

        # Click the submit button
        button_sign_in = form_element.find_element(By.CSS_SELECTOR, 'button[data-test-selector="signIn_submit"]')
        button_sign_in.click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span[data-test-selector*="header_userName"]')))

        # Check if the sign in was successful
        sing_in_success = driver.find_elements(By.CSS_SELECTOR, 'span[data-test-selector*="header_userName"]')
        if sing_in_success:
            print('Sign in successful')
            return True
        else:
            print('Sign in failed')
            return False
            raise Exception('Sign in failed')
    except (TimeoutException, NoSuchElementException) as e:
        print(f"Error: {e}")
        return False

def go_to_order_history(driver):
    """
    Function that goes to the order histort
    1. Click on 'My Account' -> button.menu-item & aria-controls="1_My Account"
    2. Get the <a> with class 'mega-menu-heading-link' and text "Order History"
    """
    try:
        driver.find_element(By.CSS_SELECTOR, 'button.menu-item[aria-controls="1_My Account"]').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.mega-menu-heading-link')))
        a_links = driver.find_elements(By.CSS_SELECTOR, 'a.mega-menu-heading-link')
        for a_link in a_links:
            if a_link.text == 'Order History':
                a_link.click()
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'tbody[data-test-selector="orderHistoryTable_tableBody"]')))
                print('Order history found')
                return True
    except (TimeoutException, NoSuchElementException) as e:
        print("Not able to go to the order history")
        print(f"Error: {e}")
        return False

def select_36_per_page(driver):
    """Function to select 36 resultes per page"""
    try:
        select_element = driver.find_element(By.CSS_SELECTOR, 'select[data-test-selector="pagination_resultsPerPage"]')
        select = Select(select_element)
        select.select_by_value('36')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'tbody[data-test-selector="orderHistoryTable_tableBody"]')))
        return True
    except (TimeoutException, NoSuchElementException) as e:
        print("Not able to select 36 results per page")
        print(f"Error: {e}")
        return False

def extract_orders_href(driver):
    """Function to extract the orders href"""
    try:
        td_tags = driver.find_elements(By.CSS_SELECTOR, 'td[data-test-selector="orderHistoryTable_tableCell_orderNumber"]')
        a_tags = [td.find_element(By.CSS_SELECTOR, 'a') for td in td_tags]
        hrefs = []
        for a_tag in a_tags:
            hrefs.append(a_tag.get_attribute('href'))
        return hrefs
    except (TimeoutException, NoSuchElementException) as e:
        print("Not able to extract the orders href")
        print(f"Error: {e}")
        return []

def extract_orders_numbers(driver):
    """Function to extract the orders numbers"""
    try:
        td_tags = driver.find_elements(By.CSS_SELECTOR, 'td[data-test-selector="orderHistoryTable_tableCell_orderNumber"]')
        a_tags = [td.find_element(By.CSS_SELECTOR, 'a') for td in td_tags]
        order_numbers = []
        for a_tag in a_tags:
            order_numbers.append(a_tag.text)
        return order_numbers
    except (TimeoutException, NoSuchElementException) as e:
        print("Not able to extract the orders href")
        print(f"Error: {e}")
        return []

def go_to_next_page(driver):
    """
    Function to go to the next page if it exists
    """
    try:
        next_button = driver.find_element(By.CSS_SELECTOR, 'button[data-test-selector="pagination_nextButton"]')

        # Check if the button has attribute 'disabled'
        if next_button.get_attribute('disabled'):
            print("No more pages")
            return False

        next_button.click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'tbody[data-test-selector="orderHistoryTable_tableBody"]')))
        return True
    except (TimeoutException, NoSuchElementException, WebDriverException) as e:
        print("Not able to go to the next page")
        print(f"Error: {e}")
        return False

def get_orders_links(driver):
    """
    Function to extract the orders links
    1. Set results per page to 36
    2. Get the links
    3. Check for next page and go to it
    """
    next_page = True
    all_orders_links = []
    while next_page:
        # Set results per page to 36
        selected_36 = select_36_per_page(driver)
        if selected_36:
            # Extract the links
            orders_links = extract_orders_href(driver)
            all_orders_links.extend(orders_links)

            # Check for next page
            next_page = go_to_next_page(driver)
            if not next_page:
                break

        else:
            print("Not able to select 36 results per page")
            break
    return all_orders_links

def get_orders_numbers(driver):
    """
    Function to extract the orders links
    1. Set results per page to 36
    2. Get the links
    3. Check for next page and go to it
    """
    next_page = True
    all_orders_numbers = []
    while next_page:
        # Set results per page to 36
        selected_36 = select_36_per_page(driver)
        if selected_36:
            # Extract the links
            orders_numbers = extract_orders_numbers(driver)
            all_orders_numbers.extend(orders_numbers)

            # Check for next page
            next_page = go_to_next_page(driver)
            if not next_page:
                break

        else:
            print("Not able to select 36 results per page")
            break
    return all_orders_numbers

def get_order_data_request(session, order_number):
    """
    Function to get the order data from API call
    1. Set the url
    2. Set/change the header 'referer' in the session
    3. Make the request
    """
    # Set the url
    URL = f"{p.ORDERS_BASE_API_PATH}{order_number}"

    # Set the referer
    REFERER = f"{p.BASE_REFERER_PATH}{order_number}"

    # Set the headers
    session.headers.update({'referer': REFERER})

    # Make the request
    response = session.get(URL, timeout=10)
    if response.status_code == 200:
        print(f"Order {order_number} data retrieved")
        return response.json()
    else:
        print(f"Error while getting order {order_number} data")
        return None

def extract_items(list_of_items, order_id):
    """Function to extract the items from the json"""
    items = []
    for item in list_of_items:
        item_data = {}
        item_data['OrderId'] = order_id
        item_data['ProductCode'] = item['productErpNumber']
        item_data['ProductDescription'] = item['description']
        item_data['QuantityOrdered'] = item['qtyOrdered']
        item_data['QuantityShipped'] = item['qtyShipped']
        item_data['Unit'] = item['unitOfMeasure']
        item_data['UnitPrice'] = item['unitPrice']
        item_data['Price'] = item['lineTotal']
        item_data['ProductUrl'] = item['productUri']
        items.append(item_data)
    return items

def get_order_data(json, output_path):
    """Function to extract the data from the json"""
    order_data = {}

    # Extract Ids and names
    order_data['OrderId'] = json['webOrderNumber']
    order_data['InvoiceDate'] = json['orderDate']

    # Format data to MM-DD-YYYY
    order_data['InvoiceDate'] = pd.to_datetime(order_data['InvoiceDate']).strftime('%m-%d-%Y')

    order_data['CustomerId'] = json['customerNumber']
    order_data['CustomerName'] = json['btCompanyName']
    order_data['VendorName'] = 'Courtesy Products'

    # Extract the shipping address
    country = json['stCountry']
    city = json['shipToCity']
    state = json['shipToState']
    postal_code = json['shipToPostalCode']
    street = json['stAddress1']
    address = f"{street}, {city}, {state}, {postal_code}, {country}"
    order_data['ShippingAddress'] = address

    # Extract the amounts
    order_data['InvoiceTotal'] = json['orderTotal']
    order_data['InvoiceSubtotal'] = json['orderSubTotal']
    order_data['TotalTax'] = json['taxAmount']
    order_data['Discount'] = json['discountAmount']
    order_data['ShippingCost'] = json['shippingCharges']
    order_data['OtherCharges'] = json['otherCharges']

    # Extract the items
    items = extract_items(json['orderLines'], order_data['OrderId'])

    # Save all the data
    fields_df = pd.DataFrame([order_data])
    items_df = pd.DataFrame(items)
    ut.write_in_excel_file(output_path, fields_df, items_df)
