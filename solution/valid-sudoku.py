class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            s = set()
            count = 0
            for j in range(0, 9):
                if board[i][j] != '.':
                    s.add(board[i][j])
                    count += 1
                    pass
                pass

            if len(s) != count:
                return False
            pass

        for j in range(9):
            s = set()
            count = 0
            for i in range(0, 9):
                if board[i][j] != '.':
                    s.add(board[i][j])
                    count += 1
                    pass
                pass

            if len(s) != count:
                return False
            pass
        
        for i in range(9):
            s = set()
            count = 0
            for j in range(9):
                x = i / 3 * 3 + j / 3
                y = i % 3 * 3 + j % 3
                if board[x][y] != '.':
                    s.add(board[x][y])
                    count += 1
                    pass
                pass

            if len(s) != count:
                return False
            pass

        return True




if __name__ == '__main__':
    s = Solution()
    r = s.isValidSudoku([
        ['5','3','.','.','7','.','.','.','.'],
        ['6','.','.','1','9','5','.','.','.'],
        ['.','9','8','.','.','.','.','6','.'],
        ['8','.','.','.','6','.','.','.','3'],
        ['4','.','.','8','.','3','.','.','1'],
        ['7','.','.','.','2','.','.','.','6'],
        ['.','6','.','.','.','.','2','8','.'],
        ['.','.','.','4','1','9','.','.','5'],
        ['.','.','.','.','8','.','.','7','9']
        ])
    print(r)