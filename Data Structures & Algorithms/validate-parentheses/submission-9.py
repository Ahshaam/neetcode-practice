class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_lst = "([{"
        close_lst = ")]}"

        for i in s:
            if i in open_lst:
                stack.append(i)
            if i in close_lst:
                if not stack:
                    return False
                cur = stack.pop()
                if i == ")" and cur != "(" or i == "}" and cur != "{" or i == "]" and cur != "[":
                    return False
        return not stack