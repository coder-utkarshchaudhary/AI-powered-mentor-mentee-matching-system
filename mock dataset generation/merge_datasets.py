import os
import json

directory = 'datasets'

merged_data = {}

"""
    All files have the same keys mentor_1 to mentor_10.
    Hence we keep a counter and then update merged_data.
"""

mentor_counter = 1

for filename in os.listdir(directory):
    if filename.endswith('.json'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r') as file:
            data = json.load(file)
            for mentor_id, mentor_info in data.items():
                new_mentor_id = f"mentor_{mentor_counter}"
                merged_data[new_mentor_id] = mentor_info
                mentor_counter += 1

output_file = 'datasets/merged_dataset.json'
with open(output_file, 'w') as outfile:
    json.dump(merged_data, outfile, indent=4)

print(f"All JSON files have been merged into {output_file}")