from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, selector):
        WebDriverWait(self.driver, 20).until(
            lambda driver: driver.find_element(*selector))
