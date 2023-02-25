
# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# @pytest.fixture(scope="function")
# def browser():
#     options = Options()
#     options.add_experimental_option('prefs', {'intl.accept_languages': 'ru'})
#     browser = webdriver.Chrome(options=options)
#     yield browser
#     browser.quit()
#
# def pytest_addoption(parser):
#     parser.addoption('--browser_name', action='store', default="chrome",
#                      help="Choose browser: chrome or firefox")
#     parser.addoption(
#         '--language',
#         action="store",
#         default="en",
#         help="Language to use for the test"
#     )
#
#
# @pytest.fixture(scope="function")
# def browser(request):
#     browser_name = request.config.getoption("browser_name")
#     user_language = request.config.getoption("language")
#     browser = None
#     if browser_name == "chrome":
#         print("\nstart chrome browser for test..")
#         options = Options()
#         options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
#
#         browser = webdriver.Chrome(options=options)
#     elif browser_name == "firefox":
#         print("\nstart firefox browser for test..")
#         browser = webdriver.Firefox()
#     else:
#         raise pytest.UsageError("--browser_name should be chrome or firefox")
#     yield browser
#     print("\nquit browser..")
#     browser.quit()


# Если что то не работает, то пробуй конфиг выше

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption(
        '--language',
        action="store",
        default="en",
        help="Language to use for the test"
    )

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()