from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q = deque()
        count = 0

        for i in students:
            q.append(i)

        while count != len(q):
            if q[0] == sandwiches[0]:
                q.popleft()
                sandwiches = sandwiches[1:]
                count = 0
            else:
                temp = q.popleft()
                q.append(temp)
                count += 1

        return len(q)
            
