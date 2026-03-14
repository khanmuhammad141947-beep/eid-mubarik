
import os
import json

def save_data(data):
    file_path = os.path.join(os.path.dirname(__file__), 'data.txt')
    with open(file_path, 'a') as f:
        json.dump(data, f)
        f.write('\n')

def get_data():
    file_path = os.path.join(os.path.dirname(__file__), 'data.txt')
    data = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        data.append(json.loads(line))
                    except json.JSONDecodeError:
                        # Fallback for old str format
                        data.append(eval(line))
    return data