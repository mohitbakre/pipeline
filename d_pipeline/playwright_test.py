# d_pipeline/playwright_test.py
import pytest
import os
from playwright.sync_api import Page, expect, sync_playwright

# Get the URL of the deployed application from an environment variable
# This will be set by GitHub Actions
APP_URL = os.environ.get("APP_URL")

# Ensure the APP_URL is provided
if not APP_URL:
    raise ValueError("APP_URL environment variable is not set. Cannot run E2E tests.")


@pytest.fixture(scope="session")
def browser_page():
    """
    Fixture to provide a Playwright page for tests.
    Uses a session scope to open and close the browser once for all tests.
    """
    with sync_playwright() as p:
        # Use Chromium browser for the test
        browser = p.chromium.launch()
        page = browser.new_page()
        yield page
        browser.close()


def test_app_hello_world(browser_page: Page):
    """
    Tests that the main page of the deployed application displays "Hello, World!".
    """
    print(f"\nNavigating to {APP_URL}")
    browser_page.goto(APP_URL)
    expect(browser_page.locator("body")).to_contain_text("Hello, World!")
    print("Successfully found 'Hello, World!' on the main page.")


def test_app_healthz(browser_page: Page):
    """
    Tests that the /healthz endpoint returns a healthy status.
    """
    healthz_url = f"{APP_URL}/healthz"
    print(f"Navigating to {healthz_url}")
    browser_page.goto(healthz_url)
    # Expect the page content to be the JSON string for healthy status
    expect(browser_page.locator("body")).to_contain_text('{"status":"healthy"}')
    print("Successfully found 'healthy' status on /healthz endpoint.")

# You can run this file locally for testing with:
# set APP_URL=https://your-render-app-url.onrender.com
# pytest playwright_test.py
# (On Linux/macOS: export APP_URL=https://your-render-app-url.onrender.com)
