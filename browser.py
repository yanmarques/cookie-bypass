from selenium import webdriver


def load_driver():
    """Create the webdriver to display custom sites."""
    options = webdriver.FirefoxOptions()
    options.binary_location = "/usr/bin/firefox"
    return webdriver.Firefox(firefox_options=options)


def open(url, cookie_string, secure=True):
    """Open given URL with """
    driver = load_driver()

    # force wait for page load
    # generic, may not work on heavy pages / low internet speed
    driver.implicitly_wait(10)

    # open full-url with correct scheme
    protocol = 'http'
    if secure:
        protocol += 's'
    driver.get(f'{protocol}://{url}')

    # re-set incoming cookies
    driver.delete_all_cookies()
    for c in cookie_string.strip().split(';'):
        (name, value) = c.split('=')
        driver.add_cookie({'name': name, 'value': value})

    driver.refresh()
