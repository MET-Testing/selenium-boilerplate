from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GooglePage:
    SEARCH_INPUT = (By.NAME, 'q')
    SEARCH_BUTTON = (By.NAME, 'btnK')
    RESULTS = (By.XPATH, '//h3')

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.google.com')

    def search(self, query):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(query)
        search_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(self.SEARCH_BUTTON))
        search_button.click()

    def get_results(self):
        return self.browser.find_elements(*self.RESULTS)
