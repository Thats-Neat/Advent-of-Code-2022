
with open('C:/Users/johnl/Desktop/Advent of Code/day 1/puzzle_input.txt', 'r') as f:
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
        

                
