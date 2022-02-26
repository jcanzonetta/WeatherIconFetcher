import time
import json
import os

UPDATE_INTERVAL = 120  # Sets the frequency to check for a new request.

# The following two parameters are not intended to be updated unless new icons are added.
# Used to check if the description value in the JSON is valid.
DESC_ARRAY = ["sun", "storm", "snow-storm",
              "snow", "sleet", "rain-cloud", "rain", "partly-cloudy-day", "moon-and-stars", "light-snow", "hail", "fog"]
# Used to check if the size in the JSON is one of three values.
SIZE_ARRAY = [24, 48, 96]


def weather_icon_fetcher():

    try:
        with open("request.json", "r") as file:
            request = json.load(file)

        # Check that the value provided for description is valid.
        desc = check_description(request["description"])

        # Check that the value provided for size is valid.
        size = request["size"]
        if size not in SIZE_ARRAY:
            raise IndexError

        icon_filename = "icons8-" + desc + "-" + str(size) + ".png"

        response = os.getcwd() + "/Weather_Icons/" + icon_filename

    except json.decoder.JSONDecodeError:
        print("JSON file is not valid.")
        response = "False"
    except KeyError:
        print("A required parameter in the JSON file was not provided.")
        response = "False"
    except IndexError:
        print("A parameter provided was out of the allowed range. Please check the readme for expected parameter ranges.")
        response = "False"
    else:
        # If there are no errors, check if the new response is the same as what is already saved.
        with open("response.txt", "r") as file:
            old_response = file.read()

        if old_response == response:
            print("No change in request.")
        else:
            print("Valid JSON parsed. Providing new icon.")

    # Finally write the response to response.txt.
    with open("response.txt", "w") as file:
        file.write(response)


def check_description(desc):
    # Checks that the description value in the JSON is within the specifications.

    i = 0
    while type(desc) == str and i < len(DESC_ARRAY):
        if desc == DESC_ARRAY[i]:
            desc = i
        else:
            i += 1

    # An IndexError is used to determine if the parameter is out of spec.
    if type(desc) == str:
        raise IndexError

    return DESC_ARRAY[desc]


if __name__ == "__main__":
    while True:
        weather_icon_fetcher()
        print(f"Waiting {UPDATE_INTERVAL} seconds for next update.")
        time.sleep(UPDATE_INTERVAL)
