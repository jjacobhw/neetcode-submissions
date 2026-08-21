class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #enables lists as a dictionary key
        result = defaultdict(list) 
        for string in strs:
            alpha = [0] * 26
            for letter in string:
                alpha[ord(letter)-ord('a')] += 1
            result[tuple(alpha)].append(string)
        
        return list(result.values())