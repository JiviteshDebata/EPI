class Solution:
    def hasAllCodes( s: str, k: int) -> bool:
        count=0
        seenCodes=set()
        if len(s)<2**k:
            return False
        else:
            i=0
            while i<len(s)-k+1:
                tempCode=s[i:i+k]
                if tempCode not in seenCodes:
                    count=count+1
                    seenCodes.add(tempCode)
                i=i+1
        if count>=2**k:
            return True
        else:
            return False
        
s=Solution
print(s.hasAllCodes("00110",2))

print(s.hasAllCodes("0110",2))
