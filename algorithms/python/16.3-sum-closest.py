#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start


class Solution:

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        return self.usingTwoPointers(nums, target)

    def usingTwoPointers(self, nums, target):
        count = len(nums)
        closest = 10**4

        for i in range(count):
            head, tail = i + 1, count - 1
            while head < tail:
                sumAll = nums[i] + nums[head] + nums[tail]

                if sumAll == target:
                    return target
                if abs(sumAll - target) < abs(closest - target):
                    closest = sumAll
                if sumAll < target:
                    head += 1
                else:
                    tail -= 1

        return closest


# @lc code=end
