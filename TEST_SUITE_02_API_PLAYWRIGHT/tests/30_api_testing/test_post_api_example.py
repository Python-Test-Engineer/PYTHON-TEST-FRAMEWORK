import json
from pyboxen import boxen
import requests

BASE_URL = "https://petstore.swagger.io/v2/pet"

payload = {"id": int(200), "name": "LEO", "status": "pending"}


def boxen_result(output, padding=1, margin=1, color="green"):
    print(
        boxen(
            output,
            padding=padding,
            margin=margin,
            color=color,
        )
    )


def boxen_info(info, padding=1, margin=1, color="blue"):
    print(
        boxen(
            info,
            padding=padding,
            margin=margin,
            color=color,
        )
    )


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
