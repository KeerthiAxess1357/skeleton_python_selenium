import logging

from automation.modules.Home_page import HomePage


def test_dominos_order(launch_browser):
    logging.info("launch chrome browser")
    driver = launch_browser
    homepage = HomePage(driver)
    logging.info("fill the cantact form...")
    homepage.cantact_form()
    homepage.another_page()
