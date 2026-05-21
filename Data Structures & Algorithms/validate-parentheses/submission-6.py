class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close = [')', '}', ']']

        for i in s:
            if i not in close:
                stack.append(i)
            elif not stack or (i == ')' and stack[-1] != '(' or i == '}' and stack[-1] != '{' or i == ']' and stack[-1] != '['):
                return False
            else:
                stack.pop() 
        return len(stack) == 0

