
from pathlib import Path


points = 0


SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")

with open(INPUT_FILE, 'r') as f:
    data = f.readlines()
    for i in range(0, len(data)):
        data[i] = data[i].replace('\n', '').strip()
        
    for i in range(len(data)):
        set = data[i].split(',')
        
        first_range = set[0].split('-')
        second_range = set[1].split('-')
        
        first_min = int(first_range[0])
        first_max = int(first_range[1])
        
        second_min = int(second_range[0])
        second_max = int(second_range[1])
        
        if (first_min <= second_min and second_max <= first_max) or (second_min <= first_min and first_max <= second_max) :
            points += 1

        
        
        
print(points)