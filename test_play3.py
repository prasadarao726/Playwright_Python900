from playwright.sync_api import sync_playwright
import pytest

@pytest.mark.reg1
def test_22():
    print("playwright")
@pytest.mark.reg2
def test_23():
    print("playwright playwright")    