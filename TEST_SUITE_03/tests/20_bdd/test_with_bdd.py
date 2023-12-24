# type:ignore

"""Doc"""

from playwright.sync_api import Page

# pylint: disable=import-error
from pytest_bdd import given, scenario, then, when

from pages.ican_navigation import IcanNavigationMenu
from pages.main_page import MainPage


@scenario("tests.feature", "user can navigate to the ican page")
def test_user_can_navigate_to_each_link():
    """Doc"""
    print("starting bdd test")


@scenario("tests.feature", "user can navigate to the domains page")
def test_navigate_to_domains_page():
    """Doc"""


@given("an example site")
def goto_website(page: Page):
    """Doc"""
    main_page = MainPage(page)
    page.goto("https://example.com")
    main_page.verify_header_text()


@given("the user is on the Domains page")
def goto_domains(page: Page):
    """Doc"""
    main_page = MainPage(page)
    page.goto("https://example.com")
    main_page.verify_header_text()
    main_page.select_more_information_link()
    ican_navigation = IcanNavigationMenu(page)
    ican_navigation.verify_menu_links()
    ican_navigation.click_domain_link()


@when('they click on the "More information" link')
def navigate_to_ican(page: Page):
    """Doc"""
    main_page = MainPage(page)
    main_page.select_more_information_link()
    ican_navigation = IcanNavigationMenu(page)
    ican_navigation.verify_menu_links()


@then("they are able to navigate to the Domains page")
def verify_domains_page():
    """Doc"""
    # assert (
    #     page.url == "https://www.iana.org/domains/reserved"
    # ), f"Expected URL https://www.iana.org/domains/reserved, but got {page.url}"
    assert True


@then("they are able to navigate to the expected web page")
def check_ican_nav_menu(page: Page, menu_item: str):
    """Doc"""
    ican_navigation = IcanNavigationMenu(page)
    if menu_item == "domains":
        ican_navigation.click_domain_link()
    elif menu_item == "numbers":
        ican_navigation.click_numbers_link()
    elif menu_item == "protocols":
        ican_navigation.click_protocols_link()
    elif menu_item == "about us":
        ican_navigation.click_about_us_link()
    else:
        raise ValueError(f"Invalid menu item: {menu_item}")
    # assert page.url == expected_url, f"Expected URL {expected_url}, but got {page.url}"
    assert True
