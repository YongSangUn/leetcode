#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start


# Exhaustive method
class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsCount = len(nums)
        for i in range(numsCount):
            for j in range(i + 1, numsCount):
                if nums[i] + nums[j] == target:
                    return [i, j]


# hash method
# class Solution:

#     def twoSum(self, nums, target):
#         pass

# @lc code=end
