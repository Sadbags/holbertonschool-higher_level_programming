#!/usr/bin/python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """ Serialize a python dictionary int XML and save it to a file """

    try:
        root = ET.Element("data")
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename)
        return True

    except:
        print(f"An error has ocurred during serialization")
        return False


def deserialize_from_xml(filename):
    """ read XML data from a file and return a deserialized python dictionary """

    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        dictionary = {child.tag: child.text for child in root}

        return dictionary

    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return None

    except Exception:
        print(f"An error ocurred during deserialization:")
        return None


if __name__ == "__main__":
    sample_dict = {
        "name": "John Doe",
        "age": "30",
        "city": "New York"
    }

    xml_file = "data.xml"
    if serialize_to_xml(sample_dict, xml_file):
        print(f"Dictionary serialized to {xml_file}")

        deserialized_data = deserialize_from_xml(xml_file)
        print("\nDeserialized Data:")
        print(deserialized_data)
    else:
        print(f"Failed to serialize the dictionary to {xml_file}")
