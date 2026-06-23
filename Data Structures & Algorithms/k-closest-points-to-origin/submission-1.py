class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = lambda p: p[0]**2 + p[1]**2

        def partition(points, l, r):
            pivot = dist(points[r])

            i = l - 1
            for j in range(l, r):
                if dist(points[j]) <= pivot:
                    i += 1
                    points[i], points[j] = points[j], points[i]
            points[i + 1], points[r] = points[r], points[i + 1]
            return i + 1

        def quickSelect(l, r):
            if l >= r:
                return
            
            pivot_idx = partition(points, l , r)
            if pivot_idx == k:
                return 
            elif pivot_idx < k:
                quickSelect(pivot_idx + 1, r)
            else:
                quickSelect(l, pivot_idx - 1)
        
        quickSelect(0, len(points) - 1)
        return points[:k]