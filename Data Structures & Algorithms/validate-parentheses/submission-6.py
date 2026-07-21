from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        parens = { ")" : "(", "]" : "[", "}" : "{" }
        for i in s:
            if i not in parens:
                stack.append(i)
            else:
                if len(stack) == 0 or stack[-1] != parens[i]:
                    return False
                stack.pop()

        return not stack