import time
import random

# Global vars
board_dimension = 0
board = []

def main():
    welcome_message()
    
    # Welcome message retrieves board dimensions. Now update the board.
    for _ in range(board_dimension + 1):
        board.append([0] * board_dimension)
    display_board()
    # player x goes first, let x be True and player o be False.
    turn = True
    turn_num = 0
    while True:
        move = ""
        if turn_num >= 9:
            print("TIE! No player wins :o")
            break
        
        while True:
            board_move = 1 if turn else -1
            player = "x" if turn else "o"
            print(f"It is {player}'s turn.")
            move = input().lower().strip()
            if valid_move(move):
                input_move(move, board_move)
                display_board()
                turn_num += 1
                break
        if found_win(move):
            break
        turn = not turn
        print("#######################################################################")
    if turn_num < 9:
        winner = "x" if turn else "o"
        print(f"{winner} wins!")
    
        

def welcome_message():
    print("WELCOME TO TIC-TAC-TOE! >:D")
    time.sleep(1)
    x = random.uniform(1, 2.5)
    y = random.uniform(0.5, 1.5)
    z = random.uniform(0.75, 1.5)
    print("Loading...")
    # time.sleep(x)
    print("Loading.....")
    # time.sleep(y)
    print("Loading............")
    # time.sleep(z)
    while True:
        try: 
            dimensions = int(input("How many dimensions do you want?"))
            if(3 <= dimensions <= 26):
                break
            else:
                print("Please enter a number between 3 and 26.")
        except ValueError:
            print("Please enter in a number.")
    print("Pay attention to who's move it is. Then, enter a square to make a move.")
    time.sleep(2)
    print("Look at the numbers and letters to find valid moves. Write the letter first, then the number.")
    time.sleep(2)
    print("#######################################################################")
    board_dimension = dimensions
    
    
    
def valid_move(move):
    valid_inputs = [
        "a1", "a2", "a3",
        "b1", "b2", "b3",
        "c1", "c2", "c3"
    ]
    
    i, j = translate_move(move)
    if (move in valid_inputs) and board[i][j] == 0:
        return True
    return False


def input_move(move, player):
    i, j = translate_move(move)
    board[i][j] = player
    

def translate_move(move):
    # Player will enter moves like chess notation
    i, j = 0, 0
    match move:
        case "a3":
            i, j = 0, 0
        case "a2":
            i, j = 1, 0
        case "a1":
            i, j = 2,0
        case "b3":
            i, j = 0, 1
        case "b2":
            i, j = 1, 1
        case "b1":
            i, j = 2, 1
        case "c3":
            i, j = 0, 2
        case "c2":
            i, j = 1, 2
        case "c1":
            i, j = 2, 2
    return (i, j)    
        
    
def display_board():
    columns = ["3", "2", "1"]
    rows = "a   b   c"
    square_separater = " # "
    row_separater = "   #########"
    print("\n")
    for i in range(len(board)):
        print(columns[i], end="  ")
        for j in range(len(board[0])):
            if (board[i][j] == 0):
                print(" ", end="")
            elif (board[i][j] == 1):
                print("x", end="")
            else:
                print("o", end="")
            if (j != len(board[0]) - 1):
                print(square_separater, end="")
        if (i != len(board) - 1):
            print("\n" + row_separater)
    print("\n   " + rows + "\n")
    
    
def found_win(last_move):
    # diag1 is upperleft to lowerright
    def check_diags():
        if (
            board[0][0] + board[1][1] + board[2][2] == 3 or 
            board[0][0] + board[1][1] + board[2][2] == -3 or
            board[0][2] + board[1][1] + board[2][0] == 3 or
            board[0][2] + board[1][1] + board[2][0] == -3
        ):
            return True
        return False
        
    def check_row_and_col(i, j):
        row_sum = 0
        for x in range(0, -3, -1):
            row_sum += board[i][j + x]

        col_sum = 0
        for x in range(0, -3, -1):
            col_sum += board[i + x][j]
            
        if (
            row_sum == 3 or row_sum == -3 or
            col_sum == 3 or col_sum == -3
        ):
            return True
        return False

    i, j = translate_move(last_move)
    match (i, j):
        # middle square
        case ((1, 1) | (0, 0) | (0, 2) | (2, 0) | (2, 2)):
            if (
                check_diags() or
                check_row_and_col(i, j)
            ):
                return True
        case ((0, 1) | (1, 0) | (1, 2) | (2, 1)):
            if check_row_and_col(i, j):
                return True
    return False

if __name__ == "__main__":
    main()
