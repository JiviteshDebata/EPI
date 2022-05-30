from typing import List
class Solution:
    def maxProduct( words: List[str]) -> int:
        wordHash={}
        for word in words:
            wordHash[word]=set()
            for letter in word:
                wordHash[word].add(letter)
        print(wordHash)
        maxProduct=-1
        for i in range(0,len(words)-1):
            for j in range(i,len(words)):
                print("words:", words[i], words[j])
                if not wordHash[words[i]] & wordHash[words[j]]:
                    
                    maxProduct=max(maxProduct,len(words[i])*len(words[j]))
                    
                    print(" \t \tInside words:", words[i], words[j] ,"max now is" ,maxProduct)
        return maxProduct
    
print(Solution.maxProduct(["eae","ea","aaf","bda","fcf","dc","ac","ce","cefde","dabae"]))