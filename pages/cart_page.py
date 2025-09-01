import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from base.base_class import Base


# Класс Cart_Page класс корзины сайта
class Cart_Page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver




    # lockators # Локаторы корзины
    go_to_cart = "//button[@id='autotest-product-card-go-to-cart']"
    cart_t_shirt_name = "//a[text()='Мужская футболка хлопок Взгляд Гатса: Берсерк']"
    total_price = "(//div//span[text()='1 240'])[3]"
    size_cart = "(//span//div//div[text()='M (50)'])[1]"
    cart_color = "(//span[text()='белый'])[1]"




    # Getters #Геттеры для наших локаторов
    def get_go_to_cart(self):
        return WebDriverWait(self.driver,30).until(Ec.element_to_be_clickable((By.XPATH, self.go_to_cart)))

    def get_cart_t_shirt_name(self):
        return WebDriverWait(self.driver,30).until(Ec.element_to_be_clickable((By.XPATH, self.cart_t_shirt_name)))

    def get_total_price(self):
        return WebDriverWait(self.driver,30).until(Ec.element_to_be_clickable((By.XPATH, self.total_price)))

    def get_size_cart(self):
        return WebDriverWait(self.driver,30).until(Ec.element_to_be_clickable((By.XPATH, self.size_cart)))

    def get_cart_color(self):
        return WebDriverWait(self.driver,30).until(Ec.element_to_be_clickable((By.XPATH, self.cart_color)))

    def click_go_to_cart(self):
        self.get_go_to_cart().click()
        print('click go to cart')




    # Asserts # Сравниваем название цену размер и цвет товара через assert (смотреть класс Base)
    def assert_berserk_name(self):
        self.assert_word(self.get_cart_t_shirt_name(), "Мужская футболка хлопок Взгляд Гатса: Берсерк")
        print('name good')

    def assert_berserk_price(self):
        self.assert_word(self.get_total_price(), "1 240 ₽")
        print('price good')

    def assert_berserk_size(self):
        self.assert_word(self.get_size_cart(), "M (50)")
        print('size good')

    def assert_cart_color(self):
        self.assert_word(self.get_cart_color(), "белый")
        print('color good')