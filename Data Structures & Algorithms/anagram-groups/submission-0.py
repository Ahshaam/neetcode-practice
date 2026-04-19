from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        result = []
        for i in strs:
            sorted_str = tuple(sorted(i))
            d[sorted_str].append(i)
            #d[sorted_str] += i

        for i in d.values():
            result.append(i)

        return result