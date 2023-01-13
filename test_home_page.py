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
def test_opening_home_page(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://www.wildberries.ru/')
    time.sleep(2)

    # сохраняем скриншот
    selenium.save_screenshot('test_opening_home_page.png')

    assert selenium.find_element(By.XPATH, '/html/body/div[1]/header/div/div[2]/div[3]/div[1]/input'), \
        print('Тест провален')


# TEST_02
# проверка возможности изменения валюты
def test_changing_currency(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://www.wildberries.ru/')
    time.sleep(2)

    # нажимаем на кнопку изменения валюты
    selenium.find_element(By.XPATH, '/html/body/div[1]/header/div/div[1]/ul/li[1]/span').click()
    time.sleep(1)
    # нажимаем на "Белорусский рубль"
    selenium.find_element(By.XPATH, '/html/body/div[1]/header/div/div[1]/ul/li[1]/div/div/div/div/form/fieldset/label[2]/span/span[2]').click()
    time.sleep(2)

    # сохраняем скриншот
    selenium.save_screenshot('test_changing_currency.png')

    assert selenium.find_element(By.XPATH, '/html/body/div[1]/header/div/div[1]/ul/li[1]/span/span[2]').text == 'BYN', \
        print('Тест провален')


# TEST_03
# проверка отображения окна выбора пункта выдачи
def test_changing_city(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://www.wildberries.ru/')
    time.sleep(2)

    # нажимаем на кнопку изменения города
    selenium.find_element(By.XPATH, '/html/body/div[1]/header/div/div[1]/ul/li[2]/span').click()
    time.sleep(2)

    # сохраняем скриншот
    selenium.save_screenshot('test_changing_city.png')

    assert selenium.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/h2').text == 'Выберите адрес доставки', \
        print('Тест провален')


# TEST_04
# проверка возможности перехода на страницу трудоустройства
def test_opening_employment_page(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://www.wildberries.ru/')
    time.sleep(2)

    # нажимаем на кнопку трудоустройства
    selenium.find_element(By.XPATH, '/html/body/div[1]/header/div/div[1]/ul/li[5]/a').click()
    time.sleep(2)

    # сохраняем скриншот
    selenium.save_screenshot('test_opening_employment_page.png')

    assert selenium.current_url == 'https://www.wildberries.ru/services/trudoustroystvo', print('Тест провален')

# TEST_05
# проверка возможности перехода на страницу с пунктами выдачи
def test_opening_delivery_page(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://www.wildberries.ru/')
    time.sleep(2)

    # нажимаем на кнопку пунктов выдачи
    selenium.find_element(By.XPATH, '//*[@id="basketContent"]/div[1]/a').click()
    time.sleep(2)

    # сохраняем скриншот
    selenium.save_screenshot('test_opening_delivery_page.png')

    assert selenium.current_url == 'https://www.wildberries.ru/services/besplatnaya-dostavka?desktop=1#terms-delivery',\
        print('Тест провален')
    assert selenium.find_element(By.TAG_NAME, 'h1').text == 'Доставка', print('Тест провален')

# TEST_06
# проверка возможности перехода на страницу авторизации
def test_opening_authorization_page(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://www.wildberries.ru/')
    time.sleep(2)

    # нажимаем на кнопку авторизации
    selenium.find_element(By.XPATH, '//*[@id="basketContent"]/div[2]/a').click()
    time.sleep(2)

    # сохраняем скриншот
    selenium.save_screenshot('test_opening_authorization_page.png')

    assert selenium.find_element(By.CLASS_NAME, 'form-block__name').text == 'Контактный телефон',\
        print('Тест провален')

# TEST_07
# проверка возможности перехода на страницу корзины
# предварительное условие: товары не выбраны
def test_opening_basket_page(testing):
    selenium = testing
    # открытие сайта
    selenium.get('https://www.wildberries.ru/')
    time.sleep(2)

    # нажимаем на кнопку корзины
    selenium.find_element(By.XPATH, '//*[@id="basketContent"]/div[3]/a').click()
    time.sleep(2)

    # сохраняем скриншот
    selenium.save_screenshot('test_opening_basket_page.png')

    assert selenium.find_element(By.TAG_NAME, 'h1').text == 'В корзине пока пусто', print('Тест провален')
    assert selenium.current_url == 'https://www.wildberries.ru/lk/basket', print('Тест провален')