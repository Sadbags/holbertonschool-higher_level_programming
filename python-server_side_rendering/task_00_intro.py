import os


def generate_invitations(template, attendees):
    # checks if template is a string
    if not isinstance(template, str):
        print("Error: template is not a string")
        return

    # checks is attendees is a list of dictionaries
    if not isinstance(attendees, list) or not all (isinstance(attendees, dict) for attendee in attendees):
        print("Error: Attendees is not a list of dictionaries")
        return

    # checks is template is empty
    if not template:
        print("Error: Template is empty, no output files generated")
        return

    #checks if attendees is empty
    if not attendees:
        print("No data provided, no output files generated")
        return

    for index, attendee in enumerate(attendees, start=1):
        output = template
        for placeholder in ["name", "event_date", "event_location"]:
            output = output.replace(f"{{{{ {placeholder} }}}}", attendee.get(placeholder, "N/A"))

        filename = f"output_{index}.txt"
        with open(filename, 'w') as file:
            file.write(output)
        print(f"Generated {filename}")


template = """
Dear {{ name}},

You are invited to the {event_title}
Date: {event_date}
Location: {event_location}

We look forward to your presence.

Best regards,
Event Team

"""

attendees = [
	{"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]

generate_invitations(template, attendees)