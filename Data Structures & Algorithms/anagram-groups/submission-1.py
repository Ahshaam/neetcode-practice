from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        res = []

        for i in strs:
            string = tuple(sorted(i))
            d[string].append(i)
            
        for i in d.values():
            res.append(i)
        
        return res