import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Test1:
    def test_select_product(self):
        driver = webdriver.Chrome(executable_path='/home/dmitry/Geek/PycharmProjects/resource/chromedriver')
        base_url = 'https://www.saucedemo.com/'
        driver.get(base_url)
        driver.maximize_window()

        print("Start Test")

        login_standard_user = "standard_user"
        password_all = "secret_sauce"

        user_name = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']")))
        user_name.send_keys(login_standard_user)
        print("Input Login")

        password = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
        password.send_keys(password_all)
        print("Input Password")

        button_login = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "\
                                                                                //input[@id='login-button']")))
        button_login.click()
        print("Click Login Button")

        select_product = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "\
                                                              //button[@id='add-to-cart-sauce-labs-backpack']")))
        select_product.click()
        print("Click Select Product")

        shopping_cart = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "\
                                                                              //div[@id='shopping_cart_container']")))
        shopping_cart.click()
        print("Click Enter Shopping Cart")

        success_test = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='title']")))
        value_success_test = success_test.text
        print(value_success_test)
        assert value_success_test == "YOUR CART"
        print("Test Success!!!")

        time.sleep(2)


test = Test1()
test.test_select_product()
