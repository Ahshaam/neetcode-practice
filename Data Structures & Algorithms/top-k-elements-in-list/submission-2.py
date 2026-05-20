class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        result = []
        for i in nums:
            if i not in h:
                h[i] = 0
            else:
                h[i] += 1
        sorted_hash = dict(sorted(h.items(), key=lambda x: x[1], reverse=True))
        for i, x in enumerate(sorted_hash):
            if i >= k:
                return result
            result.append(x)
        return result 


