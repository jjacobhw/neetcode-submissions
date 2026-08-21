class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        rows = [0]*len(picture)
        cols = [0]*len(picture[0])
        count = 0
        
        for i in range(len(picture)):
            for j in range(len(picture[i])):
                if picture[i][j] == 'B':
                    rows[i] += 1
                    cols[j] += 1
        
        for i in range(len(picture)):
            for j in range(len(picture[i])):
                if picture[i][j] == 'B' and rows[i] == 1 and cols[j] == 1:
                    count += 1
        return count