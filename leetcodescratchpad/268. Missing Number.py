class Solution:
    def missingNumber( nums) -> int:
        maxRange=len(nums)
        actualSum=(maxRange*(maxRange+1))/2
        gottenSum=0
        for element in nums:
            gottenSum=element+gottenSum
        
        return int(actualSum-gottenSum)

print(Solution.missingNumber([3,0,1]))