class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen:
                seen[nums[i]] += 1
            else:
                seen[nums[i]] = 1
        while (k > 0):
            max_key = max(seen, key=seen.get)
            result.append(max_key)
            del seen[max_key]
            k -= 1
        return result

        # Find the key with the highest value
        # max_key = max(stats, key=stats.get)