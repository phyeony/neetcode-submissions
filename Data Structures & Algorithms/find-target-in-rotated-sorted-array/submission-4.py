class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l<r:
            m = l+(r-l)//2
            m_val = nums[m]
            r_val = nums[r]

            if target == m_val:
                return m
            elif target == r_val:
                return r
            elif target == nums[l]:
                return l

            if m_val > target and target >= r_val:
                # 456723 where t = 5
                # r < t < m -> look to the left
                r=m
            elif m_val > r_val and r_val >= target:
                # t < r < m -> llok to the rogjt where t = 2
                l= m +1
            elif target >= m_val and m_val > r_val:
                # r < m < t where t = 7 => look to the right
                l = m+1
            elif m_val <= target and target < r_val:
                # m < t < r > look to the right
                l = m+1
            elif target <= m and m < r:
                # t < m < r look to the left
                r=m
            elif m < r and r <= target:
                # m < r < t look to the left
                r=m
            else:
                print('shouldnt happen')
            
            # if target == m_val:
            #     return m
            # elif target == r_val:
            #     return r
            # elif target == nums[l]:
            #     return l

        
            
        if target == nums[r]:
            return r
        elif target == nums[l]:
            return l
        else:
            return -1

