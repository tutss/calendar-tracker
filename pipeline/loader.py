import pandas as pd
import datetime

from supportobjs import Event

CSV_FOLDER = '/home/tuts/repos/tutss/calendar-tracker/week_files/'

def events_to_df_format(events):
    start_time = [e.start_time for e in events]
    end_time = [e.end_time for e in events]
    summary = [e.summary for e in events]
    id = [e.id for e in events]
    duration = [e.duration for e in events]

    return {
        'start_time': start_time,
        'end_time': end_time,
        'summary': summary,
        'id': id,
        'duration': duration,
    }

def save_events_to_csv(events):
    now_datetime = datetime.datetime.utcnow()
    file_id = f"week_d{now_datetime.day}_m{now_datetime.month}.csv"
    filename = CSV_FOLDER + file_id

    event_list = list()
    for event in events:
        event_list.append(Event(event))
    
    events_dict = events_to_df_format(event_list)
    df = pd.DataFrame(events_dict)
    df.to_csv(filename, index=False)
    print(f'Saved events to {filename}!')

    return filename, file_id

def load_events(filename):
    df = pd.read_csv(filename)
    return df
    