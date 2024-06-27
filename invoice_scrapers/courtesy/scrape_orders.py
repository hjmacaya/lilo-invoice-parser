"""
Script to scrape invoices from Courtesy
"""
# ETERNAL IMPORTS
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
    if in_order_history:
        # Get the invoices links
        order_links = f.get_orders_links(driver)
        for order_link in order_links:
            time.sleep(2)
            order_data = f.get_order_data(driver, order_link)
        driver.quit()
