class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums.sort()
        # count = defaultdict(int)
        # for num in nums:
        #     count[num] +=1
        # res = []
        # for i in range(0, len(nums) -1):
        #     count[nums[i]] -= 1
        #     twoSum = 0 - nums[i]
        #     if i > 0 and nums[i] == nums[i-1]:
        #         continue
        #     for j in range(i+1, len(nums)-1):
        #         count[nums[j]] -= 1
        #         target = twoSum - nums[j]
        #         if j-1 > i and nums[j] == nums[j-1]:
        #             continue
                
        #         if count[target] > 0:
        #             res.append([nums[i], nums[j], target])
            
        #     for j in range(i+1, len(nums) -1 ):
        #         count[nums[j]] +=1
        # return res
        nums.sort();
        res= []
        for i in range(0, len(nums) -1):
            if nums[i] > 0:
                break;
            if i > 0 and nums[i] == nums[i-1]:
                continue;
            
            l = i + 1 
            r = len(nums) - 1
            while l<r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l+=1
                elif total > 0:
                    r-=1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
       
                
             
                

        return res
            