from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options as chrome_options

import pytest
import time


# параметры Chrome
@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')
    # запускает браузер в развернутом виде
    options.add_argument('--start-maximized')
    # начальный размер окна браузера
    options.add_argument('--window-size=1440,900')
    return options


# инициализация драйвера
@pytest.fixture(autouse=True)
def testing(get_chrome_options):
    options = get_chrome_options
    selenium = webdriver.Chrome(options=options)
    selenium.implicitly_wait(10)
    selenium.get('https://www.wildberries.ru/')

    yield selenium
    selenium.quit()


# TEST_01
# проверка, что пользователь может перейти на страницу поиска товаров
def test_opening_search_page(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://www.wildberries.ru/')
    time.sleep(2)

    # сохраняем скриншот
    selenium.save_screenshot('test_opening_search_page.png')

    assert selenium.find_element(By.XPATH, '/html/body/div[1]/header/div/div[2]/div[3]/div[1]/input'), \
        print('Тест провален')


# TEST_02
# проверка, что пользователь может выбрать смартфоны по заданным условиям
def test_checkbox_smartphone(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://www.wildberries.ru/')
    time.sleep(2)

    # нажимаем на поле поиска
    selenium.find_element(By.XPATH, '//*[@id="searchInput"]').click()
    time.sleep(2)
    # в поле поиска вводим "смартфоны"
    selenium.find_element(By.XPATH, '//*[@id="searchInput"]').send_keys('смартфоны')
    time.sleep(2)
    # из выпадающего списка выбираем категорию "смартфоны"
    selenium.find_element(By.XPATH, '//*[@id="searchBlock"]/div[2]/div/div/ul[2]/li/p/span/span[2]').click()
    time.sleep(2)
    # открывается страница с выбором всех смартфонов
    # выбираем чек "Samsung"
    selenium.find_element(By.XPATH, '//*[@id="filters"]/div[2]/div[2]/fieldset/label[2]').click()
    time.sleep(2)

    # выделение текста в фильтре максимальной цены
    selenium.find_element(By.XPATH, '//*[@id="filters"]/div[4]/div[2]/div/div/div[2]/div/input').send_keys(
        Keys.CONTROL + 'A')
    time.sleep(1)
    # удаление текста в фильтре максимальной цены
    selenium.find_element(By.XPATH, '//*[@id="filters"]/div[4]/div[2]/div/div/div[2]/div/input').send_keys(Keys.DELETE)
    time.sleep(1)
    # ввод значения "10000" в фильтре максимальной цены
    selenium.find_element(By.XPATH, '//*[@id="filters"]/div[4]/div[2]/div/div/div[2]/div/input').send_keys('10000')
    time.sleep(1)
    # нажимаем Enter для применения фильтров
    selenium.find_element(By.XPATH, '//*[@id="filters"]/div[4]/div[2]/div/div/div[2]/div/input').send_keys(Keys.ENTER)
    time.sleep(2)

    # сохраняем скриншот
    selenium.save_screenshot('test_checkbox_smartphone.png')

    assert selenium.find_element(By.XPATH, '//*[@id="catalog"]/div[6]/div[1]/div[4]/ul/li').text == 'Samsung'


# TEST_03
# проверка, что на странице новогодних товаров пользователь может выбрать гирлянды
def test_checkbox_smartphone_lights(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://www.wildberries.ru/')
    time.sleep(2)

    # нажимаем на кнопку, открывающую категории товаров
    selenium.find_element(By.XPATH, '/html/body/div[1]/header/div/div[2]/div[1]/button').click()
    time.sleep(1)
    # выбираем категорию "Новый год"
    selenium.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/ul/li[6]/a').click()
    time.sleep(2)

    # выбираем категорию "Гирлянды"
    selenium.find_element(By.XPATH,
                          '//*[@id="app"]/div[2]/div/div[3]/div[2]/div[3]/div[1]/div/div[2]/div/div/a/div/img').click()
    time.sleep(2)
    # выбираем чек "светодиодная"
    selenium.find_element(By.XPATH, '//*[@id="filters"]/div[7]/div[2]/fieldset/label[2]').click()
    time.sleep(1)

    # сохраняем скриншот
    selenium.save_screenshot('test_checkbox_smartphone_lights.png')

    assert selenium.find_element(By.TAG_NAME, 'h1').text == 'Гирлянды', print('Тест провален')