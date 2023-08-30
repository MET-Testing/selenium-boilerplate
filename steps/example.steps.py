from behave import given, when, then
from pages.google_page import GooglePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@given(u'I am at google')
def open_google(context):
    context.google_page = GooglePage(context.browser)
    context.google_page.open()


@when(u'I search for "{stuff}"')
def search_stuff(context, stuff):
    context.google_page.search(stuff)


@then(u'I see "{stuff}" in results')
def check_stuff(context, stuff):
    # Esperar hasta que al menos un resultado esté visible
    WebDriverWait(context.google_page.browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//h3'))
    )
    results = context.google_page.get_results()
    result_texts = [result.text.lower() for result in results]
    assert any(stuff.lower() in text for text in result_texts)
