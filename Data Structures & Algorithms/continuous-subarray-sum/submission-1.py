class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        seen = {0:-1} # stores values based on remainder and first occurance
        sum = 0

        #check idx and num to calculate prefix
        for i, n in enumerate(nums):
            sum += n
            remainder = sum % k
            #if the same remainder appears again theres a sum div by k
            if remainder in seen: #window must be at least 2 indices
                if i - seen[remainder] > 1:
                    return True
            #add earliest occurance if remainder hasn't appeared
            else:
                seen[remainder] = i
        return False