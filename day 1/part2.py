
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")

with open(INPUT_FILE, 'r') as f:
    data = f.readlines()
    for i in range(0, len(data)):
        data[i] = data[i].replace('\n', '').strip()
    
    elf_list = []
    
    total = 0
    
    for i in range(len(data)):
        if data[i] != '':
            total += int(data[i])
        else:
            elf_list.append(total)
            total = 0
            
    elf_list.sort(reverse=True)
    
    print(sum(elf_list[:3]))
        

                
