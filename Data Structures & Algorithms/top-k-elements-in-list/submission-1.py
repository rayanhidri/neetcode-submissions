from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()  # Sort nums in-place
        elements = []
        occurence = []
        result = []

        # Gather unique elements and their occurrences
        for i in range(len(nums)):
            if nums[i] not in elements:
                elements.append(nums[i])
                occurence_i = 1  # Reset occurrence counter
                for j in range(i + 1, len(nums)):
                    if nums[i] == nums[j]:
                        occurence_i += 1
                occurence.append(occurence_i)

        # Find the top k frequent elements
        while k > 0:
            most_frequent = max(occurence)
            index = occurence.index(most_frequent)
            result.append(elements[index])
            del occurence[index]
            del elements[index]
            k -= 1

        return result

                


