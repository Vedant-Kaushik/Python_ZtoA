x = ['','','','','','','','','']  # Your moves (empty: '', marked: 'X')
y = ['','','','','','','','','']  # Computer moves (empty: '', marked: 'O')

print(f'    6 |     7 |     8')
print('------+------+-------')
print(f'    3 |     4 |     5')
print('------+------+-------')
print(f'    0 |     1 |     2')
def board():
    print(f' {x[6] or y[6] or " "}    | {x[7] or y[7] or " "}    | {x[8] or y[8] or " "} ')
    print('------+------+-------')
    print(f' {x[3] or y[3] or " "}    | {x[4] or y[4] or " "}    | {x[5] or y[5] or " "} ')
    print('------+------+-------')
    print(f' {x[0] or y[0] or " "}    | {x[1] or y[1] or " "}    | {x[2] or y[2] or " "} ')

def win():
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [2, 4, 6], [0, 4, 8]
    ]
    for win in wins:
        if all(x[pos] == 'X' for pos in win):   # hardest part logic still learing 
            print('Player won')                 # to do better and create it on my own
            return True                         # used GPT in this part
        if all(y[pos] == 'O' for pos in win):
            print('Computer won')
            return False
    return None

def main():
    import random

    turn = 1  # 1 for your turn, 0 for computer's turn
    available_positions = [i for i in range(9)]  # All positions initially available

    while True:
        board()  # Print the board
        # Your turn
        if turn == 1:
            print('Your turn (X):')
            while True:
                user_choice = int(input('Enter a position (0-8): '))
                if 0 <= user_choice <= 8 and user_choice in available_positions:
                    x[user_choice] = 'X'                   
                    available_positions.remove(user_choice)
                    turn = 0
                    break
                else:
                    print('Invalid position or already occupied. Try again.')
        else:
            # Computer's turn
            print('Computer\'s turn (O):')
            comp_choice = random.choice(available_positions)
            y[comp_choice] = 'O'            
            available_positions.remove(comp_choice)
            turn = 1

        result = win()  # Call the win function

        # Check for winner and end game if necessary
        if result is not None:
            board()  # Print the final board
            if result==True:
                print("You won!")
            else:
                print("Computer won!")
            break  # Exit the loop after win

        if not available_positions:
            board()  # Print the final board
            print('Game over: It\'s a tie!')
            break

main()

