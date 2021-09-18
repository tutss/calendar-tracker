import argparse

from processor import build_service
from extractor import extract_events
from loader import save_events_to_csv
from visualizer import CalendarDataframe

def main():

    # TODO: add parameters and use them
    parser = argparse.ArgumentParser(description='Calendar Tracker application')
    parser.add_argument('--send-report', dest='report', action='store_const',
                    const=True, help='Send email to configured email')
    
    parser.add_argument('--generate-visuals', dest='visual', action='store_const',
                    const=True, help='Generate the visuals for Calendar')

    args = parser.parse_args()

    service = build_service()
    events = extract_events(service)
    csv_filename, file_id = save_events_to_csv(events)
    calendar = CalendarDataframe(csv_filename, img_file=file_id)

    calendar.analysis()

    print('####### This week events are #######')
    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])

main()