# It's time to write test cases
import pytest
import allure
from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper_class import post_request
from src.helpers.common_verification import verify_http_status_code, verify_json_key_for_not_null
from src.helpers.payload_manager import payload_create_booking
from src.utils.utils import Util


# Util is a class as we have created this as a class. Under this class, all the functions are not normal.
# If we are creating a class, we need to import class only i.e. Util
class TestCreateBooking(object):  # We can import the object
    @pytest.mark.positive
    @allure.title("Verify that Create booking status and booking ID should not be null")
    @allure.description(
        "Creating a booking from the payload and verify that booking id should not be null and status code should be 200 for the correct payload")
    def test_create_booking_positive(self):
        # to make a request, we need URL, payload and headers. we can import URL, payload and headers.
        # Now we will write test cases.
        # we will get everything like url, auth , headers etc. directly from functions
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

    def test_create_booking_negative(self):
        response = post_request(url=APIConstants.url_create_booking(),
                                auth=None,
                                headers=Util().common_headers_json(),
                                payload={},
                                in_json=False)
        verify_http_status_code(response, 500)


