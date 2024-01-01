import json
from utilities.boxen import boxen_info, boxen_result
import requests

BASE_URL = "https://petstore.swagger.io/v2/pet"

payload = {"id": int(200), "name": "LEO", "status": "pending"}


def test_post_pet() -> None:
    """Test post api works"""
    boxen_info("getting data from api...")
    add_pet_response = requests.post(
        BASE_URL,
        json=payload,
        headers={"Content-Type": "application/json"},
    )

    response_json = add_pet_response.json()  # json.loads(add_pet_response.json())
    response_status = str(response_json["status"]).upper()
    response_id = str(response_json["id"]).upper()
    response_name = str(response_json["name"]).upper()
    boxen_result(str(response_json))

    assert (
        response_id == "200" and response_name == "LEO" and response_status == "PENDING"
    )
