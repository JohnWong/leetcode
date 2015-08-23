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

    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solveSudokuInternal(self, board, index):
        if index == 9 * 9:
            return True
        i = index / 9
        j = index % 9
        if board[i][j] == '.':
            p = self.getPossible(board, i, j)
            for k in p:
                board[i][j] = k
                if self.solveSudokuInternal(board, index + 1):
                    return True
                pass
            board[i][j] = '.'
            return False
        else:
            return self.solveSudokuInternal(board, index + 1)


    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solveSudoku(self, board):
        real = list()
        for x in board:
            real.append(list(x))
            pass

        self.solveSudokuInternal(real, 0)
        for x in range(9):
            board[x] = "".join(real[x])
            pass
        pass


if __name__ == '__main__':
    s = Solution()
    board = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
    s.solveSudoku(board)
    for x in board:
        print(x)
