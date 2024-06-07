import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    try:
        # Create the root element
        root = ET.Element("data")
        
        # Iterate through the dictionary and add items as child elements
        for key, value in dictionary.items():
            child = ET.Element(key)
            child.text = str(value)
            root.append(child)
        
        # Create an ElementTree and write to file
        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)
        return True
    except Exception as e:
        print(f"Serialization error: {e}")
        return False

def deserialize_from_xml(filename):
    try:
        # Parse the XML file
        tree = ET.parse(filename)
        root = tree.getroot()
        
        # Reconstruct the dictionary from XML elements
        dictionary = {}
        for child in root:
            dictionary[child.tag] = child.text
        
        return dictionary
    except Exception as e:
        print(f"Deserialization error: {e}")
        return None

# Save this code in a file named task_03_xml.py
