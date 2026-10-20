from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        tab = []
        test = False
        for i in range(length - 1):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    tab.append(i)
                    tab.append(j)
                    test = True
                    break
            if test == True:
                break
        return tab
