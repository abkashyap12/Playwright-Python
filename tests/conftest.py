import pytest
from playwright.sync_api import Page

@pytest.fixture(autouse=True)
def visit_page(page: Page):
    page.goto("https://playwright.dev/")
    