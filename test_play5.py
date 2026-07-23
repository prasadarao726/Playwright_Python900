from playwright.sync_api import sync_playwright,Page
import pytest


@pytest.mark.smoke
def test_search_bar(pagenavigator):
    print("the test is pagenavigator")
    pagenavigator.get_by_placeholder("Search Amazon.in").type("shoes")
    pagenavigator.wait_for_timeout(5000)
    pagenavigator.locator("//input[@id='nav-search-submit-button']").click()
    