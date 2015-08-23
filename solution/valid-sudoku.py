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
    t = """519748632
783652419
426139875
357986241
264317598
198524367
975863124
832491756
641275983"""
    src = []
    for i in t.split('\n'):
        src.append(list(i))
        pass

    src = ["139748259","725139847","928129136","317258244","264911598","898347312","591883423","483512976","762275981"]
    s = Solution()
    r = s.isValidSudoku(src)
    print(r)