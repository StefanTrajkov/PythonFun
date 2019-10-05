def instructions():
    """Display game instructions"""
    print"""
        Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.
        This will be a showdown between your human brain and my silicon proces
        sor.
        You will make your move known by entering a number, 1 - 9. The number
        will correspond to the board position as illustrated:
        \t\t0 | 1 | 2
        \t\t----------
        \t\t3 | 4 | 5
        \t\t-----------
        \t\t6y | 7 | 8
        Prepare yourself, human. The ultimate battle is about to begin. \n
        """

def ask_yes_no(question):
    response = None
    while response not in ("y","n"):
        response = raw_input(question).lower()
    return response

def ask_number(question, low, high):
    response = None
    while response not in (low,high):
        response = int(raw_input(question))
    return response

def pieces():
    """Determines if computer or human goes first"""
    go_first = ask_yes_no("Do you want to make the first move (y/n): ")
    if go_first == "y":
        human = X
        computer = O
        print("Computer is " + computer + ", Human is " + human)
    else:
        computer = X
        human = O
        print("Computer is " +  computer + ", Human is " + human)
    return computer, human

def new_board():
    """Creates an empty board"""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    """Displays the game board"""
    print "\n\t", board[0], "|", board[1], "|", board[2]
    print "\t", "------"
    print "\t", board[3], "|", board[4], "|", board[5]
    print "\t", "------"
    print "\t", board[6], "|", board[7], "|", board[8], "\n"

def legal_moves(board):
    """Create list of legal moves"""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def winner(board):
    ways_to_win = ((0,1,2),
                   (3,4,5),
                   (6,7,8),
                   (0,3,6),
                   (1,4,7),
                   (2,5,8),
                   (0,4,8),
                   (2, 4, 6))

    for row in ways_to_win:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    if EMPTY not in board:
        return  TIE
    return None

def human_move(board, human):
        """Gets the human move"""
        legal = legal_moves(board)
        move = None
        while move not in legal:
            move = ask_number("Where will you move? (0-8):", 0, NUM_SQUARES)
            if move not in legal:
                print("That square is already occupied! Choose another.")
        print("Okay")
        return move

def computer_move(board, computer, human):
    """Make computer move"""
    board1 = board[:]
    best_moves = (4,0,2,6,8,1,3,5,7)
    for move in legal_moves(board1):
        board1[move] = computer
        if winner(board1) == computer:
            print move
            return move
        board1[move] = EMPTY
    for move in legal_moves(board1):
        board1[move] = human
        if winner(board1) == human:
            print(move)
            return move
        board1[move] = EMPTY

    for move in best_moves:
        if move in legal_moves(board1):
            print move
            return move

def next_turn(turn):
    """Switch turns"""
    if turn == X:
        return O
    else:
        return X

def congrat_winner(the_winner, computer, human):
    if the_winner != TIE:
        print the_winner, "won!\n"
    else:
        print "It's a tie"



#main
X = "X"
O = "O"
EMPTY = ""
TIE = "TIE"
NUM_SQUARES = 9


def main():
    instructions()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board,human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)
    new_game = ask_yes_no("Do you want a new game? y/n")
    if new_game == 'y':
        main()
    else:
        print  "\n\nPress enter to quit."
#Start
main()