class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        seen = {0:-1} # stores values based on remainder and first occurance
        sum = 0

        #check idx and val to calculate prefix
        for i, n in enumerate(nums):
            sum += n
            remainder = sum % k
            #if the same remainder appears again theres a sum div by k
            if remainder in seen:
                if i - seen[remainder] > 1:
                    return True
            else:
                seen[remainder] = i
        return False