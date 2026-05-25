def print_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print()

def check_winner(board, player):

    wins = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]

    for combo in wins:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False
    
def is_board_full(board):
    for spot in board:
        if spot not in ['X', 'O']:
            return False
    return True
    
def minimax(board, is_maximizing):

    #check terminal states
    if check_winner(board, 'O'):
        return 1
    if check_winner(board, 'X'):
        return -1
    if is_board_full(board):
        return 0
        

    if is_maximizing:
        best_score = -1000
        for i in range(9):
            if board[i] not in ['X', 'O']:
                board[i] = 'O'
                score = minimax(board, False)
                board[i] = str(i+1)
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = 1000
        for i in range(9):
            if board[i] not in ['X', 'O']:
                board[i] = 'X'
                score = minimax(board, True)
                board[i] = str(i+1)
                best_score = min(score, best_score)
        return best_score
        
def best_move(board):
    best_score = -1000
    move = 0
    for i in range(9):
        if board[i] not in ['X', 'O']:
            board[i] = 'O'
            score = minimax(board, False)
            board[i] = str(i + 1)
            if score > best_score:
                best_score = score
                move = i
    return move
        

def play_game():
    board = ['1','2','3','4','5','6','7','8','9']
        
    print("=" * 35)
    print("   Welcome to Tic Tac Toe AI! 🎮")
    print("=" * 35)
    print("  You are X  |  AI is O")
    print("  Enter position (1-9) to play")
    print("=" * 35)
        
    print_board(board)
    
    while True:
        # Human turn
        while True:
            try:
                move = int(input("Your move (1-9): ")) - 1
                if 0 <= move <= 8 and board[move] not in ['X','O']:
                    board[move] = 'X'
                    break
                else:
                    print("Invalid move! Try again.")
            except ValueError:
                print("Please enter a number 1-9!")
            
        print_board(board)
            
            # Check human wins
        if check_winner(board, 'X'):
            print("🎉 Congratulations! You won!")
            break
            
            # Check draw
        if is_board_full(board):
            print("🤝 It's a draw!")
            break
            
            # AI turn
        print("AI is thinking... 🤖")
        ai_move = best_move(board)
        board[ai_move] = 'O'
            
        print_board(board)
            
            # Check AI wins
        if check_winner(board, 'O'):
            print("🤖 AI wins! Better luck next time!")
            break
            
            # Check draw
        if is_board_full(board):
            print("🤝 It's a draw!")
            break

# Run the game
play_game()