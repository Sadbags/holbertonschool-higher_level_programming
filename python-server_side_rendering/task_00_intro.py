import os

def generate_invitations(template, attendees):
    # Check if template is a string
    if not isinstance(template, str):
        print("Error: Template is not a string.")
        return

    # Check if attendees is a list
    if not isinstance(attendees, list):
        print(f"Error: Attendees is not a list. Type provided: {type(attendees)}")
        return

    # Check if each item in attendees list is a dictionary
    if not all(isinstance(attendee, dict) for attendee in attendees):
        print(f"Error: Each attendee should be a dictionary. Invalid items: {[type(attendee) for attendee in attendees if not isinstance(attendee, dict)]}")
        return

    # Check if template is empty
    if not template:
        print("Error: Template is empty, no output files generated.")
        return

    # Check if attendees list is empty
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee and generate output files
    for index, attendee in enumerate(attendees, start=1):
        output = template
        for placeholder in ["name", "event_title", "event_date", "event_location"]:
            output = output.replace(f"{{{{ {placeholder} }}}}", attendee.get(placeholder, "N/A"))

        # Write to output file
        filename = f"output_{index}.txt"
        with open(filename, 'w') as file:
            file.write(output)
        print(f"Generated {filename}")

# Example template
template = """
Dear {{ name }},

You are cordially invited to the {{ event_title }}.
Date: {{ event_date }}
Location: {{ event_location }}

We look forward to seeing you there!

Best regards,
Event Organizer
"""

# Example attendees data
attendees = [
    {"name": "Alice", "event_title": "Annual Gala", "event_date": "2024-07-15", "event_location": "Grand Ballroom"},
    {"name": "Bob", "event_title": "Annual Gala", "event_date": "2024-07-15"},  # Missing event_location
    {"name": "Charlie", "event_title": "Annual Gala", "event_location": "Grand Ballroom"},  # Missing event_date
]

# Generate invitations
generate_invitations(template, attendees)
