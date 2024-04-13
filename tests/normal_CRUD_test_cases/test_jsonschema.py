# Step1 : Get the response
# Step2: Create the JSON schema from: https://www.jsonschema.net/
# Step3: Save that schema into the name.json file
# Step4: if you want to validate the json schema - https://www.jsonschemavalidator.net/
import json

from jsonschema import validate  # we can install by using command:- pip install jsonschema
import pytest
import allure

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper_class import post_request
from src.helpers.common_verification import verify_http_status_code, verify_json_key_for_not_null
from src.helpers.payload_manager import payload_create_booking
from src.utils.utils import Util
import os  # to get the path of file
from jsonschema.exceptions import ValidationError  # we will get some exceptions also


class TestCreateBookingJsonSchema(object):  # We can import the object

    def load_schema(self, file_name):  # This function will load the schema
        with open('file_name', 'r') as file:
            return json.load(file)

    @pytest.mark.positive
    @allure.title("Verify that Create booking status and booking ID should not be null")
    @allure.description(
        "Creating a booking from the payload and verify that booking id should not be null and status code should be 200 for the correct payload")
    def test_create_booking_schema(self):
        # to make a request, we need URL, payload and headers. we can import URL, payload and headers.
        # Now we will write test cases.
        # we will get everything like url, auth , headers etc. directly from functions
        # Below response we want to verify
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

        # Need to verify response with schema.json stored
        # print(os.getcwd())
        file_path = os.getcwd()+"\Create_Booking_Schema.json"
        schema = self.load_schema(file_name=file_path)  # here schema is present
        try:
            # response=response.json(): means where is your response?--> Response is present in response.json()
            # Where is the layout present? --> In schema
            # where is your schema present? --> schema = self.load_schema(file_name=file_path)
            validate(response=response.json(), schema=schema)  # Validate our response with the schema stored
        except ValidationError as v:
            print(v.message)
            # pytest.xfail("Incorrect JSON schema")
            pytest.fail("Failed: JSON schema error")
            # xfail: will give you warnings
            # fail: fail will fail the test case

