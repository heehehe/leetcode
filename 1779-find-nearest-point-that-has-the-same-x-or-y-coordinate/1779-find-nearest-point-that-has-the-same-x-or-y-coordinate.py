class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        result = -1; idx = -1
        for i, p in enumerate(points):
            if not (x == p[0] or y == p[1]):
                continue

            distance = abs(x-p[0]) + abs(y-p[1])
            if result < 0 or result > distance:
                result = distance
                idx = i

        return idx