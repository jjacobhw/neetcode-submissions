class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums) #add all unique elements to set
        longest = 0
        for i in numset: 
            if i-1 not in numset: #start a new sequence if item not in sequence
                length = 1 #check if the next element is in the set
                while (i+length) in numset:
                    length += 1 #continue checking until the element is not there
                longest = max(length,longest) #keep the longest sequence
        return longest
                