# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import allure
import pytest

import codecs
import os
import sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert

from widgetastic.browser import Browser

selenium_browser = None


class CustomBrowser(Browser):
    @property
    def product_version(self):
        return '1.0.0'


@pytest.fixture(scope='session')
def selenium(request):
    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub', 
        desired_capabilities={'platform': 'LINUX', 'browserName': 'chrome', 'unexpectedAlertBehaviour': 'ignore'}
        )
    request.addfinalizer(driver.quit)
    driver.maximize_window()
    global selenium_browser
    selenium_browser = driver
    return driver


@pytest.fixture(scope='function')
def browser(selenium):
    this_module = sys.modules[__name__]
    selenium.get('http://jdoe:password@sws-istio-system.openshift.jonqe.lab.eng.bos.redhat.com/console/services')
    return CustomBrowser(selenium)


def pytest_exception_interact(node, call, report):
    if selenium_browser is not None:
        allure.attach(
            'Error screenshot', selenium_browser.get_screenshot_as_png(), allure.attach_type.PNG)
        allure.attach('Error traceback', str(report.longrepr), allure.attach_type.TEXT)
