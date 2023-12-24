# type:ignore

"""Conftest"""

from pathlib import Path

import pytest
from pytest import fixture


class Config:
    """Env"""

    def __init__(self, env: str):
        self.base_url = {
            "dev": "https://mydev-env.com",
            "qa": "https://myqa-env.com",
            "staging": "staging",
        }[env]

        self.app_port = {"dev": 8080, "qa": 80, "staging": 8088}[env]


def pytest_addoption(parser):
    """Doc"""
    parser.addoption("--env", action="store", help="Environment to run tests against")
    parser.addoption("--menu-item", default="domains")
    parser.addoption("--expected-url", default="https://www.iana.org/domains")


@fixture(scope="session")
def env(request):
    """Doc"""
    return request.config.getoption("--env")


@fixture(scope="session")
def app_config(env):
    """Doc"""
    cfg = Config(env)
    return cfg


def pytest_runtest_makereport(item, call) -> None:
    """Func"""
    if call.when == "call":
        if call.excinfo is not None and "page" in item.funcargs:
            page = item.funcargs["page"]
            screenshot_dir = Path(".playwright-screenshots")
            screenshot_dir.mkdir(exist_ok=True)
            page.screenshot(path=str(screenshot_dir / f"screenshot-{1}.png"))


@pytest.fixture
def menu_item(request):
    """Func"""
    return request.config.getoption("--menu-item")


@pytest.fixture
def expected_url(request):
    """Func"""
    return request.config.getoption("--expected-url")
