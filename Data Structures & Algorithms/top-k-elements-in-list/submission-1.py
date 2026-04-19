class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = collections.defaultdict(int)
        arr = []

        for i in nums:
            d[i] += 1

        for i in d:
            arr.append([d[i], i])
        arr.sort()

        result = []
        while len(result) < k:
            result.append(arr.pop()[1])

        return result

