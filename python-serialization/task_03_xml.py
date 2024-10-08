#!/usr/bin/python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.
    
    Parameters:
        dictionary (dict): The dictionary to serialize.
        filename (str): The filename to save the serialized XML data.
    """
    # Create the root element
    root = ET.Element("data")
    
    # Iterate through the dictionary and create child elements
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)  # Ensure the value is a string

    # Create an ElementTree object and write it to the file
    tree = ET.ElementTree(root)
    try:
        tree.write(filename)
        return True
    except Exception as e:
        print(f"Error serializing to XML: {e}")
        return False

def deserialize_from_xml(filename):
    """
    Deserialize XML data from a file to a Python dictionary.
    
    Parameters:
        filename (str): The filename to read the XML data from.
        
    Returns:
        dict: A Python dictionary with the deserialized data.
    """
    try:
        # Parse the XML file
        tree = ET.parse(filename)
        root = tree.getroot()

        # Construct the dictionary from the XML elements
        result = {}
        for child in root:
            result[child.tag] = child.text  # Convert text back to the appropriate data type if needed

        return result

    except Exception as e:
        print(f"Error deserializing from XML: {e}")
        return None
