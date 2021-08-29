from __future__ import print_function
import os.path
import json
import datetime

TIMEDELTA_IN_DAYS = 7
JSON_FOLDER = '/home/tuts/repos/tutss/calendar-tracker/json_files/'

def extract_events(service):
    now_datetime = datetime.datetime.utcnow()
    filename = JSON_FOLDER + f"week_d{now_datetime.day}_m{now_datetime.month}.json"

    if os.path.exists(filename):
        with open(filename) as json_file:
            events = json.load(json_file)
            return events
    
    # Call the Calendar API
    now = _convert_to_api_format(now_datetime) # 'Z' indicates UTC time
    one_week_from_now = _convert_to_api_format(now_datetime + datetime.timedelta(days=TIMEDELTA_IN_DAYS))

    print('Getting next week events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        timeMax=one_week_from_now, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    print('Saving events to json...')
    save_events_to_json(events, filename)
    print(f'Saved events to {filename}!')

    return events

def save_events_to_json(events, filename):
    with open(filename, "w") as outfile:
        json.dump(events, outfile)

def _convert_to_api_format(datetime_val):
    return datetime_val.isoformat() + 'Z'