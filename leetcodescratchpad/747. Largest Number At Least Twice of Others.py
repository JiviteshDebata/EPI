class Solution:
    def dominantIndex(nums) -> int:
        maxValue=0
        secondMaxValue=0
        index=0
        maxIndex=-1
        for element in nums:
            if maxValue<element:
                secondMaxValue=maxValue
                maxValue=element
                maxIndex=index
            elif element>secondMaxValue:
                secondMaxValue=element
            index=index+1
        if(secondMaxValue*2>maxValue):
            maxIndex=-1
        return maxIndex
print(Solution.dominantIndex([1,2,3,4]))