class Solution:
    def isPalindrome(self, s: str) -> bool:
        p = ""
        for i in s:
            if i.isalnum():
                p += i
        
        r = ""
        for i in p[::-1]:
            r += i

        return p.lower() == r.lower()

