import pytest
from selenium import webdriver


# для корректного отображения кириллицы в параметризаторах
def pytest_make_parametrize_id(config, val): return repr(val)

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Укажите атрибут --browser_name: chrome или firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name =request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        browser = webdriver.Chrome('C:\\Users\\vavil\\Desktop\\chromedriver')
        print("СТАРТ ХРОМ")
    elif browser_name == "firefox":
        browser = webdriver.Firefox('C:\\Users\\vavil\\Desktop\\geckodriver\\')
        print("ОТКРЫЛИ ФАЕРФОКС")
    else:
        raise pytest.UsageError("Необходимо указать --browser_name: chrome или firefox")
    yield browser
    print("Закрыли браузер")
    browser.quit()
