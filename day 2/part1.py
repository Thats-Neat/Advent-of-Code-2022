from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")



def main():
    
    opponent_win = {
        "A": "paper", 
        "B": "scissors", 
        "C": "rock"
        }
    
    opponent_play = {
        "A": "rock", 
        "B": "paper", 
        "C": "scissors"
        }
    
    my_play = {
        "X": "rock", 
        "Y": "paper", 
        "Z": "scissors"
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
            
            if my_play[set[1]] == opponent_win[set[0]]:
                points += 6 # win
            elif my_play[set[1]] == opponent_play[set[0]]:
                points += 3 # tie
            else:
                pass # lose
            

            points += points_list[my_play[set[1]]]
        
    print(points)
    



main()