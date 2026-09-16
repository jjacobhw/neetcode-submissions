class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [] # 
        for i in asteroids:
            while stack and i < 0 < stack[-1]: #check if asteroids move in opposite directions
                if stack[-1] < -i: #destroy all the smaller asteroid
                    stack.pop()
                    continue
                elif stack[-1] == -i: #destroy both asteroids if they are the same size
                    stack.pop()
                break
            else:
                stack.append(i)
        return stack
