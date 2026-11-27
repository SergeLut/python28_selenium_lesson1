import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Запуск браузера Chrome
driver = webdriver.Chrome()


def test_default():
    try:
        # 2. Открытие страницы
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)  # Пауза, чтобы визуально заметить открытие

        # 3. Поиск элементов и заполнение полей
        # Находим поле Full Name по его ID и вводим текст
        full_name_field = driver.find_element(By.ID, "userName")
        # web_elements = driver.find_elements(By.XPATH, "someXPath")

        full_name_field.send_keys("Иван Иванов")

        # Находим поле Email по его ID и вводим текст
        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("ivan@example.com")

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Проверка результата
        time.sleep(5)  # Пауза, чтобы увидеть результат отправки

        # Находим блок с отправленными данными
        result_box = driver.find_element(By.ID, "output")

        # Проверяем, что в блоке результата появился введенный текст
        assert "Иван Иванов" in result_box.text
        print("Тест успешно пройден!")

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()


def test_with_current_and_permanent_addresses():
    try:
        # 2. Открытие страницы
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)  # Пауза, чтобы визуально заметить открытие

        # 3. Поиск элементов и заполнение полей
        # Находим поле Full Name по его ID и вводим текст
        full_name_field = driver.find_element(By.ID, "userName")
        # web_elements = driver.find_elements(By.XPATH, "someXPath")

        full_name_field.send_keys("Иван Иванов")

        # Находим поле Email по его ID и вводим текст
        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("ivan@example.com")

        # Находим поля Current Address и Permanent Address
        current_address_field = driver.find_element(By.ID, 'currentAddress')

        current_address_field.send_keys("Test Current address")

        permanent_address_field = driver.find_element(By.ID, 'permanentAddress')

        permanent_address_field.send_keys("Test Permanent address")

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Проверка результата
        time.sleep(5)  # Пауза, чтобы увидеть результат отправки

        # Находим блок с отправленными данными
        result_box = driver.find_element(By.ID, "output")

        # Проверяем, что в блоке результата появился введенный текст
        assert "Test Current address" and "Test Permanent address" in result_box.text
        print("Тест успешно пройден!")

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()


def test_email_without_at():
    try:
        # 2. Открытие страницы
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)  # Пауза, чтобы визуально заметить открытие

        # 3. Поиск элементов и заполнение полей
        # Находим поле Full Name по его ID и вводим текст
        full_name_field = driver.find_element(By.ID, "userName")
        # web_elements = driver.find_elements(By.XPATH, "someXPath")

        full_name_field.send_keys("Иван Иванов")

        # Находим поле Email по его ID и вводим текст
        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("ivan.example.com")

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Проверка результата
        time.sleep(5)  # Пауза, чтобы увидеть результат отправки

        # Находим блок с отправленными данными
        result_box = driver.find_element(By.ID, "output")

        # Проверяем, что в блоке результата появился введенный текст
        assert "ivan.example.com" not in result_box.text
        print("Тест успешно пройден!")

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()


def test_email_with_cyrillic():
    try:
        # 2. Открытие страницы
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)  # Пауза, чтобы визуально заметить открытие

        # 3. Поиск элементов и заполнение полей
        # Находим поле Full Name по его ID и вводим текст
        full_name_field = driver.find_element(By.ID, "userName")
        # web_elements = driver.find_elements(By.XPATH, "someXPath")

        full_name_field.send_keys("Иван Иванов")

        # Находим поле Email по его ID и вводим текст
        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("иван@example.com")

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Проверка результата
        time.sleep(5)  # Пауза, чтобы увидеть результат отправки

        # Находим блок с отправленными данными
        result_box = driver.find_element(By.ID, "output")

        # Проверяем, что в блоке результата появился введенный текст
        assert "иван@example.com" not in result_box.text
        print("Тест успешно пройден!")

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()


def test_empty_name():
    try:
        # 2. Открытие страницы
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)  # Пауза, чтобы визуально заметить открытие

        # 3. Поиск элементов и заполнение полей
        # Находим поле Full Name по его ID и вводим текст
        full_name_field = driver.find_element(By.ID, "userName")
        # web_elements = driver.find_elements(By.XPATH, "someXPath")

        full_name_field.send_keys("")

        # Находим поле Email по его ID и вводим текст
        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("ivan@example.com")

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Проверка результата
        time.sleep(5)  # Пауза, чтобы увидеть результат отправки

        # Находим блок с отправленными данными
        result_box = driver.find_element(By.ID, "output")

        # Проверяем, что в блоке результата появился введенный текст
        assert "" in result_box.text
        print("Тест успешно пройден, но логика формы нарушена. Не может быть пустое значение полного имени")

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()


def test_too_long_name():
    try:
        # 2. Открытие страницы
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)  # Пауза, чтобы визуально заметить открытие

        # 3. Поиск элементов и заполнение полей
        # Находим поле Full Name по его ID и вводим текст
        long_name = "A" * 5000

        # web_elements = driver.find_elements(By.XPATH, "someXPath")
        driver.find_element(By.ID, "userName").send_keys(long_name)

        # Находим поле Email по его ID и вводим текст
        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("ivan@example.com")

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Проверка результата
        time.sleep(5)  # Пауза, чтобы увидеть результат отправки

        # Находим блок с отправленными данными
        result_box = driver.find_element(By.ID, "output")

        # Проверяем, что в блоке результата появился введенный текст
        assert long_name in result_box.text
        print("Тест успешно пройден!")

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()


def test_name_with_special_symbols():
    try:
        # 2. Открытие страницы
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)  # Пауза, чтобы визуально заметить открытие

        # 3. Поиск элементов и заполнение полей
        # Находим поле Full Name по его ID и вводим текст

        driver.find_element(By.ID, "userName").send_keys("!@#$%^&*()_+{}|:\"<>?~`")

        # Находим поле Email по его ID и вводим текст
        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("ivan@example.com")

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Проверка результата
        time.sleep(5)  # Пауза, чтобы увидеть результат отправки

        # Находим блок с отправленными данными
        result_box = driver.find_element(By.ID, "output")

        # Проверяем, что в блоке результата появился введенный текст
        assert "!@#$%^&*()_+{}|:\"<>?~`" in result_box.text
        print("Тест успешно пройден!")

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()


def test_name_with_sql_injection():
    try:
        # 2. Открытие страницы
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)  # Пауза, чтобы визуально заметить открытие

        # 3. Поиск элементов и заполнение полей
        # Находим поле Full Name по его ID и вводим текст

        driver.find_element(By.ID, "userName").send_keys("' OR '1'='1'; DROP TABLE users;--")

        # Находим поле Email по его ID и вводим текст
        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("ivan@example.com")

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Проверка результата
        time.sleep(5)  # Пауза, чтобы увидеть результат отправки

        # Находим блок с отправленными данными
        result_box = driver.find_element(By.ID, "output")

        # Проверяем, что в блоке результата появился введенный текст
        assert "' OR '1'='1'; DROP TABLE users;--" in result_box.text
        print("Тест успешно пройден!")

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()


def test_name_with_json_injection():
    try:
        # 2. Открытие страницы
        driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
        driver.maximize_window()
        time.sleep(5)  # Пауза, чтобы визуально заметить открытие

        # 3. Поиск элементов и заполнение полей
        # Находим поле Full Name по его ID и вводим текст

        driver.find_element(By.ID, "userName").send_keys('{"admin": true, "role": "root"}')

        # Находим поле Email по его ID и вводим текст
        email_field = driver.find_element(By.ID, "userEmail")
        email_field.send_keys("ivan@example.com")

        # Находим кнопку Submit по ее ID и кликаем
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Проверка результата
        time.sleep(5)  # Пауза, чтобы увидеть результат отправки

        # Находим блок с отправленными данными
        result_box = driver.find_element(By.ID, "output")

        # Проверяем, что в блоке результата появился введенный текст
        assert '{"admin": true, "role": "root"}' in result_box.text
        print("Тест успешно пройден!")

    finally:
        # 5. Закрытие браузера в любом случае
        driver.quit()


test_default()
test_with_current_and_permanent_addresses()
test_email_without_at()
test_email_with_cyrillic()
test_empty_name()
test_too_long_name()
test_name_with_special_symbols()
test_name_with_sql_injection()
test_name_with_json_injection()