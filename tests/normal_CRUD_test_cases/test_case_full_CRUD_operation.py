# Full CRUD operation means where will we have our below things:
# 1. Create Token
# 2. Create Booking (PUT) - from create booking, we will get booking_ID
# 3. Update the booking id - To update the booking id, we need BookingID and Token
# 4. Delete the booking

# TC#1--> Verify that created booking id and when we update, we are able to update it and delete it.
# To perform TC#1, we need
# Create Token
# Create Booking
# We need to pass the data to test_update ()
# Fixture will help to pass the data in pytest

import pytest
import allure
from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper_class import *
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import Util


# We are going to inherit from Object class. This is optional to type "object"
class TestCRUDBooking(object):

    # First 2 functions are normal function, not test functions. so, we will mark them fixture as we will
    # be passing the data.
    # create_token and get_booking_id both we have already tested. we will not be testing it and will mark
    # them as fixture

    # This function i.e. "create_token" contains test case as we have mentioned 2 assertions as well
    # as it's returning token also. This fixture is doing both things.
    # Advantage of this fixture is it can be used throughout any test case. Right now I am using this fixture
    # in this "TestCRUDBooking" class only, but I can put it into contest so that it can be used by anyone.
    # It wil basically become reusable thing.

    @pytest.fixture()
    def create_token(self):  # first we need a function to create token
        response = post_request(
            url=APIConstants.url_create_token(),
            headers=Util().common_headers_json(),
            auth=None,
            payload=payload_create_token(),
            in_json=False
        )
        verify_http_status_code(response_data=response, expect_data=200)
        verify_json_key_for_not_null_for_token(response.json()["token"])
        return response.json()["token"]

    @pytest.fixture()
    def get_booking_id(self):  # need to function to get booking id
        response = post_request(url=APIConstants.url_create_booking(),
                                auth=None,
                                headers=Util().common_headers_json(),
                                payload=payload_create_booking(),
                                in_json=False)
        # After getting the response, we want booking_id
        booking_id = response.json()["bookingid"]
        # we don't need cookies in post request
        verify_http_status_code(response_data=response, expect_data=200)
        verify_json_key_for_not_null(booking_id)
        return booking_id

    @allure.title("Test CRUD operation Update(PUT).")
    @allure.description("Verify that full update with the booking ID and Token is working.")
    def test_update_booking_id_token(self, create_token, get_booking_id):
        booking_id = get_booking_id
        token = create_token
        put_url = APIConstants.url_patch_put_delete(booking_id=booking_id)
        response = put_request(
            url=put_url,
            headers=Util().common_headers_put_patch_delete_by_cookie(token=token),
            payload=payload_create_booking(),
            auth=None,
            in_json=False
        )
        print(response.json())
        verify_http_status_code(response_data=response.json(), expect_data=200)

    @allure.title("Test CRUD operation Delete(delete).")
    @allure.description("Verify booking gets deleted with the booking ID and Token")
    def test_delete_booking_id(self):
        pass
