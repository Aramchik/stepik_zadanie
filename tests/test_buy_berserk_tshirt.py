import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec

from pages.cart_page import Cart_Page
from pages.main_page import Main_Page
from pages.method_of_obtaining import Method_of_obtaining
from pages.product_checkout_page import Product_Checkout_Page


def test_buy_product(set_up):
    # Указываем путь к geckodriver
    service = Service("C:/Users/Aram/Desktop/geckodriver.exe")

    # Настройки браузера
    options = Options()
    options.set_preference("dom.webnotifications.enabled", False)
    # options.add_argument('--headless')
    driver = webdriver.Firefox(service=service, options=options)
    driver.get("https://www.vsemayki.ru/")


    # Нажимаем на кнопку принять куки чтобы не мешало в дальнейшем
    cookie_accept = WebDriverWait(driver,30).until(Ec.element_to_be_clickable((By.XPATH, "//*[@id='autotest-cookie-confirm']"))).click()


    # mp наследует класс Main_Page
    mp = Main_Page(driver)
    mp.click_novinki()
    mp.click_man_wear()
    mp.click_man_t_shirt()
    mp.click_man_cotton_t_shirt()
    mp.send_text_in_search_subjects('берсерк')
    mp.click_berserk()
    mp.click_berserk_page_2()
    mp.click_guts_look_t_shirt()
    mp.click_white_color_tshirtt()
    mp.click_m_size_guts_tshirt()
    mp.click_guts_add_to_cart()

    # cp наследует класс Cart_Page
    cp = Cart_Page(driver)
    cp.click_go_to_cart()
    cp.assert_berserk_name()
    cp.assert_berserk_price()
    cp.assert_berserk_size()
    cp.assert_cart_color()

    # pcp наследует класс Product_Checkout_Page
    pcp = Product_Checkout_Page(driver)
    pcp.click_go_to_checkout()
    pcp.send_info()

    # moo наследует класс Method_of_obtaininge
    moo = Method_of_obtaining(driver)
    moo.click_samovivoz()
    moo.click_filtr()
    moo.click_sdek()
    moo.click_postmat()
    moo.click_payment_upon_receipt()
    moo.click_sdek_adress()
    moo.click_take_from_here()
    pcp.assert_info_pcp()

