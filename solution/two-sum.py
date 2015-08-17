class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        r = sorted(nums)
        i = 0
        j = len(r) - 1
        while i < j:
            sums = r[i] + r[j]
            if sums == target:
                s = nums.index(r[i])
                e = nums.index(r[j])
                if e == s:
                    e = nums.index(r[j], e + 1)
                    pass
                return sorted([s + 1, e + 1])
            elif sums < target:
                i += 1
                pass
            else:
                j -= 1
                pass
            pass
        pass