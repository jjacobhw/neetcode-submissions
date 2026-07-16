class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = set()
        l = 0
        largest = 0
        for i in range(len(s)): 
            while s[i] in char: #move the window right if there's a duplicate 
                char.remove(s[l]) #remove the leftmost char 
                l += 1 # update the window
            char.add(s[i]) # 
            largest = max(largest, i-l+1) #update the longest length if found 
        return largest
