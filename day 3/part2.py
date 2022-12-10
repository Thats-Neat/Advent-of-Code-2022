
points = 0

with open('day 3/input.txt', 'r') as f:
    data = f.readlines()
    for i in range(0, len(data)):
        data[i] = data[i].replace('\n', '').strip()
        
    for i in range(0, len(data), 3):
        set = data[i:i+3]
        
        for i in range(len(set[0])):
            if set[0][i] in set[1] and set[0][i] in set[2]:
                ascii_letter = ord(set[0][i])
                if set[0][i].islower():
                    points += (ascii_letter-96)
                    break
                else:
                    points += (ascii_letter-38)
                    break
        
        
print(points)
        