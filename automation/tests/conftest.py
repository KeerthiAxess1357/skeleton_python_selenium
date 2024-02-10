import time

import pytest
from selenium import webdriver


# @pytest.fixture(params=["chrome", "firefox", "edge"])
@pytest.fixture(params=["chrome"])
def launch_browser(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    elif request.param == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("Unsupported browser")
    driver.maximize_window()
    driver.get("https://atit.org.in/")
    time.sleep(3)
    driver.implicitly_wait(10)
    yield driver  # Yields the driver instance
    driver.quit()
