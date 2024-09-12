
import time
from selenium import webdriver
import unittest

class TestAuthorizedEcommerceApp(unittest.TestCase):
    def test_auth(self):
        
        # Авторизация
        driver = webdriver.Firefox()
        driver.get("https://www.saucedemo.com/")
        
        username_input = driver.find_element('xpath','//input[@id="user-name"]')
        password_input = driver.find_element('xpath','//input[@id="password"]')
        login_button = driver.find_element('xpath','//input[@id="login-button"]')

        username_input.send_keys("standard_user") # << INPUT LOGIN #
        password_input.send_keys("secret_sauce")  # <<    DATES    #
        login_button.click()

        # Выбор товара
        catalog_link = driver.find_element('xpath','(//div[@id="inventory_container"]/div[@class="inventory_list"])/div[1]//button[@id="add-to-cart-sauce-labs-backpack"]')
        catalog_link.click()
        
        add_to_cart_button = driver.find_element('xpath','//*[@id="shopping_cart_container"]/a')
        add_to_cart_button.click()

        # Оформление покупки
        checkout_button = driver.find_element('xpath','//*[@id="checkout"]')
        checkout_button.click()
        
        # Работа с формой
        driver.find_element('xpath','//*[@id="first-name"]').send_keys('SomeName')
        driver.find_element('xpath','//*[@id="last-name"]').send_keys('SomeLastName')
        driver.find_element('xpath','//*[@id="postal-code"]').send_keys('143909')
        
        driver.find_element('xpath','//*[@id="continue"]').click()
        driver.find_element('xpath','//*[@id="finish"]').click()
        
        # Проверка завершения покупки
        assert driver.find_element('xpath','//*[@id="checkout_complete_container"]/div').text!= "Thank you for your order!"
        
        
        driver.quit()
if __name__ == "__main__":
    unittest.main()