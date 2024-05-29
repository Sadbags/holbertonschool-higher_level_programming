#!/usr/bin/python3
import csv
import json


def convert_csv_to_json(csv_filename):
    """ convert a CSV file to a JSON file """

    try:
        with open(csv_filename, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]

        with open('data.json', mode='w') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        print(f"Error: The file {csv_filename} was not found.")
        return False

    except:
        print(f"An error has ocurred")
        return False


if __name__ == "__main__":
    csv_file = "data.csv"
    if convert_csv_to_json(csv_file):
        print(f"Data from {csv_file} has been converted to data.json")
    else:
        print(f"An error ocurred while converting {csv_file} to JSON")
