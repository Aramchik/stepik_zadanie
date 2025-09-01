import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from base.base_class import Base



# Класс Main_Page класс главной страницы сайта
class Main_Page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    # Lockators #Локаторы с главной страницы

    novinki = "//div//a[text()='Новинки']"
    man_wear = "//a[@id='manwear']"
    man_t_shirt = "//a[@id='man_tshirts']"
    man_cotton_t_shirt = "//a[@id='manshort']"
    search_subjects = "//input[@size=5]"
    berserk = "//span[text()='Берсерк']"
    berserk_page_2 = "//div//a[text()=2]"
    guts_look_t_shirt = "//span[text()='Мужская футболка хлопок Взгляд Гатса: Берсерк']"
    white_color_tshirt = "//li[@title='белый']"
    m_size_guts_tshirt = "//a[text()='M (50)']"
    guts_add_to_cart = "//a[@id='autotest-product-card-add-to-cart']"




    # Getters #Геттеры для наших локаторов
    def get_novinki(self):
        return WebDriverWait(self.driver,30).until(Ec.element_to_be_clickable((By.XPATH, self.novinki)))

    def get_man_wear(self):
        return WebDriverWait(self.driver,30).until(Ec.element_to_be_clickable((By.XPATH, self.man_wear)))

    def get_man_t_shirt(self):
        return WebDriverWait(self.driver,30).until(Ec.element_to_be_clickable((By.XPATH, self.man_t_shirt)))

    def get_man_cotton_t_shirt(self):
        return WebDriverWait(self.driver,30).until(Ec.element_to_be_clickable((By.XPATH, self.man_cotton_t_shirt)))

    def get_search_subjects(self):
        return WebDriverWait(self.driver,30).until(Ec.element_to_be_clickable((By.XPATH, self.search_subjects)))

    def get_berserk(self):
        return WebDriverWait(self.driver,30).until(Ec.element_to_be_clickable((By.XPATH, self.berserk)))

    def get_berserk_page_2(self):
        return WebDriverWait(self.driver,30).until(Ec.element_to_be_clickable((By.XPATH, self.berserk_page_2)))

    def get_guts_look_t_shirt(self):
        return WebDriverWait(self.driver,30).until(Ec.element_to_be_clickable((By.XPATH, self.guts_look_t_shirt)))

    def get_white_color_tshirt(self):
        return WebDriverWait(self.driver,30).until(Ec.element_to_be_clickable((By.XPATH, self.white_color_tshirt)))

    def get_m_size_guts_tshirt(self):
        return WebDriverWait(self.driver,30).until(Ec.element_to_be_clickable((By.XPATH, self.m_size_guts_tshirt)))

    def get_guts_add_to_cart(self):
        return WebDriverWait(self.driver,30).until(Ec.element_to_be_clickable((By.XPATH, self.guts_add_to_cart)))




    # Actions # Создаем методы по выбору фильтрации и добавлению товара в корзину
    def click_novinki(self):
        self.get_novinki().click()
        print('click novinki')

    def click_man_wear(self):
        self.get_man_wear().click()
        print('click man_wear')

    def click_man_t_shirt(self):
        self.get_man_t_shirt().click()
        print('click man t-shirt')

    def click_man_cotton_t_shirt(self):
        self.get_man_cotton_t_shirt().click()
        print('click cotton man t-shirt')

    def send_text_in_search_subjects(self, text):
        self.get_search_subjects().click()
        time.sleep(2)
        self.get_search_subjects().send_keys(text)
        print('Text sended')

    def click_berserk(self):
        self.get_berserk().click()
        print('click berserk')

    def click_berserk_page_2(self):
        self.get_berserk_page_2().click()
        print('click berserk page 2')

    def click_guts_look_t_shirt(self):
        self.get_guts_look_t_shirt().click()
        print('click guts look t-shirt')

    def click_white_color_tshirtt(self):
        self.get_white_color_tshirt().click()
        print('click white color t-shirt')

    def click_m_size_guts_tshirt(self):
        self.get_m_size_guts_tshirt().click()
        print('click m size')

    def click_guts_add_to_cart(self):
        self.get_guts_add_to_cart().click()
        print('click add to cart')





