"""Testing Pets API"""

from typing import Any
import logging


from utils.api_utils import delete_data, get_api_data, put_data
from utils.myconfigparser import get_pet_api_url

# uses config in pytest.ini
LOGGER = logging.getLogger(__name__)

# !Create pet first
# basebase_url = "https://petstore.swagger.io/v2/pet/"
basebase_url = get_pet_api_url()

PET_ID = "200"

# you may get failed test for GET as you will need to add a pet with id=200 via post at https://petstore.swagger.io/


# test post a pet
def test_post_pet() -> None:
    """Testing PUT"""
    payload: Any = {"id": int(PET_ID), "name": "LEO", "status": "pending"}
    data, __, __ = put_data(basebase_url, payload)
    LOGGER.info("API call done")
    assert data["id"] == int(PET_ID)
    print(data)


def test_get_pet_by_id() -> None:
    """Testing GET"""
    url = basebase_url + PET_ID
    data, resp_status, time_taken = get_api_data(url)
    assert data["id"] == int(PET_ID)
    assert resp_status == 200
    print("Time Taken: ", time_taken)


# test updating a pet
def test_update_pet() -> None:
    """Testing PUT"""
    payload: Any = {"id": int(PET_ID), "name": "LEO", "status": "pending"}
    data, __, __ = put_data(basebase_url, payload)
    LOGGER.info("API call done")
    assert data["id"] == int(PET_ID)
    print(data)


# test deleting a pet
# @pytest.mark.skip
def test_delete_delete_pet_by_id() -> None:
    """Testing DELETE"""
    url = basebase_url + PET_ID
    api_key: Any = {"api_key": "apiKeys123"}
    data, __, __ = delete_data(url, api_key)
    print(data)
    assert data["message"] == PET_ID
    assert data["code"] == 200
