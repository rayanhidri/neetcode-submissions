class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len (t):
             return False
        seen_s = {} # { char : its occurences}
        seen_t = {}
        for i in range(len(s)):
            if s[i] in seen_s:
                seen_s[s[i]] += 1 #increase the frequency of s[i] in the hash
            else:
                seen_s[s[i]] = 1
            if t[i] in seen_t:
                seen_t[t[i]] += 1 #increase the frequency of s[i] in the hash
            else:
                seen_t[t[i]] = 1
        return seen_s == seen_t #compare both hashs if theyre equal return true else return false


        