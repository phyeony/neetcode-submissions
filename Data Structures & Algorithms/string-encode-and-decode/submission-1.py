class Solution:
    charCount = []
    def encode(self, strs: List[str]) -> str:
        self.charCount=[]
        res = "";
        for word in strs:
            self.charCount.append(len(word))
            res += word
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        startIdx = 0
        # print(s)
        print(self.charCount)
        for count in self.charCount:
            
            res.append(s[startIdx:startIdx+count])
            startIdx += count
        print(res)
        return res