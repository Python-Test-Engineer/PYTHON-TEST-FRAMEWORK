""" DOC """

from playwright.sync_api import Page

from pages.ican_navigation import IcanNavigationMenu
from pages.main_page import MainPage


def open_example_site_verify_page_load(page: Page):
    """DOC"""
    main_page = MainPage(page)
    page.goto("https://example.com")
    main_page.verify_header_text()


def navigate_to_more_information_page_verify_menus(page: Page):
    """DOC"""
    main_page = MainPage(page)
    ican_navigation = IcanNavigationMenu(page)
    main_page.select_more_information_link()
    ican_navigation.verify_menu_links()


def launch_and_navigate_to_ican_page(page: Page):
    """DOC"""
    open_example_site_verify_page_load(page)
    navigate_to_more_information_page_verify_menus(page)
