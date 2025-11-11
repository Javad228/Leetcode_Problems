class Solution(object):
    def calculateTax(self, brackets, income):
        """
        :type brackets: List[List[int]]
        :type income: int
        :rtype: float
        """
        
        tax = 0

        tax+= float(min(income, brackets[0][0]) * brackets[0][1]) /100.0
        for b in range(1,len(brackets)):
            if brackets[b][0] >income:
                if  brackets[b-1][0] >income:
                    break
                dif = income - brackets[b-1][0]
                tax += float(dif*brackets[b][1])/100.0
                break

            dif = brackets[b][0] - brackets[b-1][0]
            tax += float(dif*brackets[b][1])/100.0

        return tax



