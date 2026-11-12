class TimeMap:

    def __init__(self):
        self.res = {}
        self.keyToValues = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.res[tuple([key,timestamp])] = value
        self.keyToValues[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyToValues:
            return ""
        
        if tuple([key,timestamp]) in self.res:
            return self.res[tuple([key,timestamp])]

    
        values = self.keyToValues[key]

        if values[0] > timestamp:
            return ""
        l=0
        r=len(values)-1
        
        while l<=r:
            m = l + (r-l)//2
            if values[m] > timestamp:
                r=m-1
            elif values[m] < timestamp:
                l=m+1

        return self.res[tuple([key, values[l-1]])]
                
