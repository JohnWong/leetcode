class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        t = []
        count = 0
        for i in range(len(s)):
            x = s[i]
            if t.count(x) == 0:
                t.append(x)
            else:
                t = t[t.index(x) + 1:]
                t.append(x)
                pass

            count = max(count, len(t))
            pass
        return count