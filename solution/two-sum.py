class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        r = {}
        for i in xrange(len(nums)):
            x = nums[i]
            r[x] = r[x] + [i] if x in r else [i]
            pass

        for i in xrange(len(nums)):
            x = nums[i]
            f = target - x
            if f in r:
                if len(r[f]) >= 2:
                    return [r[f][0] + 1, r[f][1] + 1]
                if r[f][0] != i:
                    return [i + 1, r[f][0] + 1]
            pass
        pass
        

if __name__ == '__main__':
    s = Solution()
    r = s.twoSum([3, 2, 4], 6)
    print(r)