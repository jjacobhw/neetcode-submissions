class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfied,window = 0,0
        max_window,l = 0,0
        for r in range(len(customers)):
            if grumpy[r] == 1: #customers satisfied if grumpy
                window += customers[r]
            else: #customers satisfied regardless
                satisfied += customers[r]
            
            if r-l+1 > minutes: #create the sliding window
                if grumpy[l] == 1: #shrink the window to m minutes
                    window -= customers[l] #remove the corresponding customer
                l += 1 #move window forward
            max_window = max(window, max_window)
        return max_window + satisfied