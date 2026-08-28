class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        #keep track of gaps, at pos 0, theres no gaps
        hash = {0:0} #key = gap loc, value = gap count

        for layer in wall: 
            total = 0
            for i in range(len(layer)-1): #don't count the last brick
                total += layer[i] #add gap to the total array
                #adds 0 if item doesnt exist + 1
                hash[total] = hash.get(total,0) + 1 
        #length of wall - gap count
        return len(wall) - max(hash.values())

