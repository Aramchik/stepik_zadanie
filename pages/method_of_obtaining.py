import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from base.base_class import Base


# Класс Method_of_obtaining для способа полечния товара
class Method_of_obtaining(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver




    #lockators # Локаторы способа получения
    samovivoz = "//div[@id='autotest-checkout-delivery-pickup']"
    filtr = "//button[@class='styles_pickup_points_filters__btn__OG2GP']"
    sdek = "(//span[@class='style_checkbox__input__sgPxt'])[1]"
    postmat = "(//span[@class='style_checkbox__input__sgPxt'])[6]"
    payment_upon_receipt = "//div[text()='Оплата при получении']"
    sdek_adress = "(//div[text()='Пресненская наб., 12'])[1]"
    take_from_here = "//button[@id='autotest-checkout-delivery-pickup-select']"





    #Getters # Геттеры наших локаторов

    def get_samovivoz(self):
        return WebDriverWait(self.driver, 30).until(Ec.element_to_be_clickable((By.XPATH, self.samovivoz)))


    def get_filtr(self):
        return WebDriverWait(self.driver, 30).until(Ec.element_to_be_clickable((By.XPATH, self.filtr)))

    def get_sdek(self):
        return WebDriverWait(self.driver, 30).until(Ec.element_to_be_clickable((By.XPATH, self.sdek)))

    def get_postmat(self):
        return WebDriverWait(self.driver, 30).until(Ec.element_to_be_clickable((By.XPATH, self.postmat)))

    def get_payment_upon_receipt(self):
        return WebDriverWait(self.driver, 30).until(Ec.element_to_be_clickable((By.XPATH, self.payment_upon_receipt)))

    def get_sdek_adress(self):
        return WebDriverWait(self.driver, 30).until(Ec.element_to_be_clickable((By.XPATH, self.sdek_adress)))


    def get_take_from_here(self):
        return WebDriverWait(self.driver, 30).until(Ec.element_to_be_clickable((By.XPATH, self.take_from_here)))




    # Actions # Создаем методы по выбору и фильтрации способа получения
    def click_samovivoz(self):
        self.get_samovivoz().click()
        print("click samovivoz ")
        time.sleep(1)

    def click_filtr(self):
        self.get_filtr().click()
        print("click filtr ")

    def click_sdek(self):
        self.get_sdek().click()
        print("click sdek ")

    def click_postmat(self):
        self.get_postmat().click()
        print("click postmat ")

    def click_payment_upon_receipt(self):
        self.get_payment_upon_receipt().click()
        print("click payment upon receipt ")

    def click_sdek_adress(self):
        self.get_sdek_adress().click()
        print("click sdek adress ")

    def click_take_from_here(self):
        self.get_take_from_here().click()
        print("click take from here ")
