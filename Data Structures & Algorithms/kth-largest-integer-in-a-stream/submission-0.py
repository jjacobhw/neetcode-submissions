import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        #init constructors
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums) #convert list into heap
        while len(self.nums) > k: #pop until k elements are left
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
