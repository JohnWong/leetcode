class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        s = nums
        i = 0
        j = len(s) - 1
        r = set()
        while i < j:
            sums = s[i] + s[j]
            if sums == target:
                r.add((s[i], s[j]))
                i += 1
                pass
            elif sums < target:
                i += 1
                pass
            else:
                j -= 1
                pass
            pass
        return r

    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        nums = sorted(nums)
        r = set()
        for i in xrange(len(nums)):
            t = self.twoSum(nums[i+1:], -nums[i])
            for x in t:
                r.add(tuple(sorted(x + (nums[i],))))
                pass
            pass
        rr = list()
        for y in r:
            rr.append(list(y))
            pass
        return rr