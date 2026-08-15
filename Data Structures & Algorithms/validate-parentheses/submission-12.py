class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parens = { ")" : "(", "]" : "[", "}" : "{" }
        for i in s:
            if i in parens:
                if len(stack) != 0 and stack[-1] == parens[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        if len(stack) == 0:
            return True
        else:
            return False