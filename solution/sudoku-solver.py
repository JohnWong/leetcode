class Solution:
    def getPossible(self, board, x, y):
        s = set()
        for i in range(0, 9):
            if i != x and type(board[i][y]) == str:
                s.add(board[i][y])
                pass
            if i != y and type(board[x][i]) == str:
                s.add(board[x][i])
                pass
            pass
        x = x / 3 * 3
        y = y / 3 * 3
        for i in range(x, x + 3):
            for j in range(y, y + 3):
                if type(board[i][j]) == str:
                    s.add(board[i][j])
                    pass
                pass
            pass
        return set(['1', '2', '3', '4', '5', '6', '7', '8', '9']) - s

    def setValue(self, board, x, y, v):
        if len(v) > 1:
            board[x][y] = v
            return
        if len(v) == 0:
            print(x, y, v)
            for line in board:
                print(line)
                pass
            pass
        board[x][y] = list(v)[0]
        for i in range(0, 9):
            if i != x and type(board[i][y]) == set:
                self.setValue(board, i, y, board[i][y] - v)
                pass
            if i != y and type(board[x][i]) == set:
                self.setValue(board, x, i, board[x][i] - v)
                pass
            pass
        x = x / 3 * 3
        y = y / 3 * 3
        for i in range(x, x + 3):
            for j in range(y, y + 3):
                if type(board[i][j]) == set:
                    self.setValue(board, i, j, board[i][j] - v)
                    pass
                pass
            pass
        pass

    def getOnlyValue(self, board, x, y):
        s = set(board[x][y])
        for z in range(9):
            if z != y and type(board[x][z]) == set:
                s = s - board[x][z]
                pass
            pass

        if len(s) == 1:
            return s

        s = set(board[x][y])
        for z in range(9):
            if z != x and type(board[z][y]) == set:
                s = s - board[z][y]
                pass
            pass

        if len(s) == 1:
            return s

        s = set(board[x][y])
        for i in range(x / 3 * 3, x / 3 * 3 + 3):
            for j in range(y / 3 * 3, y / 3 * 3 + 3):
                if (i != x or j != y) and type(board[i][j]) == set:
                    s -= board[i][j]
                pass
            pass
        return s

    def check(self, board):
        for i in range(9):
            for j in range(9):
                if type(board[i][j]) == set:
                    return False
                pass
            pass
        return True

    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solveSudokuInternal(self, board):
        for i in range(9):
            for j in range(9):
                x = board[i][j]
                if x == '.' or type(x) == set:
                    p = self.getPossible(board, i, j)
                    self.setValue(board, i, j, p)
                pass
            pass

        if self.check(board):
            return

        for i in range(9):
            for j in range(9):
                if type(board[i][j]) == set:
                    s = self.getOnlyValue(board, i, j)
                    if len(s) == 1:
                        self.setValue(board, i, j, s)
                        pass
                    pass
                pass
            pass
        pass

        if self.check(board):
            return

        count = 0
        for i in range(9):
            for j in range(9):
                if type(board[i][j]) == set and len(board[i][j]) > count:
                    mini = i
                    minj = j
                    count = len(board[i][j])
                pass
            pass

        for v in board[mini][minj]:
            boardn = self.deepcopy(board)
            self.setValue(boardn, mini, minj, set(v))
            if self.check(boardn):
                self.setValue(board, mini, minj, set(v))
                return
            pass
        pass

    def deepcopy(self, board):
        boardn = []
        for i in board:
            line = []
            for j in i:
                if type(j) == set:
                    line.append(set(j))
                else:
                    line.append(j)
                pass
            boardn.append(line)
            pass
        return boardn



    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solveSudoku(self, board):
        real = list()
        for x in board:
            real.append(list(x))
            pass

        self.solveSudokuInternal(real)
        for x in range(9):
            print(real[x])
            board[x] = "".join(real[x])
            pass
        pass


if __name__ == '__main__':
    s = Solution()
    board = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
    s.solveSudoku(board)
    board = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
    s.solveSudoku(board)
    board = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
    s.solveSudoku(board)
    for x in board:
        print(type(x))
        print(x)
