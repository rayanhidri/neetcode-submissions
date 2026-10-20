class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # dont forget to increment right and left at the end because array in 1-indexed
        left, right = 0, len(numbers) - 1
        output = []
        while left < right:
            if numbers[left] + numbers[right] == target:
                output.append(left + 1)
                output.append(right + 1)
                return output   
            if numbers[left] + numbers[right] < target:
                left +=1
            if numbers[left] + numbers[right] > target:
                right -= 1
        return output

