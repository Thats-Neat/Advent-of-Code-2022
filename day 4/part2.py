
overlapped = 0
non_overlapped = 0

with open('day 4/input.txt', 'r') as f:
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
        
        
        if (first_min <= second_min and second_max <= first_max) or (second_min <= first_min and first_max <= second_max):
            overlapped += 1
        elif (first_min < second_min and first_max < second_min) or (second_min < first_min and second_max < first_min):
            non_overlapped += 1
            
            
print(len(data) - non_overlapped)
        

            
    


        
        
        
