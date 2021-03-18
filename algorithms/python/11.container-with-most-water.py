#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start

# class Solution:


class Solution:

    def maxArea(self, height: List[int]) -> int:
        return self.usingTwoPointers(height)
        # return self.bruteForce(height)  # timeout, to be optimized.

    def usingTwoPointers(self, height):
        areaMax, head, tail = 0, 0, len(height) - 1
        while head < tail:
            area = min(height[head], height[tail]) * (tail - head)
            areaMax = max(areaMax, area)
            if height[head] < height[tail]:
                head += 1
            else:
                tail -= 1

        return areaMax

    def bruteForce(self, height):
        # These will be `Time Limit Exceeded` error by using double loop.
        count = len(height)
        areaMax = 0
        for i in range(count):
            for j in range(i, count):
                area = min(height[i], height[j]) * (j - i)
                areaMax = max(areaMax, area)

        return areaMax


# @lc code=end
