class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {} # { number : frequency}
        output = []
        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]] += 1
            else:
                hashmap[nums[i]] = 1
        # get the most k keys with biggest values idk how to get that off of a hashmap
        while k != 0:
            max_key = max(hashmap, key=hashmap.get)
            output.append(max_key)
            del hashmap[max_key] # get rid of that key to move on to the next
            k -= 1
        return output

        