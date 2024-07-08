"""
Script to scrape invoices from Courtesy
"""
# EXTERNAL IMPORTS
import os
import time
from dotenv import load_dotenv

# INTERNAL IMPORTS
import utils as ut
import functions as f
import parameters as p

# Log in to the website
load_dotenv()
driver = ut.set_up_driver()
logged_in = f.login_to_courtesy(
    driver,
    p.LOGIN_URL,
    os.getenv('USERNAME_1'),
    os.getenv('PASSWORD_1')
    )

# Go to the page
if logged_in:
    in_order_history = f.go_to_order_history(driver)
    time.sleep(2)
    if in_order_history:
        # Get the invoices links
        order_numbers = f.get_orders_numbers(driver)
        print(f"Order numbers: {order_numbers}")
        time.sleep(2)

        # Set up request session
        session = ut.set_up_session(driver)

        # Get the invoices data
        for order_number in order_numbers:
            time.sleep(2)
            order_data_json = f.get_order_data_request(session, order_number)
            if order_data_json:
                output_path = "pdfs/springhill_medford/courtesy/parsed_orders.xlsx"
                order_data = f.get_order_data(order_data_json, output_path)
        driver.quit()
