#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#


# @lc code=start
class Solution:

    def findMedianSortedArrays(self, nums1: List[int],
                               nums2: List[int]) -> float:
        return self.bruteForce(nums1, nums2)

    def bruteForce(self, nums1, nums2):
        nums = nums1 + nums2
        nums_sorted = sorted(nums)

        numsCount = len(nums_sorted)
        if numsCount == 1:
            index = 0
            return float(nums_sorted[index])

        if numsCount % 2 == 0:
            index1 = int(numsCount / 2 - 1)
            index2 = int(numsCount / 2)
            return (nums_sorted[index1] + nums_sorted[index2]) / 2
        else:
            index = int((numsCount - 1) / 2)
            return float(nums_sorted[index])


# @lc code=end
