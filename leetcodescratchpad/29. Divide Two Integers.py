class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        max=2147483648-1
        min=-2147483648
        quotient=0
        shiftAmount=0
        isNegative=(dividend>0) ^ (divisor>0)
        p_dividend=abs(dividend)
        p_divisor=abs(divisor)
        

        while(p_dividend>=p_divisor):

            while(p_dividend-(p_divisor<<shiftAmount)>=0):
                shiftAmount=shiftAmount+1

            p_dividend=p_dividend-(p_divisor<<(shiftAmount-1))
            quotient=quotient+(1<<shiftAmount-1)
            shiftAmount=0
        
        if isNegative:
            if quotient<min:
                return -min
            return -quotient
        else:
            if quotient>max:
                return max
            return quotient
s=Solution()
print(s.divide(100,3))

            
            
            
            
            