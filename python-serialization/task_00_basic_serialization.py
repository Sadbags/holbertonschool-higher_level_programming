#!/usr/bin/python3
import json


def serialize_and_save_to_file(data, filename):
    """ Serialize a python dictionary to a JSON file """

    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """ Load and deserialize a JSON file to a python dictionary """

    with open(filename, 'r') as file:
        data = json.load(file)
    return data

if __name__ == "__main__":
    data_to_serialize = {
        "name": "John Doe",
        "age": "30",
        "city": "New York"
    }


    # Serialize the data to JSON and save it to a file
    serialize_and_save_to_file(data_to_serialize, 'data.json')

    # Output: The data has been serialized and saved to 'data.json'
    print("Data serialized and saved to 'data.json'.")

    # Load and deserialize data from 'data.json'
    deserialized_data = load_and_deserialize('data.json')

    # Output: The deserialized data
    print("Deserialized Data:")
    print(deserialized_data)
