class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_seq = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
                max_seq = max(count, max_seq)
            else:
                count = 0
        return max_seq