from processor import build_service
from extractor import extract_events
from loader import save_events_to_csv

def main():
    service = build_service()
    events = extract_events(service)
    csv_filename = save_events_to_csv(events)

    print('####### This week events are #######')
    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])

main()