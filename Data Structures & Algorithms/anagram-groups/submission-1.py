class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for str in strs:
            freq = [0] * 26
            for c in str:
                freq[ord(c) - ord('a')] += 1
            key = tuple(freq)
            groups[key].append(str)
        
        ans = []
        for group in groups.values():
            ans.append(group)
        return ans
        
