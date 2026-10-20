from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in hashMap:
                hashMap[nums[i]] = i
            else:
                return [hashMap[diff], i]



        
        