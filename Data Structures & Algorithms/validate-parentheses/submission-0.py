class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = ['(', '[', '{']
        for i in s:
            if i in opening:
                stack.append(i)
            else:
                if not stack:
                    return False

                if i == ')' and stack[-1] == '(':
                    stack.pop()
                    
                elif i == '}' and stack[-1] == '{':
                    stack.pop()

                elif i == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            
        return not stack

