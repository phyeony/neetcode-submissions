class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myDict = {} 
        for num in nums:
            myDict[num] = 1
        start = {}
        for num in nums:
            if num-1 not in myDict:
                start[num] = 1;
        longest = 0
        for startNumber in start:
            i = startNumber+1
            while i in myDict:
                start[startNumber] += 1
                i += 1
        for value in start.values():
            if value > longest:
                longest = value

        return longest
                
