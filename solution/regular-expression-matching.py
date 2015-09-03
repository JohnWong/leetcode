class Solution(object):

    def isMatch(self, s, p):
        return self.isMatchI(s, p, 0, 0)

    def isMatchI(self, s, p, si, pi):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(s) - si == 0:
            if len(p) - pi == 0 or len(p) - pi == 2 and p[pi + 1] == "*":
                return True
            else:
                return False
        if len(p) - pi == 0:
            return False

        if len(p) - pi >= 2 and p[pi + 1] == "*":
            idx = si
            while idx < len(s) and (s[idx] == p[pi + 0] or p[pi + 0] == "."):
                if self.isMatchI(s, p, idx, pi + 2):
                    return True
                idx += 1
                pass
            return self.isMatchI(s, p, si, pi + 2)
        else:
            if s[si] == p[pi] or p[pi] == ".":
                return self.isMatchI(s, p, si + 1, pi + 1)
            pass
        return False


s = Solution()
# print(s.isMatch("aa","a") == False)
# print(s.isMatch("aa","aa") == True)
# print(s.isMatch("aaa","aa") == False)
# print(s.isMatch("aa", "a*") == True)
# print(s.isMatch("aa", ".*") == True)
# print(s.isMatch("ab", ".*") == True)
# print(s.isMatch("aab", "c*a*b") == True)
print(s.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c") == False)
