# E2e_authoris

**Авторизация**


**Чтобы авторизоваться на сайте, следуйте следующим шагам:**

1. Откройте браузер и перейдите по адресу https://www.saucedemo.com/.
2. Введите ваше имя пользователя и пароль в соответствующие поля.
3. Нажмите кнопку "Войти" для авторизации.


**Выбор товара**

1. Откройте браузер и перейдите по адресу https://www.saucedemo.com/.
2. Нажмите кнопку "Добавить в корзину" для добавления товара в вашу корзину.
3. Убедитесь, что товар успешно добавлен в вашу корзину.


**тестовый сценарий python**


import unittest
from selenium import webdriver
import unittest


class TestAuthorizedEcommerceApp(unittest.TestCase):
    def test_auth(self):
        # Авторизация
        driver = webdriver.Chrome()
        driver.get("https://example.com/login")
        username_input = driver.find_element("xpath","_username_element")
        password_input = driver.find_element("xpath","_password_element")
        login_button = driver.find_element("xpath","_login_button_element")

        username_input.send_keys("your_username")
        password_input.send_keys("your_password")
        login_button.click()

        # Выбор товара
        catalog_link = driver.find_element("xpath","#catalog-link")
        catalog_link.click()
        add_to_cart_button = driver.find_element("xpath","#add-to-cart-button")
        add_to_cart_button.click()

        # Оформление покупки
        checkout_button = driver.find_element("xpath","#checkout-button")
        checkout_button.click()

        # Проверка завершения покупки
        assert driver.title == "Товар успешно куплен!"

if __name__ == "__main__":
    unittest.main()# E2e_authoris
