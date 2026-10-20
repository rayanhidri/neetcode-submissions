class Solution:
    def isPalindrome(self, s: str) -> bool:
        # reversing strings the compare : T.C = O(n) S.C= O(n)
        #two pointers : T.C O(n) S.C O(1)
        # --> two pointers optimal
        left = 0
        right = len(s)-1
        while left < right: 
            while left < right and not s[left].isalnum():
                left += 1 #skip non alphanumeric char
            while left < right and not s[right].isalnum():
                right -= 1 #skip non alphanumeric char
            if s[left].lower() != s[right].lower():
                return False
            left +=1
            right -= 1
        return True
            
            
            


        