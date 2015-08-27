class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ns = '#'
        for i in s:
            ns += i + '#'
            pass

        mx = ans = po = 0
        lens = [1] * len(ns)
        for i in range(len(ns)):
            if mx > i:
                lens[i] = min(mx - i, lens[2 * po - i])
                pass
            else:
                lens[i] = 1

            while i + lens[i] < len(ns) and ns[i - lens[i]] == ns[i + lens[i]]:
                lens[i] += 1
                pass
            if lens[i] + i > mx:
                mx = lens[i] + i
                po = i
                pass
            if lens[i] > lens[ans]:
                ans = i
                pass
            pass
        return ns[ans - lens[ans] + 1:ans + lens[ans]].replace("#", "")


if __name__ == '__main__':
    s = Solution()
    r = s.longestPalindrome("a")
    print(r)