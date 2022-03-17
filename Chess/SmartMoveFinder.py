import random

pieceScore = {'K':100,'Q':9,'R':5,'B':3.2,'N':3,'p':1,'-':0}

knightScores = [[-1,1,1,1,1,1,1,-1],
               [1,2,2,2,2,2,2,1],
               [1,2,4,3,3,4,1,1],
               [1,2,3,4,4,3,1,1],
               [1,2,3,4,4,3,1,1],
               [1,2,4,3,3,4,1,1],
               [1,2,2,2,2,2,2,1],
               [-1,1,1,1,1,1,1,-1]]

bishopScores = [[4,3,2,1,1,2,3,4],
               [3,5,2,2,2,3,5,3],
               [2,3,4,3,3,4,3,2],
               [1,2,3,4,4,3,2,1],
               [1,2,3,4,4,3,2,1],
               [2,3,4,3,3,4,3,2],
               [3,5,3,2,2,3,5,3],
               [4,3,2,1,1,2,3,4]]

queenScores = [[1,1,1,3,1,1,1,1],
               [1,2,2,2,2,2,1,1],
               [1,2.5,2.5,2.5,2.5,2.5,2,1],
               [1,2.5,2.5,2.5,2.5,2.5,2,1],
               [1,2.5,2.5,2.5,2.5,2.5,2,1],
               [1,2.5,2.5,2.5,2.5,2.5,2,1],
               [1,2,2,2,2,1,1,1],
               [1,1,1,3,1,1,1,1]]

rookScores = [ [4,3,4,5,4,5,3,4],
               [4,4,4,4,4,4,4,4],
               [1,1,2,3,3,2,1,1],
               [1,2,3,4,4,3,2,1],
               [1,2,3,4,4,3,2,1],
               [1,1,2,3,3,2,1,1],
               [4,4,4,4,4,4,4,4],
               [4,3,4,5,4,5,3,4]]

whitePawnScores = [ [10,10,10,10,10,10,10,10],
                    [8,8,8,8,8,8,8,8],
                    [5,6,6,7,7,6,6,5],
                    [2,3,4,5,5,4,3,2],
                    [1,1,1.5,5,5,1.5,1,1],
                    [1,1,2,2,2,2,1,1],
                    [1,1,1,0,0,1,1,1],
                    [0,0,0,0,0,0,0,0]]

blackPawnScores = [ [0,0,0,0,0,0,0,0],
                    [1,1,1,0,0,1,1,1],
                    [1,1,2,2,2,2,1,1],
                    [1,1,1.5,5,5,1.5,1,1],
                    [2,3,4,5,5,4,3,2],
                    [5,6,6,7,7,6,6,5],
                    [8,8,8,8,8,8,8,8],
                    [10,10,10,10,10,10,10,10]]

whiteKingScores = [ [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 5, 0, 0, 0, 5, 0]]

blackKingScores =[ [0,0,5,0,0,0,5,0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0,0,0,0,0,0,0,0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0],
                    [0,0,0,0,0,0,0,0]]

kingScoresEndgame = [  [-1, -1, -1, -1, -1, -1, -1, -1],
                            [-1, 0, 0, 0, 0, 0, 0, -1],
                            [-1, 0, 3, 3, 3, 3, 0, -1],
                            [-1, 0, 3, 4, 4, 3, 0, -1],
                            [-1, 0, 3, 4, 4, 3, 0, -1],
                            [-1, 0, 3, 3, 3, 3, 0, -1],
                            [-1, 0, 0, 0, 0, 0, 0, -1],
                            [-1, -1, -1, -1, -1, -1, -1, -1]]

piecePositionScores = {'N':knightScores,'Q':queenScores,'B':bishopScores,'R':rookScores,'bp':blackPawnScores,'wp':whitePawnScores,'wK':whiteKingScores,'bK':blackKingScores,'K':kingScoresEndgame}
# isInEndgame = False
CHECKMATE = 1000
STALEMATE = 0
DEPTH = 3

'''picks and returns random move'''
def findRandomMove(validMoves):
    return random.choice(validMoves)



'''positive score good for white, negative good for black'''
def scoreBoard(gs):
    if gs.checkmate:
        if gs.whiteToMove:
            return -CHECKMATE #black wins
        else:
            return CHECKMATE # white wins
    elif gs.stalemate:
        return STALEMATE

    score = 0
    for row in range(len(gs.board)):
        for col in range(len(gs.board[row])):
            square = gs.board[row][col]
            if square != '--':
                #score it positionally
                piecePositionScore = 0
                if square[1] == 'p' or square[1] == 'K':  # pawns or kings
                    if isEndgame(gs.board) and square[1] == 'K':
                        piecePositionScore = piecePositionScores[square[1]][row][col]
                    else:
                        piecePositionScore = piecePositionScores[square][row][col]
                else:  # other pieces
                    piecePositionScore = piecePositionScores[square[1]][row][col]
                if square[0] == 'w':
                    score += pieceScore[square[1]] + piecePositionScore * 0.1
                elif square[0] == 'b':
                    score -= pieceScore[square[1]] + piecePositionScore * 0.1

    return score

def findBestMove(gs,validMoves,depth):
    global nextMove,counter
    nextMove = None
    random.shuffle(validMoves)
    bestGuesses= orderMoves(gs, validMoves)
    counter = 0
    findMoveMinMaxAlphaBeta(gs, bestGuesses, depth, -CHECKMATE, CHECKMATE, 1 if gs.whiteToMove else -1)
    print(counter)
    return nextMove


def findMoveMinMaxAlphaBeta(gs, allValidMoves, depth, alpha, beta, turnMultiplier):
    global nextMove,counter
    counter +=1
    if depth == 0:
        return turnMultiplier * scoreBoard(gs)

    maxScore = -CHECKMATE
    for move in allValidMoves:
        gs.makeMove(move)
        nextMoves = gs.getValidMoves()
        random.shuffle(nextMoves)
        score = -findMoveMinMaxAlphaBeta(gs,orderMoves(gs,nextMoves),depth-1,-beta,-alpha,-turnMultiplier)
        if score > maxScore:
            maxScore = score
            if depth == DEPTH:
                nextMove = move
                print(move,score)
        gs.undoMove()
        if maxScore > alpha: #pruning
            alpha = maxScore
        if alpha >= beta:
            break
    return maxScore

def orderMoves(gs,validMoves):
    bestGuessedMoves = []
    bestScore = 0
    for move in validMoves:
        moveScoreGuess = 0
        movePieceScore = pieceScore[move.pieceMoved[1]]
        capturePieceScore = pieceScore[move.pieceCaptured[1]]
        if move.isCapture:
            moveScoreGuess = 10 * (capturePieceScore - movePieceScore) + 1
        if move.isPawnPromotion:
            moveScoreGuess += pieceScore['Q']
       # if gs.squareUnderAttack(move.endRow,move.endCol):
       #     moveScoreGuess -= movePieceScore

        if(moveScoreGuess > bestScore):
            bestScore = moveScoreGuess
            bestGuessedMoves = [move] + bestGuessedMoves
        else:
            bestGuessedMoves.append(move)
    return bestGuessedMoves

def isEndgame(board):
    whiteScore = 0
    blackScore = 0

    for row in board:
        for square in row:
            if square[0] == 'w':
                whiteScore += pieceScore[square[1]]
            if square[0] == 'b':
                blackScore += pieceScore[square[1]]
    if whiteScore < 11 or blackScore < 11:
        return True
    else:
        return False
