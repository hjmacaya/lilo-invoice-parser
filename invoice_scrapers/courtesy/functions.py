"""
Module to store the functions
"""

# Selenium imports
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException

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

def get_order_data(driver, url):
    """
    Function to get the order data
    """
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-test-selector="page_OrderDetailsPage"]')))
        print(f"Order {url} found")

        # Get the data
        order_data = {}

        # Get the Order date
