# In utils, either we can create class or directly methods whatever is comfortable.
# We can keep here common headers and common utilities.

# common header of Json is: "Content-Type": "application/json". This is a function which will return common headers.
class Util(object):
    def common_headers_json(self):
        headers = {
            "Content-Type": "application/json"
        }
        return headers

    # for e.g. in the future, we require "application xml", we can keep it in future also if we don't use it right now.
    def common_headers_xml(self):
        headers = {
            "Content-Type": "application/xml"
        }
        return headers

    # one more common header for put and delete request is different. In this case, we need to add authorization,
    # basic authorization, we need to add. In case of put request, we can use authorization as basic authentication or we
    # can use Authorization (in Headers). If we don't use cookies, we can use Authorization. This will also work.
    # There are 2 ways of authenticate:
    # 1) Basic Authentication where we will add authorization header.
    # 2) By using cookie mechanism.
    # def common_headers_put_patch_delete_by_basic_auth(self):
    #     headers = {
    #         "Content-Type": "application/json",
    #         "Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM=" # Instead of hard coding, we can use like this also.
    #     }
    #     return headers

    def common_headers_put_patch_delete_by_basic_auth(self, basic_auth_value):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Basic" + str(basic_auth_value) # Instead of hard coding, we can use like this also.
        }
        return headers

    def common_headers_put_patch_delete_by_cookie(self, token):
        headers = {
            "Content-Type": "application/json",
            "cookie": "token=" + str(token)
        }
        return headers

    # All the common things (utilities) we can keep in utils. utils is for the common things. In the future,
    # we will keep like this also, For eg: read csv file and give me text I have added headers as of now,
    # but you will read scv file.
    def read_csv_file(self):
        pass

    # We can keep a function like read environment variable file? Yes we can.
    def read_env_variable_file(self):
        pass

    # We can keep everything (all functions) into a class also. All these are not static methods. we will create an
    # object for them (utils) like below: If we want to use utils, we need to use like this: util = Util(
    # ).common_headers_json() # Create an object of class : Util (name of the Object) and then call. This is how we
    # will be using in the future.

    def read_database(self):
        pass
    # Note: As of now we have kept common headers in utils and a couple of other utilities which we will use in the
    # future.


