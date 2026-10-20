class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_set = set(nums)
        longest = 0
        for num in num_set:
            if (num - 1) not in num_set: # check if number is the start of a sequence
                curr_num = num
                curr_streak = 1
                while (curr_num + 1) in num_set: # as long as the consecutive number is in set we good
                    curr_num += 1 # update current number
                    curr_streak += 1 # update sequence length

                longest = max(longest,curr_streak)
        return longest 