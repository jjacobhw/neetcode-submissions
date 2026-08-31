from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = deque(students)
        n = len(students)
        result = len(students)

        for s in sandwiches:
            count = 0
            #While the queue is not empty and mismatching sandwiches
            while count < len(queue) and queue[0] != s:
                queue.rotate(-1)
                count += 1 #add hungry stu if rotate
            if queue and queue[0] == s:
                queue.popleft()
                result -= 1 #sub hungry stu if removed
            else:
                break
        return result