class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        for i in range(len(s)):
            if s[i] == '[':
                stack.append(s[i])
            elif len(stack) != 0:
                stack.pop()
        return (len(stack) + 1)//2