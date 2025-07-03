# 973. K Closest Points to Origin
# https://leetcode.com/problems/k-closest-points-to-origin/
# Medium


import heapq


class Solution:
    # Time Cx: O(n log n), Space Cx: O(n)
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        return heapq.nsmallest(k, points, lambda point: point[0] ** 2 + point[1] ** 2)
