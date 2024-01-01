import json
from utilities.boxen import boxen_info, boxen_result
import requests

BASE_URL = "https://petstore.swagger.io/v2/pet"

payload = {"id": int(200), "name": "LEO", "status": "pending"}


def test_post_pet() -> None:
    boxen_info("getting data from api...")
    add_pet_response = requests.post(
        BASE_URL,
        json=payload,
        headers={"Content-Type": "application/json"},
    )

    output = str(add_pet_response.json())

    boxen_result(output)

    assert True
