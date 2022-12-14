from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")


move_dict = {
    "A": {"X": "scissors", "Y": "rock", "Z": "paper"}, 
    "B": {"X": "rock", "Y": "paper", "Z": "scissors"}, 
    "C": {"X": "paper", "Y": "scissors", "Z": "rock"}
    }

points_set = {
    "X": 0, # lose
    "Y": 3, # tie
    "Z": 6  # win
    }

points_list = {
    "rock": 1, 
    "paper": 2, 
    "scissors": 3
    }

points = 0

with open(INPUT_FILE, 'r') as f:
    data = f.readlines()
    
    for set in data:
        set = set.replace('\n', '').split(' ')
        
        points += points_set[set[1]]
        points += points_list[move_dict[set[0]][set[1]]]
        
        
print(points)
        
