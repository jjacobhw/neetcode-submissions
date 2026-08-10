class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        result = [intervals[0]]

        for start, end in intervals[1:]:
            final = result[-1][-1]
            if start <= final:
                result[-1][-1] = max(final, end)
            else:
                result.append([start,end])
        return result