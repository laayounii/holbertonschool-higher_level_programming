#!/usr/bin/python3
import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print out the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance of CustomObject and save it to the provided filename.
        
        Parameters:
            filename (str): The filename where the object will be serialized.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Error while serializing object: {e}")

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize and return an instance of CustomObject from the provided filename.
        
        Parameters:
            filename (str): The filename from which the object will be deserialized.
            
        Returns:
            CustomObject: The deserialized instance of CustomObject or None if an error occurs.
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.UnpicklingError) as e:
            print(f"Error while deserializing object: {e}")
            return None
