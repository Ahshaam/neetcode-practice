class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word = {}
        word2 = {}
        for i in s:
            if i not in word:
                word[i] = 1
            else:
                word[i] += 1
        for i in t:
            if i not in word2:
                word2[i] = 1
            else:
                word2[i] += 1

        return word == word2