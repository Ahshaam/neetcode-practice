class Solution:
    from collections import Counter

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        res = []
        for num in counts:
            idx = counts[num]
            buckets[idx].append(num)
        
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                if len(res) == k:
                    return res
                res.append(num)
        return res



                    