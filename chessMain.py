
# Main driver file. Handles user input and displayes GameState obj

import chessEngine

def main():
    """Main driver, handles all inputs and updates"""
    gs = chessEngine.GameState()
    validMoves = gs.getValidMoves()
    moveMade = False # flag variable when a move is made
    running = True
    sqSelected = () # nothing selected, tracs last selection
    playerClicks = [] # keeps track of selection [2 tuples]
    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4,
        "5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3,
            "e": 4, "f": 5, "g": 6, "h": 7}
    colsToFiles = {v: k for k, v in filesToCols.items()}
    while running:
        if not playerClicks:
            print(gs)
        user = input("enter square: col,row: ").split(",")
        if user == ["undo"]:
            gs.undoMove()
            moveMade = True
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
                    if move in validMoves:
                        gs.makeMove(move)
                        sqSelected = () # reset user clicks
                        playerClicks = []
                        moveMade = True
                    else:
                        pass # Reselect square
        if moveMade:
            validMoves = gs.getValidMoves()
            moveMade = False

if __name__ == "__main__":
    main()
