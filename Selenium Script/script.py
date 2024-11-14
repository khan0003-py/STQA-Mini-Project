from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

def signup():
    try:
        driver.get("http://localhost/ecommerce/index.php")
        time.sleep(1)
        signup_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign Up")))
        signup_button.click()
        wait.until(EC.visibility_of_element_located((By.ID, "signup")))
        driver.find_element(By.NAME, "firstName").send_keys("John")
        driver.find_element(By.NAME, "lastName").send_keys("Doe")
        driver.find_element(By.NAME, "eMail").send_keys("john.doe@example.com")
        driver.find_element(By.NAME, "password").send_keys("password123")
        time.sleep(2)
        driver.find_element(By.CLASS_NAME, "Submit").click()
        time.sleep(5)
        logout_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout")))
        logout_button.click()
        print("Signup completed and logged out successfully.")
    except Exception as e:
        print(f"Error during signup: {e}")

def login():
    try:
        driver.get("http://localhost/ecommerce/index.php")
        time.sleep(1)
        login_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
        login_button.click()
        wait.until(EC.visibility_of_element_located((By.ID, "login")))
        driver.find_element(By.NAME, "lemail").send_keys("john.doe@example.com")
        driver.find_element(By.NAME, "lpassword").send_keys("password123")
        time.sleep(2)
        driver.find_element(By.NAME, "Submit").click()
        time.sleep(5)
        logout_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout")))
        logout_button.click()
        print("Login completed and logged out successfully.")
    except Exception as e:
        print(f"Error during login: {e}")

def failed_signup():
    try:
        driver.get("http://localhost/ecommerce/index.php")
        time.sleep(1)
        signup_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign Up")))
        signup_button.click()
        wait.until(EC.visibility_of_element_located((By.ID, "signup")))
        driver.find_element(By.NAME, "firstName").send_keys("")
        driver.find_element(By.NAME, "lastName").send_keys("Doe")
        driver.find_element(By.NAME, "eMail").send_keys("john.doe@example.com")
        driver.find_element(By.NAME, "password").send_keys("password123")
        time.sleep(2)
        driver.find_element(By.CLASS_NAME, "Submit").click()
        time.sleep(2)
        logout_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout")))
        logout_button.click()
        print("Failed signup attempt completed.")
    except Exception as e:
        print(f"Error during failed signup: {e}")

def failed_login():
    try:
        driver.get("http://localhost/ecommerce/index.php")
        time.sleep(1)
        login_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
        login_button.click()
        wait.until(EC.visibility_of_element_located((By.ID, "login")))
        driver.find_element(By.NAME, "lemail").send_keys("usernotfound@gmail.com")
        driver.find_element(By.NAME, "lpassword").send_keys("password123")
        time.sleep(2)
        driver.find_element(By.NAME, "Submit").click()
        time.sleep(2)
        logout_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout")))
        logout_button.click()
        print("Failed login attempt completed.")
    except Exception as e:
        print(f"Error during failed login: {e}")

def add_product_and_checkout():
    try:
        driver.get("http://localhost/ecommerce/")
        wait = WebDriverWait(driver, 10)
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, "Shop Now").click()
        time.sleep(2)
        driver.find_element(By.NAME, "addToCart").click()
        time.sleep(2)
        driver.find_element(By.NAME, "lemail").send_keys("john.doe@example.com")
        driver.find_element(By.NAME, "lpassword").send_keys("password123")
        driver.find_element(By.NAME, "Submit").click()
        time.sleep(2)
        driver.find_element(By.NAME, "addToCart").click()
        time.sleep(2)
        driver.get("http://localhost/ecommerce/cart.php")
        time.sleep(10)
        driver.find_element(By.LINK_TEXT, "Confirm Order").click()
        print("Successfully added product to cart, logged in, and proceeded to checkout.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Test completed. Browser will remain open for observation.")

def contact_form():
    try:
        driver.get("http://localhost/ecommerce/index.php")
        time.sleep(1)
        about_us_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "About Us")))
        about_us_button.click()
        driver.find_element(By.ID, "exampleFormControlInput1").send_keys("test.email@example.com")
        driver.find_element(By.ID, "exampleFormControlTextarea1").send_keys("This is a test message.")
        time.sleep(2)
        driver.find_element(By.NAME, "SendMessage").click()
        time.sleep(2)
        driver.find_element(By.LINK_TEXT, "Go back").click()
        print("Message sent successfully via contact form.")
    except Exception as e:
        print(f"Error during sending message: {e}")

def main():
    while True:
        print("Select an option:")
        print("1. Sign Up")
        print("2. Login")
        print("3. Failed Sign Up")
        print("4. Failed Login")
        print("5. Add Product and Checkout")
        print("6. Send Message")
        print("7. Exit")
        choice = input("Enter your choice: ")
        switch = {
            "1": signup,
            "2": login,
            "3": failed_signup,
            "4": failed_login,
            "5": add_product_and_checkout,
            "6": contact_form,
            "7": exit
        }
        action = switch.get(choice, lambda: print("Invalid choice, please try again."))
        action()

if __name__ == "__main__":
    try:
        main()
    finally:
        driver.quit()