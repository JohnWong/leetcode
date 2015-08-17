class Solution:
    def findMedianAt(self, nums1, nums2, index):
        if len(nums1) == 0:
            return nums2[index]
        if len(nums2) == 0:
            return nums1[index]
        if index == 0:
            return min(nums1[0], nums2[0])

        a1 = len(nums1) * index / (len(nums1) + len(nums2))
        a2 = index - a1 - 1

        if nums1[a1] > nums2[a2]:
            index -= a2 + 1
            return self.findMedianAt(nums1[:a1 + 1], nums2[a2 + 1:], index)
        else:
            index -= a1 + 1
            return self.findMedianAt(nums1[a1 + 1:], nums2[:a2 + 1], index)

    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1) + len(nums2)
        if m % 2 == 0:
            t1 = self.findMedianAt(nums1, nums2, m / 2 - 1)
            t2 = self.findMedianAt(nums1, nums2, m / 2)
            return (t1 + t2) / 2.0
        else:
            return self.findMedianAt(nums1, nums2, m / 2)
