#!/usr/bin/python3
import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file to a JSON file and write the data to 'data.json'.
    
    Parameters:
        csv_filename (str): The filename of the input CSV file.
        
    Returns:
        bool: True if conversion is successful, False otherwise.
    """
    try:
        data_list = []

        # Open the CSV file and read the data
        with open(csv_filename, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            # Convert each row into a dictionary and add it to the list
            for row in csv_reader:
                data_list.append(row)

        # Serialize the list of dictionaries to JSON and write it to 'data.json'
        with open('data.json', mode='w') as json_file:
            json.dump(data_list, json_file, indent=4)

        return True

    except FileNotFoundError:
        print(f"Error: File '{csv_filename}' not found.")
        return False

    except Exception as e:
        print(f"An error occurred: {e}")
        return False
