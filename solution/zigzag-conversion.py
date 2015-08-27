class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        cnt = (numRows - 1) * 2
        result = [""] * numRows
        for i in range(len(s)):
            x = i % cnt
            if x < numRows:
                result[x] += s[i]
                pass
            else:
                result[numRows * 2 - 2 - x] += s[i]
                pass
            pass
        rs = ""
        for i in result:
            rs += i
            pass
        return rs


if __name__ == '__main__':
    s = Solution()
    r = s.convert("PAYPALISHIRING", 3)
    print(r)