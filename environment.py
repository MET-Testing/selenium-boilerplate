from selenium import webdriver


def before_all(context):
    browser = context.config.userdata.get('BROWSER', 'chrome').lower()

    if browser == 'chrome':
        context.browser = webdriver.Chrome()
    elif browser == 'firefox':
        context.browser = webdriver.Firefox()
    elif browser == 'edge':
        context.browser = webdriver.Edge()
    elif browser == 'safari':
        context.browser = webdriver.Safari()
    # Puedes agregar más navegadores aquí
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    context.browser.maximize_window()

    webdriver.autoinstall = True

    # context.driver = webdriver.Chrome()  # O el navegador que prefieras


def after_all(context):
    context.browser.quit()

# Puedes agregar más métodos de configuración y manejo de recursos aquí
