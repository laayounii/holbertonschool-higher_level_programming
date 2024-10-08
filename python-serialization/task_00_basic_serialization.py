#!/usr/bin/python3

import json

def serialize_and_save_to_file(data, filename):
    """
    Serialize the provided data (Python dictionary) to a JSON file.
    
    Parameters:
        data (dict): The dictionary to serialize and save.
        filename (str): The filename of the output JSON file.
    """
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)

def load_and_deserialize(filename):
    """
    Load and deserialize the data from the given JSON file.
    
    Parameters:
        filename (str): The filename of the input JSON file.
        
    Returns:
        dict: The deserialized data from the file.
    """
    with open(filename, 'r') as json_file:
        return json.load(json_file)
