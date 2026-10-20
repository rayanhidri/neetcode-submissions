from typing import List

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []                 # result = [numbers]
        frequency = []              # frequency[i] = occurrence count for distinct_numbers[i]
        distinct_numbers = []       # numbers without duplicates

        n = len(nums)

        # Count occurrences
        for i in range(0, n):
            if nums[i] in distinct_numbers:
                continue

            distinct_numbers.append(nums[i])
            elem_count = 1

            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    elem_count += 1

            frequency.append(elem_count)

        # Pick top k by repeatedly taking the max frequency
        while k != 0 and len(frequency) > 0:
            x = max(frequency)
            idx = frequency.index(x)          # index of x in frequency (same index in distinct_numbers)
            result.append(distinct_numbers[idx])

            # remove so we don't pick it again
            frequency.pop(idx)
            distinct_numbers.pop(idx)

            k -= 1

        return result

    

        
    

        

                


