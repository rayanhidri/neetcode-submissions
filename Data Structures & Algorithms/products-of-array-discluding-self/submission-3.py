class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = []
        prefix = [1] * n
        suffix = [1] * n
        suffix[n-1] = 1  
        prefix[0] = 1
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
    
        for i in range(n):
            output.append(prefix[i]*suffix[i] )
        print(prefix)
        print(suffix)
        return output  