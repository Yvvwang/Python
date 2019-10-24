import math

class BasePlayer:
    def __init__(self, maxDepth):
        self.maxDepth = maxDepth

    ##################
    #      TODO      #
    ##################
    # Assign integer scores to the three terminal states
    # P2_WIN_SCORE < TIE_SCORE < P1_WIN_SCORE
    # Access these with "self.TIE_SCORE", etc.
    P1_WIN_SCORE = 7800
    P2_WIN_SCORE = -7800
    TIE_SCORE = 0
    # Returns a heuristic for the board position
    # Good positions for 0 pieces should be positive and
    # good positions for 1 pieces should be negative
    # for all boards, P2_WIN_SCORE < heuristic(b) < P1_WIN_SCORE
    def myHeuristic(self, board):
        h_score = 0
        for i in range(board.WIDTH):
            for j in range(board.HEIGHT):
                try:
                    if board.board[i][j] == 0 and board.board[i+1][j] == 0:
                        h_score += 10
                    if board.board[i][j] == 0 and board.board[i+1][j] == 0 and board.board[i+2][j] == 0:
                        h_score += 100
                    if board.board[i][j] == 0 and board.board[i+2][j] == 0 and board.board[i+3][j] == 0:
                        h_score += 100
                    if board.board[i][j] == 0 and board.board[i+1][j] == 0 and board.board[i+3][j] == 0:
                        h_score += 100
                except IndexError:
                    pass
                try:
                    if board.board[i][j] == 1 and board.board[i+1][j] == 1:
                        h_score -= 10
                    if board.board[i][j] == 1 and board.board[i+1][j] == 1 and board.board[i+2][j] == 1:
                        h_score -= 100
                    if board.board[i][j] == 1 and board.board[i+2][j] == 1 and board.board[i+3][j] == 1:
                        h_score -= 100
                    if board.board[i][j] == 1 and board.board[i+1][j] == 1 and board.board[i+3][j] == 1:
                        h_score -= 100
                except IndexError:
                    pass
                try:
                    if board.board[i][j] == 0 and board.board[i][j+1] == 0:
                        h_score += 10
                    if board.board[i][j] == 0 and board.board[i][j+1] == 0 and board.board[i][j+2] == 0:
                        h_score += 100
                    if board.board[i][j] == 0 and board.board[i][j+1] == 0 and board.board[i][j+3] == 0:
                        h_score += 100
                    if board.board[i][j] == 0 and board.board[i][j+1] == 0 and board.board[i][j+3] == 0:
                        h_score += 100
                except IndexError:
                    pass
                try:
                    if board.board[i][j] == 1 and board.board[i][j+1] == 1:
                        h_score -= 10
                    if board.board[i][j] == 1 and board.board[i][j+1] == 1 and board.board[i][j+2] == 0:
                        h_score -= 100
                    if board.board[i][j] == 1 and board.board[i][j+1] == 1 and board.board[i][j+3] == 0:
                        h_score -= 100
                    if board.board[i][j] == 1 and board.board[i][j+1] == 1 and board.board[i][j+3] == 0:
                        h_score -= 100
                except IndexError:
                    pass
                try:
                    if (j + 3) <= board.HEIGHT:
                        if board.board[i][j] == 0 and board.board[i+1][j+1] == 0:
                            h_score += 10
                        if board.board[i][j] == 0 and board.board[i+1][j+1] == 0 and board.board[i+2][j+2] == 0:
                            h_score += 100
                        if board.board[i][j] == 0 and board.board[i+2][j+2] == 0 and board.board[i+3][j+3] == 0:
                            h_score += 100
                        if board.board[i][j] == 0 and board.board[i+1][j+1] == 0 and board.board[i+3][j+3] == 0:
                            h_score += 100
                except IndexError:
                    pass
                try:
                    if (j + 3) <= board.HEIGHT:
                        if board.board[i][j] == 1 and board.board[i+1][j+1] == 1:
                            h_score -= 10
                        if board.board[i][j] == 1 and board.board[i+1][j+1] == 1 and board.board[i+2][j+2] == 1:
                            h_score -= 100
                        if board.board[i][j] == 1 and board.board[i+2][j+2] == 1 and board.board[i+3][j+3] == 1:
                            h_score -= 100
                        if board.board[i][j] == 1 and board.board[i+1][j+1] == 1 and board.board[i+3][j+3] == 1:
                            h_score -= 100
                except IndexError:
                    pass
                try:
                    if(j - 3) >= 0:
                        if board.board[i][j] == 0 and board.board[i+1][j-1] == 0:
                            h_score += 10
                        if board.board[i][j] == 0 and board.board[i+1][j-1] == 0 and board.board[i+2][j-2] == 0:
                            h_score += 100
                        if board.board[i][j] == 0 and board.board[i+2][j-2] == 0 and board.board[i+3][j-3] == 0:
                            h_score += 100
                        if board.board[i][j] == 0 and board.board[i+1][j-1] == 0 and board.board[i+3][j-3] == 0:
                            h_score += 100
                except IndexError:
                    pass
                try:
                    if(j - 3) >= 0:
                        if board.board[i][j] == 1 and board.board[i+1][j-1] == 1:
                            h_score -= 10
                        if board.board[i][j] == 1 and board.board[i+1][j-1] == 1 and board.board[i+2][j-2] == 1:
                            h_score -= 100
                        if board.board[i][j] == 1 and board.board[i+2][j-2] == 1 and board.board[i+3][j-3] == 1:
                            h_score -= 100
                        if board.board[i][j] == 1 and board.board[i+1][j-1] == 1 and board.board[i+3][j-3] == 1:
                            h_score -= 100
                except IndexError:
                    pass
        return h_score
                        
                        
                
                    
class ManualPlayer(BasePlayer):
    def __init__(self, maxDepth=None):
        BasePlayer.__init__(self, maxDepth)

    def findMove(self, board):
        opts = " "
        for c in range(board.WIDTH):
            opts += " "+(str(c+1) if len(board.board[c]) < board.HEIGHT else ' ')+"  "
        print(opts)

        while True:
            col = input("Place a "+('O' if board.turn == 0 else 'X')+" in column: ")
            try: col = int(col) - 1
            except ValueError: continue
            if col >= 0 and col < board.WIDTH and len(board.board[col]) < board.HEIGHT:
                return col


class PlayerMM(BasePlayer):
    ##################
    #      TODO      #
    ##################
    # performs minimax on board with depth.
    # returns the best move and best score as a tuple
    def minimax(self, board, depth):
        Best_Move = None
        Best_Score = None
        if board.isEnd() == 0:
            return None, self.P1_WIN_SCORE
        if board.isEnd() == 1:
            return None, self.P2_WIN_SCORE
        if board.isEnd() == -1:
            return None, self.TIE_SCORE
        if not board.isEnd() and depth == 0:
            return None,self.myHeuristic(board)
        if board.turn == 0:
            Best_Score = -math.inf
            moves = board.getAllValidMoves()
            for move in moves:
                score = self.minimax(board.getChild(move),depth-1)[1]
                if score != None:
                    if score > Best_Score:
                        Best_Score = score
                        Best_Move = move
            return Best_Move,Best_Score
        if board.turn == 1:
            Best_Score = math.inf
            moves = board.getAllValidMoves()
            for move in moves:
                score = self.minimax(board.getChild(move),depth-1)[1]
                if score != None:
                    if score < Best_Score:
                        Best_Score = score
                        Best_Move = move
            return Best_Move, Best_Score
                    
        

    def findMove(self, board):
        move, score = self.minimax(board, self.maxDepth)
        return move

class PlayerAB(BasePlayer):
    ##################
    #      TODO      #
    ##################
    # performs minimax with alpha-beta pruning on board with depth.
    # alpha represents the score of max's current strategy
    # beta  represents the score of min's current strategy
    # in a cutoff situation, return the score that resulted in the cutoff
    # returns the best move and best score as a tuple
    def alphaBeta(self, alpha, beta, board, depth):
        Best_Move = None
        if board.isEnd() == 0:
            return None, self.P1_WIN_SCORE
        if board.isEnd() == 1:
            return None, self.P2_WIN_SCORE
        if board.isEnd() == -1:
            return None, self.TIE_SCORE
        if not board.isEnd() and depth == 0:
            return None,self.myHeuristic(board)
        if board.turn == 0:
            Best_Score = -math.inf
            moves = board.getAllValidMoves()
            for move in moves:
                score = self.alphaBeta(alpha, beta, board.getChild(move), depth-1)[1]
                if score != None:
                    if score > Best_Score:
                        Best_Score = score
                        Best_Move = move
                    if score > alpha:
                        alpha = score
                    if alpha >= beta:
                        return None, score
        if board.turn == 1:
            Best_Score = math.inf
            moves = board.getAllValidMoves()
            for move in moves:
                score = self.alphaBeta(alpha, beta, board.getChild(move), depth-1)[1]
                if score != None:
                    if score < Best_Score:
                        Best_Score = score
                        Best_Move = move
                    if beta > score:
                        beta = score
                    if alpha >= beta:
                        return None, score
        return Best_Move, Best_Score

    def findMove(self, board):
        move, score = self.alphaBeta(-math.inf, math.inf, board, self.maxDepth)
        return move

class PlayerDP(PlayerAB):
    ''' A version of PlayerAB that implements dynamic programming
        to cache values for its heuristic function, improving performance. '''
    def __init__(self, maxDepth):
        PlayerAB.__init__(self, maxDepth)

        self.resolved = {}

    ##################
    #      TODO      #
    ##################
    # if a saved heuristic value exists in self.resolved for board.state, returns that value
    # otherwise, uses BasePlayer.myHeuristic to get a heuristic value and saves it under board.state
    def myHeuristic(self, board):
        if board.state in self.resolved:
            return self.resolved[board.state]
        else:
            score = super().myHeuristic(board)
            self.resolved[board.state] = score
            return score
        
        

#######################################################
###########Example Subclass for Testing
#######################################################

# This will inherit your findMove from above, but will override the heuristic function with
# a new one; you can swap out the type of player by changing X in "class TestPlayer(X):"
class TestPlayer(BasePlayer):
    # define your new heuristic here
    def myHeurisitic(self):
        pass



