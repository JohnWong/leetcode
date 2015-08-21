class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        r = triangle[len(triangle) - 1]
        for i in xrange(len(triangle) - 2, -1, -1):
            for j in xrange(0, i + 1):
                print(i, j)
                r[j] = triangle[i][j] + min(r[j], r[j + 1])
                pass
            pass
        return r[0]


if __name__ == '__main__':
    s = Solution()
    r = s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])
    print(r)