#!/usr/bin/python3

import os

def generate_invitations(template, attendees):
    # Check if the template is a string
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    
    # Check if attendees is a list of dictionaries
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return
    
    # Handle empty template
    if not template.strip():
        print("Error: Template is empty, no output files generated.")
        return
    
    # Handle empty attendees list
    if not attendees:
        print("Error: No data provided, no output files generated.")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        output_content = template
        for placeholder in ["name", "event_title", "event_date", "event_location"]:
            value = attendee.get(placeholder, "N/A")
            output_content = output_content.replace(f"{{{placeholder}}}", str(value))
        
        # Generate output file name
        output_filename = f"output_{index}.txt"
        
        # Write to the output file
        try:
            with open(output_filename, "w") as file:
                file.write(output_content)
            print(f"Generated: {output_filename}")
        except Exception as e:
            print(f"Error writing to file {output_filename}: {e}")
