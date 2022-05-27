class Solution:
    def hIndex(citations) -> int:
        citations.sort()
        count=1
        while(count<len(citations) and citations[len(citations)-1-count]>count):
            count=count+1
        return count
                    
print(Solution.hIndex(citations=[1,3,1]))
print(Solution.hIndex(citations=[6,1,5,0,3]))