#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return self.usingTwoPointers(nums)

    def usingTwoPointers(self, nums):
        nums.sort()
        count = len(nums)
        if count < 3:
            return []

        head, tail = 0, count - 1
        targetNums = []
        while head < count - 1:
            if head < tail - 1:
                for i in range(head + 1, tail):
                    if -nums[i] == nums[head] + nums[tail]:
                        # Deduplication
                        triplets = [nums[head], nums[i], nums[tail]]
                        if triplets not in targetNums:
                            targetNums.append(triplets)
                tail -= 1
            else:
                head += 1
                tail = count - 1
        # deDupNums = []
        # for num in targetNums:
        #     if num not in deDupNums:
        #         deDupNums.append(num)
        # return deDupNums
        return targetNums


# @lc code=end
