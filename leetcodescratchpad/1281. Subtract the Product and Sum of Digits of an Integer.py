class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum=0
        prod=1
        while n>0:
            sum= sum + int(n%10)
            prod=prod*int(n%10)
            n=int(n/10)
        return prod
    
s=Solution()
print(s.subtractProductAndSum(243))