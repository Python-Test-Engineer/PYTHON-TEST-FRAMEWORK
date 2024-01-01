"""Tests for Pets API"""

import requests

from utilities.boxen import bx_info, bx_result
from utilities.resources import ApiResources

URL = ApiResources.BASE_URL_PET_API
payload = {"id": int(200), "name": "LEO", "status": "pending"}


def test_post_pet() -> None:
    """Test post api works"""
    bx_info("getting data from api...")
    add_pet_response = requests.post(
        URL,
        json=payload,
        headers={"Content-Type": "application/json"},
    )

    response_json = add_pet_response.json()
    response_status = str(response_json["status"]).upper()
    response_id = str(response_json["id"]).upper()
    response_name = str(response_json["name"]).upper()
    bx_result(str(response_json))

    assert (
        response_id == "200" and response_name == "LEO" and response_status == "PENDING"
    )
