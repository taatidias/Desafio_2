import os
from appium import webdriver
from time import sleep


def before_step(context, step):
    sleep(2)


def before_feature(context):
    app = os.path.join(os.path.dirname(__file__),
                       '../app',
                       'app-debug.apk')
    app = os.path.abspath(app)
    context.driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723/wd/hub',
        desired_capabilities={
            'app': app,
            'platformName': 'Android',
            'platformVersion': '4.4',
            'deviceName': None,
            'udid': '01a135891395669f',
            'appActivity': '.HomeActivity',
            'appPackage': 'com.android.mobile'
        }
    )


def after_feature(context, feature):
    context.driver.quit()

