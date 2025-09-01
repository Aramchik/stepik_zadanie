import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from base.base_class import Base
from faker import Faker

# Класс Product_Checkout_Page финальная страница перед оплатой товара
class Product_Checkout_Page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    # Lockators # Локатор для перехода на страницу чек-аут
    go_to_checkout = "//a[@id='autotest-cart-go-to-checkout']"




    # Getters # Геттер для перехода на страницу чек-аут
    def get_go_to_checkout(self):
        return WebDriverWait(self.driver,30).until(Ec.element_to_be_clickable((By.XPATH,self.go_to_checkout)))



    # Actions # Метод для перехода на страницу чек-аут
    def click_go_to_checkout(self):
        self.get_go_to_checkout().click()
        print('click go to checkout')




    # Lokators #Локаторы чек-аута
    user_name = "(//input[@tabindex='1'])[1]"
    last_name = "//input[@autocomplete='family-name']"
    telephon = "(//input[@tabindex='1'])[3]"
    email = "(//input[@tabindex='1'])[4]"
    cart_t_shirt_name = "//p[text()='Мужская футболка хлопок Взгляд Гатса: Берсерк']"
    size_and_color = "//p[text()='M (50), белый']"
    price = "//div//span[text()='1 240']"




    #Getters # Геттеры для наших локаторов
    def get_user_name(self):
        return WebDriverWait(self.driver,30).until(Ec.element_to_be_clickable((By.XPATH,self.user_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver,30).until(Ec.element_to_be_clickable((By.XPATH,self.last_name)))

    def get_telephon(self):
        return WebDriverWait(self.driver,30).until(Ec.element_to_be_clickable((By.XPATH,self.telephon)))

    def get_email(self):
        return WebDriverWait(self.driver,30).until(Ec.element_to_be_clickable((By.XPATH,self.email)))

    def get_cart_t_shirt_name(self):
        return WebDriverWait(self.driver,30).until(Ec.element_to_be_clickable((By.XPATH,self.cart_t_shirt_name)))

    def get_size_and_color(self):
        return WebDriverWait(self.driver,30).until(Ec.element_to_be_clickable((By.XPATH,self.size_and_color)))

    def get_price(self):
        return WebDriverWait(self.driver,30).until(Ec.element_to_be_clickable((By.XPATH,self.price)))




    # Заполняем поля чек-аута через faker (смотреть класс Base)
    def send_info(self):
        self.get_user_name().send_keys(self.name)
        print("enter Name")
        time.sleep(1)
        self.get_last_name().click()
        self.get_last_name().send_keys(self.last_namef)
        print("enter Last Name")
        time.sleep(1)
        self.get_telephon().click()
        self.get_telephon().send_keys(self.phone_number)
        print("enter phone number")
        time.sleep(1)
        self.get_email().click()
        self.get_email().send_keys(self.mailf)
        print("enter mail")




    # Сравниваем название цену размер и цвет товара через assert (смотреть класс Base)
    def assert_info_pcp(self):
        self.assert_word(self.get_cart_t_shirt_name(), "Мужская футболка хлопок Взгляд Гатса: Берсерк")
        print('name good')
        self.assert_word(self.get_size_and_color(), "M (50), белый")
        print('size and color good')
        self.assert_word(self.get_price(), "1 240 ₽")
        print('price good')


