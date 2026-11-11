import math 

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = 0
        for pile in piles:
            max_pile = max(pile, max_pile)
        print(max_pile)
        l=1
        r=max_pile
        ans=max_pile
        while l<=r:
            mid = l + (r-l)//2
            duration = 0
            for pile in piles:
                duration+= math.ceil(pile/mid)

            print(mid, 'took:',duration, l, r)
            if duration > h:
                l = mid  + 1
            else: 
                ans = min(mid, ans)
                r = mid - 1

        return ans