class Solution:
    def isPalindrome(self, s: str) -> bool:
        p = ""
        l = 0

        for i in s:
            if i.isalnum():
                p += i
        p = p.lower()

        r = len(p) - 1

        while l < r:
            if p[l] != p[r]:
                return False
            l+=1
            r-=1

        return True

