class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l = 0
        t = 0
        r = len(matrix[0])
        b = len(matrix)
        result = []
        
        while l < r or t < b:
            for i in range(l,r):
                result.append(matrix[t][i])
            t += 1
            
            for i in range(t,b):
                result.append(matrix[i][r-1])
            r -= 1

            if (l >= r or t >= b):
                break

            for i in range(r-1,l-1,-1):
                result.append(matrix[b-1][i])
            b -= 1

            if (l >= r or t >= b):
                break

            for i in range(b-1,t-1,-1):
                result.append(matrix[i][l])
            l += 1

            if (l >= r or t >= b):
                break

        return result