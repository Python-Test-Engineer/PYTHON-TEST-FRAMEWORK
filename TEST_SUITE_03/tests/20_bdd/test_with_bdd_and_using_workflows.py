# type: ignore

"""Doc"""


from playwright.sync_api import Page
from pytest_bdd import given, scenario, then, when

from pages.ican_navigation import IcanNavigationMenu
from Workflows import example_workflows


@scenario("tests.feature", "user can navigate to the ican page")
def test_user_can_navigate_to_each_link():
    """Doc"""
    print("starting bdd test")


@given("an example site")
def goto_website(page: Page):
    """Doc"""
    example_workflows.open_example_site_verify_page_load(page)


@when('they click on the "More information" link')
def navigate_to_ican(page: Page):
    """Doc"""
    example_workflows.navigate_to_more_information_page_verify_menus(page)


@then("they are able to navigate to the expected web page")
def check_ican_nav_menu(page: Page, menu_item, expected_url):
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
    assert page.url == expected_url, f"Expected URL {expected_url}, but got {page.url}"
