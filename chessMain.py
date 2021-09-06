
# Main driver file. Handles user input and displayes GameState obj

import chessEngine, AI

def main():
    """Main driver, handles all inputs and updates"""
    gs = chessEngine.GameState()
    valid_moves = gs.getValidMoves()
    move_made = False # flag variable when a move is made
    running = True
    gameOver = False
    sqSelected = () # nothing selected, tracs last selection
    playerClicks = [] # keeps track of selection [2 tuples]
    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4,
        "5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3,
            "e": 4, "f": 5, "g": 6, "h": 7}
    colsToFiles = {v: k for k, v in filesToCols.items()}
    # game type
    if input("2 player match?(y/n): ") == "y":
        playerOne, playerTwo = True, False
    else:
        if input("Play as white?(y/n): ") == "y":
            playerOne = True
        else:
            playerOne = False
    playerTwo = not playerOne
    while running:
        humanTurn = (gs.white_to_move and playerOne) or (not gs.white_to_move and playerTwo)
        if not playerClicks:
            print(gs)
        # inputs
        if not gameOver and humanTurn:
            user = input("enter square: col,row: ").split(",")
            if user == ["undo"]:
                gs.undoMove()
                move_made = True
            elif user == ["quit"] or user == ["exit"]:
                running = False
            elif user != ["quit"] or user != ["exit"] or user != ["undo"]:
                user = (filesToCols[user[0]], ranksToRows[user[1]])
                col, row = user
                if sqSelected == (row, col): # user clicked same square twice
                    sqSelected = () # reset
                    playerClicks = [] # clear clicks
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected) # append both 1st and 2nd clicks
                    if len(playerClicks) == 2: # after 2nd move
                        move = chessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                        for i in range(len(valid_moves)):
                            if move == valid_moves[i]:
                                gs.makeMove(valid_moves[i])
                                sqSelected = () # reset user clicks
                                playerClicks = []
                                move_made = True
                        if not move_made:
                            pass # Reselect square

        # ai move
        if not gameOver and not humanTurn:
            aiMove = None
            aiMove = AI.findBestMove(gs, valid_moves)
            if aiMove == None:
                aiMove = AI.findRandomMove(valid_moves)
            gs.makeMove(aiMove)
            move_made = True
        
        if move_made:
            valid_moves = gs.getValidMoves()
            move_made = False
            


if __name__ == "__main__":
    main()
