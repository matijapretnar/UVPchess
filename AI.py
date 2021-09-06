import random

pieceScore = {"K": 0, "Q": 9, "R": 5, "B": 3, "N": 3, "p": 1}
CHECKMATE = 1000
STALEMATE = 0

def findRandomMove(validMoves: list) -> tuple:
    return validMoves[random.randint(0, len(validMoves) - 1)]


def findBestMove(gs, validMoves: list) -> tuple:
    """Find the best material move"""
    turnMultiplier = 1 if gs.white_to_move else -1
    maxScore = - CHECKMATE
    bestMove = None
    for playerMove in validMoves:
        if gs.checkmate:
            score = CHECKMATE
        elif gs.stalemate:
            score = STALEMATE
        else:
            gs.makeMove(playerMove)
            score = turnMultiplier * scoreMaterial(gs.board)
        if (score > maxScore):
            maxScore = score
            bestMove = playerMove
        gs.undoMove()
    return bestMove

def scoreMaterial(board: list) -> int:
    """Scores the board based on material"""
    score = 0
    for row in board:
        for square in row:
            if square[0] == "w":
                score += pieceScore[square[1]]
            elif square[0] == "b":
                score -= pieceScore[square[1]]
    return score