class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t = 0
        b = len(matrix)-1

        #find the corresponding row
        while t <= b:
            curr = (t+b)//2
            if target > matrix[curr][-1]:
                t = curr + 1
            elif target < matrix[curr][0]:
                b = curr - 1
            else:
                break

        #Check if no row contains solution
        if t>b:
            return False

        l = 0
        r = len(matrix[curr])-1

        while l <= r:
            mid = (l+r)//2
            if target > matrix[curr][mid]:
                l = mid + 1
            elif target < matrix[curr][mid]:
                r = mid - 1
            else:
                return True
        return False

