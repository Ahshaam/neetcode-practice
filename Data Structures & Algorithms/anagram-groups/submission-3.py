from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = defaultdict(list)
        for i in strs:
            table[''.join(sorted(i))].append(i)
        
        res = []
        for i in table:
            res.append(table[i])
        
        return res