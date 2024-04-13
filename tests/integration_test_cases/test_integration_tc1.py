# Integration Scenarios:

# Scenario_1 Verify that after Create Booking-> Will do Patch Request-> Verify that firstname is updated.
# Scenario_2 Create a Booking, Delete the Booking with ID and Verify using GET request that it should not exist.
# Scenario_3 Get an Existing Booking id from Get All Bookings Ids, Update a booking and verify using GET by id.
# Scenario_4 Create a booking and delete it.
# Scenario_5 Invalid creation - enter a wrong payload or wrong JSON.
# Scenario_6 Trying to update on a delete ID -> 404

# We will be verifying for each request:
# 1. Response
# 2. Status Code
# 3. Headers

# Assertions will always pass even for -ve scenarios as well. For eg:
# In Create Booking -ve test case, If we don't give any payload, our assertion is that it should give us 500.
# Overall this -ve test case will get pass. Even though -ve test cases also we want to pass.
# As an automation tester, our responsibility is you create a test case and those will pass even if it is a
# -ve test case.

