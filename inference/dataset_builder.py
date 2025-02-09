import os
import csv
import re

data_folder = './dataset' 
output_csv = 'urgency_data.csv'  

data = []

# Iterate through all files in the data folder
for filename in os.listdir(data_folder):
    if filename.endswith('.txt'):
        file_path = os.path.join(data_folder, filename)
        print(f"Processing file: {file_path}")
        
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

            # Use regex to find the conversation and label pairs
            entries = re.findall(r'\{(.*?)\}', content, re.DOTALL)
            
            for entry in entries:
                conversation_match = re.search(r'"conversation":\s*\(\s*"(.+?)"\s*\)', entry, re.DOTALL)
                label_match = re.search(r'"label":\s*"([^"]*)"', entry)

                if conversation_match and label_match:
                    # Clean up the conversation text
                    conversation = conversation_match.group(1)
                    # Replace all newlines inside the conversation with a space and trim extra spaces
                    conversation = re.sub(r'\s*\n\s*', ' ', conversation).strip()  
                    conversation = conversation.replace('’', "'")  # Normalize quotes
                    conversation = conversation.replace('"', '')  # Remove double quotes
                    conversation = conversation.replace('\n', ' ').strip()
                    conversation = re.sub(r'[\r\n\t\f\v]+', ' ', conversation).strip()
                    conversation = conversation.replace('\n', ' ').replace('\r', ' ').strip()
                    label = label_match.group(1).strip()

                    # Append cleaned conversation and label to the data list
                    data.append([conversation, label])

# Write the cleaned data to a CSV file
with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['conversation', 'label'])  # Write header
    writer.writerows(data)  # Write the conversation data

print(f"Data has been written to {output_csv}")
