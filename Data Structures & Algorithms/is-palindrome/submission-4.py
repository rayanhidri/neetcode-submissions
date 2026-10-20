class Solution:
    def isPalindrome(self, s: str) -> bool:
       new_s =""
       for i in range(len(s)):
        #Remove non-alphanumeric characters
        if "A" <= s[i].upper() <= "Z" or "0" <= s[i] <= "9":
            new_s += s[i].upper()
        #Check if a string and its reverse are identical
       return new_s == new_s[::-1]