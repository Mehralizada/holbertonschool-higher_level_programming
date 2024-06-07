import json

def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.

    :param data: A Python Dictionary with data
    :param filename: The filename of the output JSON file
    """
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """
    Load and deserialize data from a JSON file.

    :param filename: The filename of the input JSON file
    :return: A Python Dictionary with the deserialized JSON data
    """
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

if __name__ == "__main__":
    # Sample data to be serialized
    data_to_serialize = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }

    # Serialize the data to JSON and save it to a file
    serialize_and_save_to_file(data_to_serialize, 'data.json')
    print("Data serialized and saved to 'data.json'.")

    # Load and deserialize data from 'data.json'
    deserialized_data = load_and_deserialize('data.json')
    print("Deserialized Data:")
    print(deserialized_data)
