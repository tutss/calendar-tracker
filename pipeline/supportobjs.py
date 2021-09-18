import dateutil.parser as dup
from datetime import timedelta

class Event:
    def __init__(self, event: dict) -> None:
        self.start_time = event['start'].get('dateTime', event['start'].get('date'))
        self.end_time = event['end'].get('dateTime', event['start'].get('date'))
        self.summary = event['summary']
        self.id = event['id']
        self.calculate_event_time()

    def calculate_event_time(self):
        event_duration = dup.isoparse(self.end_time) - dup.isoparse(self.start_time)
        if event_duration.seconds > 0:
            self.duration = timedelta_to_hours(event_duration)
        else:
            self.duration = -1

def timedelta_to_hours(td):
    return td / timedelta(hours=1)