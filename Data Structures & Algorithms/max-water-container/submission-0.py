class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        left = 0
        right = len(heights)-1

        for i in range(len(heights)):
            curr = min(heights[left], heights[right]) * (right - left)
            if curr > max: 
                max = curr
            if heights[right] > heights[left]: 
                left += 1
            else:
                right -= 1
        return max