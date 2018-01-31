# -*- coding: latin-1 -*-

# Made by Johannes Kvamme, 04.09.17
# This scripts uses OW4's API to find dinners and courses for 2. graders at Online studentorganisation.
# The URL contains a query with todays date and pulls all coming events, sorts through the JSON-data and adds
# it to a list if all criterias meet.

import json
import datetime

import requests

today = str(datetime.date.today())

url = 'https://online.ntnu.no/api/v1/events/?event_start__gte='+today

# Empty list for scanApi to fill with the events with the correct rules.
availableEvents = []

# The list of rule names including 2. grade. These are predefined by dotkom and is used in the api.
correctRules = ["Mastere og PhD, BiT etter 3 dager", "Bachelor", "1. og 2. klasse", "Bachelor, Master og PhD",
                "2. - 5. klasse","2. - 4. klasse","1. og 2. etter 72 timer","1. og 2. etter 48 timer",
                "Mastere, BiT etter 2 dager","2. klasse etter 48 timer"," 1. og 2. etter 24 timer","2. og 3.",
                " Alle utenom 1. og 4. etter 24 timer","3., 2. og 4. etter 24 timer, 1. og 5. etter 48 timer",
                "1., 2. og 5. etter 48 timer","Alle utenom 1. og 4. etter 48 timer","1. - 3. Klasse"]

# page = urlopen(url)
# apiMenu = json.loads(page.content.decode("latin1"))
#
# print(apiMenu)


def bedpressFinderApi():
    # Global url is used, so that the global variable can be updated to load next page.
    # Could have been done with a parameter as well.
    global url
    page = requests.get(url)
    # Uses Pythons JSON-library to convert the API-data to a dictionary.
    # Used Latin-1 for norwegian characters, as the API is written with that encoding.
    apiMenu = json.loads(page.content.decode("latin1"))
    # Results is the actual events, as apiMenu contains the metadata as well.
    allFutureEvents = apiMenu['results']
    for element in allFutureEvents:
        # Checks whether it is a company-backed event, to remove parties and other non-relevant events.
        # Also checks whether the event has rules for whom to allow which is located inside [attendance_event].
        # If these fields are null, it is not worth checking.
        if element['company_event'] and element['attendance_event']:
            for rules in element['attendance_event']['rule_bundles']:
                # Ignores rules with numbers and bases only on the textual description of the rules.
                if rules['description'] != "":
                    if rules['description'] in correctRules:
                        # Adds the event to the list with a sleek format.
                        availableEvents.append(element['title'] + ",\nPåmelding: "
                                               + element['attendance_event']['registration_start']+"\n")
    # If the metadata contains a next page, update url to this and run again.
    if(apiMenu['next']):
        url = apiMenu['next']
        bedpressFinderApi()

    return availableEvents

# Runs the script first time
# bedpressFinderApi()

# print(availableEvents[1])

# Writes to output variable

# for item in availableEvents:
#     print("\n"+item)
# f.close()
