"""
Script to scrape the invoices of Pepsico
"""
# External imports
import os
import time
from dotenv import load_dotenv

# Internal imports
import utils as ut
import functions as f
import parameters as p


# 1. Loggin with user
load_dotenv()
driver = ut.set_up_driver()
logged_in = f.login_to_pepsico(
    driver,
    p.LOGIN_URL,
    os.getenv('PEPSICO_USERNAME'),
    os.getenv('PEPSICO_PASSWORD')
    )

# 2. Go to invoices pages
in_order_history = f.go_to_order_history_page(driver)
time.sleep(2)
if in_order_history:
    # TODO: Get links with pagination
    # Get the orders link
    orders_urls = f.get_the_urls(driver)
    print(orders_urls)

    # Loop through the orders
    for url in orders_urls:
        order_data = f.get_order_data(driver, url)
        for key, value in order_data.items():
            print(f"{key}: {value}")
        break

    pass
else:
    print("Failed to go to order history page")

# Close the driver
print("Closing driver...")
driver.quit()
