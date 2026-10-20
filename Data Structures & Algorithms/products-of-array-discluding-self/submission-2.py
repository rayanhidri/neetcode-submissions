class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output =[]
        for i in range(len(nums)):
            new_nums = nums[:i] + nums[i+1:]
            product = 1 
            for j in range (len(new_nums)):
                product *= new_nums[j]
            output.append(product)
        return output
        