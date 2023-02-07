import time

from selenium import webdriver


class Test1:
    def test_select_product(self):
        driver = webdriver.Chrome(executable_path='/home/dmitry/Geek/PycharmProjects/resource/chromedriver')
        base_url = 'https://www.saucedemo.com/'
        driver.get(base_url)
        driver.maximize_window()
        time.sleep(2)


test = Test1()
test.test_select_product()
