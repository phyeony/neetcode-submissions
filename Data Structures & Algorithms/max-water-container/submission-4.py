class Solution:
    def maxArea(self, height: list[int]) -> int:
        l =0 
        r = len(height)-1
        max_area = 0
        while l<r:
            max_area = max(max_area, (r-l) * min(height[l], height[r]))
            if height[r] > height[l]:
                l+=1
            # elif height[l+1]-height[l] == height[r-1]-height[r]:
            #     if height[l+1] > height[r-1]:
            #         l+=1
                
            else:
                r-=1
        return max_area
            