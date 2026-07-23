from playwright.sync_api import sync_playwright
import pytest

@pytest.fixture(autouse=True,scope="session")
#automatically calls the function
def test_precondition():
    print("precondition1")
    yield
    print("postcondition")
@pytest.mark.smok99
def test_m88():
    print("the world")
    print("playwright")    