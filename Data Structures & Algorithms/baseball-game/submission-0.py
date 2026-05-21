class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        top = -1
        for i in operations:
            if i == "C":
                top -= 1
                stack = stack[:top+1]
            elif i == "D":
                stack.append(int(stack[top]) * 2) 
                top += 1
            elif i == "+":
                stack.append(int(stack[top]) + int(stack[top-1]))
                top += 1
            else:
                stack.append(int(i))
                top += 1

        return sum(stack)

