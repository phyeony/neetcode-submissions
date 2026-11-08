class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalProdWithoutZero = 1;

        zeroCount = 0;
        for num in nums:
            if num != 0:
                totalProdWithoutZero *= num
            else:
                zeroCount+=1
            
        result = []
        for num in nums:
            if num == 0 and zeroCount > 1:
                result.append(0)
            elif num == 0 and zeroCount == 1:
                result.append(totalProdWithoutZero)
            elif num != 0 and zeroCount > 0: 
                result.append(0)
            else:
                result.append(int(totalProdWithoutZero/num))
        return result;