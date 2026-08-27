class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        pre = n*[0]
        suf = n*[0]
        
        pre[0] = 1
        suf[-1] = 1
        #build prefix array
        for i in range(1,n):
            pre[i] = nums[i-1] * pre[i-1]
        #build suffix array
        for i in range(n-2,-1,-1):
            suf[i] = nums[i+1] * suf[i+1]
        #build except self array
        for i in range(n):
            res.append(pre[i]*suf[i])
        return res