class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} 
        result = []
        for i in range (len (nums)):
            comp = target - nums[i]
            if comp in seen:
                 result.append(seen[comp]) # add index of the elem thats already in seen to the result
                 result.append(i)# add i to result
            seen[nums[i]] = i #if its not in the hash, add it
        return result

