class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #count chars in substr
        target = {}
        for char in s1:
            target[char] = target.get(char, 0) + 1

        left = 0
        window = {}
        for right in range(len(s2)):
            #Add char to the sliding window
            right_char = s2[right]
            window[right_char] = window.get(right_char, 0) + 1
            #remove left char if window becomes too big, then slide the window left
            if right - left + 1 > len(s1):
                left_char = s2[left]
                window[left_char] -= 1
                if window[left_char] == 0:
                    del window[left_char]
                left += 1
            if window == target:
                return True
        return False