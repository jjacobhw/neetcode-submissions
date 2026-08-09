import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            st1 = heapq.heappop(stones)
            st2 = heapq.heappop(stones)
            if st2 > st1:
                st1 -= st2
                heapq.heappush(stones,st1)
        stones.append(0)
        return abs(stones[0])