from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0  
        
        nums.sort()  
        sequence = 1  
        tab_seq = []

        
        for i in range(1, len(nums)):
           
            if nums[i] == nums[i - 1] + 1:
                sequence += 1  
            elif nums[i] != nums[i - 1]:  
                tab_seq.append(sequence)
                sequence = 1  

        
        tab_seq.append(sequence)

        return max(tab_seq)  

                
                

