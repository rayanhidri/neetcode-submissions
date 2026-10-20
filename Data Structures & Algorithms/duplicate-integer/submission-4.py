class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {} #store numbers in a hashmap for O(1) lookup
        for i in range(len(nums)):
            if nums[i] in hashmap:
                return True
            else:
                hashmap[nums[i]] = nums[i]
        return False
     
          