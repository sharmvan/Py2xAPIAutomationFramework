# In this, we can create a class or functions in which we are comfortable. Wrapper means if you have seen
# "request.get()": This function is common. I can make this request 100 times. So, we can create utilities,
# a helper function which means if I want to make a get request, To make a get request, we will be required:
# URL, amy authentication if needed, and we want in json. To make this request, we need to import requests.
import requests
import json


# we have created a common utility to make a get request. Pass the url and in the future,
# if we require authentication, directly we can use api_wrappers.
# No need to add exception here. we will add in our test cases.
def get_request(url, auth):  # To make a get request, we require url, auth
    get_response = requests.get(url=url, auth=auth)
    # return response  --> in this get request, we are not returning our response in json. we are directly returning as
    # normal response. So, we can return in json like below:
    return get_response.json()  # whatever the response will come, it will return in json form.


def post_request(url, auth, headers, payload,
                 in_json):  # To make a post request, we require url, auth, headers, payload
    post_response = requests.post(url=url, auth=auth, headers=headers, data=json.dumps(payload))  # "json.dump" will
    # make sure that whatever the payload you are setting as a dictionary, it will get converted into json only because
    # while making the create request, it should be json. for eg: we have a dictionary like this:
    # Can I create a dictionary with single quotes? In Python, we can create a dictionary with single quotes also.
    # But this is not a valid json
    # dict{
    # 'name':'Vandana # this was created by one person and I have created with double quotes like "name":"Vandana".
    # }              # so, there will be a problem. double quotes is resembling with the json. Hence, we are assuming is it
    # doesn't matter what you put, we will always convert this into json."json.dump" means always convert payload into
    # pure json. In this function, we will add a samrt logic. smart logic is do you want response is in json?
    # A boolean variable i will add i.e. "in_json". If I want "in_json is True (in boolean)", then I will return in json
    # else I will return normal. because sometimes we need to use "response.status_code", "response.txt", "response.headers"
    # In that case, we will not pass through "in_json".
    if in_json is True:
        return post_response.json()
    return post_response

    # For patch request, we need everything like "post_request". just need to modify the method name from "post
    # method" to "patch method".


def patch_request(url, auth, headers, payload, in_json):
    patch_response = requests.patch(url=url, auth=auth, headers=headers, data=json.dumps(payload))
    if in_json is True:
        return patch_response.json()
    return patch_response


# For put request, we need everything like "post_request". just need to modify the method name from "post
# method" to "put method".


def put_request(url, auth, headers, payload, in_json):
    put_response = requests.put(url=url, auth=auth, headers=headers, data=json.dumps(payload))
    if in_json is True:
        return put_response.json()
    return put_response


# We don't need payload in "delete" method.
# We don't need booking_id here as URL will contain the booking id.
# URL will come from "APIConstant" class which contains multiple functions.
def delete_request(url, auth, headers, in_json):
    delete_response = requests.delete(url=url, auth=auth, headers=headers)
    if in_json is True:
        return delete_response.json()
    return delete_response

