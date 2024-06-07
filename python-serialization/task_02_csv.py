import csv
import json

def convert_csv_to_json(csv_filename):
    try:
        # Read the CSV file
        with open(csv_filename, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]
        
        # Write the JSON file
        with open('data.json', mode='w') as json_file:
            json.dump(data, json_file, indent=4)
        
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

# Save this code in a file named task_02_csv.py
