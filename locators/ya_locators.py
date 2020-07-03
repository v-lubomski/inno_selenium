"""Локаторы."""

from selenium.webdriver.common.by import By


class YaPageLocators:
    """Локаторы поисковой страницы Яндекс."""
    INPUT_SEARCH = (By.ID, 'text')
    SEARCH_BUTTON = (By.XPATH, '//button')
