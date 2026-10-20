from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()  
        elements = []
        occurence = []
        result = []

        # Get elements and their occurence 
        for i in range(len(nums)):
            if nums[i] not in elements:
                elements.append(nums[i])
                occurence_i = 1  
                for j in range(i + 1, len(nums)):
                    if nums[i] == nums[j]:
                        occurence_i += 1
                occurence.append(occurence_i)

        # Find the most k frequent elements
        while k > 0:
            most_frequent = max(occurence)
            index = occurence.index(most_frequent)
            result.append(elements[index])
            del occurence[index]
            del elements[index]
            k -= 1

        return result

                


