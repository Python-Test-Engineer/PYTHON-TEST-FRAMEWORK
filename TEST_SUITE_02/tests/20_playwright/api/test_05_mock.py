from playwright.sync_api import Route, Page


def on_api_call(route: Route):
    """
    Perform an API call and modify the user data.

    Args:
        route (Route): The route object representing the API call.

    Returns:
        None
    """
    response = route.fetch()
    user_data = response.json()

    user_data["lastName"] = "Smith"
    user_data["age"] = 20

    route.fulfill(
        response=response,
        json=user_data,
    )


def test_user_api(page: Page):
    USERS_API_URL = "https://dummyjson.com/users/1"

    page.route(USERS_API_URL, on_api_call)

    response = page.goto(USERS_API_URL)
    print("Got data:", response.json())
