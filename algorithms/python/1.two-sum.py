#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return self.usingExhaustive(nums, target)

    def usingExhaustive(self, nums, target):
        numsCount = len(nums)
        for i in range(numsCount):
            for j in range(i + 1, numsCount):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def usingHashMap(self, nums, target):
        pass


# hash method
# class Solution:

#     def twoSum(self, nums, target):
#         pass

# @lc code=end
