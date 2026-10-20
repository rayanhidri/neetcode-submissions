class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # idea : hashmap that looks like this { signature -> [strings]}
        # in order to get signature, i have to sort the string
        hashmap = {}
        for i in range(len(strs)):
            signature = "".join(sorted(strs[i])) 
            if signature in hashmap:
                hashmap[signature].append(strs[i])
            else:
                hashmap[signature] = [strs[i]]
        return list(hashmap.values())
            