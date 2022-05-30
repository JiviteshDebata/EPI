class Solution:
    def countOdds( low: int, high: int) -> int:
        if low%2==0 and high%2==0:
            return int((high-low)/2)
        return int((high-low)/2) + 1
    
print(Solution.countOdds(1,10))