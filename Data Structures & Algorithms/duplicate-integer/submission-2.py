class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
     countMap = {}
     for num in nums:
        if num not in countMap:
            countMap[num] = 1
        else:
            countMap[num] += 1
            return True
     return False
          