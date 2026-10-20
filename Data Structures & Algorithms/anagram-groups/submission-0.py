from typing import List

def Anagram(str1, str2):
    # Check if two strings are anagrams by comparing their sorted forms
    sorted_str1 = ''.join(sorted(str1))
    sorted_str2 = ''.join(sorted(str2))
    return sorted_str1 == sorted_str2

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tab = []
        visited = [False] * len(strs)  # Keep track of which strings have been added to a group

        for i in range(len(strs)):
            if not visited[i]:
                tab1 = [strs[i]]
                visited[i] = True  # Mark the current string as visited

                for j in range(i + 1, len(strs)):
                    if not visited[j] and Anagram(strs[i], strs[j]):
                        tab1.append(strs[j])
                        visited[j] = True  # Mark the matched string as visited
                
                tab.append(tab1)  # Add the group to the result list

        return tab
