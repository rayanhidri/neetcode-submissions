class Solution:
    def isPalindrome(self, s: str) -> bool:
        # reversing strings the compare : T.C = O(n) S.C= O(n)
        #two pointers : T.C O(n) S.C O(1)
        # --> two pointers optimal
        left = 0
        right = len(s)-1
        while left < right: 
            #make sure to skip non alphanumeric chars from left and/or right
            while left < right and not s[left].isalnum():
                left += 1 #skip non alphanumeric char
            while left < right and not s[right].isalnum():
                right -= 1 #skip non alphanumeric char
            #check if palindrome at the time being
            if s[left].lower() != s[right].lower():
                return False
            # increment left and decrement right
            left +=1
            right -= 1
        return True
            
            
            


        