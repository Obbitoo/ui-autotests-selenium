import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help="Выберите язык интерфейса. Пример: es, en, ru")

    # Можно было создать множество, элементами, которого являются языки.
    # И при отсутствии значения для language рейзить исключение.
    # Однако в задании такого требования небыло, поэтому просто в дефолт значении указал ру.

@pytest.fixture(scope="function")
def browser(request):
    print("\nНачало работы браузера")
    interface_language = request.config.getoption("language")

    options = Options()
    options.add_experimental_option('prefs', {
        'intl.accept_languages': interface_language
    })

    browser = webdriver.Chrome(options=options)  # Инициализация браузера
    yield browser
    print("\nЗавершение работы браузера")
    browser.quit()
