import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

global driver

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="Type in browser name")

@pytest.fixture(scope="function")
def browserInstance(request):
    options = Options()
    options.add_argument("--incognito")

    # ✅ Disable password manager and credential saving
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2,
        "profile.default_content_setting_values.popups": 2,
        "profile.default_content_setting_values.automatic_downloads": 1
    }
    options.add_experimental_option("prefs", prefs)

    # ✅ Disable Chrome automation banners and infobars
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--no-default-browser-check")
    options.add_argument("--disable-blink-features=AutomationControlled")

    options.add_experimental_option("prefs", prefs)

    global driver
    browser_name=request.config.getoption("--browser_name")
    if browser_name== "chrome":
        driver= webdriver.Chrome(options=options)
    elif browser_name== "firefox":
        driver= webdriver.Firefox()


    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.close()

@pytest.hookimpl( hookwrapper=True )
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin( 'html' )
    outcome = yield
    report = outcome.get_result()
    extra = getattr( report, 'extra', [] )

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr( report, 'wasxfail' )
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join( os.path.dirname( __file__ ), 'reports' )
            file_name = os.path.join( reports_dir, report.nodeid.replace( "::", "_" ) + ".png" )
            print( "file name is " + file_name )
            _capture_screenshot( file_name )
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append( pytest_html.extras.html( html ) )
        report.extras = extra


def _capture_screenshot(file_name):
    driver.get_screenshot_as_file(file_name)



# pytest test_e2eTestFramework.py --browser_name firefox