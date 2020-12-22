import random

def playarea(area):
    [print(*area[x]) for x in range(5)]

def get_input():
    print("____________Tic Tac Toe______________\n\n")
    print("Choose X or O: ")
    global player,computer
    player=input()
    computer='X'
    if player=='X': computer='O'

def players_turn():
    print('\nYour turn: ')
    try:
        pos=input()
        x_pos=[x for x in (0,2,4) if pos in area[x]][0]
        y_pos=[y for y in (0,2,4) if pos==area[x_pos][y]][0]
        area[x_pos][y_pos]=player
    except:
        print('Enter a valid position')
        return players_turn()
    playarea(area)

def computers_turn():
    print("\nComputers' turn: ")
    while True:
        x_pos=random.choice((0,2,4))
        y_pos=random.choice((0,2,4))
        if area[x_pos][y_pos]!=player and area[x_pos][y_pos]!=computer:break
    area[x_pos][y_pos]=computer
    playarea(area)
    
def gameover():
    possibilities=[]
    possibilities.append([area[0][x] for x in (0,2,4)])
    possibilities.append([area[2][x] for x in (0,2,4)])
    possibilities.append([area[4][x] for x in (0,2,4)])
    possibilities.append([area[x][0] for x in (0,2,4)])
    possibilities.append([area[x][2] for x in (0,2,4)])
    possibilities.append([area[x][4] for x in (0,2,4)])
    possibilities.append([area[x][y] for (x,y) in zip((0,2,4),(0,2,4))])
    possibilities.append([area[x][y] for (x,y) in zip((0,2,4),(4,2,0))])
    if any(len(set(possibilities[x]))==1 for x in range(8)):
        winner=[possibilities[x][0]  for x in range(8) if len(set(possibilities[x]))==1] 
        if winner[0]==player:
            print('You Win')
        else:
            print('You Lost')
        return True
    elif all((possibilities[x][y]=='X' or possibilities[x][y]=='O') for x in range(8) for y in range(3)):
        print("Game is draw")
        return True
    else:
        return False

           
area = [['1','|','2','|','3'],['-',' ','-',' ','-'],['4','|','5','|','6'],['-',' ','-',' ','-'],['7','|','8','|','9']]
get_input()
playarea(area)
while not gameover():
    players_turn()
    if not gameover():
        computers_turn()
    else: break