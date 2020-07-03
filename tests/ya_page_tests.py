"""Тесты."""

from pages.ya_pages import YaPage


def test_page() -> None:
    """Функция проверяет нахождение запроса в результатах выдачи Яндекса."""
    python_page = YaPage()
    try:
        python_page.open_page()
        python_page.search('Python')
        assert "Python" in python_page.get_page_source()
    finally:
        python_page.quit_driver()


test_page()
