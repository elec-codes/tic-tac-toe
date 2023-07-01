###this program is a tic-tac-toe game for 2 players ###

import random

#board base array
board_array= [[" " for row in range(0,3)] for elem in range(0,3)]

#base variables
board= (f"""+-------+-------+-------+
|1      |2      |3      |
|   {board_array[0][0]}   |   {board_array[0][1]}   |   {board_array[0][2]}   |
|       |       |       |
+-------+-------+-------+
|4      |5      |6      |
|   {board_array[1][0]}   |   {board_array[1][1]}   |   {board_array[1][2]}   |
|       |       |       |
+-------+-------+-------+
|7      |8      |9      |
|   {board_array[2][0]}   |   {board_array[2][1]}   |   {board_array[2][2]}   |
|       |       |       |
+-------+-------+-------+""")  

occupied_spots=[]
user1_spots=[]
user2_spots=[]

global who_wins
who_wins = ""

#user enters the move
def enter_move_user1():
    global user1_move
    print(player1, "'s turn.", end=" " )
    user1_move = int(input("Enter your move: "))
    if user1_move in occupied_spots:
        print("Input another move.")
        enter_move_user1()
    else:
        occupied_spots.append(user1_move)
        user1_spots.append(user1_move)

#computer enter the move
def enter_move_user2() :
    global user2_move
    print(player2, "'s turn.", end=" " )
    user2_move = int(input("Enter your move: "))
    if user2_move in occupied_spots:
        print("Input another move.")
        enter_move_user2()
    else:
        occupied_spots.append(user2_move)
        user2_spots.append(user2_move)
#update the board every time someone enter a new move
def update_board(board):
    winner()
    for item in occupied_spots:

        #find the right line
        if item in range(1,4): #number 1 to 3
            row = 0 #first line
            int(row)
        elif item in range(4, 7): #number 4 to 6
            row = 1 #second line
            int(row)
        elif item in range(7, 10):
            row = 2 #third line  
            int(row)       
        
        #find the right spot in the row
        if item in range(4, 7):
            new_item = item - 3 #position in the list/row
        elif item in range(7, 10):
            new_item = item - 6
        elif item in range(1, 4):
            new_item = item
        
        #draw the shape in the board
        if item in user2_spots and occupied_spots:
            board_array[row][new_item-1] = "X"
        elif item in user1_spots and occupied_spots:
            board_array[row][new_item-1] = "O"
    
    board= (f"""+-------+-------+-------+
|1      |2      |3      |
|   {board_array[0][0]}   |   {board_array[0][1]}   |   {board_array[0][2]}   |
|       |       |       |
+-------+-------+-------+
|4      |5      |6      |
|   {board_array[1][0]}   |   {board_array[1][1]}   |   {board_array[1][2]}   |
|       |       |       |
+-------+-------+-------+
|7      |8      |9      |
|   {board_array[2][0]}   |   {board_array[2][1]}   |   {board_array[2][2]}   |
|       |       |       |
+-------+-------+-------+""")  

    return board

#check if someone wins
def winner():
    global who_wins

    for row in board_array:
        if row == ["X", "X", "X"]:
            who_wins= "user2"
            program_on = False
        elif row == ["O", "O", "O"]:
            who_wins= "user1"
            program_on = False

    #columns
    column_1 =[board_array[0][0], board_array[1][0], board_array[2][0]]
    column_2 =[board_array[0][1], board_array[1][1], board_array[2][1]]
    column_3 =[board_array[0][2], board_array[1][2], board_array[2][2]]
    #diagonals
    diagonal_1 = [board_array[0][0], board_array[1][1], board_array[2][2]]
    diagonal_2 = [board_array[0][2], board_array[1][1], board_array[2][0]]
    
    user1_wins= ["O", "O", "O"]
    user2_wins= ["X", "X", "X"]
    
    if column_1 == user1_wins:
        who_wins= player1
        program_on = False
    elif column_2 == user1_wins:
        who_wins= player1
        program_on = False
    elif column_3 == user1_wins:
        who_wins= player1
        program_on = False
    elif diagonal_1 == user1_wins:
        who_wins= player1
        program_on = False
    elif diagonal_2 == user1_wins:
        who_wins= player1
        program_on = False
    #pc wins    
    elif column_1 == user2_wins:
        who_wins= player2
        program_on = False
    elif column_2 == user2_wins:
        who_wins= player2
        program_on = False
    elif column_3 == user2_wins:
        who_wins= player2
        program_on = False    
    elif diagonal_1 == user2_wins:
        who_wins= player2
        program_on = False
    elif diagonal_2 == user2_wins:
        who_wins= player2
        program_on = False
    elif sorted(occupied_spots)== [1,2,3,4,5,6,7,8,9]:
        print("it's a draw")
        who_wins = ""
        program_on = False
    else:
        program_on = True
    
    return program_on        
 
#MAIN PROGRAM
print(board)

player1 = input("Enter your name[O]: ")
player2 = input("Enter your name[X]: ")

while winner() == True:
    
    #user move
    enter_move_user1()
    #print move
    updated_board = update_board(board)
    print(updated_board)

    
    if winner() == False:
        break
    	
    enter_move_user2()
    #print move
    updated_board = update_board(board)
    print(updated_board)
    
    if winner() == False:
    	break
    	
    	
if who_wins == "":
    pass
else:
	print("The winner is: ",who_wins, "!")