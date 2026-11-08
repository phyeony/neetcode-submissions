class Solution:

    def encode(self, strs: List[str]) -> str:
        res = "";
        for word in strs:
            res += str(len(word)) + '#' + word 
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        startIdx = 0
        print(s)
        if len(s) == 0:
            return []
        while True:
            print(startIdx)
            hitDelimiter = False
            nextDelimiterIdx = startIdx
            while True:
                if s[nextDelimiterIdx] != '#':
                    nextDelimiterIdx += 1
                else:
                    break;
            count = int(s[startIdx: nextDelimiterIdx])
            startIdx = nextDelimiterIdx + 1
            res.append(s[startIdx: startIdx + count])
            print(res)
            startIdx += count
            if startIdx >= len(s) - 1:
                break;

        print(res)
        return res