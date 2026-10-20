class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s # input : [hello, world] #encode = 4#hello5#world
        return result


    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            # find the # delimiter
            j = i
            while j < len(s) and s[j] != '#':
                j += 1
        
        # extract (after finding #)
            length = int(s[i:j])
            result.append(s[j+1 : j+1+length])
            i = j + 1 + length #move to next word
    
        return result

