class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        count = 0
        for i in s:
            if i == "]":
                if len(stack)!=0:
                    if stack[-1] == "]":
                        count+=1
                        stack.append(i)
                    else:
                        stack.pop()
                else:
                    count+=1
                    stack.append(i)
            else:
                stack.append(i)
        

        return (count+1)//2