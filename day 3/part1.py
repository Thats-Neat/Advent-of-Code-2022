
from pathlib import Path

points = 0

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")

with open(INPUT_FILE, 'r') as f:
    data = f.readlines()
    for i in range(0, len(data)):
        data[i] = data[i].replace('\n', '').strip()
        
        
    for i in range(0, len(data)):
        first_set = data[i][:int(len(data[i])/2)]
        second_set = data[i][int(len(data[i])/2):]
        
        for i in range(0, len(first_set)):
            if first_set[i] in second_set:
                ascii_letter = ord(first_set[i])
                if first_set[i].islower():
                    points += (ascii_letter-96)
                    break
                else:
                    points += (ascii_letter-38)
                    break


                
print(points)