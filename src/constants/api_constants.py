# All the URLs we will keep here.
# "APIConstants" is a class which contains all the endpoints. 
# This is the class which will contains all the endpoints.
class APIConstants(object):  # Created a class which will inherit from the object.
    @staticmethod
    def base_url():
        return "https://restful-booker.herokuapp.com"  # This class "APIConstants" will just return what is the base url.

    # Static method which can be called by without the object. Directly by using the class, we can call it.
    # It means we don't have to create the instance of "APIConstants". Directly we can call "base_url".
    # If there is no static method, that needs to be call with the object. So, we need to create an object for that.
    @staticmethod
    def url_create_booking():
        return "https://restful-booker.herokuapp.com/booking"

    @staticmethod
    def url_create_token():
        return "https://restful-booker.herokuapp.com/auth"

    # update, PUT, PATCH, DELETE - bookingID
    @staticmethod
    def url_patch_put_delete(booking_id):  # A parameter is required.
        return "https://restful-booker.herokuapp.com/booking" + str(
            booking_id)  # We have to append the bookingID in the end.
