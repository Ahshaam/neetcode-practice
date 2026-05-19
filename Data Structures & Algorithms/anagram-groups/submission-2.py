from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for i in strs:
            string = tuple(sorted(i))
            d[string].append(i)
        
        return list(d.values())