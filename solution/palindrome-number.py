class Solution(object):
    
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        for i in range(len(x) / 2):
            if x[i] != x[len(x) - i - 1]:
                return False
            pass
        return True


s = Solution()
print(s.isPalindrome(1331331))