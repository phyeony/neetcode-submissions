class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashMap = {}
        for word in strs:
            letterCount = [0] * 26;
            for letter in word:
                order = ord(letter) - ord('a')
                letterCount[order] += 1;
            letterCountTuple = tuple(letterCount)
        
            if letterCountTuple in hashMap:
                hashMap[letterCountTuple].append(word)
            else:
                hashMap[letterCountTuple] = [word]
        return list(hashMap.values())