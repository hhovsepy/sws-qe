from project.sws_view import ServiceListView
import time
import pytest

@pytest.mark.group2
def test_service_search1(browser):
    view = ServiceListView(browser)
    for row in view.services:
        assert row
    view.simple_search('sws')
    for row in view.services:
        assert "sws" in row[0].text
    time.sleep(5)

@pytest.mark.group2
def test_service_search2(browser):
    view = ServiceListView(browser)
    for row in view.services:
        assert row
    view.simple_search('sws')
    for row in view.services:
        assert "sws" in row[0].text
    time.sleep(5)   
    
    
@pytest.mark.group2
def test_service_search3(browser):
    view = ServiceListView(browser)
    for row in view.services:
        assert row
    view.simple_search('sws')
    for row in view.services:
        assert "sws" in row[0].text
    time.sleep(5)   
    
@pytest.mark.group2
def test_service_search4(browser):
    view = ServiceListView(browser)
    for row in view.services:
        assert row
    view.simple_search('sws')
    for row in view.services:
        assert "sws" in row[0].text
    time.sleep(5)   
    
@pytest.mark.group2   
def test_service_search5(browser):
    view = ServiceListView(browser)
    for row in view.services:
        assert row
    view.simple_search('sws')
    for row in view.services:
        assert "sws" in row[0].text
    time.sleep(5)   
