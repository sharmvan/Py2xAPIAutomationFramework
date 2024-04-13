def verify_http_status_code(response_data, expect_data):
    # Whatever the response is there, status code should be equal to the whatever the expected status code that you have given.
    assert response_data.status_code == expect_data, "Failed ER!=AR"


# We can also verify keys.
# If you give me key, it should not be zero. This should be greater than 0.
# This function can be used for booking_id.
# booking_id should not be null. booking_id should be grater than zero.
def verify_json_key_for_not_null(key):
    assert key != 0, "Failed - Key is non Empty" + key
    assert key > 0, "Failed - key is greater than zero"

def verify_json_key_for_not_null_for_token(key):
    assert key != 0, "Failed - Key is non Empty" + key

def verify_response_key_should_not_be_none(key):
    assert key is not None

# Common Verification
# HTTP Status Code
# Headers
# Data Verification
# JSON Schema
