"""Описание методов работы со страницами."""

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from locators.ya_locators import YaPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

YA_URL = 'http://www.ya.ru'


class YaPage:
    """Методы для работы со страницей Яндекса."""

    driver = webdriver.Chrome(ChromeDriverManager().install())

    # функция из задания 2 - с локатором и временем ожидания
    def click_to_element(self, locator: tuple, time_to_wait: int = 5) -> None:
        """Метод нажатия на какой-либо элемент на странице.

        Принимает на вход:
        locator - локатор элемента
        time_to_wait - время, в течение которого осуществляется попытка
        обнаружить элемент на странице и затем нажать на него.
        """
        driver = self.driver
        try:
            # WebDriverWait по умолчанию опрашивает элемент с шагом 0.5 сек
            # и если время time_to_wait истекло - возбуждает исключение
            elem = WebDriverWait(driver, time_to_wait).until(
                EC.element_to_be_clickable(locator))
            elem.click()
        except TimeoutException:
            raise TimeoutException(f'Время {time_to_wait} истекло')

    def search(self, request: str) -> None:
        """Метод поиска в Яндексе какого либо запроса (request)."""
        driver = self.driver
        elem = driver.find_element(*YaPageLocators.INPUT_SEARCH)
        elem.send_keys(request)
        self.click_to_element(YaPageLocators.SEARCH_BUTTON, 5)

    def open_page(self) -> None:
        """Метод для перехода на страницу по адресу YA_URL."""
        self.driver.get(YA_URL)

    def quit_driver(self) -> None:
        """Метод, который закрывает все окна и процессы вебдрайвера."""
        self.driver.quit()

    def get_page_source(self) -> None:
        """Метод для получения содержимого открытой страницы."""
        return self.driver.page_source
