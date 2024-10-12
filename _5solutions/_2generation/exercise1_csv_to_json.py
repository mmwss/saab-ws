import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    data = []
    with open(csv_file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    with open(json_file_path, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)

# Example usage
if __name__ == '__main__':
    csv_file = 'data/data.csv'
    json_file = 'data/data.json'
    csv_to_json(csv_file, json_file)
    # print(f"Converted {csv_file} to {json_file}")
