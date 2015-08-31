class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = 0
        y = max(x, -x)
        while y > 0:
            r = r * 10 + y % 10
            y = y / 10
            pass
        return 0 if r > 0x7fffffff or r < -0x80000000 else r if x > -x else -r



s = Solution()
r = s.reverse(1534236469)
print(r)