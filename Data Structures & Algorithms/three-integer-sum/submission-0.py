class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # if sum of 3 numbers equals 0 , group them together. input ex: [-4,-1,-1,0,1,2]. -4 + -1 + 2 = 3 > 0
        output = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: #this condition is to avoid having duplicate triplets
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right: 
                curr_sum = nums[i] + nums[left] + nums[right]
                if curr_sum == 0:
                    output.append([nums[i], nums[left], nums[right]])
                    left += 1 #increment to look for a potentiel new group with fixed i index
                    while left < right and nums[left] == nums[left-1]: 
                        left += 1 # avoid duplicate PAIRSd
                elif curr_sum < 0:
                    left += 1
                else:
                    right -= 1
        return output