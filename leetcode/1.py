#!/usr/bin/python2.7

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        ret = []
        d = {}

        for i, var in enumerate(nums):
            d[var] = i

        for i in range(len(nums)):
            other = target - nums[i]
            if other in d and d[other] != i:
                ret.append(i)
                ret.append(d[other])
                break

        return ret

if __name__ == '__main__':
    a = Solution()
    src = [2, 7, 11, 15]
    target = 9
    print a.twoSum(src, target)
