from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()
class yndex:
    def __init__(self,url) -> None:
        self.url = url
        self.driver = webdriver.Chrome()

    # driver = webdriver.Chrome()
    def load_yandex(self):
        driver = webdriver.Chrome()

        # Загружаем страницу
        driver.get('https://www.ya.ru')

        # Поиск поля ввода
        try:
            
            element = driver.find_element(By.ID, 'text')
            
            # driver.find_elements(By.XPATH, '//input')
            print("yes")
        except NoSuchElementException:
            print('Error')

        # time.sleep(100)
        # вводим текст в поле ввода
        element.send_keys('Тензор')
        try:
            
            element = driver.find_element(By.CSS_SELECTOR, "mini-suggest__popup")
            
            # driver.find_elements(By.XPATH, '//input')
            print("yes sug")
        except NoSuchElementException:
            print('Zero element for U!')
        # нажимаем Enter
        element.submit() #//*[@id="search-result"]/li[2]/div/div[1]/a
        time.sleep(1)

        return True
    def go_links(self):        
    # Переход по ссылке тензор
        driver = webdriver.Chrome()

        driver.get("https://yandex.ru/search/?text=%D1%82%D0%B5%D0%BD%D0%B7%D0%BE%D1%80&lr=55&search_source=yaru_desktop_common&src=suggest_Pers")

        element = driver.find_element(By.XPATH, """//*[@id="search-result"]/li[1]/div/div[1]/a""")
        # выводим текст ссылки и ее адрес
        print(element.text)
        print(element.get_attribute('href') == "https://tensor.ru/")
        try:
            lement = driver.find_element(By.XPATH, '///*[@id="search-result"]/li[2]/div/div[1]/a')
            if lement.get_attribute('href') == 'https://tensor.ru/':
                print('Первая ссылка ведет на сайт tensor.ru')
            else:
                print('Первая ссылка не ведет на сайт tensor.ru')
        except:
            print("no element")
        return True
    def load_picte(self):

    # Переход в картингки

        driver = webdriver.Chrome()
        driver.get('https://www.ya.ru')

        # Поиск поля ввода
        try:
            element = driver.find_element(By.ID, 'text')
            element.send_keys(' ')

            element = driver.find_element(By.XPATH, """/html/body/main/div[2]/form/div[2]/div/nav/ul/li[11]/a/div[1]""")
            element.click()

            # driver.find_elements(By.XPATH, '//input')
            print("yes")
            time.sleep(2)
            element = driver.find_element(By.CLASS_NAME, """services-more-popup__item-icon""")
            element.click()
            time.sleep(2)
        except :
            print('Zero element for U!')
        return True

    def click_picche(self):
        #  работа с картинки 
        driver = webdriver.Chrome()

        # Переход на URL https://yandex.ru/images/
        driver.get("https://yandex.ru/images/")

        # Получение текущего URL и проверка
        if driver.current_url == "https://yandex.ru/images/":
            print("Успешно перешли на URL https://yandex.ru/images/")
        else:
            print("Не удалось перейти на URL https://yandex.ru/images/")

        # Закрытие веб-драйвера
        driver.quit()
        return True

    def category(self):

        # 6) Проверить, что название категории отображается в поле поиска
        driver = webdriver.Chrome()

        # Переход на URL https://yandex.ru/images/
        driver.get("https://yandex.ru/images/")


        # /html/body/div[3]/div[2]/div/div/div/div[1]/a/div[1]
        element = driver.find_element(By.XPATH, """/html/body/div[3]/div[2]/div/div/div/div[1]/a/div[1]""")
        element_text = driver.find_element(By.XPATH, """/html/body/div[3]/div[2]/div/div/div/div[1]/a/div[2]""")

        text1 = element_text.text
        print(element_text.text)
        element.click()
        time.sleep(1)
        element = driver.find_element(By.XPATH, """/html/body/header/div/div[1]/div[2]/form/div[1]/span/span/input""")
        print(element.get_attribute("value"))

        print(text1 == element.get_attribute("value"))

        time.sleep(1)
        return True

    def click_picte1(self):
        # 7) Открыть 1 картинку

        #  работа с картинки 
        from selenium.webdriver.common.action_chains import ActionChains
        driver = webdriver.Chrome()

        # Переход на URL https://yandex.ru/images/
        driver.get("https://yandex.ru/images/")
        element = driver.find_element(By.XPATH, """/html/body/div[3]/div[2]/div/div/div/div[1]/a/div[1]""")
        element.click()
        time.sleep(2)
        # /html/body/div[3]/div[2]/div/div[1]/div/div[2]
        element = driver.find_element(By.XPATH,"""/html/body/div[3]/div[2]/div/div[2]/div/div[1]""")
        actions = ActionChains(driver)
        actions.move_to_element(element)
        actions.click()
        time.sleep(2)
        return True



    def lload(self):
        #Переход на URL https://yandex.ru/images/
        driver.get("https://yandex.ru/images/")
        element = driver.find_element(By.XPATH, """/html/body/div[3]/div[2]/div/div/div/div[1]/a/div[1]""")
        element.click()
        time.sleep(2)
        driver.get("https://yandex.ru/images/search?text=%D0%98%D1%81%D0%BB%D0%B0%D0%BD%D0%B4%D0%B8%D1%8F&nl=1&source=morda")
        time.sleep(2)

        element = driver.find_element(By.XPATH,"""/html/body/div[3]/div[2]/div/div[2]/div/div[1]/div/a/img""")
        element.click()
        current_url = """https://yandex.ru/images/search?text=%D0%98%D1%81%D0%BB%D0%B0%D0%BD%D0%B4%D0%B8%D1%8F&nl=1&source=morda&pos=0&rpt=simage&img_url=http%3A%2F%2Ftraveltimes.ru%2Fwp-content%2Fuploads%2F2021%2F11%2F1920x1200-px-cliff-clouds-fall-field-Iceland-lake-landscape-lava-mountain-nature-river-turquoise-water-waterfall-1103888.jpg&lr=55"""
        driver.get(current_url)
        time.sleep(2)

        element = driver.find_element(By.XPATH,"""/html/body/div[12]/div[2]/div/div/div/div[3]/div/div[1]/div[2]/div[1]/div[3]/div/img""")
        if element.get_attribute("src"):
            print("yes")

        # вывод адреса на экран
        print(current_url)
        time.sleep(2)
        return True
    def load_button(self):

        # 9) Нажать кнопку вперед

        # открытие галере с картинко
        current_url = """https://yandex.ru/images/search?text=%D0%98%D1%81%D0%BB%D0%B0%D0%BD%D0%B4%D0%B8%D1%8F&nl=1&source=morda&pos=0&rpt=simage&img_url=http%3A%2F%2Ftraveltimes.ru%2Fwp-content%2Fuploads%2F2021%2F11%2F1920x1200-px-cliff-clouds-fall-field-Iceland-lake-landscape-lava-mountain-nature-river-turquoise-water-waterfall-1103888.jpg&lr=55"""
        driver.get(current_url)
        time.sleep(1)
        # получение картинки
        element = driver.find_element(By.XPATH,"""/html/body/div[3]/div[2]/div/div[2]/div/div[1]/div/a/img""")
        element.click()
        time.sleep(2)
        # получение первой картинки
        element = driver.find_element(By.XPATH,"""/html/body/div[12]/div[2]/div/div/div/div[3]/div/div[1]/div[2]/div[1]/div[3]/div/div[5]/img""")
        src1 = element.get_attribute("src")
        print(src1)
        # нажатие кнопки
        element = driver.find_element(By.XPATH,"""/html/body/div[12]/div[2]/div/div/div/div[3]/div/div[1]/div[2]/div[1]/div[4]/i""")
        element.click()
        time.sleep(2)

        # получение первой картинки

        element = driver.find_element(By.XPATH,"""/html/body/div[12]/div[2]/div/div/div/div[3]/div/div[1]/div[2]/div[1]/div[3]/div/div[5]/img""")
        src2 = element.get_attribute("src")
        # 10) проверка что картинка сменилась

        print(src2!=src1)
        return True
    def click_button_back(self):
        # 11) Нажать назад
        element = driver.find_element(By.XPATH,"""/html/body/div[12]/div[2]/div/div/div/div[3]/div/div[1]/div[2]/div[1]/div[1]/i""")
        element.click()
        time.sleep(1)
        # 12) Проверить, что картинка осталась из шага 8
        element = driver.find_element(By.XPATH,"""/html/body/div[12]/div[2]/div/div/div/div[3]/div/div[1]/div[2]/div[1]/div[3]/div/div[5]/img""")
        src3 = element.get_attribute("src")
        element = driver.find_element(By.XPATH,"""/html/body/div[12]/div[2]/div/div/div/div[3]/div/div[1]/div[2]/div[1]/div[3]/div/div[5]/img""")
        src1 = element.get_attribute("src")
        print(src1 == src3)
        return True


 






