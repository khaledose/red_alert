import xml.etree.ElementTree as ET
import json

# Parse the XML file
tree = ET.parse('./test.CT')
root = tree.getroot()

# Initialize a list to store the extracted data
data = {}

# Loop through each CheatEntry
for entry in root.findall('./CheatEntries/CheatEntry'):        
    # Extract the Description, Address and Offsets
    try:
        description = entry.find('Description').text.strip('"')
    
        script = entry.find('AssemblerScript').text
    
        # Create a dictionary with the extracted data
        data[description] = {
                    'Script': script
                }
    except:
        continue

# Write the extracted data to a JSON file
with open('scripts.json', 'w') as f:
    json.dump(data, f, indent=4)