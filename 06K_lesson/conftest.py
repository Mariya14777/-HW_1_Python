import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
import os

DRIVERS_PATH = r"C:\Users\Admin\OneDrive\Desktop\01_lesson\drivers"


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="edge",
        help="Browser: edge")


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")

    if browser_name == "edge":
        service = EdgeService(
            executable_path=os.path.join(
                DRIVERS_PATH,
                "msedgedriver.exe"))
        driver = webdriver.Edge(service=service)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.maximize_window()
    yield driver
    driver.quit()
