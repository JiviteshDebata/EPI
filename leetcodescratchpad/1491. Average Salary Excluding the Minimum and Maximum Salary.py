from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        maxSalary=salary[0]
        minSalary=salary[0]
        sum=0
        for element in salary:
            if element>maxSalary:
                maxSalary=element
            if element<minSalary:
                minSalary=element
            sum=sum+element
        return (sum-maxSalary-minSalary)/(len(salary)-2)