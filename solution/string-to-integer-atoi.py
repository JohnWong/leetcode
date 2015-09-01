class Solution(object):
    def myAtoi(self, str1):
        """
        :type str: str
        :rtype: int
        """

        str1 = str1.strip()
        st = str1[1:] if len(str1) > 0 and (str1[0] == "-" or str1[0] == "+") else str1
        ret = 0
        for i in st:
            if i < '0' or i > '9':
                break
            ret = ret * 10 + (ord(i) - ord('0'))
            pass
        ret = ret if len(str1) > 0 and str1[0] != "-" else -ret
        return max(min(0x7fffffff, ret), -0x80000000)


s = Solution()
print(s.myAtoi("  -21474836480"))