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
        # pass
        nums.sort()
        count = len(nums)

        if count < 3 or nums[0] > 0 or nums[-1] < 0:
            return []

        targetNum = []
        for i in range(count - 1):
            head = i + 1
            tail = count - 1
            while head < tail:
                numSum = nums[i] + nums[head] + nums[tail]
                if numSum == 0:
                    tripLet = [nums[i], nums[head], nums[tail]]
                    if tripLet not in targetNum:
                        targetNum.append(tripLet)
                    head += 1
                    tail -= 1
                elif numSum < 0:
                    head += 1
                else:
                    tail -= 1
            i += 1
        return targetNum

    def usingTwoPointersOld(self, nums):
        # time limit exceeded. 2021.03.18
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

        return targetNums


# @lc code=end
