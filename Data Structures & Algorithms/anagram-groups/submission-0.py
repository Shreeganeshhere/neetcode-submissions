class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        freq = {}
        anagrams = []

        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1
            
            count = tuple(count)
            if count in freq:
                freq[count].append(s)
            else:
                freq[count] = [s]

        return [val for val in freq.values()]
            