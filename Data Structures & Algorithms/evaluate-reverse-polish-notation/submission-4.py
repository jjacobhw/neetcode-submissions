class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens: 
            if i == "+":
                t1 = stack.pop()
                t2 = stack.pop()
                stack.append(int(t1) + int(t2))
            elif i == "*":
                t1 = stack.pop()
                t2 = stack.pop()
                stack.append(int(t1) * int(t2))
            elif i == "-":
                t1 = stack.pop()
                t2 = stack.pop()
                stack.append(int(t2) - int(t1))
            elif i == "/":
                t1 = stack.pop()
                t2 = stack.pop()
                stack.append(int(float(t2)/int(t1)))
            else:
                stack.append(int(i))
        return stack[0]