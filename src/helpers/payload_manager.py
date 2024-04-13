# payload manager help you to keep the payloads.
# We have dictionary payload with keys and values.
from faker import Faker

faker = Faker()
import json


def payload_create_booking():
    payload = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    return payload


# above-mentioned function is hardcoded. I can also create dynamic.
# dynamic means I can import Faker library from faker and import Json also.
def payload_create_booking_dynamic():
    payload = {
        "firstname": faker.first_name(),  # If I want to generate fake data instead of James then I can use. This will
        # generate fake name automatically if we need dynamic data.
        "lastname": faker.first_name(),
        "totalprice": faker.random_int(min=100, max=1000),
        "depositpaid": faker.boolean(),
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": faker.ramdom_element(elements=("Breakfast", "Parking", "Wifi"))
    }
    return payload


# Real time use of faker is. Let's say suppose I have checked my data where the name='vandana' but i want to check
# name with some Arabic name, then we can use faker. Also check like booking_id is working or not with Arabic name,
# then we can ask faker to give me a random first name which can be in chinese, Arabic or some other extra languages.
# These are extra test cases. In Extra test cases, dynamic data is required but right we are testing only happy path.
# happy path means create booking +ve test case. Create booking -ve test case will be name=chinese
def payload_create_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    return payload


# We can also import create booking data from Excel file also in the future.
# def payload_create_booking_data_excel():
#     payload = {
#         "firstname": read_from_excel["firstname"],
#         "lastname": faker.first_name(),
#         "totalprice": faker.random_int(min=100, max=1000),
#         "depositpaid": faker.boolean(),
#         "bookingdates": {
#             "checkin": "2018-01-01",
#             "checkout": "2019-01-01"
#         },
#         "additionalneeds": faker.ramdom_element(elements=("Breakfast", "Parking", "Wifi"))
#     }
#     return payload
