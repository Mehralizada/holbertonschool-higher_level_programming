import os

def generate_invitations(template, attendees):
    # Check input types
    if not isinstance(template, str):
        print("Error: Template should be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return

    # Check if template or attendees list is empty
    if not template.strip():
        print("Error: Template is empty, no output files generated.")
        return
    if not attendees:
        print("Error: No data provided, no output files generated.")
        return

    # Process each attendee
    for i, attendee in enumerate(attendees, start=1):
        try:
            # Replace placeholders with attendee data
            output_content = template
            for placeholder in ["name", "event_title", "event_date", "event_location"]:
                value = attendee.get(placeholder, "N/A")
                if value is None:
                    value = "N/A"
                output_content = output_content.replace(f"{{{placeholder}}}", str(value))

            # Write to output file
            output_filename = f"output_{i}.txt"
            if os.path.exists(output_filename):
                print(f"Error: File {output_filename} already exists.")
                continue

            with open(output_filename, 'w') as output_file:
                output_file.write(output_content)
            print(f"Generated: {output_filename}")
        
        except Exception as e:
            print(f"Error generating file for attendee {i}: {e}")

# Read the template from a file
try:
    with open('template.txt', 'r') as file:
        template_content = file.read()
except FileNotFoundError:
    print("Error: The template file 'template.txt' was not found.")
    template_content = ""

# List of attendees
attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]

# Call the function with the template and attendees list
generate_invitations(template_content, attendees)

